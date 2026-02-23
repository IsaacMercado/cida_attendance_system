from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_CARD_PORT_STATE(Structure):
    pass

_S(struct_tagNET_DVR_CARD_PORT_STATE, [
    ('byValid', BYTE),
    ('byPortType', BYTE),
    ('byLinkState', BYTE),
    ('byRes1', BYTE),
    ('dwSendBytes', DWORD),
    ('dwRecvBytes', DWORD),
    ('dwRecvLostPackets', DWORD),
    ('dwRecvCrcErrPackets', DWORD),
    ('dwRecvFragmentPackets', DWORD),
    ('byRes2', BYTE * 16),
])

NET_DVR_CARD_PORT_STATE = struct_tagNET_DVR_CARD_PORT_STATE
LPNET_DVR_CARD_PORT_STATE = POINTER(struct_tagNET_DVR_CARD_PORT_STATE)
tagNET_DVR_CARD_PORT_STATE = struct_tagNET_DVR_CARD_PORT_STATE
