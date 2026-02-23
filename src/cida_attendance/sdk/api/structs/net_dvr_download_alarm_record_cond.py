from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_DOWNLOAD_ALARM_RECORD_COND(Structure):
    pass

_S(struct_tagNET_DVR_DOWNLOAD_ALARM_RECORD_COND, [
    ('dwSize', DWORD),
    ('wAlarmRecordID', WORD),
    ('byRes', BYTE * 130),
])

NET_DVR_DOWNLOAD_ALARM_RECORD_COND = struct_tagNET_DVR_DOWNLOAD_ALARM_RECORD_COND
LPNET_DVR_DOWNLOAD_ALARM_RECORD_COND = POINTER(struct_tagNET_DVR_DOWNLOAD_ALARM_RECORD_COND)
tagNET_DVR_DOWNLOAD_ALARM_RECORD_COND = struct_tagNET_DVR_DOWNLOAD_ALARM_RECORD_COND
