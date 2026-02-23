from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_ALARMHOST_FAULT_CFG(Structure):
    pass

_S(struct_tagNET_DVR_ALARMHOST_FAULT_CFG, [
    ('dwSize', DWORD),
    ('dwCheckFault', DWORD),
    ('dwOverallFaultJointLED', DWORD),
    ('dwOverallFaultJointSound', DWORD),
    ('dwSubSystemFaultJointLED', DWORD * 32),
    ('dwSubSystemFaultJointSound', DWORD * 32),
    ('dwFaultJointFaultLight', DWORD),
    ('byRes', BYTE * 60),
])

NET_DVR_ALARMHOST_FAULT_CFG = struct_tagNET_DVR_ALARMHOST_FAULT_CFG
LPNET_DVR_ALARMHOST_FAULT_CFG = POINTER(struct_tagNET_DVR_ALARMHOST_FAULT_CFG)
tagNET_DVR_ALARMHOST_FAULT_CFG = struct_tagNET_DVR_ALARMHOST_FAULT_CFG
