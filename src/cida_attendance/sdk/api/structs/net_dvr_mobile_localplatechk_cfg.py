from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_MOBILE_LOCALPLATECHK_CFG(Structure):
    pass

_S(struct_tagNET_DVR_MOBILE_LOCALPLATECHK_CFG, [
    ('dwSize', DWORD),
    ('byCheck', BYTE),
    ('byCheckAlarm', BYTE),
    ('byCheckHint', BYTE),
    ('byUploadUnlicensedCar', BYTE),
    ('byRes', BYTE * 64),
])

NET_DVR_MOBILE_LOCALPLATECHK_CFG = struct_tagNET_DVR_MOBILE_LOCALPLATECHK_CFG
LPNET_DVR_MOBILE_LOCALPLATECHK_CFG = POINTER(struct_tagNET_DVR_MOBILE_LOCALPLATECHK_CFG)
tagNET_DVR_MOBILE_LOCALPLATECHK_CFG = struct_tagNET_DVR_MOBILE_LOCALPLATECHK_CFG
