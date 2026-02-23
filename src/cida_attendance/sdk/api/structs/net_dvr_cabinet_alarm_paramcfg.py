from ctypes import Structure, c_char

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_CABINET_AlARM_PARAMCFG(Structure):
    pass

_S(struct_tagNET_DVR_CABINET_AlARM_PARAMCFG, [
    ('sCabinetName', c_char * 32),
    ('byAssociateIO', BYTE),
    ('byCabinetState', BYTE),
    ('byAlarmIntervalTime', BYTE),
    ('byRes1', BYTE * 25),
])

NET_DVR_CABINET_AlARM_PARAMCFG = struct_tagNET_DVR_CABINET_AlARM_PARAMCFG
LPNET_DVR_CABINET_AlARM_PARAMCFG = POINTER(struct_tagNET_DVR_CABINET_AlARM_PARAMCFG)
tagNET_DVR_CABINET_AlARM_PARAMCFG = struct_tagNET_DVR_CABINET_AlARM_PARAMCFG
