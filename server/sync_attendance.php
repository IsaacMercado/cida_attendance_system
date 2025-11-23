<?php
declare(strict_types=1);

// sync_attendance.php

/**
 * Carga variables de entorno desde un archivo .env simple.
 */
class DotEnv
{
    public static function load(string $path = __DIR__ . '/.env', int $maxBytes = 1048576): void
    {
        if (!is_readable($path) || (@filesize($path) ?: 0) > $maxBytes) {
            return;
        }

        $lines = @file($path, FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);
        if ($lines === false) {
            return;
        }

        foreach ($lines as $raw) {
            $line = trim($raw);
            if ($line === '' || $line[0] === '#') {
                continue;
            }

            if (stripos($line, 'export ') === 0) {
                $line = trim(substr($line, 7));
            }

            $pos = strpos($line, '=');
            if ($pos === false) {
                continue;
            }

            $name = trim(substr($line, 0, $pos));
            $value = trim(substr($line, $pos + 1));

            if ($name === '') {
                continue;
            }

            if (strlen($value) >= 2) {
                $first = $value[0];
                $last = $value[strlen($value) - 1];
                if (($first === '"' && $last === '"') || ($first === "'" && $last === "'")) {
                    $value = substr($value, 1, -1);
                    if ($first === '"') {
                        $value = str_replace(
                            ["\\n", "\\r", "\\t", "\\\"", "\\\\", "\\'"],
                            ["\n", "\r", "\t", "\"", "\\", "'"],
                            $value
                        );
                    }
                } else {
                    $hashPos = strpos($value, ' #');
                    if ($hashPos !== false) {
                        $value = trim(substr($value, 0, $hashPos));
                    }
                }
            }

            if (getenv($name) === false) {
                @putenv("$name=$value");
            }
            $_ENV[$name] = $value;
            $_SERVER[$name] = $value;
        }
    }
}

class AttendanceSync
{
    private ?PDO $pdo = null;

    public function __construct()
    {
        DotEnv::load();
    }

    public function run(): void
    {
        try {
            $this->authenticate();

            $method = $_SERVER['REQUEST_METHOD'] ?? 'GET';

            switch ($method) {
                case 'GET':
                    $this->handleGet();
                    break;
                case 'POST':
                    $this->handlePost();
                    break;
                default:
                    $this->sendResponse(405, ['error' => 'Method not allowed']);
                    break;
            }

        } catch (PDOException $e) {
            error_log('Database Error: ' . $e->getMessage());
            $this->sendResponse(500, ['error' => 'Database connection error']);
        } catch (JsonException $e) {
            $this->sendResponse(400, ['error' => 'Invalid JSON structure']);
        } catch (Exception $e) {
            $code = $e->getCode();
            $status = ($code >= 400 && $code < 600) ? $code : 500;
            $this->sendResponse($status, ['error' => $e->getMessage()]);
        }
    }

    private function authenticate(): void
    {
        $authHeader = $_SERVER['HTTP_AUTHORIZATION'] ?? getallheaders()['Authorization'] ?? '';
        $token = '';

        if (stripos($authHeader, 'Bearer ') === 0) {
            $token = trim(substr($authHeader, 7));
        }

        $expectedToken = getenv('AUTH_TOKEN');
        if (!$expectedToken) {
            $expectedToken = 'CAMBIA_ESTE_TOKEN_POR_UNO_MUY_LARGO_Y_ALEATORIO';
        }

        if (!hash_equals($expectedToken, $token)) {
            throw new Exception('Unauthorized', 401);
        }
    }

    private function getDb(): PDO
    {
        if ($this->pdo === null) {
            $uri = getenv('DB_URI');
            $dsn = 'pgsql:host=localhost;port=5432;dbname=cida_attendance';
            $user = 'tu_usuario';
            $pass = '';

            if (is_string($uri) && $uri !== '') {
                $parts = parse_url($uri);
                if ($parts && ($parts['scheme'] ?? '') === 'postgres') {
                    $host = $parts['host'] ?? 'localhost';
                    $port = $parts['port'] ?? 5432;
                    $user = $parts['user'] ?? '';
                    $pass = $parts['pass'] ?? '';
                    $dbname = ltrim($parts['path'] ?? '', '/') ?: 'cida_attendance';
                    $dsn = sprintf('pgsql:host=%s;port=%d;dbname=%s', $host, (int) $port, $dbname);
                }
            }

            $this->pdo = new PDO($dsn, $user, $pass, [
                PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
                PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
                PDO::ATTR_EMULATE_PREPARES => false,
            ]);
        }
        return $this->pdo;
    }

    private function handleGet(): void
    {
        $pdo = $this->getDb();
        $deviceSerial = $_GET['device_serial'] ?? null;
        $deviceModel = $_GET['device_model'] ?? null;

        $queryParams = [];
        $query = 'SELECT MAX(event_time) as last_sync FROM cida_attendance';

        if (!empty($deviceSerial) && is_string($deviceSerial)) {
            $queryParams['device_serial'] = $deviceSerial;
        }

        if (!empty($deviceModel) && is_string($deviceModel)) {
            $queryParams['device_model'] = $deviceModel;
        }

        if (count($queryParams) > 0) {
            $conditions = [];
            foreach ($queryParams as $key => $value) {
                $conditions[] = "$key = :$key";
            }
            $query .= " WHERE " . implode(' AND ', $conditions);

            $stmt = $pdo->prepare($query);
            $stmt->execute($queryParams);
        } else {
            $stmt = $pdo->query($query);
        }

        $row = $stmt->fetch();
        $this->sendResponse(200, ['last_sync' => $row['last_sync'] ?? null]);
    }

