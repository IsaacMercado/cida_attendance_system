from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_AUXILIARY_DEV_UPGRADE_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_AUXILIARY_DEV_UPGRADE_PARAM, [
    ('dwSize', DWORD),
    ('dwDevNo', DWORD),
    ('byDevType', BYTE),
    ('byRes', BYTE * 131),
])

NET_DVR_AUXILIARY_DEV_UPGRADE_PARAM = struct_tagNET_DVR_AUXILIARY_DEV_UPGRADE_PARAM
LPNET_DVR_AUXILIARY_DEV_UPGRADE_PARAM = POINTER(struct_tagNET_DVR_AUXILIARY_DEV_UPGRADE_PARAM)
tagNET_DVR_AUXILIARY_DEV_UPGRADE_PARAM = struct_tagNET_DVR_AUXILIARY_DEV_UPGRADE_PARAM
