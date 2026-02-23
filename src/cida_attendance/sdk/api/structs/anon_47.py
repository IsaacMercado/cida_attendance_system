from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_anon_47(Structure):
    pass

_S(struct_anon_47, [
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
])

NET_DVR_DECODERCFG_V30 = struct_anon_47
LPNET_DVR_DECODERCFG_V30 = POINTER(struct_anon_47)
