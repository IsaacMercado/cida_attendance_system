from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_ALARM_VARIABLE_CFG(Structure):
    pass

_S(struct_tagNET_DVR_ALARM_VARIABLE_CFG, [
    ('dwSize', DWORD),
    ('wVariableIndex', WORD),
    ('wVariableType', WORD),
    ('sDescribe', BYTE * 32),
    ('byLimitLineType', BYTE),
    ('byRemoteType', BYTE),
    ('byOsdEnabled', BYTE),
    ('byRes', BYTE * 29),
])

NET_DVR_ALARM_VARIABLE_CFG = struct_tagNET_DVR_ALARM_VARIABLE_CFG
LPNET_DVR_ALARM_VARIABLE_CFG = POINTER(struct_tagNET_DVR_ALARM_VARIABLE_CFG)
tagNET_DVR_ALARM_VARIABLE_CFG = struct_tagNET_DVR_ALARM_VARIABLE_CFG
