from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER, String


class struct_tagNET_DVR_ALARM_ISAPI_INFO(Structure):
    pass

_S(struct_tagNET_DVR_ALARM_ISAPI_INFO, [
    ('pAlarmData', String),
    ('dwAlarmDataLen', DWORD),
    ('byDataType', BYTE),
    ('byPicturesNumber', BYTE),
    ('byRes', BYTE * 2),
    ('pPicPackData', POINTER(None)),
    ('byRes1', BYTE * 32),
])

NET_DVR_ALARM_ISAPI_INFO = struct_tagNET_DVR_ALARM_ISAPI_INFO
LPNET_DVR_ALARM_ISAPI_INFO = POINTER(struct_tagNET_DVR_ALARM_ISAPI_INFO)
tagNET_DVR_ALARM_ISAPI_INFO = struct_tagNET_DVR_ALARM_ISAPI_INFO
