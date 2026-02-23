from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_NET_DVR_SECURITY_CFG_FILE_COND(Structure):
    pass

_S(struct_NET_DVR_SECURITY_CFG_FILE_COND, [
    ('dwSize', DWORD),
    ('szSecretKey', c_char * 128),
    ('byRes', BYTE * 128),
])

NET_DVR_SECURITY_CFG_FILE_COND = struct_NET_DVR_SECURITY_CFG_FILE_COND
LPNET_DVR_SECURITY_CFG_FILE_COND = POINTER(struct_NET_DVR_SECURITY_CFG_FILE_COND)
NET_DVR_SECURITY_CFG_FILE_COND = struct_NET_DVR_SECURITY_CFG_FILE_COND
