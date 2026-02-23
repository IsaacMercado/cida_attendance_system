from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_video_intercom_unit_deviceid_union import (
    NET_DVR_VIDEO_INTERCOM_UNIT_DEVICEID_UNION,
)


class struct_tagNET_DVR_VIDEO_INTERCOM_DEVICEID_CFG(Structure):
    pass

_S(struct_tagNET_DVR_VIDEO_INTERCOM_DEVICEID_CFG, [
    ('dwSize', DWORD),
    ('byUnitType', BYTE),
    ('byIsAutoReg', BYTE),
    ('byRes1', BYTE * 2),
    ('uVideoIntercomUnit', NET_DVR_VIDEO_INTERCOM_UNIT_DEVICEID_UNION),
    ('byRes2', BYTE * 128),
])

NET_DVR_VIDEO_INTERCOM_DEVICEID_CFG = struct_tagNET_DVR_VIDEO_INTERCOM_DEVICEID_CFG
LPNET_DVR_VIDEO_INTERCOM_DEVICEID_CFG = POINTER(struct_tagNET_DVR_VIDEO_INTERCOM_DEVICEID_CFG)
tagNET_DVR_VIDEO_INTERCOM_DEVICEID_CFG = struct_tagNET_DVR_VIDEO_INTERCOM_DEVICEID_CFG
