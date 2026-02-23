from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_ipc_single_wireless_alarmcfg import NET_IPC_SINGLE_WIRELESS_ALARMCFG


class struct_tagNET_IPC_WIRELESS_ALARMCFG(Structure):
    pass

_S(struct_tagNET_IPC_WIRELESS_ALARMCFG, [
    ('struWirelessAlarm', NET_IPC_SINGLE_WIRELESS_ALARMCFG * 8),
    ('byRes', BYTE * 32),
])

NET_IPC_WIRELESS_ALARMCFG = struct_tagNET_IPC_WIRELESS_ALARMCFG
LPNET_IPC_WIRELESS_ALARMCFG = POINTER(struct_tagNET_IPC_WIRELESS_ALARMCFG)
tagNET_IPC_WIRELESS_ALARMCFG = struct_tagNET_IPC_WIRELESS_ALARMCFG
