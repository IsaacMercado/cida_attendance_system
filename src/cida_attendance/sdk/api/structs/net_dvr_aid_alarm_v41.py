from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER, String
from .net_dvr_aid_info import NET_DVR_AID_INFO
from .net_dvr_scene_info import NET_DVR_SCENE_INFO
from .net_vca_dev_info import NET_VCA_DEV_INFO


class struct_tagNET_DVR_AID_ALARM_V41(Structure):
    pass

_S(struct_tagNET_DVR_AID_ALARM_V41, [
    ('dwSize', DWORD),
    ('dwRelativeTime', DWORD),
    ('dwAbsTime', DWORD),
    ('struDevInfo', NET_VCA_DEV_INFO),
    ('struAIDInfo', NET_DVR_AID_INFO),
    ('struSceneInfo', NET_DVR_SCENE_INFO),
    ('dwPicDataLen', DWORD),
    ('pImage', POINTER(BYTE)),
    ('byDataType', BYTE),
    ('byLaneNo', BYTE),
    ('wMilliSecond', WORD),
    ('byMonitoringSiteID', BYTE * 48),
    ('byDeviceID', BYTE * 48),
    ('dwXmlLen', DWORD),
    ('pXmlBuf', String),
    ('byTargetType', BYTE),
    ('byRuleID', BYTE),
    ('wDevInfoIvmsChannelEx', WORD),
    ('byBrokenNetHttp', BYTE),
    ('byRes', BYTE * 3),
    ('dwPlateSmallPicDataLen', DWORD),
    ('pPlateSmallImage', String),
])

NET_DVR_AID_ALARM_V41 = struct_tagNET_DVR_AID_ALARM_V41
LPNET_DVR_AID_ALARM_V41 = POINTER(struct_tagNET_DVR_AID_ALARM_V41)
tagNET_DVR_AID_ALARM_V41 = struct_tagNET_DVR_AID_ALARM_V41
