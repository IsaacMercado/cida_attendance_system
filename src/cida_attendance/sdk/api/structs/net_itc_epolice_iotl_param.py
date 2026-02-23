from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_itc_plate_recog_param import NET_ITC_PLATE_RECOG_PARAM
from .net_itc_single_iotl_param import NET_ITC_SINGLE_IOTL_PARAM


class struct_tagNET_ITC_EPOLICE_IOTL_PARAM(Structure):
    pass

_S(struct_tagNET_ITC_EPOLICE_IOTL_PARAM, [
    ('struPlateRecog', NET_ITC_PLATE_RECOG_PARAM),
    ('struSingleIOTL', NET_ITC_SINGLE_IOTL_PARAM * 4),
    ('byRes', BYTE * 32),
])

NET_ITC_EPOLICE_IOTL_PARAM = struct_tagNET_ITC_EPOLICE_IOTL_PARAM
LPNET_ITC_EPOLICE_IOTL_PARAM = POINTER(struct_tagNET_ITC_EPOLICE_IOTL_PARAM)
tagNET_ITC_EPOLICE_IOTL_PARAM = struct_tagNET_ITC_EPOLICE_IOTL_PARAM
