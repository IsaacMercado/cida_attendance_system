from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_anon_93(Structure):
    pass

_S(struct_anon_93, [
    ('dwSize', DWORD),
    ('byPreviewNumber', BYTE),
    ('byEnableAudio', BYTE),
    ('wSwitchTime', WORD),
    ('bySwitchSeq', BYTE * 16),
])

NET_DVR_PREVIEWCFG = struct_anon_93
LPNET_DVR_PREVIEWCFG = POINTER(struct_anon_93)
