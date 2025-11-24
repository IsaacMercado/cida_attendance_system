import json
import urllib.error
import urllib.parse
import urllib.request


class HttpClientError(Exception):
    def __init__(
        self,
        message: str,
        code: int | None = None,
        data: dict | None = None,
    ):
        super().__init__(message)
        self.code = code
        self.data = data


class HttpClient:
    def __init__(self, auth_token: str, url: str):
        self.auth_token = auth_token
        self.url = url.strip().rstrip("?")

    def __send(
        self,
        request: urllib.request.Request,
        success_code: int = 200,
    ) -> dict | None:
        try:
            with urllib.request.urlopen(request) as response:
                status_code = response.getcode()
                response_text = response.read().decode("utf-8")
                data = json.loads(response_text)

                if status_code != success_code:
                    raise HttpClientError(
                        f"HTTP error: {status_code}",
                        code=status_code,
                        data=data,
                    )

                return data
        except urllib.error.HTTPError as e:
            raise HttpClientError(
                f"HTTP error: {e.code}",
                code=e.code,
                data=json.loads(e.read().decode("utf-8")),
            ) from e
        except urllib.error.URLError as e:
            raise HttpClientError(f"URL error: {e.reason}") from e

    def __get_default_headers(self) -> dict:
        return {
            "Authorization": f"Bearer {self.auth_token}",
        }

    def get(self, **params) -> dict | None:
        url = self.url
        if params:
            query_string = urllib.parse.urlencode(params)
            url = f"{url}?{query_string}"
        req = urllib.request.Request(
            url,
            headers=self.__get_default_headers(),
        )
        return self.__send(req)

    def post(self, data: dict):
        json_data = json.dumps(data).encode("utf-8")
        req = urllib.request.Request(
            self.url,
            data=json_data,
            headers={
                **self.__get_default_headers(),
                "Content-Type": "application/json",
            },
            method="POST",
        )

        return self.__send(req)
