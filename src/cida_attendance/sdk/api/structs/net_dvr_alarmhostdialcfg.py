from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .net_dvr_phonecenterdialcfg import NET_DVR_PHONECENTERDIALCFG


class struct_tagNET_DVR_ALARMHOSTDIALCFG(Structure):
    pass

_S(struct_tagNET_DVR_ALARMHOSTDIALCFG, [
    ('dwSize', DWORD),
    ('struPhoneCenterParam', NET_DVR_PHONECENTERDIALCFG * 4),
    ('wReportPeriod', WORD),
    ('wFirstReportTime', WORD),
    ('byReportValid', BYTE),
    ('byRes', BYTE * 19),
])

NET_DVR_ALARMHOSTDIALCFG = struct_tagNET_DVR_ALARMHOSTDIALCFG
LPNET_DVR_ALARMHOSTDIALCFG = POINTER(struct_tagNET_DVR_ALARMHOSTDIALCFG)
tagNET_DVR_ALARMHOSTDIALCFG = struct_tagNET_DVR_ALARMHOSTDIALCFG
