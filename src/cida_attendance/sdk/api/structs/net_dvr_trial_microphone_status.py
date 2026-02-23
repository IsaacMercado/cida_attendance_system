from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct__NET_DVR_TRIAL_MICROPHONE_STATUS(Structure):
    pass

_S(struct__NET_DVR_TRIAL_MICROPHONE_STATUS, [
    ('dwSize', DWORD),
    ('byMicrophoneStatus', BYTE * 16),
    ('byRes', BYTE * 32),
])

NET_DVR_TRIAL_MICROPHONE_STATUS = struct__NET_DVR_TRIAL_MICROPHONE_STATUS
LPNET_DVR_TRIAL_MICROPHONE_STATUS = POINTER(struct__NET_DVR_TRIAL_MICROPHONE_STATUS)
_NET_DVR_TRIAL_MICROPHONE_STATUS = struct__NET_DVR_TRIAL_MICROPHONE_STATUS
