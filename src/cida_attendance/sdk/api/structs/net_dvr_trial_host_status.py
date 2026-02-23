from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct__NET_DVR_TRIAL_HOST_STATUS(Structure):
    pass

_S(struct__NET_DVR_TRIAL_HOST_STATUS, [
    ('dwSize', DWORD),
    ('dwFanSpeed', DWORD * 8),
    ('wMainBoardTemp', WORD * 8),
    ('byFpgaTempWarn', BYTE * 8),
    ('byRes', BYTE * 32),
])

NET_DVR_TRIAL_HOST_STATUS = struct__NET_DVR_TRIAL_HOST_STATUS
LPNET_DVR_TRIAL_HOST_STATUS = POINTER(struct__NET_DVR_TRIAL_HOST_STATUS)
_NET_DVR_TRIAL_HOST_STATUS = struct__NET_DVR_TRIAL_HOST_STATUS
