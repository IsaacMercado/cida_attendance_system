from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_LOCAL_CONTROLLER_STATUS_COND(Structure):
    pass

_S(struct_tagNET_DVR_LOCAL_CONTROLLER_STATUS_COND, [
    ('dwSize', DWORD),
    ('wLocalControllerID', WORD),
    ('byRes', BYTE * 306),
])

NET_DVR_LOCAL_CONTROLLER_STATUS_COND = struct_tagNET_DVR_LOCAL_CONTROLLER_STATUS_COND
LPNET_DVR_LOCAL_CONTROLLER_STATUS_COND = POINTER(struct_tagNET_DVR_LOCAL_CONTROLLER_STATUS_COND)
tagNET_DVR_LOCAL_CONTROLLER_STATUS_COND = struct_tagNET_DVR_LOCAL_CONTROLLER_STATUS_COND
