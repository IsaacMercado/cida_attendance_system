from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER, String


class struct_tagNET_SDK_P2P_SERVER_2C(Structure):
    pass

_S(struct_tagNET_SDK_P2P_SERVER_2C, [
    ('byPlatformType', BYTE),
    ('byRes1', BYTE * 3),
    ('pAppID', String),
    ('pAuthAddr', String),
    ('pPlatformAddr', String),
    ('pUserName', String),
    ('pPassword', String),
    ('byRes', BYTE * 40),
])

NET_SDK_P2P_SERVER_2C = struct_tagNET_SDK_P2P_SERVER_2C
LPNET_DVR_P2P_SERVER_2C = POINTER(struct_tagNET_SDK_P2P_SERVER_2C)
tagNET_SDK_P2P_SERVER_2C = struct_tagNET_SDK_P2P_SERVER_2C
