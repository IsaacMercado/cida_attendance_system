from ctypes import Structure, c_char, c_int

from ..base_classes import _S, BYTE, LONG, WORD
from ..ctypes_preamble import POINTER
from ..functions import fLoginResultCallBack


class struct_anon_356(Structure):
    pass

_S(struct_anon_356, [
    ('sDeviceAddress', c_char * 129),
    ('byUseTransport', BYTE),
    ('wPort', WORD),
    ('sUserName', c_char * 64),
    ('sPassword', c_char * 64),
    ('cbLoginResult', fLoginResultCallBack),
    ('pUser', POINTER(None)),
    ('bUseAsynLogin', c_int),
    ('byProxyType', BYTE),
    ('byUseUTCTime', BYTE),
    ('byLoginMode', BYTE),
    ('byHttps', BYTE),
    ('iProxyID', LONG),
    ('byVerifyMode', BYTE),
    ('byRes3', BYTE * 119),
])

NET_DVR_USER_LOGIN_INFO = struct_anon_356
LPNET_DVR_USER_LOGIN_INFO = POINTER(struct_anon_356)
