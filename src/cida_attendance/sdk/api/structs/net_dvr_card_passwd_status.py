from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_CARD_PASSWD_STATUS(Structure):
    pass

_S(struct_tagNET_DVR_CARD_PASSWD_STATUS, [
    ('dwSize', DWORD),
    ('byCardNo', BYTE * 32),
    ('dwErrorCode', DWORD),
    ('byRes2', BYTE * 24),
])

NET_DVR_CARD_PASSWD_STATUS = struct_tagNET_DVR_CARD_PASSWD_STATUS
LPNET_DVR_CARD_PASSWD_STATUS = POINTER(struct_tagNET_DVR_CARD_PASSWD_STATUS)
tagNET_DVR_CARD_PASSWD_STATUS = struct_tagNET_DVR_CARD_PASSWD_STATUS
