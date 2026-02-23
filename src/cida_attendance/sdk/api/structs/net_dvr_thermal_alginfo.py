from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_THERMAL_ALGINFO(Structure):
    pass

_S(struct_tagNET_DVR_THERMAL_ALGINFO, [
    ('dwSize', DWORD),
    ('sThermometryAlgName', c_char * 128),
    ('sShipsAlgName', c_char * 128),
    ('sFireAlgName', c_char * 128),
    ('byRes', BYTE * 768),
])

NET_DVR_THERMAL_ALGINFO = struct_tagNET_DVR_THERMAL_ALGINFO
LPNET_DVR_THERMAL_ALGINFO = POINTER(struct_tagNET_DVR_THERMAL_ALGINFO)
tagNET_DVR_THERMAL_ALGINFO = struct_tagNET_DVR_THERMAL_ALGINFO
