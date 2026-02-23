from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_transparent_chan_work_mode_union import (
    NET_DVR_TRANSPARENT_CHAN_WORK_MODE_UNION,
)


class struct_tagNET_DVR_TRANSPARENT_CHAN_CFG(Structure):
    pass

_S(struct_tagNET_DVR_TRANSPARENT_CHAN_CFG, [
    ('dwSize', DWORD),
    ('byWorkMode', BYTE),
    ('byRes', BYTE * 3),
    ('struTransparentPara', NET_DVR_TRANSPARENT_CHAN_WORK_MODE_UNION),
])

NET_DVR_TRANSPARENT_CHAN_CFG = struct_tagNET_DVR_TRANSPARENT_CHAN_CFG
LPNET_DVR_TRANSPARENT_CHAN_CFG = POINTER(struct_tagNET_DVR_TRANSPARENT_CHAN_CFG)
tagNET_DVR_TRANSPARENT_CHAN_CFG = struct_tagNET_DVR_TRANSPARENT_CHAN_CFG
