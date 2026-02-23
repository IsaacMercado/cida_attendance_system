from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER
from .net_dvr_single_associated_chan_cfg import NET_DVR_SINGLE_ASSOCIATED_CHAN_CFG


class struct_tagNET_DVR_ALARMIN_ASSOCIATED_CHAN_CFG(Structure):
    pass

_S(struct_tagNET_DVR_ALARMIN_ASSOCIATED_CHAN_CFG, [
    ('wZoneNo', WORD),
    ('byRes1', BYTE * 2),
    ('struSingleChanCfg', NET_DVR_SINGLE_ASSOCIATED_CHAN_CFG * 4),
    ('byRes2', BYTE * 64),
])

NET_DVR_ALARMIN_ASSOCIATED_CHAN_CFG = struct_tagNET_DVR_ALARMIN_ASSOCIATED_CHAN_CFG
LPNET_DVR_ALARMIN_ASSOCIATED_CHAN_CFG = POINTER(struct_tagNET_DVR_ALARMIN_ASSOCIATED_CHAN_CFG)
tagNET_DVR_ALARMIN_ASSOCIATED_CHAN_CFG = struct_tagNET_DVR_ALARMIN_ASSOCIATED_CHAN_CFG
