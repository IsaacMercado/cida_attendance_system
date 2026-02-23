from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_SETUPALARM_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_SETUPALARM_PARAM, [
    ('dwSize', DWORD),
    ('byLevel', BYTE),
    ('byAlarmInfoType', BYTE),
    ('byRetAlarmTypeV40', BYTE),
    ('byRetDevInfoVersion', BYTE),
    ('byRetVQDAlarmType', BYTE),
    ('byFaceAlarmDetection', BYTE),
    ('bySupport', BYTE),
    ('byBrokenNetHttp', BYTE),
    ('wTaskNo', WORD),
    ('byDeployType', BYTE),
    ('bySubScription', BYTE),
    ('byRes1', BYTE * 2),
    ('byAlarmTypeURL', BYTE),
    ('byCustomCtrl', BYTE),
])

NET_DVR_SETUPALARM_PARAM = struct_tagNET_DVR_SETUPALARM_PARAM
LPNET_DVR_SETUPALARM_PARAM = POINTER(struct_tagNET_DVR_SETUPALARM_PARAM)
tagNET_DVR_SETUPALARM_PARAM = struct_tagNET_DVR_SETUPALARM_PARAM
