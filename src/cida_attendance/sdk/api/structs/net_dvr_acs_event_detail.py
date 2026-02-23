from ctypes import Structure, c_float

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER, String
from .net_vca_point import NET_VCA_POINT


class struct_tagNET_DVR_ACS_EVENT_DETAIL(Structure):
    pass

_S(struct_tagNET_DVR_ACS_EVENT_DETAIL, [
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
    ('byEventAttribute', BYTE),
    ('dwSerialNo', DWORD),
    ('byChannelControllerID', BYTE),
    ('byChannelControllerLampID', BYTE),
    ('byChannelControllerIRAdaptorID', BYTE),
    ('byChannelControllerIREmitterID', BYTE),
    ('dwRecordChannelNum', DWORD),
    ('pRecordChannelData', String),
    ('byUserType', BYTE),
    ('byCurrentVerifyMode', BYTE),
    ('byAttendanceStatus', BYTE),
    ('byStatusValue', BYTE),
    ('byEmployeeNo', BYTE * 32),
    ('byRes1', BYTE),
    ('byMask', BYTE),
    ('byThermometryUnit', BYTE),
    ('byIsAbnomalTemperature', BYTE),
    ('fCurrTemperature', c_float),
    ('struRegionCoordinates', NET_VCA_POINT),
    ('byRes', BYTE * 48),
])

NET_DVR_ACS_EVENT_DETAIL = struct_tagNET_DVR_ACS_EVENT_DETAIL
LPNET_DVR_ACS_EVENT_DETAIL = POINTER(struct_tagNET_DVR_ACS_EVENT_DETAIL)
tagNET_DVR_ACS_EVENT_DETAIL = struct_tagNET_DVR_ACS_EVENT_DETAIL
