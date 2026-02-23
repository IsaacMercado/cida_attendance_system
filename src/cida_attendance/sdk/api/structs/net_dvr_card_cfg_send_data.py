from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct__NET_DVR_CARD_CFG_SEND_DATA(Structure):
    pass

_S(struct__NET_DVR_CARD_CFG_SEND_DATA, [
    ('dwSize', DWORD),
    ('byCardNo', BYTE * 32),
    ('dwCardUserId', DWORD),
    ('byRes', BYTE * 12),
])

NET_DVR_CARD_CFG_SEND_DATA = struct__NET_DVR_CARD_CFG_SEND_DATA
LPNET_DVR_CARD_CFG_SEND_DATA = POINTER(struct__NET_DVR_CARD_CFG_SEND_DATA)
_NET_DVR_CARD_CFG_SEND_DATA = struct__NET_DVR_CARD_CFG_SEND_DATA
