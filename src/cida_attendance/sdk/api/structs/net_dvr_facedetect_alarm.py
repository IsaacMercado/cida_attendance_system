from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .net_vca_dev_info import NET_VCA_DEV_INFO
from .net_vca_target_info import NET_VCA_TARGET_INFO


class struct_tagNET_DVR_FACEDETECT_ALARM(Structure):
    pass

_S(struct_tagNET_DVR_FACEDETECT_ALARM, [
    ('dwSize', DWORD),
    ('dwRelativeTime', DWORD),
    ('dwAbsTime', DWORD),
    ('byRuleName', BYTE * 32),
    ('struTargetInfo', NET_VCA_TARGET_INFO),
    ('struDevInfo', NET_VCA_DEV_INFO),
    ('dwPicDataLen', DWORD),
    ('byAlarmPicType', BYTE),
    ('byPanelChan', BYTE),
    ('byRelAlarmPicNum', BYTE),
    ('byRes1', BYTE),
    ('dwFacePicDataLen', DWORD),
    ('dwAlarmID', DWORD),
    ('wDevInfoIvmsChannelEx', WORD),
    ('byRes2', BYTE * 42),
    ('pFaceImage', POINTER(BYTE)),
    ('pImage', POINTER(BYTE)),
])

NET_DVR_FACEDETECT_ALARM = struct_tagNET_DVR_FACEDETECT_ALARM
LPNET_DVR_FACEDETECT_ALARM = POINTER(struct_tagNET_DVR_FACEDETECT_ALARM)
tagNET_DVR_FACEDETECT_ALARM = struct_tagNET_DVR_FACEDETECT_ALARM
