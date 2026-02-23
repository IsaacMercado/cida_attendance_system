from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_SETUPALARM_PARAM_V50(Structure):
    pass

_S(struct_tagNET_DVR_SETUPALARM_PARAM_V50, [
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
    ('byBrokenNetHttpV60', BYTE),
    ('byRes1', BYTE),
    ('byAlarmTypeURL', BYTE),
    ('byCustomCtrl', BYTE),
    ('byRes4', BYTE * 128),
])

NET_DVR_SETUPALARM_PARAM_V50 = struct_tagNET_DVR_SETUPALARM_PARAM_V50
LPNET_DVR_SETUPALARM_PARAM_V50 = POINTER(struct_tagNET_DVR_SETUPALARM_PARAM_V50)
tagNET_DVR_SETUPALARM_PARAM_V50 = struct_tagNET_DVR_SETUPALARM_PARAM_V50
