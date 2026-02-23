from ctypes import Structure, c_float

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_AZIMUTHINFO(Structure):
    pass

_S(struct_tagNET_DVR_AZIMUTHINFO, [
    ('dwSize', DWORD),
    ('fDegree', c_float),
    ('byAzimuth', BYTE),
    ('byRes', BYTE * 127),
])

NET_DVR_AZIMUTHINFO = struct_tagNET_DVR_AZIMUTHINFO
LPNET_DVR_AZIMUTHINFO = POINTER(struct_tagNET_DVR_AZIMUTHINFO)
tagNET_DVR_AZIMUTHINFO = struct_tagNET_DVR_AZIMUTHINFO
