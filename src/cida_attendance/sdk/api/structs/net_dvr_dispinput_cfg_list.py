from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_dispinput_cfg import LPNET_DVR_DISPINPUT_CFG


class struct_tagNET_DVR_DISPINPUT_CFG_LIST(Structure):
    pass

_S(struct_tagNET_DVR_DISPINPUT_CFG_LIST, [
    ('dwSize', DWORD),
    ('dwDispInputNum', DWORD),
    ('lpstruBuffer', LPNET_DVR_DISPINPUT_CFG),
    ('dwBufferSize', DWORD),
    ('byRes', BYTE * 32),
])

NET_DVR_DISPINPUT_CFG_LIST = struct_tagNET_DVR_DISPINPUT_CFG_LIST
LPNET_DVR_DISPINPUT_CFG_LIST = POINTER(struct_tagNET_DVR_DISPINPUT_CFG_LIST)
tagNET_DVR_DISPINPUT_CFG_LIST = struct_tagNET_DVR_DISPINPUT_CFG_LIST
