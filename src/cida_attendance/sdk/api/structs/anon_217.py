from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_anon_217(Structure):
    pass

_S(struct_anon_217, [
    ('bySmoke', BYTE),
    ('byPhone', BYTE),
    ('byTiredDriving', BYTE),
    ('byNoVisualFront', BYTE),
    ('byNoHead', BYTE),
    ('byWithoutBelt', BYTE),
    ('byPickingUpThing', BYTE),
    ('byYawn', BYTE),
    ('byEatOrDrink', BYTE),
    ('byChatting', BYTE),
    ('byTampering', BYTE),
    ('byWithoutUniform', BYTE),
    ('byDriverCmpFail', BYTE),
    ('byDriverChange', BYTE),
    ('byDriveLongTime', BYTE),
    ('byInfraredBlockingSunglasses', BYTE),
    ('byOutOfWheel', BYTE),
    ('byRes', BYTE * 7),
])

NET_DVR_DBD_ALARM_STATE = struct_anon_217
LPNET_DVR_DBD_ALARM_STATE = POINTER(struct_anon_217)
