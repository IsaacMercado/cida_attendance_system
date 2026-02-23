from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_CRUISE_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_CRUISE_PARAM, [
    ('dwSize', DWORD),
    ('byCruiseMode', BYTE),
    ('byRes', BYTE * 123),
])

NET_DVR_CRUISE_PARAM = struct_tagNET_DVR_CRUISE_PARAM
LPNET_DVR_CRUISE_PARAM = POINTER(struct_tagNET_DVR_CRUISE_PARAM)
tagNET_DVR_CRUISE_PARAM = struct_tagNET_DVR_CRUISE_PARAM
