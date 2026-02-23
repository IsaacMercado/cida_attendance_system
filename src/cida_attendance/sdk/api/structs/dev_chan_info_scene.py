from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR


class struct_tagDEV_CHAN_INFO_SCENE(Structure):
    pass

_S(struct_tagDEV_CHAN_INFO_SCENE, [
    ('struIP', NET_DVR_IPADDR),
    ('wDVRPort', WORD),
    ('byChannel', BYTE),
    ('byTransProtocol', BYTE),
    ('byTransMode', BYTE),
    ('byFactoryType', BYTE),
    ('byDeviceType', BYTE),
    ('byRes', BYTE * 5),
    ('sUserName', BYTE * 32),
    ('sPassword', BYTE * 16),
])

NET_DVR_DEV_CHAN_INFO_SCENE = struct_tagDEV_CHAN_INFO_SCENE
LPNET_DVR_DEV_CHAN_INFO_SCENE = POINTER(struct_tagDEV_CHAN_INFO_SCENE)
tagDEV_CHAN_INFO_SCENE = struct_tagDEV_CHAN_INFO_SCENE
