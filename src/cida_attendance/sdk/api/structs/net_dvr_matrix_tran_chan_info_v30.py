from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR
from .anon_166 import TTY_CONFIG


class struct_tagNET_DVR_MATRIX_TRAN_CHAN_INFO_V30(Structure):
    pass

_S(struct_tagNET_DVR_MATRIX_TRAN_CHAN_INFO_V30, [
    ('byTranChanEnable', BYTE),
    ('byLocalSerialDevice', BYTE),
    ('byRemoteSerialDevice', BYTE),
    ('res1', BYTE),
    ('struRemoteDevIP', NET_DVR_IPADDR),
    ('wRemoteDevPort', WORD),
    ('byIsEstablished', BYTE),
    ('res2', BYTE),
    ('RemoteSerialDevCfg', TTY_CONFIG),
    ('byUsername', BYTE * 32),
    ('byPassword', BYTE * 16),
    ('dwLocalSerialNo', DWORD),
    ('dwRemoteSerialNo', DWORD),
    ('byRes3', BYTE * 8),
])

NET_DVR_MATRIX_TRAN_CHAN_INFO_V30 = struct_tagNET_DVR_MATRIX_TRAN_CHAN_INFO_V30
LPNET_DVR_MATRIX_TRAN_CHAN_INFO_V30 = POINTER(struct_tagNET_DVR_MATRIX_TRAN_CHAN_INFO_V30)
tagNET_DVR_MATRIX_TRAN_CHAN_INFO_V30 = struct_tagNET_DVR_MATRIX_TRAN_CHAN_INFO_V30
