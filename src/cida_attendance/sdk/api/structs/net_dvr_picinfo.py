from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_PICINFO(Structure):
    pass

_S(struct_tagNET_DVR_PICINFO, [
    ('dwSize', DWORD),
    ('byChanIndex', BYTE),
    ('byRes1', BYTE * 3),
    ('byDeviceID', BYTE * 32),
    ('byAbsTime', BYTE * 32),
    ('dwPicLen', DWORD),
    ('byRes2', BYTE * 32),
    ('pPicBuffer', POINTER(BYTE)),
])

NET_DVR_PICTUREINFO = struct_tagNET_DVR_PICINFO
LPNET_DVR_PICTUREINFO = POINTER(struct_tagNET_DVR_PICINFO)
tagNET_DVR_PICINFO = struct_tagNET_DVR_PICINFO
