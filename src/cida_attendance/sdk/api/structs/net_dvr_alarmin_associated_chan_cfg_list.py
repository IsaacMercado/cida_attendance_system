from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_alarmin_associated_chan_cfg import NET_DVR_ALARMIN_ASSOCIATED_CHAN_CFG


class struct_tagNET_DVR_ALARMIN_ASSOCIATED_CHAN_CFG_LIST_(Structure):
    pass

_S(struct_tagNET_DVR_ALARMIN_ASSOCIATED_CHAN_CFG_LIST_, [
    ('dwSize', DWORD),
    ('struAssociatedChanCfg', NET_DVR_ALARMIN_ASSOCIATED_CHAN_CFG * 64),
    ('byRes', BYTE * 64),
])

NET_DVR_ALARMIN_ASSOCIATED_CHAN_CFG_LIST = struct_tagNET_DVR_ALARMIN_ASSOCIATED_CHAN_CFG_LIST_
LPNET_DVR_ALARMIN_ASSOCIATED_CHAN_CFG_LIST = POINTER(struct_tagNET_DVR_ALARMIN_ASSOCIATED_CHAN_CFG_LIST_)
tagNET_DVR_ALARMIN_ASSOCIATED_CHAN_CFG_LIST_ = struct_tagNET_DVR_ALARMIN_ASSOCIATED_CHAN_CFG_LIST_
