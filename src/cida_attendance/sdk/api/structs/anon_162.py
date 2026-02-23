from ctypes import Structure, c_char

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER


class struct_anon_162(Structure):
    pass

_S(struct_anon_162, [
    ('dwSize', DWORD),
    ('dwIsLinked', DWORD),
    ('dwStreamCpRate', DWORD),
    ('cRes', c_char * 64),
])

NET_DVR_MATRIX_DEC_CHAN_STATUS = struct_anon_162
LPNET_DVR_MATRIX_DEC_CHAN_STATUS = POINTER(struct_anon_162)
