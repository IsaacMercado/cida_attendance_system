from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_NOTICE_PIC(Structure):
    pass

_S(struct_tagNET_DVR_NOTICE_PIC, [
    ('pPicData', POINTER(BYTE)),
    ('dwPicDataLen', DWORD),
    ('byRes', BYTE * 32),
])

NET_DVR_NOTICE_PIC = struct_tagNET_DVR_NOTICE_PIC
LPNET_DVR_NOTICE_PIC = POINTER(struct_tagNET_DVR_NOTICE_PIC)
tagNET_DVR_NOTICE_PIC = struct_tagNET_DVR_NOTICE_PIC
