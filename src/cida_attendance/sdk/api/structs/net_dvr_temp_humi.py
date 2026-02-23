from ctypes import Structure, c_int

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_TEMP_HUMI(Structure):
    pass

_S(struct_tagNET_DVR_TEMP_HUMI, [
    ('dwSize', DWORD),
    ('dwChannel', DWORD),
    ('iHumidity', c_int),
    ('iTemp', c_int),
    ('byRes', BYTE * 8),
])

NET_DVR_TEMP_HUMI = struct_tagNET_DVR_TEMP_HUMI
LPNET_DVR_TEMP_HUMI = POINTER(struct_tagNET_DVR_TEMP_HUMI)
tagNET_DVR_TEMP_HUMI = struct_tagNET_DVR_TEMP_HUMI
