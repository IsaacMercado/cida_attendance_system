from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_anon_221(Structure):
    pass

_S(struct_anon_221, [
    ('dwFcw', BYTE),
    ('dwLdw', BYTE),
    ('dwHmw', BYTE),
    ('dwPcw', BYTE),
    ('dwBsd', BYTE),
    ('byAcc', BYTE),
    ('byBrake', BYTE),
    ('byTurn', BYTE),
    ('byRollover', BYTE),
    ('byNoCourtesy', BYTE),
    ('byTsr', BYTE),
    ('byRes', BYTE * 13),
])

NET_DVR_ADAS_ALARM_STATE = struct_anon_221
LPNET_DVR_ADAS_ALARM_STATE = POINTER(struct_anon_221)
