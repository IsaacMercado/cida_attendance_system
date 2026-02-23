from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct__NET_DVR_CARD_STATUS(Structure):
    pass

_S(struct__NET_DVR_CARD_STATUS, [
    ('dwSize', DWORD),
    ('byCardNo', BYTE * 32),
    ('dwErrorCode', DWORD),
    ('byStatus', BYTE),
    ('byRes', BYTE * 23),
])

NET_DVR_CARD_STATUS = struct__NET_DVR_CARD_STATUS
LPNET_DVR_CARD_STATUS = POINTER(struct__NET_DVR_CARD_STATUS)
_NET_DVR_CARD_STATUS = struct__NET_DVR_CARD_STATUS
