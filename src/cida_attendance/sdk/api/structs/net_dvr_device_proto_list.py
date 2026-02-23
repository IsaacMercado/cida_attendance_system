from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_proto_type import NET_DVR_PROTO_TYPE


class struct_tagNET_DVR_DEVICE_PROTO_LIST(Structure):
    pass

_S(struct_tagNET_DVR_DEVICE_PROTO_LIST, [
    ('dwSize', DWORD),
    ('dwProtoNum', DWORD),
    ('struProtoType', NET_DVR_PROTO_TYPE * 256),
    ('byRes', BYTE * 12),
])

NET_DVR_DEVICE_PROTO_LIST = struct_tagNET_DVR_DEVICE_PROTO_LIST
LPNET_DVR_DEVICE_PROTO_LIST = POINTER(struct_tagNET_DVR_DEVICE_PROTO_LIST)
tagNET_DVR_DEVICE_PROTO_LIST = struct_tagNET_DVR_DEVICE_PROTO_LIST
