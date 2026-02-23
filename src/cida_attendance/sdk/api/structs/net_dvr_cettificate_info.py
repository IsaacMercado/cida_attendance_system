from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_1 import NET_DVR_TIME


class struct_tagNET_DVR_CETTIFICATE_INFO(Structure):
    pass

_S(struct_tagNET_DVR_CETTIFICATE_INFO, [
    ('dwSize', DWORD),
    ('szIssuer', c_char * 64),
    ('szSubject', c_char * 64),
    ('struStartTime', NET_DVR_TIME),
    ('struEndTime', NET_DVR_TIME),
    ('byRes1', BYTE * 1024),
])

NET_DVR_CETTIFICATE_INFO = struct_tagNET_DVR_CETTIFICATE_INFO
LPNET_DVR_CETTIFICATE_INFO = POINTER(struct_tagNET_DVR_CETTIFICATE_INFO)
tagNET_DVR_CETTIFICATE_INFO = struct_tagNET_DVR_CETTIFICATE_INFO
