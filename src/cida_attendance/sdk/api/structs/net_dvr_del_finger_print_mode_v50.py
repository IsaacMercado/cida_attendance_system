from ctypes import Union

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_dvr_finger_print_bycard_v50 import NET_DVR_FINGER_PRINT_BYCARD_V50
from .net_dvr_finger_print_byreader_v50 import NET_DVR_FINGER_PRINT_BYREADER_V50


class union_tagNET_DVR_DEL_FINGER_PRINT_MODE_V50(Union):
    pass

_S(union_tagNET_DVR_DEL_FINGER_PRINT_MODE_V50, [
    ('uLen', BYTE * 588),
    ('struByCard', NET_DVR_FINGER_PRINT_BYCARD_V50),
    ('struByReader', NET_DVR_FINGER_PRINT_BYREADER_V50),
])

NET_DVR_DEL_FINGER_PRINT_MODE_V50 = union_tagNET_DVR_DEL_FINGER_PRINT_MODE_V50
LPNET_DVR_DEL_FINGER_PRINT_MODE_V50 = POINTER(union_tagNET_DVR_DEL_FINGER_PRINT_MODE_V50)
tagNET_DVR_DEL_FINGER_PRINT_MODE_V50 = union_tagNET_DVR_DEL_FINGER_PRINT_MODE_V50
