from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct__NET_DVR_CARD_CFG_COND(Structure):
    pass

_S(struct__NET_DVR_CARD_CFG_COND, [
    ('dwSize', DWORD),
    ('dwCardNum', DWORD),
    ('byCheckCardNo', BYTE),
    ('byRes1', BYTE * 3),
    ('wLocalControllerID', WORD),
    ('byRes2', BYTE * 2),
    ('dwLockID', DWORD),
    ('byRes3', BYTE * 20),
])

NET_DVR_CARD_CFG_COND = struct__NET_DVR_CARD_CFG_COND
LPNET_DVR_CARD_CFG_COND = POINTER(struct__NET_DVR_CARD_CFG_COND)
_NET_DVR_CARD_CFG_COND = struct__NET_DVR_CARD_CFG_COND
