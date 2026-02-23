from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_anon_183(Structure):
    pass

_S(struct_anon_183, [
    ('byDispStatus', BYTE),
    ('byBVGA', BYTE),
    ('byVideoFormat', BYTE),
    ('byWindowMode', BYTE),
    ('byJoinDecChan', BYTE * 16),
    ('byFpsDisp', BYTE * 16),
    ('byRes2', BYTE * 32),
])

NET_DVR_DISP_CHAN_STATUS = struct_anon_183
LPNET_DVR_DISP_CHAN_STATUS = POINTER(struct_anon_183)
