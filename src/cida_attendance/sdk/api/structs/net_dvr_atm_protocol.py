from ctypes import Structure

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_atm_proto_list import NET_DVR_ATM_PROTO_LIST
from .net_dvr_atm_proto_type import NET_DVR_ATM_PROTO_TYPE


class struct_tagNET_DVR_ATM_PROTOCOL(Structure):
    pass

_S(struct_tagNET_DVR_ATM_PROTOCOL, [
    ('dwSize', DWORD),
    ('struNetListenList', NET_DVR_ATM_PROTO_LIST),
    ('struSerialListenList', NET_DVR_ATM_PROTO_LIST),
    ('struNetProtoList', NET_DVR_ATM_PROTO_LIST),
    ('struSerialProtoList', NET_DVR_ATM_PROTO_LIST),
    ('struCustomProto', NET_DVR_ATM_PROTO_TYPE),
])

NET_DVR_ATM_PROTOCOL = struct_tagNET_DVR_ATM_PROTOCOL
LPNET_DVR_ATM_PROTOCOL = POINTER(struct_tagNET_DVR_ATM_PROTOCOL)
tagNET_DVR_ATM_PROTOCOL = struct_tagNET_DVR_ATM_PROTOCOL
