from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_anon_299(Structure):
    pass

_S(struct_anon_299, [
    ('byStrFlag', BYTE),
    ('byEndFlag', BYTE),
    ('wCardIdx', WORD),
    ('dwCardLen', DWORD),
    ('dwTriggerPicChans', DWORD),
])

NET_DVR_SERIAL_CATCHPIC_PARA = struct_anon_299
LPNET_DVR_SERIAL_CATCHPIC_PARA = POINTER(struct_anon_299)
