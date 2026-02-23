from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_HKDDNS_STREAM(Structure):
    pass

_S(struct_tagNET_DVR_HKDDNS_STREAM, [
    ('byEnable', BYTE),
    ('byRes', BYTE * 3),
    ('byDDNSDomain', BYTE * 64),
    ('wPort', WORD),
    ('wAliasLen', WORD),
    ('byAlias', BYTE * 32),
    ('wDVRSerialLen', WORD),
    ('byRes1', BYTE * 2),
    ('byDVRSerialNumber', BYTE * 48),
    ('byUserName', BYTE * 32),
    ('byPassWord', BYTE * 16),
    ('byChannel', BYTE),
    ('byRes2', BYTE * 11),
])

NET_DVR_HKDDNS_STREAM = struct_tagNET_DVR_HKDDNS_STREAM
LPNET_DVR_HKDDNS_STREAM = POINTER(struct_tagNET_DVR_HKDDNS_STREAM)
tagNET_DVR_HKDDNS_STREAM = struct_tagNET_DVR_HKDDNS_STREAM
