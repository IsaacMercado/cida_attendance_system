from ctypes import Structure

from ..base_classes import _S, DWORD, WORD


class struct_anon_94(Structure):
    pass

_S(struct_anon_94, [
    ('wResolution', WORD),
    ('wFreq', WORD),
    ('dwBrightness', DWORD),
])

NET_DVR_VGAPARA = struct_anon_94
