from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_DECODERCFG_V40(Structure):
    pass

_S(struct_tagNET_DVR_DECODERCFG_V40, [
    ('dwSize', DWORD),
    ('dwBaudRate', DWORD),
    ('byDataBit', BYTE),
    ('byStopBit', BYTE),
    ('byParity', BYTE),
    ('byFlowcontrol', BYTE),
    ('wDecoderType', WORD),
    ('wDecoderAddress', WORD),
    ('bySetPreset', BYTE * 256),
    ('bySetCruise', BYTE * 256),
    ('bySetTrack', BYTE * 256),
    ('bySerialNO', BYTE),
    ('byWorkMode', BYTE),
    ('byRes', BYTE * 254),
])

NET_DVR_DECODERCFG_V40 = struct_tagNET_DVR_DECODERCFG_V40
LPNET_DVR_DECODERCFG_V40 = POINTER(struct_tagNET_DVR_DECODERCFG_V40)
tagNET_DVR_DECODERCFG_V40 = struct_tagNET_DVR_DECODERCFG_V40
