from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR


class struct_tagNET_DVR_PRIVATE_PROTOCOL_CFG(Structure):
    pass

_S(struct_tagNET_DVR_PRIVATE_PROTOCOL_CFG, [
    ('dwSize', DWORD),
    ('struIP', NET_DVR_IPADDR),
    ('wPort', WORD),
    ('byEnable', BYTE),
    ('byRes', BYTE),
    ('dwInterval', DWORD),
    ('byServerType', BYTE),
    ('byEcryptedSMSEnable', BYTE),
    ('byAlgorithm', BYTE),
    ('byAcauisitionMode', BYTE),
    ('dwDistanceLimit', DWORD),
    ('byPKModeEnable', BYTE),
    ('byMACAddrReductionEnable', BYTE),
    ('byRes1', BYTE * 214),
    ('szIndexCode', c_char * 64),
    ('dwSecretKeyLen', DWORD),
    ('szSecretKey', c_char * 512),
])

NET_DVR_PRIVATE_PROTOCOL_CFG = struct_tagNET_DVR_PRIVATE_PROTOCOL_CFG
LPNET_DVR_PRIVATE_PROTOCOL_CFG = POINTER(struct_tagNET_DVR_PRIVATE_PROTOCOL_CFG)
tagNET_DVR_PRIVATE_PROTOCOL_CFG = struct_tagNET_DVR_PRIVATE_PROTOCOL_CFG
