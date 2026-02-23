from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_CURRENT_VALID_PORT(Structure):
    pass

_S(struct_tagNET_DVR_CURRENT_VALID_PORT, [
    ('dwSize', DWORD),
    ('wHTTPPort', WORD),
    ('byRes', BYTE * 122),
])

NET_DVR_CURRENT_VALID_PORT = struct_tagNET_DVR_CURRENT_VALID_PORT
LPNET_DVR_CURRENT_VALID_PORT = POINTER(struct_tagNET_DVR_CURRENT_VALID_PORT)
tagNET_DVR_CURRENT_VALID_PORT = struct_tagNET_DVR_CURRENT_VALID_PORT
