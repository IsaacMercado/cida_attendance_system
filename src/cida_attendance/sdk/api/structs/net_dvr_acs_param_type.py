from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_ACS_PARAM_TYPE(Structure):
    pass

_S(struct_tagNET_DVR_ACS_PARAM_TYPE, [
    ('dwSize', DWORD),
    ('dwParamType', DWORD),
    ('wLocalControllerID', WORD),
    ('byRes', BYTE * 30),
])

NET_DVR_ACS_PARAM_TYPE = struct_tagNET_DVR_ACS_PARAM_TYPE
LPNET_DVR_ACS_PARAM_TYPE = POINTER(struct_tagNET_DVR_ACS_PARAM_TYPE)
tagNET_DVR_ACS_PARAM_TYPE = struct_tagNET_DVR_ACS_PARAM_TYPE
