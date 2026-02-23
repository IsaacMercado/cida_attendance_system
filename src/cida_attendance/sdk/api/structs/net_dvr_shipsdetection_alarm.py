from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER, String
from .net_dvr_shipimage_info import NET_DVR_SHIPIMAGE_INFO
from .net_dvr_shipsinfo import NET_DVR_SHIPSINFO
from .net_vca_dev_info import NET_VCA_DEV_INFO


class struct_tagNET_DVR_SHIPSDETECTION_ALARM(Structure):
    pass

_S(struct_tagNET_DVR_SHIPSDETECTION_ALARM, [
    ('dwSize', DWORD),
    ('struDevInfo', NET_VCA_DEV_INFO),
    ('dwRelativeTime', DWORD),
    ('dwAbsTime', DWORD),
    ('byShipsNum', BYTE),
    ('byShipsNumHead', BYTE),
    ('byShipsNumEnd', BYTE),
    ('byPicTransType', BYTE),
    ('struShipInfo', NET_DVR_SHIPSINFO * 20),
    ('dwPicLen', DWORD),
    ('dwThermalPicLen', DWORD),
    ('pPicBuffer', POINTER(BYTE)),
    ('pThermalPicBuffer', POINTER(BYTE)),
    ('wDevInfoIvmsChannelEx', WORD),
    ('byTimeDiffFlag', BYTE),
    ('cTimeDifferenceH', c_char),
    ('cTimeDifferenceM', c_char),
    ('bySID', BYTE),
    ('byRes1', BYTE * 2),
    ('szSceneName', c_char * 32),
    ('byRes', BYTE * 132),
    ('dwXmlLen', DWORD),
    ('pXmlBuf', String),
    ('struShipImageInfo', NET_DVR_SHIPIMAGE_INFO * 6),
])

NET_DVR_SHIPSDETECTION_ALARM = struct_tagNET_DVR_SHIPSDETECTION_ALARM
LPNET_DVR_SHIPSDETECTION_ALARM = POINTER(struct_tagNET_DVR_SHIPSDETECTION_ALARM)
tagNET_DVR_SHIPSDETECTION_ALARM = struct_tagNET_DVR_SHIPSDETECTION_ALARM
