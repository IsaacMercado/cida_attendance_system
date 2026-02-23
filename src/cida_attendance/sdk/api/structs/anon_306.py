from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_anon_306(Structure):
    pass

_S(struct_anon_306, [
    ('dwEnable', DWORD),
    ('dwStatus', DWORD),
    ('dwVolumn', DWORD),
    ('dwFreeSpace', DWORD),
    ('dwTimeLeft', DWORD),
    ('byCDType', BYTE),
    ('byRes', BYTE * 3),
])

NET_DVR_INQUEST_CDRW = struct_anon_306
LPNET_DVR_INQUEST_CDRW = POINTER(struct_anon_306)
