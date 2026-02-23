from ctypes import Structure, c_float

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER, String
from .net_vca_point import NET_VCA_POINT


class struct_tagNET_DVR_ACS_EVENT_INFO_EXTEND_V20(Structure):
    pass

_S(struct_tagNET_DVR_ACS_EVENT_INFO_EXTEND_V20, [
    ('byRemoteCheck', BYTE),
    ('byThermometryUnit', BYTE),
    ('byIsAbnomalTemperature', BYTE),
    ('byRes2', BYTE),
    ('fCurrTemperature', c_float),
    ('struRegionCoordinates', NET_VCA_POINT),
    ('dwQRCodeInfoLen', DWORD),
    ('dwVisibleLightDataLen', DWORD),
    ('dwThermalDataLen', DWORD),
    ('pQRCodeInfo', String),
    ('pVisibleLightData', String),
    ('pThermalData', String),
    ('byAttendanceLabel', BYTE * 64),
    ('byRes', BYTE * 960),
])

NET_DVR_ACS_EVENT_INFO_EXTEND_V20 = struct_tagNET_DVR_ACS_EVENT_INFO_EXTEND_V20
LPNET_DVR_ACS_EVENT_INFO_EXTEND_V20 = POINTER(struct_tagNET_DVR_ACS_EVENT_INFO_EXTEND_V20)
tagNET_DVR_ACS_EVENT_INFO_EXTEND_V20 = struct_tagNET_DVR_ACS_EVENT_INFO_EXTEND_V20
