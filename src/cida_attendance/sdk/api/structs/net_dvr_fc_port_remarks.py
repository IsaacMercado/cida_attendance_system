from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_FC_PORT_REMARKS(Structure):
    pass

_S(struct_tagNET_DVR_FC_PORT_REMARKS, [
    ('dwSize', DWORD),
    ('byLocalRemarks', BYTE * 128),
    ('byPeerRemarks', BYTE * 128),
    ('byRes', BYTE * 32),
])

NET_DVR_FC_PORT_REMARKS = struct_tagNET_DVR_FC_PORT_REMARKS
LPNET_DVR_FC_PORT_REMARKS = POINTER(struct_tagNET_DVR_FC_PORT_REMARKS)
tagNET_DVR_FC_PORT_REMARKS = struct_tagNET_DVR_FC_PORT_REMARKS
