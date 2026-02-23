from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from ..functions import DEV_WORK_STATE_CB


class struct_tagNetDVRCheckDevState(Structure):
    pass

_S(struct_tagNetDVRCheckDevState, [
    ('dwTimeout', DWORD),
    ('fnStateCB', DEV_WORK_STATE_CB),
    ('pUserData', POINTER(None)),
    ('byRes', BYTE * 60),
])

NET_DVR_CHECK_DEV_STATE = struct_tagNetDVRCheckDevState
LPNET_DVR_CHECK_DEV_STATE = POINTER(struct_tagNetDVRCheckDevState)
tagNetDVRCheckDevState = struct_tagNetDVRCheckDevState
