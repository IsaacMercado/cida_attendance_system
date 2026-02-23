from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_EXDEVDET_CFG(Structure):
    pass

_S(struct_tagNET_DVR_EXDEVDET_CFG, [
    ('dwSize', DWORD),
    ('byExternalDevStatus', BYTE),
    ('byRes', BYTE * 63),
])

NET_DVR_EXDEVDET_CFG = struct_tagNET_DVR_EXDEVDET_CFG
LPNET_DVR_EXDEVDET_CFG = POINTER(struct_tagNET_DVR_EXDEVDET_CFG)
tagNET_DVR_EXDEVDET_CFG = struct_tagNET_DVR_EXDEVDET_CFG
