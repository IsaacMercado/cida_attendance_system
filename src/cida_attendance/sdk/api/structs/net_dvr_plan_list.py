from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_PLAN_LIST(Structure):
    pass

_S(struct_tagNET_DVR_PLAN_LIST, [
    ('dwSize', DWORD),
    ('dwPlanNums', DWORD),
    ('pBuffer', POINTER(BYTE)),
    ('byWallNo', BYTE),
    ('byRes1', BYTE * 2),
    ('dwBufLen', DWORD),
    ('byRes2', BYTE * 64),
])

NET_DVR_PLAN_LIST = struct_tagNET_DVR_PLAN_LIST
LPNET_DVR_PLAN_LIST = POINTER(struct_tagNET_DVR_PLAN_LIST)
tagNET_DVR_PLAN_LIST = struct_tagNET_DVR_PLAN_LIST
