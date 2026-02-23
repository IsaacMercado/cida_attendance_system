from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_6 import NET_DVR_SCHEDTIME
from .anon_7 import NET_DVR_HANDLEEXCEPTION_V30


class struct_tagNET_DVR_SWITCH_LAMP_CFG(Structure):
    pass

_S(struct_tagNET_DVR_SWITCH_LAMP_CFG, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byTriggerMode', BYTE),
    ('byUploadPic', BYTE),
    ('byRes1', BYTE),
    ('dwTimeInterval', DWORD),
    ('struHandleType', NET_DVR_HANDLEEXCEPTION_V30),
    ('byRelRecordChan', BYTE * 128),
    ('struAlarmTime', (NET_DVR_SCHEDTIME * 8) * 7),
    ('byRes', BYTE * 256),
])

NET_DVR_SWITCH_LAMP_CFG = struct_tagNET_DVR_SWITCH_LAMP_CFG
LPNET_DVR_SWITCH_LAMP_CFG = POINTER(struct_tagNET_DVR_SWITCH_LAMP_CFG)
tagNET_DVR_SWITCH_LAMP_CFG = struct_tagNET_DVR_SWITCH_LAMP_CFG
