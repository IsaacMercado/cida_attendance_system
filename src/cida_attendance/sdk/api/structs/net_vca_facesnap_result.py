from ctypes import Structure, c_char, c_float

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .net_vca_dev_info import NET_VCA_DEV_INFO
from .net_vca_human_feature import NET_VCA_HUMAN_FEATURE
from .net_vca_rect import NET_VCA_RECT
from .net_vca_target_info import NET_VCA_TARGET_INFO


class struct_tagNET_VCA_FACESNAP_RESULT(Structure):
    pass

_S(struct_tagNET_VCA_FACESNAP_RESULT, [
    ('dwSize', DWORD),
    ('dwRelativeTime', DWORD),
    ('dwAbsTime', DWORD),
    ('dwFacePicID', DWORD),
    ('dwFaceScore', DWORD),
    ('struTargetInfo', NET_VCA_TARGET_INFO),
    ('struRect', NET_VCA_RECT),
    ('struDevInfo', NET_VCA_DEV_INFO),
    ('dwFacePicLen', DWORD),
    ('dwBackgroundPicLen', DWORD),
    ('bySmart', BYTE),
    ('byAlarmEndMark', BYTE),
    ('byRepeatTimes', BYTE),
    ('byUploadEventDataType', BYTE),
    ('struFeature', NET_VCA_HUMAN_FEATURE),
    ('fStayDuration', c_float),
    ('sStorageIP', c_char * 16),
    ('wStoragePort', WORD),
    ('wDevInfoIvmsChannelEx', WORD),
    ('byFacePicQuality', BYTE),
    ('byUIDLen', BYTE),
    ('byLivenessDetectionStatus', BYTE),
    ('byAddInfo', BYTE),
    ('pUIDBuffer', POINTER(BYTE)),
    ('pAddInfoBuffer', POINTER(BYTE)),
    ('byTimeDiffFlag', BYTE),
    ('cTimeDifferenceH', c_char),
    ('cTimeDifferenceM', c_char),
    ('byBrokenNetHttp', BYTE),
    ('pBuffer1', POINTER(BYTE)),
    ('pBuffer2', POINTER(BYTE)),
])

NET_VCA_FACESNAP_RESULT = struct_tagNET_VCA_FACESNAP_RESULT
LPNET_VCA_FACESNAP_RESULT = POINTER(struct_tagNET_VCA_FACESNAP_RESULT)
tagNET_VCA_FACESNAP_RESULT = struct_tagNET_VCA_FACESNAP_RESULT
