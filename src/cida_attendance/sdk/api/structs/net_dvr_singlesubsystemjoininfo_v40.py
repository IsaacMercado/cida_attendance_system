from ctypes import Structure

from ..base_classes import _S, BYTE
from .net_dvr_decsubsystemjionstatus import NET_DVR_DECSUBSYSTEMJIONSTATUS


class struct_tagNET_DVR_SINGLESUBSYSTEMJOININFO_V40(Structure):
    pass

_S(struct_tagNET_DVR_SINGLESUBSYSTEMJOININFO_V40, [
    ('bySubSystemType', BYTE),
    ('byConnectStatus', BYTE),
    ('byMatrixNum', BYTE),
    ('bySubSystemNum', BYTE),
    ('struDecSub', NET_DVR_DECSUBSYSTEMJIONSTATUS * 4),
    ('byBindStatus', BYTE),
    ('bySlotNum', BYTE),
    ('byDecodeAbility', BYTE),
    ('byUsedTrunk', BYTE),
    ('byRes', BYTE * 64),
])

NET_DVR_SINGLESUBSYSTEMJOININFO_V40 = struct_tagNET_DVR_SINGLESUBSYSTEMJOININFO_V40
LPNET_DVR_SINGLESUBSYSTEMJOININFO_V40 = struct_tagNET_DVR_SINGLESUBSYSTEMJOININFO_V40
tagNET_DVR_SINGLESUBSYSTEMJOININFO_V40 = struct_tagNET_DVR_SINGLESUBSYSTEMJOININFO_V40
