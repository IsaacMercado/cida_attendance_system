from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER, String
from .anon_2 import NET_DVR_IPADDR
from .net_dvr_id_card_info import NET_DVR_ID_CARD_INFO
from .net_dvr_time_v30 import NET_DVR_TIME_V30


class struct_tagNET_DVR_ID_CARD_INFO_ALARM(Structure):
    pass

_S(struct_tagNET_DVR_ID_CARD_INFO_ALARM, [
    ('dwSize', DWORD),
    ('struIDCardCfg', NET_DVR_ID_CARD_INFO),
    ('dwMajor', DWORD),
    ('dwMinor', DWORD),
    ('struSwipeTime', NET_DVR_TIME_V30),
    ('byNetUser', BYTE * 16),
    ('struRemoteHostAddr', NET_DVR_IPADDR),
    ('dwCardReaderNo', DWORD),
    ('dwDoorNo', DWORD),
    ('dwPicDataLen', DWORD),
    ('pPicData', String),
    ('byCardType', BYTE),
    ('byDeviceNo', BYTE),
    ('byMask', BYTE),
    ('byCurrentEvent', BYTE),
    ('dwFingerPrintDataLen', DWORD),
    ('pFingerPrintData', String),
    ('dwCapturePicDataLen', DWORD),
    ('pCapturePicData', String),
    ('dwCertificatePicDataLen', DWORD),
    ('pCertificatePicData', String),
    ('byCardReaderKind', BYTE),
    ('byHelmet', BYTE),
    ('byRes3', BYTE),
    ('byIDCardInfoExtend', BYTE),
    ('pIDCardInfoExtend', String),
    ('dwSerialNo', DWORD),
    ('byRes', BYTE * 168),
])

NET_DVR_ID_CARD_INFO_ALARM = struct_tagNET_DVR_ID_CARD_INFO_ALARM
LPNET_DVR_ID_CARD_INFO_ALARM = POINTER(struct_tagNET_DVR_ID_CARD_INFO_ALARM)
tagNET_DVR_ID_CARD_INFO_ALARM = struct_tagNET_DVR_ID_CARD_INFO_ALARM
