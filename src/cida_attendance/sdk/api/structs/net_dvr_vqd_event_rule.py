from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_6 import NET_DVR_SCHEDTIME
from .anon_7 import NET_DVR_HANDLEEXCEPTION_V30
from .net_dvr_vqd_event_param import NET_DVR_VQD_EVENT_PARAM


class struct_tagNET_DVR_VQD_EVENT_RULE(Structure):
    pass

_S(struct_tagNET_DVR_VQD_EVENT_RULE, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byRes1', BYTE * 3),
    ('struEventParam', NET_DVR_VQD_EVENT_PARAM),
    ('struAlarmTime', (NET_DVR_SCHEDTIME * 8) * 7),
    ('struHandleType', NET_DVR_HANDLEEXCEPTION_V30),
    ('byRelRecordChan', BYTE * 128),
    ('byRes2', BYTE * 128),
])

NET_DVR_VQD_EVENT_RULE = struct_tagNET_DVR_VQD_EVENT_RULE
LPNET_DVR_VQD_EVENT_RULE = POINTER(struct_tagNET_DVR_VQD_EVENT_RULE)
tagNET_DVR_VQD_EVENT_RULE = struct_tagNET_DVR_VQD_EVENT_RULE
