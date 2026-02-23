from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR
from .net_dvr_platecheck_para import NET_DVR_PLATECHECK_PARA
from .net_dvr_speedlmt_para import NET_DVR_SPEEDLMT_PARA


class struct_tagNET_DVR_ENFORCESYS_PARA(Structure):
    pass

_S(struct_tagNET_DVR_ENFORCESYS_PARA, [
    ('dwSize', DWORD),
    ('struSpeedLmtPara', NET_DVR_SPEEDLMT_PARA),
    ('struPlateCheckPara', NET_DVR_PLATECHECK_PARA),
    ('bySelPeccType', BYTE),
    ('byEnfOptHabit', BYTE),
    ('byAdjPrevFpsMode', BYTE),
    ('byRes1', BYTE),
    ('struUploadServerIp', NET_DVR_IPADDR),
    ('wUploadServerPort', WORD),
    ('byRes2', BYTE * 18),
])

NET_DVR_ENFORCESYS_PARA = struct_tagNET_DVR_ENFORCESYS_PARA
LPNET_DVR_ENFORCESYS_PARA = POINTER(struct_tagNET_DVR_ENFORCESYS_PARA)
tagNET_DVR_ENFORCESYS_PARA = struct_tagNET_DVR_ENFORCESYS_PARA
