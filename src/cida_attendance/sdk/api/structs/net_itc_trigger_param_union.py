from ctypes import Union

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_via_vtcoil_param import NET_DVR_VIA_VTCOIL_PARAM
from .net_ipc_post_hvt_param import NET_IPC_POST_HVT_PARAM
from .net_itc_epolice_iotl_param import NET_ITC_EPOLICE_IOTL_PARAM
from .net_itc_epolice_rs485_param import NET_ITC_EPOLICE_RS485_PARAM
from .net_itc_nocomity_pedestrian_param import NET_ITC_NOCOMITY_PEDESTRIAN_PARAM
from .net_itc_post_hvt_param import NET_ITC_POST_HVT_PARAM
from .net_itc_post_hvt_param_v50 import NET_ITC_POST_HVT_PARAM_V50
from .net_itc_post_imt_param import NET_ITC_POST_IMT_PARAM
from .net_itc_post_iospeed_param import NET_ITC_POST_IOSPEED_PARAM
from .net_itc_post_mobile_param import NET_ITC_POST_MOBILE_PARAM
from .net_itc_post_mpr_param import NET_ITC_POST_MPR_PARAM
from .net_itc_post_prs_param import NET_ITC_POST_PRS_PARAM
from .net_itc_post_rs485_param import NET_ITC_POST_RS485_PARAM
from .net_itc_post_rs485_radar_param import NET_ITC_POST_RS485_RADAR_PARAM
from .net_itc_post_singleio_param import NET_ITC_POST_SINGLEIO_PARAM
from .net_itc_post_vtcoil_param import NET_ITC_POST_VTCOIL_PARAM
from .net_itc_redlight_pedestrian_param import NET_ITC_REDLIGHT_PEDESTRIAN_PARAM


class union_tagNET_ITC_TRIGGER_PARAM_UNION(Union):
    pass

_S(union_tagNET_ITC_TRIGGER_PARAM_UNION, [
    ('uLen', DWORD * 1070),
    ('struIOSpeed', NET_ITC_POST_IOSPEED_PARAM),
    ('struSingleIO', NET_ITC_POST_SINGLEIO_PARAM),
    ('struPostRs485', NET_ITC_POST_RS485_PARAM),
    ('struPostRadar', NET_ITC_POST_RS485_RADAR_PARAM),
    ('struVtCoil', NET_ITC_POST_VTCOIL_PARAM),
    ('struHvt', NET_ITC_POST_HVT_PARAM),
    ('struIOTL', NET_ITC_EPOLICE_IOTL_PARAM),
    ('struEpoliceRs485', NET_ITC_EPOLICE_RS485_PARAM),
    ('struPERs485', NET_ITC_EPOLICE_RS485_PARAM),
    ('struPostMpr', NET_ITC_POST_MPR_PARAM),
    ('struViaVtCoil', NET_DVR_VIA_VTCOIL_PARAM),
    ('struPostImt', NET_ITC_POST_IMT_PARAM),
    ('struPostPrs', NET_ITC_POST_PRS_PARAM),
    ('struIpcHvt', NET_IPC_POST_HVT_PARAM),
    ('struHvtV50', NET_ITC_POST_HVT_PARAM_V50),
    ('struPostMobile', NET_ITC_POST_MOBILE_PARAM),
    ('struNoComityPed', NET_ITC_NOCOMITY_PEDESTRIAN_PARAM),
    ('struRedLightPed', NET_ITC_REDLIGHT_PEDESTRIAN_PARAM),
])

NET_ITC_TRIGGER_PARAM_UNION = union_tagNET_ITC_TRIGGER_PARAM_UNION
LPNET_ITC_TRIGGER_PARAM_UNION = POINTER(union_tagNET_ITC_TRIGGER_PARAM_UNION)
tagNET_ITC_TRIGGER_PARAM_UNION = union_tagNET_ITC_TRIGGER_PARAM_UNION
