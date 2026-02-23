from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR


class struct_tagNET_DVR_ALARM_DEVICE_USER(Structure):
    pass

_S(struct_tagNET_DVR_ALARM_DEVICE_USER, [
    ('dwSize', DWORD),
    ('sUserName', BYTE * 32),
    ('sPassword', BYTE * 16),
    ('struUserIP', NET_DVR_IPADDR),
    ('byMACAddr', BYTE * 6),
    ('byUserType', BYTE),
    ('byAlarmOnRight', BYTE),
    ('byAlarmOffRight', BYTE),
    ('byBypassRight', BYTE),
    ('byOtherRight', BYTE * 32),
    ('byNetPreviewRight', BYTE * int((64 / 8))),
    ('byNetRecordRight', BYTE * int((64 / 8))),
    ('byNetPlaybackRight', BYTE * int((64 / 8))),
    ('byNetPTZRight', BYTE * int((64 / 8))),
    ('sOriginalPassword', BYTE * 16),
    ('sKeypadPassword', BYTE * 16),
    ('byUserEnabled', BYTE),
    ('byRes2', BYTE * 135),
])

NET_DVR_ALARM_DEVICE_USER = struct_tagNET_DVR_ALARM_DEVICE_USER
LPNET_DVR_ALARM_DEVICE_USER = POINTER(struct_tagNET_DVR_ALARM_DEVICE_USER)
tagNET_DVR_ALARM_DEVICE_USER = struct_tagNET_DVR_ALARM_DEVICE_USER
