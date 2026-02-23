from ctypes import Union

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER
from .net_ipc_callhelp_alarmcfg import NET_IPC_CALLHELP_ALARMCFG
from .net_ipc_pir_alarmcfg_ex import NET_IPC_PIR_ALARMCFG_EX
from .net_ipc_wireless_alarmcfg import NET_IPC_WIRELESS_ALARMCFG


class union_tagNET_IPC_AUX_ALARMCFG_UNION(Union):
    pass

_S(union_tagNET_IPC_AUX_ALARMCFG_UNION, [
    ('uLen', DWORD * 472),
    ('struPIRAlarm', NET_IPC_PIR_ALARMCFG_EX),
    ('struWirelessAlarm', NET_IPC_WIRELESS_ALARMCFG),
    ('struCallHelpAlarm', NET_IPC_CALLHELP_ALARMCFG),
])

NET_IPC_AUX_ALARMCFG_UNION = union_tagNET_IPC_AUX_ALARMCFG_UNION
LPNET_IPC_AUX_ALARMCFG_UNION = POINTER(union_tagNET_IPC_AUX_ALARMCFG_UNION)
tagNET_IPC_AUX_ALARMCFG_UNION = union_tagNET_IPC_AUX_ALARMCFG_UNION
