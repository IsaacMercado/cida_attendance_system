from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_CERT_NAME(Structure):
    pass

_S(struct_tagNET_DVR_CERT_NAME, [
    ('byCountry', BYTE * 4),
    ('byState', BYTE * 64),
    ('byLocality', BYTE * 64),
    ('byOrganization', BYTE * 64),
    ('byUnit', BYTE * 64),
    ('byCommonName', BYTE * 64),
    ('byEmail', BYTE * 64),
    ('byRes', BYTE * 128),
])

NET_DVR_CERT_NAME = struct_tagNET_DVR_CERT_NAME
LPNET_DVR_CERT_NAME = POINTER(struct_tagNET_DVR_CERT_NAME)
tagNET_DVR_CERT_NAME = struct_tagNET_DVR_CERT_NAME
