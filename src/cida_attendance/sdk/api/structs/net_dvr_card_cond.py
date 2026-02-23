from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct__NET_DVR_CARD_COND(Structure):
    pass

_S(struct__NET_DVR_CARD_COND, [
    ('dwSize', DWORD),
    ('dwCardNum', DWORD),
    ('byRes', BYTE * 64),
])

NET_DVR_CARD_COND = struct__NET_DVR_CARD_COND
LPNET_DVR_CARD_COND = POINTER(struct__NET_DVR_CARD_COND)
_NET_DVR_CARD_COND = struct__NET_DVR_CARD_COND
