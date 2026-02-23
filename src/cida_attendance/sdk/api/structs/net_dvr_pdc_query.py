from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_1 import NET_DVR_TIME


class struct_tagNET_DVR_PDC_QUERY(Structure):
    pass

_S(struct_tagNET_DVR_PDC_QUERY, [
    ('tmStart', NET_DVR_TIME),
    ('tmEnd', NET_DVR_TIME),
    ('dwLeaveNum', DWORD),
    ('dwEnterNum', DWORD),
    ('byRes1', BYTE * 256),
])

NET_DVR_PDC_QUERY = struct_tagNET_DVR_PDC_QUERY
LPNET_DVR_PDC_QUERY = POINTER(struct_tagNET_DVR_PDC_QUERY)
tagNET_DVR_PDC_QUERY = struct_tagNET_DVR_PDC_QUERY
