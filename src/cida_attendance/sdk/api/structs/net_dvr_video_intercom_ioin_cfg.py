from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_VIDEO_INTERCOM_IOIN_CFG(Structure):
    pass

_S(struct_tagNET_DVR_VIDEO_INTERCOM_IOIN_CFG, [
    ('dwSize', DWORD),
    ('byIOUseType', BYTE),
    ('byRes', BYTE * 63),
])

NET_DVR_VIDEO_INTERCOM_IOIN_CFG = struct_tagNET_DVR_VIDEO_INTERCOM_IOIN_CFG
LPNET_DVR_VIDEO_INTERCOM_IOIN_CFG = POINTER(struct_tagNET_DVR_VIDEO_INTERCOM_IOIN_CFG)
tagNET_DVR_VIDEO_INTERCOM_IOIN_CFG = struct_tagNET_DVR_VIDEO_INTERCOM_IOIN_CFG
