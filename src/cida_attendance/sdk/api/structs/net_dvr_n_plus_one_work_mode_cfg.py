from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_N_PLUS_ONE_WORK_MODE_CFG(Structure):
    pass

_S(struct_tagNET_DVR_N_PLUS_ONE_WORK_MODE_CFG, [
    ('dwSize', DWORD),
    ('byWorkMode', BYTE),
    ('byRes', BYTE * 127),
])

NET_DVR_N_PLUS_ONE_WORK_MODE_CFG = struct_tagNET_DVR_N_PLUS_ONE_WORK_MODE_CFG
LPNET_DVR_N_PLUS_ONE_WORK_MODE_CFG = POINTER(struct_tagNET_DVR_N_PLUS_ONE_WORK_MODE_CFG)
tagNET_DVR_N_PLUS_ONE_WORK_MODE_CFG = struct_tagNET_DVR_N_PLUS_ONE_WORK_MODE_CFG
