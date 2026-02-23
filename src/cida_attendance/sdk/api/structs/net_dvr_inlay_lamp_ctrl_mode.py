from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_dvr_park_inlay_subinfo import NET_DVR_PARK_INLAY_SUBINFO


class struct_tagNET_DVR_INLAY_LAMP_CTRL_MODE(Structure):
    pass

_S(struct_tagNET_DVR_INLAY_LAMP_CTRL_MODE, [
    ('struLampStateCtrl', NET_DVR_PARK_INLAY_SUBINFO * 8),
    ('byRes', BYTE * 96),
])

NET_DVR_INLAY_LAMP_CTRL_MODE = struct_tagNET_DVR_INLAY_LAMP_CTRL_MODE
LPNET_DVR_INLAY_LAMP_CTRL_MODE = POINTER(struct_tagNET_DVR_INLAY_LAMP_CTRL_MODE)
tagNET_DVR_INLAY_LAMP_CTRL_MODE = struct_tagNET_DVR_INLAY_LAMP_CTRL_MODE
