from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_ITS_OVERLAP_INFO_PARAM(Structure):
    pass

_S(struct_tagNET_ITS_OVERLAP_INFO_PARAM, [
    ('bySite', BYTE * 128),
    ('byRoadNum', BYTE * 32),
    ('byInstrumentNum', BYTE * 32),
    ('byDirection', BYTE * 32),
    ('byDirectionDesc', BYTE * 32),
    ('byLaneDes', BYTE * 32),
    ('byRes1', BYTE * 32),
    ('byMonitoringSite1', BYTE * 44),
    ('byMonitoringSite2', BYTE * 32),
    ('byRes', BYTE * 64),
])

NET_ITS_OVERLAP_INFO_PARAM = struct_tagNET_ITS_OVERLAP_INFO_PARAM
LPNET_ITS_OVERLAP_INFO_PARAM = POINTER(struct_tagNET_ITS_OVERLAP_INFO_PARAM)
tagNET_ITS_OVERLAP_INFO_PARAM = struct_tagNET_ITS_OVERLAP_INFO_PARAM
