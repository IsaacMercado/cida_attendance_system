from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_CRUISEPOINT_COND(Structure):
    pass

_S(struct_tagNET_DVR_CRUISEPOINT_COND, [
    ('dwSize', DWORD),
    ('dwChan', DWORD),
    ('wRouteNo', WORD),
    ('byRes', BYTE * 30),
])

NET_DVR_CRUISEPOINT_COND = struct_tagNET_DVR_CRUISEPOINT_COND
LPNET_DVR_CRUISEPOINT_COND = POINTER(struct_tagNET_DVR_CRUISEPOINT_COND)
tagNET_DVR_CRUISEPOINT_COND = struct_tagNET_DVR_CRUISEPOINT_COND
