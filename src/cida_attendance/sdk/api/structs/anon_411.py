from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_pos_osd_region import NET_DVR_POS_OSD_REGION


class struct_anon_411(Structure):
    pass

_S(struct_anon_411, [
    ('dwDelayTime', DWORD),
    ('byPrevOsd', BYTE),
    ('byRes1', BYTE * 3),
    ('struOsdPosInfo', NET_DVR_POS_OSD_REGION),
    ('byRes', BYTE * 64),
])

NET_DVR_POS_ACTION = struct_anon_411
LPNET_DVR_POS_ACTION = POINTER(struct_anon_411)
