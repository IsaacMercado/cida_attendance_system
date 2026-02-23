from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_WPS_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_WPS_PARAM, [
    ('dwSize', DWORD),
    ('byEnableWps', BYTE),
    ('byRes', BYTE * 31),
])

NET_DVR_WPS_PARAM = struct_tagNET_DVR_WPS_PARAM
LPNET_DVR_WPS_PARAM = POINTER(struct_tagNET_DVR_WPS_PARAM)
tagNET_DVR_WPS_PARAM = struct_tagNET_DVR_WPS_PARAM
