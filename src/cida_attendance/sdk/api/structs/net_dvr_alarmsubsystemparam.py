from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .net_dvr_joint_sub_system import NET_DVR_JOINT_SUB_SYSTEM


class struct_tagNET_DVR_ALARMSUBSYSTEMPARAM(Structure):
    pass

_S(struct_tagNET_DVR_ALARMSUBSYSTEMPARAM, [
    ('dwSize', DWORD),
    ('wEnterDelay', WORD),
    ('wExitDelay', WORD),
    ('byHostageReport', BYTE),
    ('bySubsystemEnable', BYTE),
    ('byKeyToneOfArmOrDisarm', BYTE),
    ('byKeyToneOfManualTestReport', BYTE),
    ('wDelayTime', WORD),
    ('byEnableAlarmInDelay', BYTE),
    ('byPublicAttributeEnable', BYTE),
    ('struJointSubSystem', NET_DVR_JOINT_SUB_SYSTEM),
    ('byKeyZoneArm', BYTE),
    ('byKeyZoneArmReport', BYTE),
    ('byKeyZoneDisarm', BYTE),
    ('byKeyZoneDisarmReport', BYTE),
    ('bySubSystemID', BYTE * 16),
    ('byKeyZoneArmReportEnable', BYTE),
    ('byKeyZoneArmEnable', BYTE),
    ('byOneKeySetupAlarmEnable', BYTE),
    ('bySingleZoneSetupAlarmEnable', BYTE),
    ('byCenterType', BYTE),
    ('sCenterAccount', BYTE * 6),
    ('sCenterAccountV40', BYTE * 32),
    ('byRes2', BYTE * 565),
])

NET_DVR_ALARMSUBSYSTEMPARAM = struct_tagNET_DVR_ALARMSUBSYSTEMPARAM
LPNET_DVR_ALARMSUBSYSTEMPARAM = POINTER(struct_tagNET_DVR_ALARMSUBSYSTEMPARAM)
tagNET_DVR_ALARMSUBSYSTEMPARAM = struct_tagNET_DVR_ALARMSUBSYSTEMPARAM
