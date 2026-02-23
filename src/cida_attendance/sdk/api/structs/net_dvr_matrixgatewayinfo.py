from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_matrixgatewaynote import NET_DVR_MATRIXGATEWAYNOTE


class struct_tagNET_DVR_MATRIXGATEWAYINFO(Structure):
    pass

_S(struct_tagNET_DVR_MATRIXGATEWAYINFO, [
    ('dwSize', DWORD),
    ('struGatewayNote', NET_DVR_MATRIXGATEWAYNOTE * 1024),
    ('byRes', BYTE * 32),
])

NET_DVR_MATRIXGATEWAYINFO = struct_tagNET_DVR_MATRIXGATEWAYINFO
LPNET_DVR_MATRIXGATEWAYINFO = POINTER(struct_tagNET_DVR_MATRIXGATEWAYINFO)
tagNET_DVR_MATRIXGATEWAYINFO = struct_tagNET_DVR_MATRIXGATEWAYINFO
