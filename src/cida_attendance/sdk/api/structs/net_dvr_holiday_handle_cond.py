from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_HOLIDAY_HANDLE_COND(Structure):
    pass

_S(struct_tagNET_DVR_HOLIDAY_HANDLE_COND, [
    ('dwSize', DWORD),
    ('dwChannel', DWORD),
    ('dwSMDHandleType', DWORD),
    ('byRes2', BYTE * 32),
])

NET_DVR_HOLIDAY_HANDLE_COND = struct_tagNET_DVR_HOLIDAY_HANDLE_COND
LPNET_DVR_HOLIDAY_HANDLE_COND = POINTER(struct_tagNET_DVR_HOLIDAY_HANDLE_COND)
tagNET_DVR_HOLIDAY_HANDLE_COND = struct_tagNET_DVR_HOLIDAY_HANDLE_COND
