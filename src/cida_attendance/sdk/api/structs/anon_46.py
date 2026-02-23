from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_proto_type import NET_DVR_PROTO_TYPE


class struct_anon_46(Structure):
    pass

_S(struct_anon_46, [
    ('dwSize', DWORD),
    ('dwProtoNum', DWORD),
    ('struProto', NET_DVR_PROTO_TYPE * 50),
    ('byRes', BYTE * 8),
])

NET_DVR_IPC_PROTO_LIST = struct_anon_46
LPNET_DVR_IPC_PROTO_LIST = POINTER(struct_anon_46)
