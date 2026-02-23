from ctypes import Structure

from ..base_classes import _S, BYTE


class struct_tagNET_DVR_DECSUBSYSTEMJIONSTATUS_V41(Structure):
    pass

_S(struct_tagNET_DVR_DECSUBSYSTEMJIONSTATUS_V41, [
    ('byJoinStatus', BYTE),
    ('byJoinSubSystem', BYTE),
    ('byJoinDispNum', BYTE),
    ('byJoinSubWindowNum', BYTE),
    ('byDecodeAbility', BYTE),
    ('byRes', BYTE * 15),
])

NET_DVR_DECSUBSYSTEMJIONSTATUS_V41 = struct_tagNET_DVR_DECSUBSYSTEMJIONSTATUS_V41
LPNET_DVR_DECSUBSYSTEMJIONSTATUS_V41 = struct_tagNET_DVR_DECSUBSYSTEMJIONSTATUS_V41
tagNET_DVR_DECSUBSYSTEMJIONSTATUS_V41 = struct_tagNET_DVR_DECSUBSYSTEMJIONSTATUS_V41
