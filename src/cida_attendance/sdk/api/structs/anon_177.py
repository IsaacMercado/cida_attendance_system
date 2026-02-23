from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_anon_177(Structure):
    pass

_S(struct_anon_177, [
    ('byDecodeStatus', BYTE),
    ('byStreamType', BYTE),
    ('byPacketType', BYTE),
    ('byRecvBufUsage', BYTE),
    ('byDecBufUsage', BYTE),
    ('byFpsDecV', BYTE),
    ('byFpsDecA', BYTE),
    ('byCpuLoad', BYTE),
    ('byRes1', BYTE * 4),
    ('dwDecodedV', DWORD),
    ('dwDecodedA', DWORD),
    ('wImgW', WORD),
    ('wImgH', WORD),
    ('byVideoFormat', BYTE),
    ('byRes2', BYTE * 3),
    ('dwDecChan', DWORD),
    ('byRes3', BYTE * 20),
])

NET_DVR_MATRIX_CHAN_STATUS = struct_anon_177
LPNET_DVR_MATRIX_CHAN_STATUS = POINTER(struct_anon_177)
