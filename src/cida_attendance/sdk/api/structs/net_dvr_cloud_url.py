from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_CLOUD_URL(Structure):
    pass

_S(struct_tagNET_DVR_CLOUD_URL, [
    ('dwSize', DWORD),
    ('szURL', c_char * 256),
    ('byRes', BYTE * 256),
])

NET_DVR_CLOUD_URL = struct_tagNET_DVR_CLOUD_URL
LPNET_DVR_CLOUD_URL = POINTER(struct_tagNET_DVR_CLOUD_URL)
tagNET_DVR_CLOUD_URL = struct_tagNET_DVR_CLOUD_URL
