from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_MEASURESPEEDCFG(Structure):
    pass

_S(struct_tagNET_DVR_MEASURESPEEDCFG, [
    ('dwSize', DWORD),
    ('byTrigIo1', BYTE),
    ('byTrigIo2', BYTE),
    ('byRelatedDriveWay', BYTE),
    ('byTestSpeedTimeOut', BYTE),
    ('dwDistance', DWORD),
    ('byCapSpeed', BYTE),
    ('bySpeedLimit', BYTE),
    ('bySnapTimes1', BYTE),
    ('bySnapTimes2', BYTE),
    ('wIntervalTime1', WORD * 4),
    ('wIntervalTime2', WORD * 4),
    ('byRes', BYTE * 32),
])

NET_DVR_MEASURESPEEDCFG = struct_tagNET_DVR_MEASURESPEEDCFG
LPNET_DVR_MEASURESPEEDCFG = POINTER(struct_tagNET_DVR_MEASURESPEEDCFG)
tagNET_DVR_MEASURESPEEDCFG = struct_tagNET_DVR_MEASURESPEEDCFG
