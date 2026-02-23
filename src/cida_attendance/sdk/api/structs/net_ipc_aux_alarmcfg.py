from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_ipc_single_aux_alarmcfg import NET_IPC_SINGLE_AUX_ALARMCFG


class struct_tagNET_IPC_AUX_ALARMCFG(Structure):
    pass

_S(struct_tagNET_IPC_AUX_ALARMCFG, [
    ('dwSize', DWORD),
    ('struAlarm', NET_IPC_SINGLE_AUX_ALARMCFG * 8),
    ('byRes', BYTE * 64),
])

NET_IPC_AUX_ALARMCFG = struct_tagNET_IPC_AUX_ALARMCFG
LPNET_IPC_AUX_ALARMCFG = POINTER(struct_tagNET_IPC_AUX_ALARMCFG)
tagNET_IPC_AUX_ALARMCFG = struct_tagNET_IPC_AUX_ALARMCFG
