from ctypes import Structure, c_float

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER, String
from .net_vca_point import NET_VCA_POINT


class struct_tagNET_DVR_ID_CARD_INFO_EXTEND(Structure):
    pass

_S(struct_tagNET_DVR_ID_CARD_INFO_EXTEND, [
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
    ('byRes', BYTE * 1024),
])

NET_DVR_ID_CARD_INFO_EXTEND = struct_tagNET_DVR_ID_CARD_INFO_EXTEND
LPNET_DVR_ID_CARD_INFO_EXTEND = POINTER(struct_tagNET_DVR_ID_CARD_INFO_EXTEND)
tagNET_DVR_ID_CARD_INFO_EXTEND = struct_tagNET_DVR_ID_CARD_INFO_EXTEND
