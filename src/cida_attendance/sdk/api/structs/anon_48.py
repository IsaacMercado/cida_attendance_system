from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_anon_48(Structure):
    pass

_S(struct_anon_48, [
    ('dwSize', DWORD),
    ('dwBaudRate', DWORD),
    ('byDataBit', BYTE),
    ('byStopBit', BYTE),
    ('byParity', BYTE),
    ('byFlowcontrol', BYTE),
    ('wDecoderType', WORD),
    ('wDecoderAddress', WORD),
    ('bySetPreset', BYTE * 128),
    ('bySetCruise', BYTE * 128),
    ('bySetTrack', BYTE * 128),
])

NET_DVR_DECODERCFG = struct_anon_48
LPNET_DVR_DECODERCFG = POINTER(struct_anon_48)
