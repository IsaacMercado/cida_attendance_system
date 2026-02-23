from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD, HWND, LONG, WORD
from ..ctypes_preamble import POINTER
from .anon_1 import NET_DVR_TIME
from .anon_2 import NET_DVR_IPADDR


class struct_tagNET_DVR_PLAYBCK_BYTIME_COND_PCNVR(Structure):
    pass

_S(struct_tagNET_DVR_PLAYBCK_BYTIME_COND_PCNVR, [
    ('dwSize', DWORD),
    ('struIpAddr', NET_DVR_IPADDR),
    ('wIpPort', WORD),
    ('byRes', BYTE * 2),
    ('sDomainName', c_char * 64),
    ('sSerial', c_char * 48),
    ('iChannel', LONG),
    ('struStartTime', NET_DVR_TIME),
    ('struStopTime', NET_DVR_TIME),
    ('hWnd', HWND),
])

NET_DVR_PLAYBCK_BYTIME_COND_PCNVR = struct_tagNET_DVR_PLAYBCK_BYTIME_COND_PCNVR
LPNET_DVR_PLAYBCK_BYTIME_COND_PCNVR = POINTER(struct_tagNET_DVR_PLAYBCK_BYTIME_COND_PCNVR)
tagNET_DVR_PLAYBCK_BYTIME_COND_PCNVR = struct_tagNET_DVR_PLAYBCK_BYTIME_COND_PCNVR
