from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_AUTH_INFO(Structure):
    pass

_S(struct_tagNET_DVR_AUTH_INFO, [
    ('byAuthResult', BYTE),
    ('byAuthType', BYTE),
    ('byRes1', BYTE * 2),
    ('byCardNo', BYTE * 32),
    ('dwPicDataLen', DWORD),
    ('pImage', POINTER(BYTE)),
    ('byEmployeeNo', BYTE * 32),
    ('byRes', BYTE * 180),
])

NET_DVR_AUTH_INFO = struct_tagNET_DVR_AUTH_INFO
LPNET_DVR_AUTH_INFO = POINTER(struct_tagNET_DVR_AUTH_INFO)
tagNET_DVR_AUTH_INFO = struct_tagNET_DVR_AUTH_INFO
