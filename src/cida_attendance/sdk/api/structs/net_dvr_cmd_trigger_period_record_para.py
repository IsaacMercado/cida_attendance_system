from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_stream_info import NET_DVR_STREAM_INFO


class struct_tagNET_DVR_CMD_TRIGGER_PERIOD_RECORD_PARA(Structure):
    pass

_S(struct_tagNET_DVR_CMD_TRIGGER_PERIOD_RECORD_PARA, [
    ('struStreamInfo', NET_DVR_STREAM_INFO),
    ('dwCmdType', DWORD),
    ('dwRecordTimeLen', DWORD),
    ('byEventID', BYTE * 64),
    ('dwLockDuration', DWORD),
    ('byBackUp', BYTE),
    ('byPreRecord', BYTE),
    ('byRes', BYTE * 122),
])

NET_DVR_CMD_TRIGGER_PERIOD_RECORD_PARA = struct_tagNET_DVR_CMD_TRIGGER_PERIOD_RECORD_PARA
LPNET_DVR_CMD_TRIGGER_PERIOD_RECORD_PARA = POINTER(struct_tagNET_DVR_CMD_TRIGGER_PERIOD_RECORD_PARA)
tagNET_DVR_CMD_TRIGGER_PERIOD_RECORD_PARA = struct_tagNET_DVR_CMD_TRIGGER_PERIOD_RECORD_PARA
