from ctypes import Structure

from ..base_classes import _S, BYTE


class struct_tagNET_DVR_DECSUBSYSTEMJIONSTATUS(Structure):
    pass

_S(struct_tagNET_DVR_DECSUBSYSTEMJIONSTATUS, [
    ('byJoinStatus', BYTE),
    ('byJoinSubSystem', BYTE),
    ('byJoinDispNum', BYTE),
    ('byJoinSubWindowNum', BYTE),
    ('byRes', BYTE * 4),
])

NET_DVR_DECSUBSYSTEMJIONSTATUS = struct_tagNET_DVR_DECSUBSYSTEMJIONSTATUS
LPNET_DVR_DECSUBSYSTEMJIONSTATUS = struct_tagNET_DVR_DECSUBSYSTEMJIONSTATUS
tagNET_DVR_DECSUBSYSTEMJIONSTATUS = struct_tagNET_DVR_DECSUBSYSTEMJIONSTATUS
