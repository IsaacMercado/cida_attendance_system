from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .net_dvr_cert_addition_param import NET_DVR_CERT_ADDITION_PARAM


class struct_tagNET_DVR_CERT_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_CERT_PARAM, [
    ('dwSize', DWORD),
    ('wCertFunc', WORD),
    ('wCertType', WORD),
    ('byFileType', BYTE),
    ('byRes1', BYTE * 2),
    ('byAddition', BYTE),
    ('pStruAdditionParam', POINTER(NET_DVR_CERT_ADDITION_PARAM)),
    ('byRes', BYTE * 28),
])

NET_DVR_CERT_PARAM = struct_tagNET_DVR_CERT_PARAM
LPNET_DVR_CERT_PARAM = POINTER(struct_tagNET_DVR_CERT_PARAM)
tagNET_DVR_CERT_PARAM = struct_tagNET_DVR_CERT_PARAM
