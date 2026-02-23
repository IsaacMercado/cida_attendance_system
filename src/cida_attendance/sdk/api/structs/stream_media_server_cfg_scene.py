from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR


class struct_tagSTREAM_MEDIA_SERVER_CFG_SCENE(Structure):
    pass

_S(struct_tagSTREAM_MEDIA_SERVER_CFG_SCENE, [
    ('byValid', BYTE),
    ('byRes1', BYTE * 3),
    ('struDevIP', NET_DVR_IPADDR),
    ('wDevPort', WORD),
    ('byTransmitType', BYTE),
    ('byRes2', BYTE * 5),
])

NET_DVR_STREAM_MEDIA_SERVER_CFG_SCENE = struct_tagSTREAM_MEDIA_SERVER_CFG_SCENE
LPNET_DVR_STREAM_MEDIA_SERVER_CFG_SCENE = POINTER(struct_tagSTREAM_MEDIA_SERVER_CFG_SCENE)
tagSTREAM_MEDIA_SERVER_CFG_SCENE = struct_tagSTREAM_MEDIA_SERVER_CFG_SCENE
