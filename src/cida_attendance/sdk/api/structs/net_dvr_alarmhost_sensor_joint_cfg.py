from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_ALARMHOST_SENSOR_JOINT_CFG(Structure):
    pass

_S(struct_tagNET_DVR_ALARMHOST_SENSOR_JOINT_CFG, [
    ('dwSize', DWORD),
    ('bySensorJointAlarmOut', BYTE * 512),
    ('bySensorJointSiren', BYTE * 8),
    ('bySensorAlarmTypeJointAlarmOut', BYTE * 64),
    ('bySesorAlarmTypeJointSiren', BYTE * 8),
    ('byChan', BYTE),
    ('byRes', BYTE * 55),
])

NET_DVR_ALARMHOST_SENSOR_JOINT_CFG = struct_tagNET_DVR_ALARMHOST_SENSOR_JOINT_CFG
LPNET_DVR_ALARMHOST_SENSOR_JOINT_CFG = POINTER(struct_tagNET_DVR_ALARMHOST_SENSOR_JOINT_CFG)
tagNET_DVR_ALARMHOST_SENSOR_JOINT_CFG = struct_tagNET_DVR_ALARMHOST_SENSOR_JOINT_CFG
