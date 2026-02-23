from ctypes import Union

from ..base_classes import _S
from ..ctypes_preamble import POINTER
from .anon_177 import NET_DVR_MATRIX_CHAN_STATUS
from .net_dvr_analoginputstatus import NET_DVR_ANALOGINPUTSTATUS


class union_tagNET_DVR_INPUTSTATUS_UNION(Union):
    pass

_S(union_tagNET_DVR_INPUTSTATUS_UNION, [
    ('struIpInputStatus', NET_DVR_MATRIX_CHAN_STATUS),
    ('struAnalogInputStatus', NET_DVR_ANALOGINPUTSTATUS),
])

NET_DVR_INPUTSTATUS_UNION = union_tagNET_DVR_INPUTSTATUS_UNION
LPNET_DVR_INPUTSTATUS_UNION = POINTER(union_tagNET_DVR_INPUTSTATUS_UNION)
tagNET_DVR_INPUTSTATUS_UNION = union_tagNET_DVR_INPUTSTATUS_UNION
