from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, LONG
from ..ctypes_preamble import POINTER
from .net_dvr_time_ex import NET_DVR_TIME_EX


class struct_tagNET_DVR_GOP_INFO(Structure):
    pass

_S(struct_tagNET_DVR_GOP_INFO, [
    ('dwSize', DWORD),
    ('lChannel', LONG),
    ('struStartTime', NET_DVR_TIME_EX),
    ('struEndTime', NET_DVR_TIME_EX),
    ('byRes', BYTE * 256),
])

NET_DVR_GOP_INFO = struct_tagNET_DVR_GOP_INFO
LPNET_DVR_GOP_INFO = POINTER(struct_tagNET_DVR_GOP_INFO)
tagNET_DVR_GOP_INFO = struct_tagNET_DVR_GOP_INFO
