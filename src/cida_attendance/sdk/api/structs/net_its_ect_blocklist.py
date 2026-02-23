from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_plate_info import NET_DVR_PLATE_INFO


class struct_tagNET_ITS_ECT_BLOCKLIST(Structure):
    pass

_S(struct_tagNET_ITS_ECT_BLOCKLIST, [
    ('dwSize', DWORD),
    ('dwChannel', DWORD),
    ('bylogicalLaneNo', BYTE),
    ('byRes1', BYTE * 3),
    ('byLaneName', BYTE * 32),
    ('struPlateInfo', NET_DVR_PLATE_INFO),
    ('byRes2', BYTE * 256),
])

NET_ITS_ECT_BLOCKLIST = struct_tagNET_ITS_ECT_BLOCKLIST
LPNET_ITS_ECT_BLOCKLIST = POINTER(struct_tagNET_ITS_ECT_BLOCKLIST)
tagNET_ITS_ECT_BLOCKLIST = struct_tagNET_ITS_ECT_BLOCKLIST
