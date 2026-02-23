from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_LOGIN_PASSWORDCFG(Structure):
    pass

_S(struct_tagNET_DVR_LOGIN_PASSWORDCFG, [
    ('dwSize', DWORD),
    ('sLoginPassWord', c_char * 128),
    ('byRes', BYTE * 256),
])

NET_DVR_LOGIN_PASSWORDCFG = struct_tagNET_DVR_LOGIN_PASSWORDCFG
LPNET_DVR_LOGIN_PASSWORDCFG = POINTER(struct_tagNET_DVR_LOGIN_PASSWORDCFG)
tagNET_DVR_LOGIN_PASSWORDCFG = struct_tagNET_DVR_LOGIN_PASSWORDCFG
