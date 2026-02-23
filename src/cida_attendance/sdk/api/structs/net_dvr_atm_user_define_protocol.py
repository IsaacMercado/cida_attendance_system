from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_dvr_atm_package_action import NET_DVR_ATM_PACKAGE_ACTION
from .net_dvr_atm_package_date import NET_DVR_ATM_PACKAGE_DATE
from .net_dvr_atm_package_others import NET_DVR_ATM_PACKAGE_OTHERS
from .net_dvr_atm_package_time import NET_DVR_ATM_PACKAGE_TIME
from .net_dvr_filter import NET_DVR_FILTER
from .net_dvr_identificat import NET_DVR_IDENTIFICAT
from .net_dvr_overlay_channel import NET_DVR_OVERLAY_CHANNEL


class struct_tagNET_DVR_ATM_USER_DEFINE_PROTOCOL(Structure):
    pass

_S(struct_tagNET_DVR_ATM_USER_DEFINE_PROTOCOL, [
    ('struIdentification', NET_DVR_IDENTIFICAT),
    ('struFilter', NET_DVR_FILTER),
    ('struCardNoPara', NET_DVR_ATM_PACKAGE_OTHERS),
    ('struTradeActionPara', NET_DVR_ATM_PACKAGE_ACTION * 12),
    ('struAmountPara', NET_DVR_ATM_PACKAGE_OTHERS),
    ('struSerialNoPara', NET_DVR_ATM_PACKAGE_OTHERS),
    ('struOverlayChan', NET_DVR_OVERLAY_CHANNEL),
    ('struRes1', NET_DVR_ATM_PACKAGE_DATE),
    ('struRes2', NET_DVR_ATM_PACKAGE_TIME),
    ('byRes3', BYTE * 124),
])

NET_DVR_ATM_USER_DEFINE_PROTOCOL = struct_tagNET_DVR_ATM_USER_DEFINE_PROTOCOL
LPNET_DVR_ATM_USER_DEFINE_PROTOCOL = POINTER(struct_tagNET_DVR_ATM_USER_DEFINE_PROTOCOL)
tagNET_DVR_ATM_USER_DEFINE_PROTOCOL = struct_tagNET_DVR_ATM_USER_DEFINE_PROTOCOL
