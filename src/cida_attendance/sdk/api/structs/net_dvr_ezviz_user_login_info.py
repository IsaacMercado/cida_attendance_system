from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_EZVIZ_USER_LOGIN_INFO(Structure):
    pass

_S(struct_tagNET_DVR_EZVIZ_USER_LOGIN_INFO, [
    ('sEzvizServerAddress', c_char * 129),
    ('wPort', WORD),
    ('byLogin', BYTE),
    ('byRes1', BYTE * 1),
    ('sClassSession', c_char * 64),
    ('sDeviceID', c_char * 32),
    ('byRes2', BYTE * 128),
])

NET_DVR_EZVIZ_USER_LOGIN_INFO = struct_tagNET_DVR_EZVIZ_USER_LOGIN_INFO
LPNET_DVR_EZVIZ_USER_LOGIN_INFO = POINTER(struct_tagNET_DVR_EZVIZ_USER_LOGIN_INFO)
tagNET_DVR_EZVIZ_USER_LOGIN_INFO = struct_tagNET_DVR_EZVIZ_USER_LOGIN_INFO
