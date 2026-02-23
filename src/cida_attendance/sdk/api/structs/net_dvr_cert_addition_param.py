from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_CERT_ADDITION_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_CERT_ADDITION_PARAM, [
    ('dwSize', DWORD),
    ('csCustomID', c_char * 64),
    ('byRes1', BYTE * 2),
    ('byCertificateMode', BYTE),
    ('byPrivateKeyMode', BYTE),
    ('byPassword', BYTE * 64),
    ('byRes', BYTE * 128),
])

NET_DVR_CERT_ADDITION_PARAM = struct_tagNET_DVR_CERT_ADDITION_PARAM
LPNET_DVR_CERT_ADDITION_PARAM = POINTER(struct_tagNET_DVR_CERT_ADDITION_PARAM)
tagNET_DVR_CERT_ADDITION_PARAM = struct_tagNET_DVR_CERT_ADDITION_PARAM
