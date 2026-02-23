from ctypes import Structure

from ..base_classes import _S, BYTE, WORD


class struct_anon_97(Structure):
    pass

_S(struct_anon_97, [
    ('byVideoFormat', BYTE),
    ('byMenuAlphaValue', BYTE),
    ('wScreenSaveTime', WORD),
    ('wVOffset', WORD),
    ('wBrightness', WORD),
    ('byStartMode', BYTE),
    ('byEnableScaler', BYTE),
])

NET_DVR_VOOUT = struct_anon_97
