from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_1 import NET_DVR_TIME


class struct_tagNET_VCA_INQUIRE_SNAPDB_COND(Structure):
    pass

_S(struct_tagNET_VCA_INQUIRE_SNAPDB_COND, [
    ('dwChannel', DWORD),
    ('struStartTime', NET_DVR_TIME),
    ('struStopTime', NET_DVR_TIME),
    ('bySex', BYTE),
    ('byRes1', BYTE * 3),
    ('byStartBirthDate', BYTE * 10),
    ('byEndBirthDate', BYTE * 10),
    ('byAttribute1', BYTE * 32),
    ('byAttribute2', BYTE * 32),
    ('byRes', BYTE * 12),
])

NET_VCA_INQUIRE_SNAPDB_COND = struct_tagNET_VCA_INQUIRE_SNAPDB_COND
LPNET_VCA_INQUIRE_SNAPDB_COND = POINTER(struct_tagNET_VCA_INQUIRE_SNAPDB_COND)
tagNET_VCA_INQUIRE_SNAPDB_COND = struct_tagNET_VCA_INQUIRE_SNAPDB_COND
