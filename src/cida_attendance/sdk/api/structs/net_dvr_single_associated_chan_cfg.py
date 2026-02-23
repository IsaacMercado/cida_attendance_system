from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_SINGLE_ASSOCIATED_CHAN_CFG(Structure):
    pass

_S(struct_tagNET_DVR_SINGLE_ASSOCIATED_CHAN_CFG, [
    ('byDevSerialNo', BYTE * 48),
    ('dwChannel', DWORD),
    ('byRes', BYTE * 64),
])

NET_DVR_SINGLE_ASSOCIATED_CHAN_CFG = struct_tagNET_DVR_SINGLE_ASSOCIATED_CHAN_CFG
LPNET_DVR_SINGLE_ASSOCIATED_CHAN_CFG = POINTER(struct_tagNET_DVR_SINGLE_ASSOCIATED_CHAN_CFG)
tagNET_DVR_SINGLE_ASSOCIATED_CHAN_CFG = struct_tagNET_DVR_SINGLE_ASSOCIATED_CHAN_CFG
