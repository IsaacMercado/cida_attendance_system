from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, WORD
from .anon_2 import NET_DVR_IPADDR
from .net_dvr_poolparam import NET_DVR_POOLPARAM


class struct_anon_379(Structure):
    pass

_S(struct_anon_379, [
    ('struIPAdder', NET_DVR_IPADDR),
    ('wPort', WORD),
    ('byRes2', BYTE * 2),
    ('szUser', c_char * 48),
    ('szPassword', c_char * 48),
    ('struPoolInfo', NET_DVR_POOLPARAM * 16),
    ('byProtocolType', BYTE),
    ('byRes3', BYTE * 3),
    ('szAccessKey', c_char * 64),
    ('szSecretKey', c_char * 64),
    ('byRes1', BYTE * 354),
])

