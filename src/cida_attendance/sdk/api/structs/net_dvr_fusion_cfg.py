from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_FUSION_CFG(Structure):
    pass

_S(struct_tagNET_DVR_FUSION_CFG, [
    ('dwSize', DWORD),
    ('byFusion', BYTE),
    ('byUseHistoryMap', BYTE),
    ('byRes', BYTE * 30),
])

NET_DVR_FUSION_CFG = struct_tagNET_DVR_FUSION_CFG
LPNET_DVR_FUSION_CFG = POINTER(struct_tagNET_DVR_FUSION_CFG)
tagNET_DVR_FUSION_CFG = struct_tagNET_DVR_FUSION_CFG
