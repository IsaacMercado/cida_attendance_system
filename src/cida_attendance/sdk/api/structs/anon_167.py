from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER
from .anon_166 import TTY_CONFIG


class struct_anon_167(Structure):
    pass

_S(struct_anon_167, [
    ('byTranChanEnable', BYTE),
    ('byLocalSerialDevice', BYTE),
    ('byRemoteSerialDevice', BYTE),
    ('res1', BYTE),
    ('sRemoteDevIP', c_char * 16),
    ('wRemoteDevPort', WORD),
    ('res2', BYTE * 2),
    ('RemoteSerialDevCfg', TTY_CONFIG),
])

NET_DVR_MATRIX_TRAN_CHAN_INFO = struct_anon_167
LPNET_DVR_MATRIX_TRAN_CHAN_INFO = POINTER(struct_anon_167)
