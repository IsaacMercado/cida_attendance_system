from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_USER_RIGHT_CFG(Structure):
    pass

_S(struct_tagNET_DVR_USER_RIGHT_CFG, [
    ('dwSize', DWORD),
    ('byAddMonitoringPointRight', BYTE),
    ('byModMonitoringPointRight', BYTE),
    ('byDelMonitoringPointRight', BYTE),
    ('bySetRecordPlanRight', BYTE),
    ('byDelRecordPlanRight', BYTE),
    ('byEnableOrDisableRecordPlanRight', BYTE),
    ('byManualRecordRight', BYTE),
    ('bySetAlarmRecordRight', BYTE),
    ('byRecordBackupRight', BYTE),
    ('byRecordDownloadRight', BYTE),
    ('byRecordDeleteRight', BYTE),
    ('byDelBackupRecordRight', BYTE),
    ('bySetBackupVolumeRight', BYTE),
    ('byRecordPlayBackRight', BYTE),
    ('byLogDeleteRight', BYTE),
    ('byLogDownloadRight', BYTE),
    ('byAddUserRight', BYTE),
    ('byDelUserRight', BYTE),
    ('byModUserRight', BYTE),
    ('byAllocUserRight', BYTE),
    ('byRes', BYTE * 128),
])

NET_DVR_USER_RIGHT_CFG = struct_tagNET_DVR_USER_RIGHT_CFG
LPNET_DVR_USER_RIGHT_CFG = POINTER(struct_tagNET_DVR_USER_RIGHT_CFG)
tagNET_DVR_USER_RIGHT_CFG = struct_tagNET_DVR_USER_RIGHT_CFG
