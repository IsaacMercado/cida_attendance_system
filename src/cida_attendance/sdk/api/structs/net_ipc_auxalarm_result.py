from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_ipc_auxalarm_upload_union import NET_IPC_AUXALARM_UPLOAD_UNION


class struct_tagNET_IPC_AUXALARM_RESULT(Structure):
    pass

_S(struct_tagNET_IPC_AUXALARM_RESULT, [
    ('dwSize', DWORD),
    ('dwChannel', DWORD),
    ('byAlarmType', BYTE),
    ('byRes1', BYTE * 3),
    ('struAuxAlarm', NET_IPC_AUXALARM_UPLOAD_UNION),
    ('byDeviceID', BYTE * 32),
    ('byRes', BYTE * 32),
])

NET_IPC_AUXALARM_RESULT = struct_tagNET_IPC_AUXALARM_RESULT
LPNET_IPC_AUXALARM_RESULT = POINTER(struct_tagNET_IPC_AUXALARM_RESULT)
tagNET_IPC_AUXALARM_RESULT = struct_tagNET_IPC_AUXALARM_RESULT
