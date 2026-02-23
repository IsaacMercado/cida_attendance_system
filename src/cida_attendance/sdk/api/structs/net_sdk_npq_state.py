from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_sdk_npq_state_single import NET_SDK_NPQ_STATE_SINGLE


class struct_tagNET_SDK_NPQ_STATE(Structure):
    pass

_S(struct_tagNET_SDK_NPQ_STATE, [
    ('dwSize', DWORD),
    ('struAudioState', NET_SDK_NPQ_STATE_SINGLE),
    ('struVideoState', NET_SDK_NPQ_STATE_SINGLE),
    ('byRes', BYTE * 256),
])

NET_SDK_NPQ_STATE = struct_tagNET_SDK_NPQ_STATE
LPNET_SDK_NPQ_STATE = POINTER(struct_tagNET_SDK_NPQ_STATE)
tagNET_SDK_NPQ_STATE = struct_tagNET_SDK_NPQ_STATE
