from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .net_dvr_addr_domain_info import NET_DVR_ADDR_DOMAIN_INFO


class struct_tagNET_DVR_ALARMCENTER_NETCFG(Structure):
    pass

_S(struct_tagNET_DVR_ALARMCENTER_NETCFG, [
    ('dwSize', DWORD),
    ('byAuxiliaryAlarmAddr', BYTE * 64),
    ('wAuxiliaryAlarmPort', WORD),
    ('struHostAddr', NET_DVR_ADDR_DOMAIN_INFO * 6),
    ('byRes', BYTE * 172),
])

NET_DVR_ALARMCENTER_NETCFG = struct_tagNET_DVR_ALARMCENTER_NETCFG
LPNET_DVR_ALARMCENTER_NETCFG = POINTER(struct_tagNET_DVR_ALARMCENTER_NETCFG)
tagNET_DVR_ALARMCENTER_NETCFG = struct_tagNET_DVR_ALARMCENTER_NETCFG
