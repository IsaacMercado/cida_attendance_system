from ctypes import Structure

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER
from .net_its_traffic_data_host import NET_ITS_TRAFFIC_DATA_HOST


class struct_tagNET_ITS_UPLOAD_CFG(Structure):
    pass

_S(struct_tagNET_ITS_UPLOAD_CFG, [
    ('dwSize', DWORD),
    ('struRemoteDataHost1', NET_ITS_TRAFFIC_DATA_HOST),
    ('struRemoteDataHost2', NET_ITS_TRAFFIC_DATA_HOST),
])

NET_ITS_UPLOAD_CFG = struct_tagNET_ITS_UPLOAD_CFG
LPNET_ITS_UPLOAD_CFG = POINTER(struct_tagNET_ITS_UPLOAD_CFG)
tagNET_ITS_UPLOAD_CFG = struct_tagNET_ITS_UPLOAD_CFG
