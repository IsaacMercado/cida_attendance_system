from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_CASE_SENSOR_CFG(Structure):
    pass

_S(struct_tagNET_DVR_CASE_SENSOR_CFG, [
    ('dwSize', DWORD),
    ('byHostBuzzer', BYTE),
    ('byRes1', BYTE * 3),
    ('byCardReaderBuzzer', BYTE * 64),
    ('byAssociateAlarmOut', BYTE * 512),
    ('byDoorOpen', BYTE * 32),
    ('byDoorClose', BYTE * 32),
    ('byRes2', BYTE * 64),
])

NET_DVR_CASE_SENSOR_CFG = struct_tagNET_DVR_CASE_SENSOR_CFG
LPNET_DVR_CASE_SENSOR_CFG = POINTER(struct_tagNET_DVR_CASE_SENSOR_CFG)
tagNET_DVR_CASE_SENSOR_CFG = struct_tagNET_DVR_CASE_SENSOR_CFG
