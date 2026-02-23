from ctypes import Structure

from ..base_classes import _S, BYTE, WORD


class struct_anon_245(Structure):
    pass

_S(struct_anon_245, [
    ('wChanNo', WORD * int((32 + 32))),
    ('byRuleID', BYTE),
    ('byDriverBehaviortType', BYTE),
    ('byADASType', BYTE),
    ('byGSensorType', BYTE),
    ('bySensorInType', BYTE),
    ('byRes', BYTE * 667),
])

