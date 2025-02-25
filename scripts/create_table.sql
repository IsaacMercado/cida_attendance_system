CREATE TABLE cida_attendance (
    id SERIAL PRIMARY KEY,
    event_user_id VARCHAR(100) NOT NULL,
    event_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    event_type INTEGER NOT NULL,
    device_model VARCHAR(100) NOT NULL,
    device_serial VARCHAR(100) NOT NULL,
    device_name VARCHAR(100)
);