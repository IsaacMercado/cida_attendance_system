from ctypes import Structure

from ..base_classes import _S, BYTE
from .net_dvr_decsubsystemjionstatus_v41 import NET_DVR_DECSUBSYSTEMJIONSTATUS_V41


class struct_tagNET_DVR_SINGLESUBSYSTEMJOININFO_V41(Structure):
    pass

_S(struct_tagNET_DVR_SINGLESUBSYSTEMJOININFO_V41, [
    ('bySubSystemType', BYTE),
    ('byConnectStatus', BYTE),
    ('byMatrixNum', BYTE),
    ('bySubSystemNum', BYTE),
    ('struSubSystem', NET_DVR_DECSUBSYSTEMJIONSTATUS_V41 * 32),
    ('byBindStatus', BYTE),
    ('bySlotNum', BYTE),
    ('byUsedTrunk', BYTE),
    ('byRes', BYTE * 65),
])

NET_DVR_SINGLESUBSYSTEMJOININFO_V41 = struct_tagNET_DVR_SINGLESUBSYSTEMJOININFO_V41
LPNET_DVR_SINGLESUBSYSTEMJOININFO_V41 = struct_tagNET_DVR_SINGLESUBSYSTEMJOININFO_V41
tagNET_DVR_SINGLESUBSYSTEMJOININFO_V41 = struct_tagNET_DVR_SINGLESUBSYSTEMJOININFO_V41
