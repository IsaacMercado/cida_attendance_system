from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_chan_record_publish_info import NET_DVR_RECORD_PUBLISH_INFO
from .net_dvr_publish_add_union import NET_DVR_PUBLISH_ADD_UNION


class struct_tagNET_DVR_PUBLISH_CFG(Structure):
    pass

_S(struct_tagNET_DVR_PUBLISH_CFG, [
    ('dwSize', DWORD),
    ('byPublishType', BYTE),
    ('byRes1', BYTE * 3),
    ('struPublishAddr', NET_DVR_PUBLISH_ADD_UNION),
    ('struChanPublish', NET_DVR_RECORD_PUBLISH_INFO * int((32 + 32))),
    ('struDirectChanPublish', NET_DVR_RECORD_PUBLISH_INFO),
    ('byUploadTime', BYTE),
    ('byTimerMode', BYTE),
    ('byUploadStartHour', BYTE),
    ('byUoploadStartMin', BYTE),
    ('byRes', BYTE * 1020),
])

NET_DVR_PUBLISH_CFG = struct_tagNET_DVR_PUBLISH_CFG
LPNET_DVR_PUBLISH_CFG = POINTER(struct_tagNET_DVR_PUBLISH_CFG)
tagNET_DVR_PUBLISH_CFG = struct_tagNET_DVR_PUBLISH_CFG
