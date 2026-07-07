"""
Ejemplo: listar personas registradas en el dispositivo.

Extrae los números de empleado únicos desde los eventos de control
de acceso (ACS). Solo aparecen personas que han generado eventos.

Si el usuario tuviera permisos de gestión (UserInfo), se podría
usar la API ISAPI /UserInfo/Search para obtener también nombres.
"""

import json
from random import randint

from cida_attendance.config import load_config
from cida_attendance.sdk.session import Session


def main() -> int:
    config = load_config()

    with Session() as session:
        if not session.login(**config):
            print("No se pudo iniciar sesión en el dispositivo")
            return 1

        search_id = f"query_{randint(1000, 9999)}"
        users = []
        counter = 0

        try:
            while True:
                res = session.request_stdxmlconfig(
                    "POST /ISAPI/AccessControl/UserInfo/Search?format=json",
                    json.dumps(
                        {
                            "UserInfoSearchCond": {
                                "searchID": search_id,
                                "searchResultPosition": counter,
                                "maxResults": 100,
                            }
                        }
                    ),
                )
                data = json.loads(res)
                info_search = data.get("UserInfoSearch", {})

                if not info_search:
                    break

                user_info = info_search.get("UserInfo", [])
                users.extend(user_info)
                counter += info_search.get("numOfMatches") or len(user_info)

                if user_info:
                    del info_search["UserInfo"]

                print(info_search)

                if info_search.get("responseStatusStrg", "").lower() != "more":
                    break
        except KeyboardInterrupt:
            print("Interrumpido por el usuario")

        print(f"Total de personas encontradas: {len(users)}")
        for user in users:
            print(
                f"Empleado: {user.get('employeeNo')}, "
                f"Nombre: {user.get('name')}, "
                f"Tipo: {user.get('userType')}"
            )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
