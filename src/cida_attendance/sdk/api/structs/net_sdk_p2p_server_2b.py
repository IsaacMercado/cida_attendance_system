from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER, String


class struct_tagNET_SDK_P2P_SERVER_2B(Structure):
    pass

_S(struct_tagNET_SDK_P2P_SERVER_2B, [
    ('byPlatformType', BYTE),
    ('byRes1', BYTE * 3),
    ('pAppID', String),
    ('pAuthAddr', String),
    ('pPlatformAddr', String),
    ('pToken', String),
    ('byRes', BYTE * 44),
])

NET_SDK_P2P_SERVER_2B = struct_tagNET_SDK_P2P_SERVER_2B
LPNET_DVR_P2P_SERVER_2B = POINTER(struct_tagNET_SDK_P2P_SERVER_2B)
tagNET_SDK_P2P_SERVER_2B = struct_tagNET_SDK_P2P_SERVER_2B
