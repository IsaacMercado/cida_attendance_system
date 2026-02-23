from ctypes import Structure, c_int

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_VIDEOPLATFORM_ALRAMINFO(Structure):
    pass

_S(struct_tagNET_DVR_VIDEOPLATFORM_ALRAMINFO, [
    ('dwSize', DWORD),
    ('byAlarmType', BYTE),
    ('byBoardNum', BYTE),
    ('byRes1', BYTE * 2),
    ('bySubSystemChan', BYTE * 8),
    ('iTemperature', c_int),
    ('byMainboardSeq', BYTE),
    ('byRes2', BYTE * 3),
    ('byFanSequence', BYTE * 32),
    ('byRes3', BYTE * 100),
])

NET_DVR_VIDEOPLATFORM_ALRAMINFO = struct_tagNET_DVR_VIDEOPLATFORM_ALRAMINFO
LPNET_DVR_VIDEOPLATFORM_ALRAMINFO = POINTER(struct_tagNET_DVR_VIDEOPLATFORM_ALRAMINFO)
tagNET_DVR_VIDEOPLATFORM_ALRAMINFO = struct_tagNET_DVR_VIDEOPLATFORM_ALRAMINFO
