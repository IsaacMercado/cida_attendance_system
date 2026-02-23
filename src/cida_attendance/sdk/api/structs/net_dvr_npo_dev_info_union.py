from ctypes import Union

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_dvr_redundant_device_info import NET_DVR_REDUNDANT_DEVICE_INFO
from .net_dvr_redundant_device_info_v50 import NET_DVR_REDUNDANT_DEVICE_INFO_V50
from .net_dvr_working_device_info import NET_DVR_WORKING_DEVICE_INFO
from .net_dvr_working_device_info_v50 import NET_DVR_WORKING_DEVICE_INFO_V50


class union_tagNET_DVR_NPO_DEV_INFO_UNION(Union):
    pass

_S(union_tagNET_DVR_NPO_DEV_INFO_UNION, [
    ('byUnionLen', BYTE * 512),
    ('struWorkingDeviceInfo', NET_DVR_WORKING_DEVICE_INFO),
    ('struRedundantDeviceInfo', NET_DVR_REDUNDANT_DEVICE_INFO),
    ('struWorkingDeviceInfoV50', NET_DVR_WORKING_DEVICE_INFO_V50),
    ('struRedundantDeviceInfoV50', NET_DVR_REDUNDANT_DEVICE_INFO_V50),
])

NET_DVR_NPO_DEV_INFO_UNION = union_tagNET_DVR_NPO_DEV_INFO_UNION
LPNET_DVR_NPO_DEV_INFO_UNION = POINTER(union_tagNET_DVR_NPO_DEV_INFO_UNION)
tagNET_DVR_NPO_DEV_INFO_UNION = union_tagNET_DVR_NPO_DEV_INFO_UNION
