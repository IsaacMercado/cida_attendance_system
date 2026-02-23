from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_IO_OUTCFG(Structure):
    pass

_S(struct_tagNET_DVR_IO_OUTCFG, [
    ('dwSize', DWORD),
    ('byDefaultStatus', BYTE),
    ('byIoOutStatus', BYTE),
    ('wAheadTime', WORD),
    ('dwTimePluse', DWORD),
    ('dwTimeDelay', DWORD),
    ('byFreqMulti', BYTE),
    ('byDutyRate', BYTE),
    ('byRes2', BYTE * 2),
])

NET_DVR_IO_OUTCFG = struct_tagNET_DVR_IO_OUTCFG
LPNET_DVR_IO_OUTCFG = POINTER(struct_tagNET_DVR_IO_OUTCFG)
tagNET_DVR_IO_OUTCFG = struct_tagNET_DVR_IO_OUTCFG
