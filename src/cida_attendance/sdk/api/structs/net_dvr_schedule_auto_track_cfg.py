from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_day_schedule import NET_DVR_DAY_SCHEDULE


class struct_tagNET_DVR_SCHEDULE_AUTO_TRACK_CFG(Structure):
    pass

_S(struct_tagNET_DVR_SCHEDULE_AUTO_TRACK_CFG, [
    ('dwSize', DWORD),
    ('byEnableTrack', BYTE),
    ('byRes1', BYTE * 3),
    ('struSchedule', NET_DVR_DAY_SCHEDULE * 7),
    ('byRes2', BYTE * 128),
])

NET_DVR_SCHEDULE_AUTO_TRACK_CFG = struct_tagNET_DVR_SCHEDULE_AUTO_TRACK_CFG
LPNET_DVR_SCHEDULE_AUTO_TRACK_CFG = POINTER(struct_tagNET_DVR_SCHEDULE_AUTO_TRACK_CFG)
tagNET_DVR_SCHEDULE_AUTO_TRACK_CFG = struct_tagNET_DVR_SCHEDULE_AUTO_TRACK_CFG
