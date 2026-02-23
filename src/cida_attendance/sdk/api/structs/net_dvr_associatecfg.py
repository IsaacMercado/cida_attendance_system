from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_ASSOCIATECFG(Structure):
    pass

_S(struct_tagNET_DVR_ASSOCIATECFG, [
    ('byAssociateType', BYTE),
    ('wAlarmDelay', WORD),
    ('byAlarmNum', BYTE),
    ('byRes', BYTE * 8),
])

NET_DVR_ASSOCIATECFG = struct_tagNET_DVR_ASSOCIATECFG
LPNET_DVR_ASSOCIATECFG = POINTER(struct_tagNET_DVR_ASSOCIATECFG)
tagNET_DVR_ASSOCIATECFG = struct_tagNET_DVR_ASSOCIATECFG
