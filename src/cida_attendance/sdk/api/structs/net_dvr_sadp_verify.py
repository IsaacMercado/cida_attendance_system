from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR


class struct_tagNET_DVR_SADP_VERIFY(Structure):
    pass

_S(struct_tagNET_DVR_SADP_VERIFY, [
    ('chPassword', c_char * 16),
    ('struOldIP', NET_DVR_IPADDR),
    ('wOldPort', WORD),
    ('byRes', BYTE * 62),
])

NET_DVR_SADP_VERIFY = struct_tagNET_DVR_SADP_VERIFY
LPNET_DVR_SADP_VERIFY = POINTER(struct_tagNET_DVR_SADP_VERIFY)
tagNET_DVR_SADP_VERIFY = struct_tagNET_DVR_SADP_VERIFY
