from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_single_alarmin_param import NET_DVR_SINGLE_ALARMIN_PARAM


class struct_tagNET_DVR_ALARMIN_PARAM_LIST(Structure):
    pass

_S(struct_tagNET_DVR_ALARMIN_PARAM_LIST, [
    ('dwSize', DWORD),
    ('struSingleAlarmInParam', NET_DVR_SINGLE_ALARMIN_PARAM * 64),
    ('byRes', BYTE * 128),
])

NET_DVR_ALARMIN_PARAM_LIST = struct_tagNET_DVR_ALARMIN_PARAM_LIST
LPNET_DVR_ALARMIN_PARAM_LIST = POINTER(struct_tagNET_DVR_ALARMIN_PARAM_LIST)
tagNET_DVR_ALARMIN_PARAM_LIST = struct_tagNET_DVR_ALARMIN_PARAM_LIST
