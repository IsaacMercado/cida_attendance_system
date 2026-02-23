from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_CARD_PORT_STATE_V50(Structure):
    pass

_S(struct_tagNET_DVR_CARD_PORT_STATE_V50, [
    ('byPortNo', BYTE),
    ('byPortType', BYTE),
    ('byLinkState', BYTE),
    ('byPortSpeed', BYTE),
    ('byPortDuplexMode', BYTE),
    ('byRes1', BYTE * 3),
    ('byPortName', BYTE * 32),
    ('dwSendBytes', DWORD),
    ('dwSendByteSpeed', DWORD),
    ('dwSendPackets', DWORD),
    ('dwSendPacketSpeed', DWORD),
    ('dwRecvBytes', DWORD),
    ('dwRecvByteSpeed', DWORD),
    ('dwRecvPackets', DWORD),
    ('dwRecvPacketSpeed', DWORD),
    ('dwRecvLostPackets', DWORD),
    ('dwRecvCrcErrPackets', DWORD),
    ('dwRecvFragmentPackets', DWORD),
    ('byRes2', BYTE * 48),
])

NET_DVR_CARD_PORT_STATE_V50 = struct_tagNET_DVR_CARD_PORT_STATE_V50
LPNET_DVR_CARD_PORT_STATE_V50 = POINTER(struct_tagNET_DVR_CARD_PORT_STATE_V50)
tagNET_DVR_CARD_PORT_STATE_V50 = struct_tagNET_DVR_CARD_PORT_STATE_V50
