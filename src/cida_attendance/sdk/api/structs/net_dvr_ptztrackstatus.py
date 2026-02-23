from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_PTZTRACKSTATUS(Structure):
    pass

_S(struct_tagNET_DVR_PTZTRACKSTATUS, [
    ('dwSize', DWORD),
    ('byID', BYTE),
    ('byLinkageType', BYTE),
    ('byRes', BYTE * 254),
])

NET_DVR_PTZTRACKSTATUS = struct_tagNET_DVR_PTZTRACKSTATUS
LPNET_DVR_PTZTRACKSTATUS = POINTER(struct_tagNET_DVR_PTZTRACKSTATUS)
tagNET_DVR_PTZTRACKSTATUS = struct_tagNET_DVR_PTZTRACKSTATUS
