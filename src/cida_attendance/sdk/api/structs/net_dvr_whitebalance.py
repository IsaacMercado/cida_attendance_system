from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_WHITEBALANCE(Structure):
    pass

_S(struct_tagNET_DVR_WHITEBALANCE, [
    ('byWhiteBalanceMode', BYTE),
    ('byWhiteBalanceModeRGain', BYTE),
    ('byWhiteBalanceModeBGain', BYTE),
    ('byRes', BYTE * 5),
])

NET_DVR_WHITEBALANCE = struct_tagNET_DVR_WHITEBALANCE
LPNET_DVR_WHITEBALANCE = POINTER(struct_tagNET_DVR_WHITEBALANCE)
tagNET_DVR_WHITEBALANCE = struct_tagNET_DVR_WHITEBALANCE
