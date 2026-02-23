from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_INIT_CHECK_MODULE_COM(Structure):
    pass

_S(struct_tagNET_DVR_INIT_CHECK_MODULE_COM, [
    ('byEnable', BYTE),
    ('byRes', BYTE * 255),
])

NET_DVR_INIT_CHECK_MODULE_COM = struct_tagNET_DVR_INIT_CHECK_MODULE_COM
LPNET_DVR_INIT_CHECK_MODULE_COM = POINTER(struct_tagNET_DVR_INIT_CHECK_MODULE_COM)
tagNET_DVR_INIT_CHECK_MODULE_COM = struct_tagNET_DVR_INIT_CHECK_MODULE_COM
