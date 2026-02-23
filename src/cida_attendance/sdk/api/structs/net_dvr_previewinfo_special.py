from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD, HWND
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_PREVIEWINFO_SPECIAL(Structure):
    pass

_S(struct_tagNET_DVR_PREVIEWINFO_SPECIAL, [
    ('sURL', c_char * 1024),
    ('dwLinkMode', DWORD),
    ('hPlayWnd', HWND),
    ('bBlocked', DWORD),
    ('dwDisplayBufNum', DWORD),
    ('byRes', BYTE * 64),
])

NET_DVR_PREVIEWINFO_SPECIAL = struct_tagNET_DVR_PREVIEWINFO_SPECIAL
LPNET_DVR_PREVIEWINFO_SPECIAL = POINTER(struct_tagNET_DVR_PREVIEWINFO_SPECIAL)
tagNET_DVR_PREVIEWINFO_SPECIAL = struct_tagNET_DVR_PREVIEWINFO_SPECIAL
