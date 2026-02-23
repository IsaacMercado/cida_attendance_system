from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_anon_184(Structure):
    pass

_S(struct_anon_184, [
    ('dwSize', DWORD),
    ('sUserName', c_char * 32),
    ('sPassWord', c_char * 32),
    ('sFromName', c_char * 32),
    ('sFromAddr', c_char * 48),
    ('sToName1', c_char * 32),
    ('sToName2', c_char * 32),
    ('sToAddr1', c_char * 48),
    ('sToAddr2', c_char * 48),
    ('sEmailServer', c_char * 32),
    ('byServerType', BYTE),
    ('byUseAuthen', BYTE),
    ('byAttachment', BYTE),
    ('byMailinterval', BYTE),
])

NET_DVR_EMAILCFG = struct_anon_184
LPNET_DVR_EMAILCFG = POINTER(struct_anon_184)
