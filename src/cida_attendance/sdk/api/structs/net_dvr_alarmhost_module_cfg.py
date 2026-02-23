from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_ALARMHOST_MODULE_CFG(Structure):
    pass

_S(struct_tagNET_DVR_ALARMHOST_MODULE_CFG, [
    ('dwSize', DWORD),
    ('byModuleType', BYTE),
    ('byZoneType', BYTE),
    ('byTriggerType', BYTE),
    ('byRes1', BYTE * 1),
    ('sModelInfo', c_char * 32),
    ('sDeviceVersionInfo', c_char * 32),
    ('byRes', BYTE * 188),
])

NET_DVR_ALARMHOST_MODULE_CFG = struct_tagNET_DVR_ALARMHOST_MODULE_CFG
LPNET_DVR_ALARMHOST_MODULE_CFG = POINTER(struct_tagNET_DVR_ALARMHOST_MODULE_CFG)
tagNET_DVR_ALARMHOST_MODULE_CFG = struct_tagNET_DVR_ALARMHOST_MODULE_CFG
