from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_TERMINAL_CALL_CFG(Structure):
    pass

_S(struct_tagNET_DVR_TERMINAL_CALL_CFG, [
    ('dwSize', DWORD),
    ('byAnswerType', BYTE),
    ('byProtocolType', BYTE),
    ('byTransmissionProtocol', BYTE),
    ('byRes', BYTE * 29),
])

NET_DVR_TERMINAL_CALL_CFG = struct_tagNET_DVR_TERMINAL_CALL_CFG
LPNET_DVR_TERMINAL_CALL_CFG = POINTER(struct_tagNET_DVR_TERMINAL_CALL_CFG)
tagNET_DVR_TERMINAL_CALL_CFG = struct_tagNET_DVR_TERMINAL_CALL_CFG
