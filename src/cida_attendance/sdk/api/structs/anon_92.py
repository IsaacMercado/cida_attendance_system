from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_anon_92(Structure):
    pass

_S(struct_anon_92, [
    ('dwSize', DWORD),
    ('byPreviewNumber', BYTE),
    ('byEnableAudio', BYTE),
    ('wSwitchTime', WORD),
    ('bySwitchSeq', (BYTE * 32) * 8),
    ('byRes', BYTE * 24),
])

NET_DVR_PREVIEWCFG_V30 = struct_anon_92
LPNET_DVR_PREVIEWCFG_V30 = POINTER(struct_anon_92)
