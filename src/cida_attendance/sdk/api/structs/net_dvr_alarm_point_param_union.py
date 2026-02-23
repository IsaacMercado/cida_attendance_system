from ctypes import Union

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_dvr_alarm_sensor_point_cfg import NET_DVR_ALARM_SENSOR_POINT_CFG
from .net_dvr_alarm_switch_point_cfg import NET_DVR_ALARM_SWITCH_POINT_CFG


class union_tagNET_DVR_ALARM_POINT_PARAM_UNION(Union):
    pass

_S(union_tagNET_DVR_ALARM_POINT_PARAM_UNION, [
    ('byLength', BYTE * 64),
    ('struSensor', NET_DVR_ALARM_SENSOR_POINT_CFG),
    ('struSwitch', NET_DVR_ALARM_SWITCH_POINT_CFG),
])

NET_DVR_ALARM_POINT_PARAM_UNION = union_tagNET_DVR_ALARM_POINT_PARAM_UNION
LPNET_DVR_ALARM_POINT_PARAM_UNION = POINTER(union_tagNET_DVR_ALARM_POINT_PARAM_UNION)
tagNET_DVR_ALARM_POINT_PARAM_UNION = union_tagNET_DVR_ALARM_POINT_PARAM_UNION
