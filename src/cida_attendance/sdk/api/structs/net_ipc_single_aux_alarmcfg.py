from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_ipc_aux_alarmcfg_union import NET_IPC_AUX_ALARMCFG_UNION


class struct_tagNET_IPC_SINGLE_AUX_ALARMCFG(Structure):
    pass

_S(struct_tagNET_IPC_SINGLE_AUX_ALARMCFG, [
    ('byAlarmType', BYTE),
    ('byRes1', BYTE * 3),
    ('uAlarm', NET_IPC_AUX_ALARMCFG_UNION),
    ('byRes', BYTE * 16),
])

NET_IPC_SINGLE_AUX_ALARMCFG = struct_tagNET_IPC_SINGLE_AUX_ALARMCFG
LPNET_IPC_SINGLE_AUX_ALARMCFG = POINTER(struct_tagNET_IPC_SINGLE_AUX_ALARMCFG)
tagNET_IPC_SINGLE_AUX_ALARMCFG = struct_tagNET_IPC_SINGLE_AUX_ALARMCFG
