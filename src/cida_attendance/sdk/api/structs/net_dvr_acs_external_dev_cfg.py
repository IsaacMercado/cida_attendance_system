from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_ACS_EXTERNAL_DEV_CFG(Structure):
    pass

_S(struct_tagNET_DVR_ACS_EXTERNAL_DEV_CFG, [
    ('dwSize', DWORD),
    ('byIDCardUpMode', BYTE),
    ('byRes1', BYTE),
    ('byCardVerifyMode', BYTE),
    ('byACSDevType', BYTE),
    ('byDoorMode', BYTE),
    ('byRes2', BYTE),
    ('wDevDetailType', WORD),
    ('byRes', BYTE * 300),
])

NET_DVR_ACS_EXTERNAL_DEV_CFG = struct_tagNET_DVR_ACS_EXTERNAL_DEV_CFG
LPNET_DVR_ACS_EXTERNAL_DEV_CFG = POINTER(struct_tagNET_DVR_ACS_EXTERNAL_DEV_CFG)
tagNET_DVR_ACS_EXTERNAL_DEV_CFG = struct_tagNET_DVR_ACS_EXTERNAL_DEV_CFG
