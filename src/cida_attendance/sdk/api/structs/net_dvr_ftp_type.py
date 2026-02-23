from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_FTP_TYPE(Structure):
    pass

_S(struct_tagNET_DVR_FTP_TYPE, [
    ('byType', BYTE),
    ('byRes', BYTE * 3),
])

NET_DVR_FTP_TYPE = struct_tagNET_DVR_FTP_TYPE
LPNET_DVR_FTP_TYPE = POINTER(struct_tagNET_DVR_FTP_TYPE)
tagNET_DVR_FTP_TYPE = struct_tagNET_DVR_FTP_TYPE
