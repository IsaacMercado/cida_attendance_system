from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_OPEN_EZVIZ_USER_LOGIN_INFO(Structure):
    pass

_S(struct_tagNET_DVR_OPEN_EZVIZ_USER_LOGIN_INFO, [
    ('sEzvizServerAddress', c_char * 129),
    ('byRes1', BYTE * 3),
    ('wPort', WORD),
    ('byRes2', BYTE * 2),
    ('sUrl', c_char * 64),
    ('sAccessToken', c_char * 128),
    ('sDeviceID', c_char * 32),
    ('sClientType', c_char * 32),
    ('sFeatureCode', c_char * 64),
    ('sOsVersion', c_char * 32),
    ('sNetType', c_char * 32),
    ('sSdkVersion', c_char * 32),
    ('sAppID', c_char * 64),
    ('byRes3', BYTE * 512),
])

NET_DVR_OPEN_EZVIZ_USER_LOGIN_INFO = struct_tagNET_DVR_OPEN_EZVIZ_USER_LOGIN_INFO
LPNET_DVR_OPEN_EZVIZ_USER_LOGIN_INFO = POINTER(struct_tagNET_DVR_OPEN_EZVIZ_USER_LOGIN_INFO)
tagNET_DVR_OPEN_EZVIZ_USER_LOGIN_INFO = struct_tagNET_DVR_OPEN_EZVIZ_USER_LOGIN_INFO
