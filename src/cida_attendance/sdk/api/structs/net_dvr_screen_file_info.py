from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_SCREEN_FILE_INFO(Structure):
    pass

_S(struct_tagNET_DVR_SCREEN_FILE_INFO, [
    ('dwSize', DWORD),
    ('dwFileIndex', DWORD),
    ('byFileType', BYTE),
    ('byPictureFormat', BYTE),
    ('byVideoFormat', BYTE),
    ('byDocumentFormat', BYTE),
    ('byFileName', BYTE * 256),
    ('dwFileSize', DWORD),
    ('dwPPTPage', DWORD),
    ('byOtherFileFormat', BYTE * 8),
    ('byRes1', BYTE * 56),
])

NET_DVR_SCREEN_FILE_INFO = struct_tagNET_DVR_SCREEN_FILE_INFO
LPNET_DVR_SCREEN_FILE_INFO = POINTER(struct_tagNET_DVR_SCREEN_FILE_INFO)
tagNET_DVR_SCREEN_FILE_INFO = struct_tagNET_DVR_SCREEN_FILE_INFO
