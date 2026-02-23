from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_dvr_structhead import NET_DVR_STRUCTHEAD


class struct_tagNET_DVR_WD1_CFG(Structure):
    pass

_S(struct_tagNET_DVR_WD1_CFG, [
    ('struStruceHead', NET_DVR_STRUCTHEAD),
    ('byWD1Enable', BYTE),
    ('byRes', BYTE * 31),
])

NET_DVR_WD1_CFG = struct_tagNET_DVR_WD1_CFG
LPNET_DVR_WD1_CFG = POINTER(struct_tagNET_DVR_WD1_CFG)
tagNET_DVR_WD1_CFG = struct_tagNET_DVR_WD1_CFG
