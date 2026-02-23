from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_SPEEDLMT_PARA(Structure):
    pass

_S(struct_tagNET_DVR_SPEEDLMT_PARA, [
    ('bStartMaxSpeedLimit', BYTE),
    ('bStartMinSpeedLimit', BYTE),
    ('byRes', BYTE * 6),
    ('dwMaxSpeedLimit', DWORD),
    ('dwMinSpeedLimit', DWORD),
])

NET_DVR_SPEEDLMT_PARA = struct_tagNET_DVR_SPEEDLMT_PARA
LPNET_DVR_SPEEDLMT_PARA = POINTER(struct_tagNET_DVR_SPEEDLMT_PARA)
tagNET_DVR_SPEEDLMT_PARA = struct_tagNET_DVR_SPEEDLMT_PARA
