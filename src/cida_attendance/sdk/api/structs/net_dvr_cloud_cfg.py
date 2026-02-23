from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD, INT64
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_CLOUD_CFG(Structure):
    pass

_S(struct_tagNET_DVR_CLOUD_CFG, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byType', BYTE),
    ('byStatus', BYTE),
    ('byRes1', BYTE),
    ('szAuthCode', c_char * 64),
    ('szAlias', c_char * 32),
    ('i64TotalCapability', INT64),
    ('i64UsedSpace', INT64),
    ('byRes2', BYTE * 256),
])

NET_DVR_CLOUD_CFG = struct_tagNET_DVR_CLOUD_CFG
LPNET_DVR_CLOUD_CFG = POINTER(struct_tagNET_DVR_CLOUD_CFG)
tagNET_DVR_CLOUD_CFG = struct_tagNET_DVR_CLOUD_CFG
