from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_PICTURE_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_PICTURE_PARAM, [
    ('dwSize', DWORD),
    ('byControlCommand', BYTE),
    ('byUseType', BYTE),
    ('byWallNo', BYTE),
    ('byPictureNo', BYTE),
    ('byRes', BYTE * 64),
])

NET_DVR_PICTURE_PARAM = struct_tagNET_DVR_PICTURE_PARAM
LPNET_DVR_PICTURE_PARAM = POINTER(struct_tagNET_DVR_PICTURE_PARAM)
tagNET_DVR_PICTURE_PARAM = struct_tagNET_DVR_PICTURE_PARAM
