from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_LOCAL_MEM_POOL_CFG(Structure):
    pass

_S(struct_tagNET_DVR_LOCAL_MEM_POOL_CFG, [
    ('dwAlarmMaxBlockNum', DWORD),
    ('dwAlarmReleaseInterval', DWORD),
    ('dwObjectReleaseInterval', DWORD),
    ('byRes', BYTE * 508),
])

NET_DVR_LOCAL_MEM_POOL_CFG = struct_tagNET_DVR_LOCAL_MEM_POOL_CFG
LPNET_DVR_LOCAL_MEM_POOL_CFG = POINTER(struct_tagNET_DVR_LOCAL_MEM_POOL_CFG)
tagNET_DVR_LOCAL_MEM_POOL_CFG = struct_tagNET_DVR_LOCAL_MEM_POOL_CFG
