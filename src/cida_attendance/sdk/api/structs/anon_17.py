from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_anon_17(Structure):
    pass

_S(struct_anon_17, [
    ('dwMaxRecordChanNum', DWORD),
    ('dwCurRecordChanNum', DWORD),
    ('dwRelRecordChan', DWORD * int((32 + 32))),
    ('byRes', BYTE * 64),
])

NET_DVR_RECORDCHAN = struct_anon_17
LPNET_DVR_RECORDCHAN = POINTER(struct_anon_17)
