from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER, String


class struct_tagNET_DVR_BLOCKLIST_PICTURE_CFG(Structure):
    pass

_S(struct_tagNET_DVR_BLOCKLIST_PICTURE_CFG, [
    ('dwSize', DWORD),
    ('byCardNo', BYTE * 32),
    ('byName', BYTE * 32),
    ('bySex', BYTE),
    ('byPictureValid', BYTE),
    ('byRes1', BYTE * 2),
    ('dwPictureLen', DWORD),
    ('pPictureBuffer', String),
    ('byRes', BYTE * 128),
])

NET_DVR_BLOCKLIST_PICTURE_CFG = struct_tagNET_DVR_BLOCKLIST_PICTURE_CFG
LPNET_DVR_BLOCKLIST_PICTURE_CFG = POINTER(struct_tagNET_DVR_BLOCKLIST_PICTURE_CFG)
tagNET_DVR_BLOCKLIST_PICTURE_CFG = struct_tagNET_DVR_BLOCKLIST_PICTURE_CFG
