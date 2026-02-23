from ctypes import Structure

from ..base_classes import _S, DWORD


class struct_anon_143(Structure):
    pass

_S(struct_anon_143, [
    ('dwMonth', DWORD),
    ('dwWeekNo', DWORD),
    ('dwWeekDate', DWORD),
    ('dwHour', DWORD),
    ('dwMin', DWORD),
])

NET_DVR_TIMEPOINT = struct_anon_143
