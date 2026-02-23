from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_ITC_FTP_TYPE_COND(Structure):
    pass

_S(struct_tagNET_ITC_FTP_TYPE_COND, [
    ('dwChannel', DWORD),
    ('byWorkMode', BYTE),
    ('byRes', BYTE * 7),
])

NET_ITC_FTP_TYPE_COND = struct_tagNET_ITC_FTP_TYPE_COND
LPNET_ITC_FTP_TYPE_COND = POINTER(struct_tagNET_ITC_FTP_TYPE_COND)
tagNET_ITC_FTP_TYPE_COND = struct_tagNET_ITC_FTP_TYPE_COND
