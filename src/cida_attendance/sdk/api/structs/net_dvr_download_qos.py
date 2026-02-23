from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_DOWNLOAD_QOS(Structure):
    pass

_S(struct_tagNET_DVR_DOWNLOAD_QOS, [
    ('dwMaxSpeed', DWORD),
    ('byRes', BYTE * 256),
])

NET_DVR_DOWNLOAD_QOS = struct_tagNET_DVR_DOWNLOAD_QOS
LPNET_DVR_DOWNLOAD_QOS = POINTER(struct_tagNET_DVR_DOWNLOAD_QOS)
tagNET_DVR_DOWNLOAD_QOS = struct_tagNET_DVR_DOWNLOAD_QOS
