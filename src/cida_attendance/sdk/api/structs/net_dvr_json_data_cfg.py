from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_JSON_DATA_CFG(Structure):
    pass

_S(struct_tagNET_DVR_JSON_DATA_CFG, [
    ('dwSize', DWORD),
    ('lpJsonData', POINTER(None)),
    ('dwJsonDataSize', DWORD),
    ('lpPicData', POINTER(None)),
    ('dwPicDataSize', DWORD),
    ('dwInfraredFacePicSize', DWORD),
    ('lpInfraredFacePicBuffer', POINTER(None)),
    ('byRes', BYTE * 248),
])

NET_DVR_JSON_DATA_CFG = struct_tagNET_DVR_JSON_DATA_CFG
LPNET_DVR_JSON_DATA_CFG = POINTER(struct_tagNET_DVR_JSON_DATA_CFG)
tagNET_DVR_JSON_DATA_CFG = struct_tagNET_DVR_JSON_DATA_CFG
