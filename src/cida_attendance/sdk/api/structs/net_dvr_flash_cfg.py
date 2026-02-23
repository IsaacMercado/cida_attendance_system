from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_FLASH_CFG(Structure):
    pass

_S(struct_tagNET_DVR_FLASH_CFG, [
    ('dwSize', DWORD),
    ('dwChan', DWORD),
    ('dwInNumbers', DWORD),
    ('dwOutNumbers', DWORD),
    ('dwStartTime', DWORD),
    ('dwEndTime', DWORD),
    ('dwEhomeFlag', DWORD),
    ('dwAlarmFlag', DWORD),
    ('byRes', BYTE * 1024),
])

NET_DVR_FLASH_CFG = struct_tagNET_DVR_FLASH_CFG
LPNET_DVR_FLASH_CFG = POINTER(struct_tagNET_DVR_FLASH_CFG)
tagNET_DVR_FLASH_CFG = struct_tagNET_DVR_FLASH_CFG
