from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_alarmhost_netparam_v50 import NET_DVR_ALARMHOST_NETPARAM_V50


class struct__tagNET_DVR_ALARMHOST_NETCFG_V50(Structure):
    pass

_S(struct__tagNET_DVR_ALARMHOST_NETCFG_V50, [
    ('dwSize', DWORD),
    ('struNetCenter', NET_DVR_ALARMHOST_NETPARAM_V50 * 4),
    ('byRes1', BYTE * 128),
])

NET_DVR_ALARMHOST_NETCFG_V50 = struct__tagNET_DVR_ALARMHOST_NETCFG_V50
LPNET_DVR_ALARMHOST_NETCFG_V50 = POINTER(struct__tagNET_DVR_ALARMHOST_NETCFG_V50)
_tagNET_DVR_ALARMHOST_NETCFG_V50 = struct__tagNET_DVR_ALARMHOST_NETCFG_V50