    private function handlePost(): void
    {
        $contentType = $_SERVER['CONTENT_TYPE'] ?? $_SERVER['HTTP_CONTENT_TYPE'] ?? '';
        if (stripos($contentType, 'application/json') !== 0) {
            throw new Exception('Content-Type must be application/json', 400);
        }

        $rawBody = $this->getRawBody();
        $data = json_decode($rawBody, true, 512, JSON_THROW_ON_ERROR);

        if (!is_array($data)) {
            throw new Exception('Invalid JSON structure', 400);
        }

        $payload = $this->validatePayload($data);
        $pdo = $this->getDb();

        try {
            $pdo->beginTransaction();
            $inserted = $this->insertRecords($pdo, $payload);
            $pdo->commit();
        } catch (Throwable $e) {
            if ($pdo->inTransaction()) {
                $pdo->rollBack();
            }
            error_log('Insert Error: ' . $e->getMessage());
            throw new Exception('Failed to store data', 500);
        }

        $this->sendResponse(200, [
            'status' => 'ok',
            'inserted' => $inserted,
        ]);
    }

    private function getRawBody(): string
    {
        $maxBytes = (int) (getenv('MAX_BODY_BYTES') ?: 1048576);
        $contentLength = (int) ($_SERVER['CONTENT_LENGTH'] ?? 0);

        if ($contentLength > $maxBytes) {
            throw new Exception('Payload too large', 413);
        }

        $body = file_get_contents('php://input', false, null, 0, $maxBytes + 1);

        if ($body === false) {
            throw new Exception('Unable to read request body', 400);
        }
        if ($body === '') {
            throw new Exception('Empty body', 400);
        }
        if (strlen($body) > $maxBytes) {
            throw new Exception('Payload too large', 413);
        }

        return $body;
    }

    private function validatePayload(array $data): array
    {
        if (empty($data['device_id']) || !is_string($data['device_id'])) {
            throw new Exception('Invalid or missing device_id', 400);
        }

        $deviceModel = $data['device_model'] ?? 'Unknown';
        $deviceName = $data['device_name'] ?? null;

        if (empty($data['records']) || !is_array($data['records'])) {
            throw new Exception('Invalid or missing records', 400);
        }

        $cleanRecords = [];
        foreach ($data['records'] as $idx => $rec) {
            if (!is_array($rec)) {
                throw new Exception("Record $idx must be an object", 400);
            }

            $employeeId = $rec['employee_id'] ?? '';
            $timestamp = $rec['timestamp'] ?? '';
            $eventType = $rec['event_type'] ?? '';
            $eventMinor = $rec['event_minor'] ?? 0;

            if (!is_string($employeeId) || $employeeId === '') {
                throw new Exception("Record $idx: invalid employee_id", 400);
            }
            if (!$this->validateIso8601($timestamp)) {
                throw new Exception("Record $idx: invalid timestamp", 400);
            }
            if (!is_int($eventType) && !ctype_digit($eventType)) {
                throw new Exception("Record $idx: invalid event_type", 400);
            }
            if (!is_int($eventMinor) && !ctype_digit($eventMinor)) {
                throw new Exception("Record $idx: invalid event_minor", 400);
            }

            $cleanRecords[] = [
                'employee_id' => $employeeId,
                'timestamp' => $timestamp,
                'event_type' => (int) $eventType,
                'event_minor' => (int) $eventMinor,
            ];
        }

        return [
            'device_id' => $data['device_id'],
            'device_model' => $deviceModel,
            'device_name' => $deviceName,
            'records' => $cleanRecords,
        ];
    }

    private function validateIso8601($value): bool
    {
        if (!is_string($value))
            return false;
        try {
            new DateTime($value);
            return true;
        } catch (Exception $e) {
            return false;
        }
    }

    private function insertRecords(PDO $pdo, array $payload): int
    {
        $sql = 'INSERT INTO cida_attendance
                (event_user_id, event_time, event_type, device_model, device_serial, device_name, event_minor)
                VALUES (:event_user_id, :event_time, :event_type, :device_model, :device_serial, :device_name, :event_minor)';

        $stmt = $pdo->prepare($sql);
        $inserted = 0;

        foreach ($payload['records'] as $rec) {
            $ok = $stmt->execute([
                ':event_user_id' => $rec['employee_id'],
                ':event_time' => $rec['timestamp'],
                ':event_type' => (int) $rec['event_type'],
                ':device_model' => $payload['device_model'],
                ':device_serial' => $payload['device_id'],
                ':device_name' => $payload['device_name'],
                ':event_minor' => (int) $rec['event_minor'],
            ]);
            if ($ok)
                $inserted++;
        }

        return $inserted;
    }

    private function sendResponse(int $statusCode, array $data): void
    {
        http_response_code($statusCode);
        header('Content-Type: application/json; charset=utf-8');
        echo json_encode($data, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES);
        exit;
    }
}

// Run the application
(new AttendanceSync())->run();
