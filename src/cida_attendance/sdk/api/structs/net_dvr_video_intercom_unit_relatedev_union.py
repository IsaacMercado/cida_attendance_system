from ctypes import Union

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_again_relatedev import NET_DVR_AGAIN_RELATEDEV
from .net_dvr_indoor_unit_relatedev import NET_DVR_INDOOR_UNIT_RELATEDEV
from .net_dvr_manage_unit_relatedev import NET_DVR_MANAGE_UNIT_RELATEDEV
from .net_dvr_outdoor_unit_relatedev import NET_DVR_OUTDOOR_UNIT_RELATEDEV


class union_tagNET_DVR_VIDEO_INTERCOM_UNIT_RELATEDEV_UNION(Union):
    pass

_S(union_tagNET_DVR_VIDEO_INTERCOM_UNIT_RELATEDEV_UNION, [
    ('dwRes', DWORD * 256),
    ('struIndoorUnit', NET_DVR_INDOOR_UNIT_RELATEDEV),
    ('struMainOutdoorUnit', NET_DVR_OUTDOOR_UNIT_RELATEDEV),
    ('struManageUnit', NET_DVR_MANAGE_UNIT_RELATEDEV),
    ('struVillaUnit', NET_DVR_OUTDOOR_UNIT_RELATEDEV),
    ('struAgainUnit', NET_DVR_AGAIN_RELATEDEV),
])

NET_DVR_VIDEO_INTERCOM_UNIT_RELATEDEV_UNION = union_tagNET_DVR_VIDEO_INTERCOM_UNIT_RELATEDEV_UNION
LPNET_DVR_VIDEO_INTERCOM_UNIT_RELATEDEV_UNION = POINTER(union_tagNET_DVR_VIDEO_INTERCOM_UNIT_RELATEDEV_UNION)
tagNET_DVR_VIDEO_INTERCOM_UNIT_RELATEDEV_UNION = union_tagNET_DVR_VIDEO_INTERCOM_UNIT_RELATEDEV_UNION
