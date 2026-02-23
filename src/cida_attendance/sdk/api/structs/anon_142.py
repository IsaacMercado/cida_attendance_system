from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_anon_142(Structure):
    pass

_S(struct_anon_142, [
    ('dwSize', DWORD),
    ('byPresetNo', BYTE * 32),
    ('byCruiseSpeed', BYTE * 32),
    ('wDwellTime', WORD * 32),
    ('byEnableThisCruise', BYTE),
    ('res', BYTE * 15),
])

NET_DVR_CRUISE_PARA = struct_anon_142
LPNET_DVR_CRUISE_PARA = POINTER(struct_anon_142)
