from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_passback_day import NET_DVR_PASSBACK_DAY
from .net_dvr_passback_sched import NET_DVR_PASSBACK_SCHED


class struct_tagNET_DVR_RECORD_PASSBACK_SCH_CFG_(Structure):
    pass

_S(struct_tagNET_DVR_RECORD_PASSBACK_SCH_CFG_, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byPassBackWeek', BYTE),
    ('byRes1', BYTE * 2),
    ('struPassBackDay', NET_DVR_PASSBACK_DAY * 7),
    ('struPassBackSched', (NET_DVR_PASSBACK_SCHED * 8) * 7),
    ('byRes', BYTE * 128),
])

NET_DVR_RECORD_PASSBACK_SCH_CFG = struct_tagNET_DVR_RECORD_PASSBACK_SCH_CFG_
LPNET_DVR_RECORD_PASSBACK_SCH_CFG = POINTER(struct_tagNET_DVR_RECORD_PASSBACK_SCH_CFG_)
tagNET_DVR_RECORD_PASSBACK_SCH_CFG_ = struct_tagNET_DVR_RECORD_PASSBACK_SCH_CFG_
