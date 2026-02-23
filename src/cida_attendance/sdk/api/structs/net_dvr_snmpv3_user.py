from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_SNMPv3_USER(Structure):
    pass

_S(struct_tagNET_DVR_SNMPv3_USER, [
    ('byUserName', BYTE * 32),
    ('bySecLevel', BYTE),
    ('byAuthtype', BYTE),
    ('byPrivtype', BYTE),
    ('byRes', BYTE * 5),
    ('byAuthpass', BYTE * 16),
    ('byPrivpass', BYTE * 16),
])

NET_DVR_SNMPv3_USER = struct_tagNET_DVR_SNMPv3_USER
LPNET_DVR_SNMPv3_USER = POINTER(struct_tagNET_DVR_SNMPv3_USER)
tagNET_DVR_SNMPv3_USER = struct_tagNET_DVR_SNMPv3_USER
