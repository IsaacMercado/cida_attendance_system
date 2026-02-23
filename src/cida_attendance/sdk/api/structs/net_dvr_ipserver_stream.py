from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR


class struct_tagNET_DVR_IPSERVER_STREAM(Structure):
    pass

_S(struct_tagNET_DVR_IPSERVER_STREAM, [
    ('byEnable', BYTE),
    ('byRes', BYTE * 3),
    ('struIPServer', NET_DVR_IPADDR),
    ('wPort', WORD),
    ('wDvrNameLen', WORD),
    ('byDVRName', BYTE * 32),
    ('wDVRSerialLen', WORD),
    ('byRes1', WORD * 2),
    ('byDVRSerialNumber', BYTE * 48),
    ('byUserName', BYTE * 32),
    ('byPassWord', BYTE * 16),
    ('byChannel', BYTE),
    ('byRes2', BYTE * 11),
])

NET_DVR_IPSERVER_STREAM = struct_tagNET_DVR_IPSERVER_STREAM
LPNET_DVR_IPSERVER_STREAM = POINTER(struct_tagNET_DVR_IPSERVER_STREAM)
tagNET_DVR_IPSERVER_STREAM = struct_tagNET_DVR_IPSERVER_STREAM
