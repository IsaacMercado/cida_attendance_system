from ctypes import Structure

from ..base_classes import _S
from ..ctypes_preamble import POINTER
from .net_dvr_socks_proxy_para import NET_DVR_SOCKS_PROXY_PARA


class struct_tagNET_DVR_SOCKS_PROXYS(Structure):
    pass

_S(struct_tagNET_DVR_SOCKS_PROXYS, [
    ('struProxy', NET_DVR_SOCKS_PROXY_PARA * 32),
])

NET_DVR_SOCKS_PROXYS = struct_tagNET_DVR_SOCKS_PROXYS
LPNET_DVR_SOCKS_PROXYS = POINTER(struct_tagNET_DVR_SOCKS_PROXYS)
tagNET_DVR_SOCKS_PROXYS = struct_tagNET_DVR_SOCKS_PROXYS
