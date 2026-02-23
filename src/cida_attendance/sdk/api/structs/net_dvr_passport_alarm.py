from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER, String
from .anon_2 import NET_DVR_IPADDR
from .net_dvr_passport_info import NET_DVR_PASSPORT_INFO
from .net_dvr_time_v30 import NET_DVR_TIME_V30


class struct_tagNET_DVR_PASSPORT_ALARM(Structure):
    pass

_S(struct_tagNET_DVR_PASSPORT_ALARM, [
    ('dwSize', DWORD),
    ('dwMajor', DWORD),
    ('dwMinor', DWORD),
    ('struSwipeTime', NET_DVR_TIME_V30),
    ('byNetUser', BYTE * 16),
    ('struRemoteHostAddr', NET_DVR_IPADDR),
    ('dwCardReaderNo', DWORD),
    ('byCardType', BYTE),
    ('byRes2', BYTE * 11),
    ('struPassportInfo', NET_DVR_PASSPORT_INFO),
    ('dwFaceDataLen', DWORD),
    ('pFaceData', String),
    ('dwPicDataLen', DWORD),
    ('pPicData', String),
    ('dwCapturePicDataLen', DWORD),
    ('pCapturePicData', String),
    ('byRes', BYTE * 128),
])

NET_DVR_PASSPORT_ALARM = struct_tagNET_DVR_PASSPORT_ALARM
LPNET_DVR_PASSPORT_ALARM = POINTER(struct_tagNET_DVR_PASSPORT_ALARM)
tagNET_DVR_PASSPORT_ALARM = struct_tagNET_DVR_PASSPORT_ALARM
