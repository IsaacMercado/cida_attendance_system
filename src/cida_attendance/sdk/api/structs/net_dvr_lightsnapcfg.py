from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_LIGHTSNAPCFG(Structure):
    pass

_S(struct_tagNET_DVR_LIGHTSNAPCFG, [
    ('dwSize', DWORD),
    ('byLightIoIn', BYTE),
    ('byTrigIoIn', BYTE),
    ('byRelatedDriveWay', BYTE),
    ('byTrafficLight', BYTE),
    ('bySnapTimes1', BYTE),
    ('bySnapTimes2', BYTE),
    ('byRes1', BYTE * 2),
    ('wIntervalTime1', WORD * 4),
    ('wIntervalTime2', WORD * 4),
    ('byRecord', BYTE),
    ('bySessionTimeout', BYTE),
    ('byPreRecordTime', BYTE),
    ('byVideoDelay', BYTE),
    ('byRes2', BYTE * 32),
])

NET_DVR_LIGHTSNAPCFG = struct_tagNET_DVR_LIGHTSNAPCFG
LPNET_DVR_LIGHTSNAPCFG = POINTER(struct_tagNET_DVR_LIGHTSNAPCFG)
tagNET_DVR_LIGHTSNAPCFG = struct_tagNET_DVR_LIGHTSNAPCFG
