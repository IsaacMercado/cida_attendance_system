from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_EDID_FILE_INFO(Structure):
    pass

_S(struct_tagNET_DVR_EDID_FILE_INFO, [
    ('dwSize', DWORD),
    ('dwEDIDFileNo', DWORD),
    ('byFileName', BYTE * 32),
    ('byRes', BYTE * 32),
])

NET_DVR_EDID_FILE_INFO = struct_tagNET_DVR_EDID_FILE_INFO
LPNET_DVR_EDID_FILE_INFO = POINTER(struct_tagNET_DVR_EDID_FILE_INFO)
tagNET_DVR_EDID_FILE_INFO = struct_tagNET_DVR_EDID_FILE_INFO
