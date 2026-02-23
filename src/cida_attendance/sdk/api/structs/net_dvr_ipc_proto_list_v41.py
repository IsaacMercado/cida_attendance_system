from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_IPC_PROTO_LIST_V41(Structure):
    pass

_S(struct_tagNET_DVR_IPC_PROTO_LIST_V41, [
    ('dwSize', DWORD),
    ('dwProtoNum', DWORD),
    ('pBuffer', POINTER(BYTE)),
    ('dwBufferLen', DWORD),
    ('byRes', BYTE * 32),
])

NET_DVR_IPC_PROTO_LIST_V41 = struct_tagNET_DVR_IPC_PROTO_LIST_V41
LPNET_DVR_IPC_PROTO_LIST_V41 = POINTER(struct_tagNET_DVR_IPC_PROTO_LIST_V41)
tagNET_DVR_IPC_PROTO_LIST_V41 = struct_tagNET_DVR_IPC_PROTO_LIST_V41
