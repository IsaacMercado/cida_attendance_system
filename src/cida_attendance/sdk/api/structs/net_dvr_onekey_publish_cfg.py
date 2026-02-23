from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_chan_record_publish_info import NET_DVR_RECORD_PUBLISH_INFO
from .net_dvr_time_ex import NET_DVR_TIME_EX


class struct_tagNET_DVR_ONEKEY_PUBLISH_CFG(Structure):
    pass

_S(struct_tagNET_DVR_ONEKEY_PUBLISH_CFG, [
    ('dwSize', DWORD),
    ('byUseDefine', BYTE),
    ('byRes1', BYTE * 3),
    ('struChanPublish', NET_DVR_RECORD_PUBLISH_INFO * int((32 + 32))),
    ('struDirectChanPublish', NET_DVR_RECORD_PUBLISH_INFO),
    ('struStartTime', NET_DVR_TIME_EX),
    ('struEndTime', NET_DVR_TIME_EX),
    ('byRes', BYTE * 64),
])

NET_DVR_ONEKEY_PUBLISH_CFG = struct_tagNET_DVR_ONEKEY_PUBLISH_CFG
LPNET_DVR_ONEKEY_PUBLISH_CFG = POINTER(struct_tagNET_DVR_ONEKEY_PUBLISH_CFG)
tagNET_DVR_ONEKEY_PUBLISH_CFG = struct_tagNET_DVR_ONEKEY_PUBLISH_CFG
