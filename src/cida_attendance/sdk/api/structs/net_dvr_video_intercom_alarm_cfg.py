from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_VIDEO_INTERCOM_ALARM_CFG(Structure):
    pass

_S(struct_tagNET_DVR_VIDEO_INTERCOM_ALARM_CFG, [
    ('dwSize', DWORD),
    ('byDoorNotCloseAlarm', BYTE),
    ('byRes', BYTE * 603),
])

NET_DVR_VIDEO_INTERCOM_ALARM_CFG = struct_tagNET_DVR_VIDEO_INTERCOM_ALARM_CFG
LPNET_DVR_VIDEO_INTERCOM_ALARM_CFG = POINTER(struct_tagNET_DVR_VIDEO_INTERCOM_ALARM_CFG)
tagNET_DVR_VIDEO_INTERCOM_ALARM_CFG = struct_tagNET_DVR_VIDEO_INTERCOM_ALARM_CFG
