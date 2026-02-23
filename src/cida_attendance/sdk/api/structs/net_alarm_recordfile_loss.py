from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR
from .net_dvr_time_ex import NET_DVR_TIME_EX


class struct_tagNET_ALARM_RECORDFILE_LOSS(Structure):
    pass

_S(struct_tagNET_ALARM_RECORDFILE_LOSS, [
    ('struInspectStart', NET_DVR_TIME_EX),
    ('struInspectEnd', NET_DVR_TIME_EX),
    ('struIP', NET_DVR_IPADDR),
    ('dwChanNo', DWORD),
    ('dwIDIndex', DWORD),
    ('sName', BYTE * 32),
    ('struLossStartTime', NET_DVR_TIME_EX),
    ('struLossEndTime', NET_DVR_TIME_EX),
    ('dwLostNum', DWORD),
    ('byRes', BYTE * 240),
])

NET_ALARM_RECORDFILE_LOSS = struct_tagNET_ALARM_RECORDFILE_LOSS
LPNET_ALARM_RECORDFILE_LOSS = POINTER(struct_tagNET_ALARM_RECORDFILE_LOSS)
tagNET_ALARM_RECORDFILE_LOSS = struct_tagNET_ALARM_RECORDFILE_LOSS
