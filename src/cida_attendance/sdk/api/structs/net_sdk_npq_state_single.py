from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_SDK_NPQ_STATE_SINGLE(Structure):
    pass

_S(struct_tagNET_SDK_NPQ_STATE_SINGLE, [
    ('dwRttUs', DWORD),
    ('dwRealRttUs', DWORD),
    ('dwBitRate', DWORD),
    ('byLossFraction', BYTE),
    ('byLossFraction2', BYTE),
    ('byRes', BYTE * 126),
])

NET_SDK_NPQ_STATE_SINGLE = struct_tagNET_SDK_NPQ_STATE_SINGLE
LPNET_SDK_NPQ_STATE_SINGLE = POINTER(struct_tagNET_SDK_NPQ_STATE_SINGLE)
tagNET_SDK_NPQ_STATE_SINGLE = struct_tagNET_SDK_NPQ_STATE_SINGLE
