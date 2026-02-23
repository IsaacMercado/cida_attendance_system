from ctypes import Structure

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_atm_proto_type import NET_DVR_ATM_PROTO_TYPE


class struct_tagNET_DVR_ATM_PROTO_LIST(Structure):
    pass

_S(struct_tagNET_DVR_ATM_PROTO_LIST, [
    ('dwAtmProtoNum', DWORD),
    ('struAtmProtoType', NET_DVR_ATM_PROTO_TYPE * 256),
])

NET_DVR_ATM_PROTO_LIST = struct_tagNET_DVR_ATM_PROTO_LIST
LPNET_DVR_ATM_PROTO_LIST = POINTER(struct_tagNET_DVR_ATM_PROTO_LIST)
tagNET_DVR_ATM_PROTO_LIST = struct_tagNET_DVR_ATM_PROTO_LIST
