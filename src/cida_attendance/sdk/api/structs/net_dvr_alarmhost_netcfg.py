from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_alarmhost_netparam import NET_DVR_ALARMHOST_NETPARAM


class struct_tagNET_DVR_ALARMHOST_NETCFG(Structure):
    pass

_S(struct_tagNET_DVR_ALARMHOST_NETCFG, [
    ('dwSize', DWORD),
    ('struNetCenter', NET_DVR_ALARMHOST_NETPARAM * 4),
    ('byRes1', BYTE * 32),
])

NET_DVR_ALARMHOST_NETCFG = struct_tagNET_DVR_ALARMHOST_NETCFG
LPNET_DVR_ALARMHOST_NETCFG = POINTER(struct_tagNET_DVR_ALARMHOST_NETCFG)
tagNET_DVR_ALARMHOST_NETCFG = struct_tagNET_DVR_ALARMHOST_NETCFG
