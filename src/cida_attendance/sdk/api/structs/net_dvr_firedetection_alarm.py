from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .net_ptz_info import NET_PTZ_INFO
from .net_vca_dev_info import NET_VCA_DEV_INFO
from .net_vca_point import NET_VCA_POINT
from .net_vca_rect import NET_VCA_RECT


class struct_tagNET_DVR_FIREDETECTION_ALARM(Structure):
    pass

_S(struct_tagNET_DVR_FIREDETECTION_ALARM, [
    ('dwSize', DWORD),
    ('dwRelativeTime', DWORD),
    ('dwAbsTime', DWORD),
    ('struDevInfo', NET_VCA_DEV_INFO),
    ('wPanPos', WORD),
    ('wTiltPos', WORD),
    ('wZoomPos', WORD),
    ('byPicTransType', BYTE),
    ('byRes1', BYTE),
    ('dwPicDataLen', DWORD),
    ('pBuffer', POINTER(BYTE)),
    ('struRect', NET_VCA_RECT),
    ('struPoint', NET_VCA_POINT),
    ('wFireMaxTemperature', WORD),
    ('wTargetDistance', WORD),
    ('byStrategyType', BYTE),
    ('byAlarmSubType', BYTE),
    ('byPTZPosExEnable', BYTE),
    ('byRes2', BYTE),
    ('struPtzPosEx', NET_PTZ_INFO),
    ('dwVisiblePicLen', DWORD),
    ('pVisiblePicBuf', POINTER(BYTE)),
    ('pSmokeBuf', POINTER(BYTE)),
    ('wDevInfoIvmsChannelEx', WORD),
    ('byRes3', BYTE),
    ('byFireScanWaitMode', BYTE),
    ('dwVisibleChannel', DWORD),
    ('byTimeDiffFlag', BYTE),
    ('cTimeDifferenceH', c_char),
    ('cTimeDifferenceM', c_char),
    ('byRes', BYTE * 49),
])

NET_DVR_FIREDETECTION_ALARM = struct_tagNET_DVR_FIREDETECTION_ALARM
LPNET_DVR_FIREDETECTION_ALARM = POINTER(struct_tagNET_DVR_FIREDETECTION_ALARM)
tagNET_DVR_FIREDETECTION_ALARM = struct_tagNET_DVR_FIREDETECTION_ALARM
