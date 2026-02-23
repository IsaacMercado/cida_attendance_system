from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_CARD_PORT_INFO(Structure):
    pass

_S(struct_tagNET_DVR_CARD_PORT_INFO, [
    ('dwPortNo', DWORD),
    ('byPortName', BYTE * 32),
    ('byWorkMode', BYTE),
    ('byBandWidth', BYTE),
    ('byPortType', BYTE),
    ('byRes', BYTE * 13),
])

NET_DVR_CARD_PORT_INFO = struct_tagNET_DVR_CARD_PORT_INFO
LPNET_DVR_CARD_PORT_INFO = POINTER(struct_tagNET_DVR_CARD_PORT_INFO)
tagNET_DVR_CARD_PORT_INFO = struct_tagNET_DVR_CARD_PORT_INFO
