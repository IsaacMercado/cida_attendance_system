from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_SCREEM_FILE_DOWNLOAD_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_SCREEM_FILE_DOWNLOAD_PARAM, [
    ('dwSize', DWORD),
    ('dwFileIndex', DWORD),
    ('dwPPTPageNo', DWORD),
    ('byRes2', BYTE * 64),
])

NET_DVR_SCREEM_FILE_DOWNLOAD_PARAM = struct_tagNET_DVR_SCREEM_FILE_DOWNLOAD_PARAM
LPNET_DVR_SCREEM_FILE_DOWNLOAD_PARAM = POINTER(struct_tagNET_DVR_SCREEM_FILE_DOWNLOAD_PARAM)
tagNET_DVR_SCREEM_FILE_DOWNLOAD_PARAM = struct_tagNET_DVR_SCREEM_FILE_DOWNLOAD_PARAM
