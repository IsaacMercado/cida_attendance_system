from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_RTSP_PARAMS_CFG(Structure):
    pass

_S(struct_tagNET_DVR_RTSP_PARAMS_CFG, [
    ('dwMaxBuffRoomNum', DWORD),
    ('byUseSort', BYTE),
    ('byRes', BYTE * 123),
])

NET_DVR_RTSP_PARAMS_CFG = struct_tagNET_DVR_RTSP_PARAMS_CFG
LPNET_DVR_RTSP_PARAMS_CFG = POINTER(struct_tagNET_DVR_RTSP_PARAMS_CFG)
tagNET_DVR_RTSP_PARAMS_CFG = struct_tagNET_DVR_RTSP_PARAMS_CFG
