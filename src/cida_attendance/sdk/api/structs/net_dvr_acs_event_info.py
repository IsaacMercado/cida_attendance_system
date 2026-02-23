from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_ACS_EVENT_INFO(Structure):
    pass

_S(struct_tagNET_DVR_ACS_EVENT_INFO, [
    ('dwSize', DWORD),
    ('byCardNo', BYTE * 32),
    ('byCardType', BYTE),
    ('byAllowListNo', BYTE),
    ('byReportChannel', BYTE),
    ('byCardReaderKind', BYTE),
    ('dwCardReaderNo', DWORD),
    ('dwDoorNo', DWORD),
    ('dwVerifyNo', DWORD),
    ('dwAlarmInNo', DWORD),
    ('dwAlarmOutNo', DWORD),
    ('dwCaseSensorNo', DWORD),
    ('dwRs485No', DWORD),
    ('dwMultiCardGroupNo', DWORD),
    ('wAccessChannel', WORD),
    ('byDeviceNo', BYTE),
    ('byDistractControlNo', BYTE),
    ('dwEmployeeNo', DWORD),
    ('wLocalControllerID', WORD),
    ('byInternetAccess', BYTE),
    ('byType', BYTE),
    ('byMACAddr', BYTE * 6),
    ('bySwipeCardType', BYTE),
    ('byMask', BYTE),
    ('dwSerialNo', DWORD),
    ('byChannelControllerID', BYTE),
    ('byChannelControllerLampID', BYTE),
    ('byChannelControllerIRAdaptorID', BYTE),
    ('byChannelControllerIREmitterID', BYTE),
    ('byHelmet', BYTE),
    ('byRes', BYTE * 3),
])

NET_DVR_ACS_EVENT_INFO = struct_tagNET_DVR_ACS_EVENT_INFO
LPNET_DVR_ACS_EVENT_INFO = POINTER(struct_tagNET_DVR_ACS_EVENT_INFO)
tagNET_DVR_ACS_EVENT_INFO = struct_tagNET_DVR_ACS_EVENT_INFO
