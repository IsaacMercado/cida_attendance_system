from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_dvr_parkinfo import NET_DVR_PARKINFO


class struct_tagNET_DVR_EXTERNAL_LAMP_CTRL_MODE(Structure):
    pass

_S(struct_tagNET_DVR_EXTERNAL_LAMP_CTRL_MODE, [
    ('struParkInfo', NET_DVR_PARKINFO * 4),
    ('byRes', BYTE * 32),
])

NET_DVR_EXTERNAL_LAMP_CTRL_MODE = struct_tagNET_DVR_EXTERNAL_LAMP_CTRL_MODE
LPNET_DVR_EXTERNAL_LAMP_CTRL_MODE = POINTER(struct_tagNET_DVR_EXTERNAL_LAMP_CTRL_MODE)
tagNET_DVR_EXTERNAL_LAMP_CTRL_MODE = struct_tagNET_DVR_EXTERNAL_LAMP_CTRL_MODE
