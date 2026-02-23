from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_SIMXML_LOGIN(Structure):
    pass

_S(struct_tagNET_DVR_SIMXML_LOGIN, [
    ('byLoginWithSimXml', BYTE),
    ('byRes', BYTE * 127),
])

NET_DVR_SIMXML_LOGIN = struct_tagNET_DVR_SIMXML_LOGIN
LPNET_DVR_SIMXML_LOGIN = POINTER(struct_tagNET_DVR_SIMXML_LOGIN)
tagNET_DVR_SIMXML_LOGIN = struct_tagNET_DVR_SIMXML_LOGIN
