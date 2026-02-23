from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, LONG
from ..ctypes_preamble import POINTER
from .anon_1 import NET_DVR_TIME


class struct_anon_205(Structure):
    pass

_S(struct_anon_205, [
    ('lChannel', LONG),
    ('dwFileType', DWORD),
    ('dwIsLocked', DWORD),
    ('dwUseCardNo', DWORD),
    ('sCardNumber', BYTE * 32),
    ('struStartTime', NET_DVR_TIME),
    ('struStopTime', NET_DVR_TIME),
])

NET_DVR_FILECOND = struct_anon_205
LPNET_DVR_FILECOND = POINTER(struct_anon_205)
