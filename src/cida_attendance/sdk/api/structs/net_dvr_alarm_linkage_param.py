from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_ALARM_LINKAGE_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_ALARM_LINKAGE_PARAM, [
    ('dwSize', DWORD),
    ('wChanRec', WORD),
    ('byRes1', BYTE * 2),
    ('wRecTime', WORD * 16),
    ('wChanPic', WORD),
    ('byRes2', BYTE * 2),
    ('byPicNum', BYTE * 16),
    ('byTriggerEnabled', BYTE * 64),
    ('bySensorJointAlarmOut', BYTE * 64),
    ('byRes3', BYTE * 128),
])

NET_DVR_ALARM_LINKAGE_PARAM = struct_tagNET_DVR_ALARM_LINKAGE_PARAM
LPNET_DVR_ALARM_LINKAGE_PARAM = POINTER(struct_tagNET_DVR_ALARM_LINKAGE_PARAM)
tagNET_DVR_ALARM_LINKAGE_PARAM = struct_tagNET_DVR_ALARM_LINKAGE_PARAM
