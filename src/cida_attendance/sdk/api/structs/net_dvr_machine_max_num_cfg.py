from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_MACHINE_MAX_NUM_CFG(Structure):
    pass

_S(struct_tagNET_DVR_MACHINE_MAX_NUM_CFG, [
    ('dwSize', DWORD),
    ('dwMaxNum', DWORD),
    ('byRes', BYTE * 32),
])

NET_DVR_MACHINE_MAX_NUM_CFG = struct_tagNET_DVR_MACHINE_MAX_NUM_CFG
LPNETDVR_MACHINE_MAX_NUM_CFG = POINTER(struct_tagNET_DVR_MACHINE_MAX_NUM_CFG)
tagNET_DVR_MACHINE_MAX_NUM_CFG = struct_tagNET_DVR_MACHINE_MAX_NUM_CFG
