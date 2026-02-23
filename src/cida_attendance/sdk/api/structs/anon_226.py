from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_225 import NET_DVR_VCA_ATTEND_PICTURE_INFO


class struct_anon_226(Structure):
    pass

_S(struct_anon_226, [
    ('dwSize', DWORD),
    ('byMethod', BYTE),
    ('byStatus', BYTE),
    ('byCertIDType', BYTE),
    ('byCertIDLen', BYTE),
    ('sCertId', c_char * 32),
    ('dwTime', DWORD),
    ('sName', c_char * 64),
    ('sAlarmIdNo', c_char * 32),
    ('struPicInfo', NET_DVR_VCA_ATTEND_PICTURE_INFO),
    ('byRes', BYTE * 128),
])

NET_DVR_VCA_ATTEND_ALARM_INFO = struct_anon_226
LPNET_DVR_VCA_ATTEND_ALARM_INFO = POINTER(struct_anon_226)
