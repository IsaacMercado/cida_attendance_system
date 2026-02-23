from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_single_alarmin_param_v50 import NET_DVR_SINGLE_ALARMIN_PARAM_V50


class struct_tagNET_DVR_ALARMIN_PARAM_LIST_V50(Structure):
    pass

_S(struct_tagNET_DVR_ALARMIN_PARAM_LIST_V50, [
    ('dwSize', DWORD),
    ('struSingleAlarmInParam', NET_DVR_SINGLE_ALARMIN_PARAM_V50 * 64),
    ('byRes', BYTE * 128),
])

NET_DVR_ALARMIN_PARAM_LIST_V50 = struct_tagNET_DVR_ALARMIN_PARAM_LIST_V50
LPNET_DVR_ALARMIN_PARAM_LIST_V50 = POINTER(struct_tagNET_DVR_ALARMIN_PARAM_LIST_V50)
tagNET_DVR_ALARMIN_PARAM_LIST_V50 = struct_tagNET_DVR_ALARMIN_PARAM_LIST_V50
