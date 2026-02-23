from ctypes import Structure, c_float

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_TAMPER_ALARMIN_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_TAMPER_ALARMIN_PARAM, [
    ('dwSize', DWORD),
    ('byTamperType', BYTE),
    ('byUploadAlarmRecoveryReport', BYTE),
    ('byRes1', BYTE * 2),
    ('byAssociateAlarmOut', BYTE * 512),
    ('byAssociateSirenOut', BYTE * 8),
    ('byTamperResistor', BYTE),
    ('byRes2', BYTE * 3),
    ('fTamperResistorManual', c_float),
    ('byRes3', BYTE * 36),
])

NET_DVR_TAMPER_ALARMIN_PARAM = struct_tagNET_DVR_TAMPER_ALARMIN_PARAM
LPNET_DVR_TAMPER_ALARMIN_PARAM = POINTER(struct_tagNET_DVR_TAMPER_ALARMIN_PARAM)
tagNET_DVR_TAMPER_ALARMIN_PARAM = struct_tagNET_DVR_TAMPER_ALARMIN_PARAM
