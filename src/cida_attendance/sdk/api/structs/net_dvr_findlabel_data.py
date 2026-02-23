from ctypes import Structure, c_char

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .anon_1 import NET_DVR_TIME
from .net_dvr_label_identify import NET_DVR_LABEL_IDENTIFY


class struct_tagNET_DVR_FINDLABEL_DATA(Structure):
    pass

_S(struct_tagNET_DVR_FINDLABEL_DATA, [
    ('sLabelName', BYTE * 40),
    ('struTimeLabel', NET_DVR_TIME),
    ('struLabelIdentify', NET_DVR_LABEL_IDENTIFY),
    ('byISO8601', BYTE),
    ('cTimeDifferenceH', c_char),
    ('cTimeDifferenceM', c_char),
    ('byRes', BYTE * 29),
])

NET_DVR_FINDLABEL_DATA = struct_tagNET_DVR_FINDLABEL_DATA
LPNET_DVR_FINDLABEL_DATA = POINTER(struct_tagNET_DVR_FINDLABEL_DATA)
tagNET_DVR_FINDLABEL_DATA = struct_tagNET_DVR_FINDLABEL_DATA
