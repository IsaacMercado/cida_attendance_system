from ctypes import Union

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_dvr_finger_print_bycard import NET_DVR_FINGER_PRINT_BYCARD
from .net_dvr_finger_print_byreader import NET_DVR_FINGER_PRINT_BYREADER


class union_tagNET_DVR_DEL_FINGER_PRINT_MODE(Union):
    pass

_S(union_tagNET_DVR_DEL_FINGER_PRINT_MODE, [
    ('uLen', BYTE * 588),
    ('struByCard', NET_DVR_FINGER_PRINT_BYCARD),
    ('struByReader', NET_DVR_FINGER_PRINT_BYREADER),
])

NET_DVR_DEL_FINGER_PRINT_MODE = union_tagNET_DVR_DEL_FINGER_PRINT_MODE
LPNET_DVR_DEL_FINGER_PRINT_MODE = POINTER(union_tagNET_DVR_DEL_FINGER_PRINT_MODE)
tagNET_DVR_DEL_FINGER_PRINT_MODE = union_tagNET_DVR_DEL_FINGER_PRINT_MODE
