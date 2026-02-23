from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_IPC_PASSWD(Structure):
    pass

_S(struct_tagNET_DVR_IPC_PASSWD, [
    ('dwSize', DWORD),
    ('sOldPasswd', c_char * 16),
    ('sNewPasswd', c_char * 16),
    ('byRes', BYTE * 32),
])

NET_DVR_IPC_PASSWD = struct_tagNET_DVR_IPC_PASSWD
LPNET_DVR_IPC_PASSWD = POINTER(struct_tagNET_DVR_IPC_PASSWD)
tagNET_DVR_IPC_PASSWD = struct_tagNET_DVR_IPC_PASSWD
