from ctypes import Union

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER
from .net_ipc_callhelp_alarmcfg import NET_IPC_CALLHELP_ALARMCFG
from .net_ipc_pir_alarmcfg import NET_IPC_PIR_ALARMCFG
from .net_ipc_single_wireless_alarmcfg import NET_IPC_SINGLE_WIRELESS_ALARMCFG


class union_tagNET_IPC_AUXALARM_UPLOAD_UNION(Union):
    pass

_S(union_tagNET_IPC_AUXALARM_UPLOAD_UNION, [
    ('uLen', DWORD * 66),
    ('struPIRAlarm', NET_IPC_PIR_ALARMCFG),
    ('struWirelessAlarm', NET_IPC_SINGLE_WIRELESS_ALARMCFG),
    ('struCallHelpAlarm', NET_IPC_CALLHELP_ALARMCFG),
])

NET_IPC_AUXALARM_UPLOAD_UNION = union_tagNET_IPC_AUXALARM_UPLOAD_UNION
LPNET_IPC_AUXALARM_UPLOAD_UNION = POINTER(union_tagNET_IPC_AUXALARM_UPLOAD_UNION)
tagNET_IPC_AUXALARM_UPLOAD_UNION = union_tagNET_IPC_AUXALARM_UPLOAD_UNION
