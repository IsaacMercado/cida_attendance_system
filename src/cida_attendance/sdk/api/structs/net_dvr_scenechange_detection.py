from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_6 import NET_DVR_SCHEDTIME
from .net_dvr_handleexception_v40 import NET_DVR_HANDLEEXCEPTION_V40


class struct_tagNET_DVR_SCENECHANGE_DETECTION(Structure):
    pass

_S(struct_tagNET_DVR_SCENECHANGE_DETECTION, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('bySensitiveLevel', BYTE),
    ('byRes1', BYTE * 2),
    ('struAlarmSched', (NET_DVR_SCHEDTIME * 8) * 7),
    ('struHandleException', NET_DVR_HANDLEEXCEPTION_V40),
    ('dwMaxRelRecordChanNum', DWORD),
    ('dwRelRecordChanNum', DWORD),
    ('dwRelRecordChan', DWORD * int((32 + 32))),
    ('byRes2', BYTE * 128),
])

NET_DVR_SCENECHANGE_DETECTION = struct_tagNET_DVR_SCENECHANGE_DETECTION
LPNET_DVR_SCENECHANGE_DETECTION = POINTER(struct_tagNET_DVR_SCENECHANGE_DETECTION)
tagNET_DVR_SCENECHANGE_DETECTION = struct_tagNET_DVR_SCENECHANGE_DETECTION
