from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_pu_stream_cfg_v41 import NET_DVR_PU_STREAM_CFG_V41
from .net_dvr_time_v30 import NET_DVR_TIME_V30


class struct_tagNET_DVR_DEC_VCA_ALARM(Structure):
    pass

_S(struct_tagNET_DVR_DEC_VCA_ALARM, [
    ('dwSize', DWORD),
    ('dwDisplayNo', DWORD),
    ('bySubWinNo', BYTE),
    ('byRes1', BYTE * 3),
    ('struTime', NET_DVR_TIME_V30),
    ('struSourceInfo', NET_DVR_PU_STREAM_CFG_V41),
    ('byAlarmPic', POINTER(BYTE)),
    ('dwAlarmPicSize', DWORD),
    ('byRes2', BYTE * 64),
])

NET_DVR_DEC_VCA_ALARM = struct_tagNET_DVR_DEC_VCA_ALARM
LPNET_DVR_DEC_VCA_ALARM = POINTER(struct_tagNET_DVR_DEC_VCA_ALARM)
tagNET_DVR_DEC_VCA_ALARM = struct_tagNET_DVR_DEC_VCA_ALARM
