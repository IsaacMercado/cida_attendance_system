from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_GUID_FILE_EXPORT(Structure):
    pass

_S(struct_tagNET_DVR_GUID_FILE_EXPORT, [
    ('dwSize', DWORD),
    ('sLoginPassWord', c_char * 128),
    ('byRes', BYTE * 128),
])

NET_DVR_GUID_FILE_EXPORT = struct_tagNET_DVR_GUID_FILE_EXPORT
LPNET_DVR_GUID_FILE_EXPORT = POINTER(struct_tagNET_DVR_GUID_FILE_EXPORT)
tagNET_DVR_GUID_FILE_EXPORT = struct_tagNET_DVR_GUID_FILE_EXPORT
