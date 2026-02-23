from ctypes import Structure

from ..base_classes import _S
from ..ctypes_preamble import POINTER
from .net_itc_plate_recog_param import NET_ITC_PLATE_RECOG_PARAM
from .net_itc_singleio_param import NET_ITC_SINGLEIO_PARAM


class struct_tagNET_ITC_POST_SINGLEIO_PARAM(Structure):
    pass

_S(struct_tagNET_ITC_POST_SINGLEIO_PARAM, [
    ('struPlateRecog', NET_ITC_PLATE_RECOG_PARAM),
    ('struSingleIO', NET_ITC_SINGLEIO_PARAM * 10),
])

NET_ITC_POST_SINGLEIO_PARAM = struct_tagNET_ITC_POST_SINGLEIO_PARAM
LPNET_ITC_POST_SINGLEIO_PARAM = POINTER(struct_tagNET_ITC_POST_SINGLEIO_PARAM)
tagNET_ITC_POST_SINGLEIO_PARAM = struct_tagNET_ITC_POST_SINGLEIO_PARAM
