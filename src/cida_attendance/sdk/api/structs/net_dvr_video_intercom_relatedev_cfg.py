from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_video_intercom_unit_relatedev_union import (
    NET_DVR_VIDEO_INTERCOM_UNIT_RELATEDEV_UNION,
)


class struct_tagNET_DVR_VIDEO_INTERCOM_RELATEDEV_CFG(Structure):
    pass

_S(struct_tagNET_DVR_VIDEO_INTERCOM_RELATEDEV_CFG, [
    ('dwSize', DWORD),
    ('byUnitType', BYTE),
    ('byRes1', BYTE * 3),
    ('uVideoIntercomUnit', NET_DVR_VIDEO_INTERCOM_UNIT_RELATEDEV_UNION),
    ('byRes2', BYTE * 128),
])

NET_DVR_VIDEO_INTERCOM_RELATEDEV_CFG = struct_tagNET_DVR_VIDEO_INTERCOM_RELATEDEV_CFG
LPNET_DVR_VIDEO_INTERCOM_RELATEDEV_CFG = POINTER(struct_tagNET_DVR_VIDEO_INTERCOM_RELATEDEV_CFG)
tagNET_DVR_VIDEO_INTERCOM_RELATEDEV_CFG = struct_tagNET_DVR_VIDEO_INTERCOM_RELATEDEV_CFG
