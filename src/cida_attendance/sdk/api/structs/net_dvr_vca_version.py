from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_VCA_VERSION(Structure):
    pass

_S(struct_tagNET_DVR_VCA_VERSION, [
    ('wMajorVersion', WORD),
    ('wMinorVersion', WORD),
    ('wRevisionNumber', WORD),
    ('wBuildNumber', WORD),
    ('wVersionYear', WORD),
    ('byVersionMonth', BYTE),
    ('byVersionDay', BYTE),
    ('byType', BYTE),
    ('byRes', BYTE * 7),
])

NET_DVR_VCA_VERSION = struct_tagNET_DVR_VCA_VERSION
LPNET_DVR_VCA_VERSION = POINTER(struct_tagNET_DVR_VCA_VERSION)
tagNET_DVR_VCA_VERSION = struct_tagNET_DVR_VCA_VERSION
