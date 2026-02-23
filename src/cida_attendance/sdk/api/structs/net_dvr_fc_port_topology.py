from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_FC_PORT_TOPOLOGY(Structure):
    pass

_S(struct_tagNET_DVR_FC_PORT_TOPOLOGY, [
    ('dwPortNo', DWORD),
    ('byPortType', BYTE),
    ('byLocalWorkMode', BYTE),
    ('byLocalBandWidth', BYTE),
    ('byRes1', BYTE * 1),
    ('byPeerTypeName', BYTE * 32),
    ('byPeerMac', BYTE * 6),
    ('dwPeerPortNo', DWORD),
    ('byPeerWorkMode', BYTE),
    ('byPeerBandWidth', BYTE),
    ('byRes2', BYTE * 30),
])

NET_DVR_FC_PORT_TOPOLOGY = struct_tagNET_DVR_FC_PORT_TOPOLOGY
LPNET_DVR_FC_PORT_TOPOLOGY = POINTER(struct_tagNET_DVR_FC_PORT_TOPOLOGY)
tagNET_DVR_FC_PORT_TOPOLOGY = struct_tagNET_DVR_FC_PORT_TOPOLOGY
