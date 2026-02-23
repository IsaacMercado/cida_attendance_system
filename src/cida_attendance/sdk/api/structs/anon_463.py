from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from .net_dvr_time_segment import NET_DVR_TIME_SEGMENT


class struct_anon_463(Structure):
    pass

_S(struct_anon_463, [
    ('dwPlayPlanNo', DWORD),
    ('struTime', NET_DVR_TIME_SEGMENT),
    ('byPlayType', BYTE),
    ('byRes', BYTE * 3),
    ('dwPlaylistNo', DWORD),
    ('byPlaylistName', BYTE * 32),
    ('dwPlayItem', DWORD),
    ('byPlayItemName', BYTE * 32),
    ('wPlayIndex', WORD),
    ('byRes2', BYTE * 18),
])

