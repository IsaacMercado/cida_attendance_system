from ctypes import Union

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_dvr_indoor_unit_deviceid import NET_DVR_INDOOR_UNIT_DEVICEID
from .net_dvr_manage_unit_deviceid import NET_DVR_MANAGE_UNIT_DEVICEID
from .net_dvr_outdoor_fence_deviceid import NET_DVR_OUTDOOR_FENCE_DEVICEID
from .net_dvr_outdoor_unit_deviceid import NET_DVR_OUTDOOR_UNIT_DEVICEID


class union_tagNET_DVR_VIDEO_INTERCOM_UNIT_DEVICEID_UNION(Union):
    pass

_S(union_tagNET_DVR_VIDEO_INTERCOM_UNIT_DEVICEID_UNION, [
    ('byLen', BYTE * 128),
    ('struIndoorUnit', NET_DVR_INDOOR_UNIT_DEVICEID),
    ('struOutdoorUnit', NET_DVR_OUTDOOR_UNIT_DEVICEID),
    ('struManageUnit', NET_DVR_MANAGE_UNIT_DEVICEID),
    ('struFenceUnit', NET_DVR_OUTDOOR_FENCE_DEVICEID),
    ('struVillaOutdoorUnit', NET_DVR_OUTDOOR_UNIT_DEVICEID),
    ('struAgainConfirmUnit', NET_DVR_OUTDOOR_UNIT_DEVICEID),
])

NET_DVR_VIDEO_INTERCOM_UNIT_DEVICEID_UNION = union_tagNET_DVR_VIDEO_INTERCOM_UNIT_DEVICEID_UNION
LPNET_DVR_VIDEO_INTERCOM_UNIT_DEVICEID_UNION = POINTER(union_tagNET_DVR_VIDEO_INTERCOM_UNIT_DEVICEID_UNION)
tagNET_DVR_VIDEO_INTERCOM_UNIT_DEVICEID_UNION = union_tagNET_DVR_VIDEO_INTERCOM_UNIT_DEVICEID_UNION
