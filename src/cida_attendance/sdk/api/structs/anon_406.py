from ctypes import Structure, c_int

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_anon_406(Structure):
    pass

_S(struct_anon_406, [
    ('iAirTemperature', c_int),
    ('dwAirHumidity', DWORD),
    ('dwWindSpeed', DWORD),
    ('dwWindDirection', DWORD),
    ('dwIlluminationIntensity', DWORD),
    ('dwCO2', DWORD),
    ('dwPM25', DWORD),
    ('dwAirPressure', DWORD),
    ('iSoilTemperature', c_int),
    ('dwSoilHumidity', DWORD),
    ('dwIsRainSnow', DWORD),
    ('byRes', BYTE * 468),
])

NET_DVR_WEATHER_STATION_STATE = struct_anon_406
LPNET_DVR_WEATHER_STATION_STATE = POINTER(struct_anon_406)
