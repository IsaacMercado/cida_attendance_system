from ctypes import Union

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_dvr_indoor_unit_operation_time_cfg import (
    NET_DVR_INDOOR_UNIT_OPERATION_TIME_CFG,
)
from .net_dvr_manage_unit_operation_time_cfg import (
    NET_DVR_MANAGE_UNIT_OPERATION_TIME_CFG,
)
from .net_dvr_outdoor_unit_operation_time_cfg import (
    NET_DVR_OUTDOOR_UNIT_OPERATION_TIME_CFG,
)


class union_tagNET_DVR_VIDEO_INTERCOM_OPERATION_TIME_UNION(Union):
    pass

_S(union_tagNET_DVR_VIDEO_INTERCOM_OPERATION_TIME_UNION, [
    ('byLen', BYTE * 128),
    ('struIndoorUnit', NET_DVR_INDOOR_UNIT_OPERATION_TIME_CFG),
    ('struOutdoorUnit', NET_DVR_OUTDOOR_UNIT_OPERATION_TIME_CFG),
    ('struManageUnit', NET_DVR_MANAGE_UNIT_OPERATION_TIME_CFG),
])

NET_DVR_VIDEO_INTERCOM_OPERATION_TIME_UNION = union_tagNET_DVR_VIDEO_INTERCOM_OPERATION_TIME_UNION
LPNET_DVR_VIDEO_INTERCOM_OPERATION_TIME_UNION = POINTER(union_tagNET_DVR_VIDEO_INTERCOM_OPERATION_TIME_UNION)
tagNET_DVR_VIDEO_INTERCOM_OPERATION_TIME_UNION = union_tagNET_DVR_VIDEO_INTERCOM_OPERATION_TIME_UNION
