from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_DISPINPUT_CFG(Structure):
    pass

_S(struct_tagNET_DVR_DISPINPUT_CFG, [
    ('dwSize', DWORD),
    ('dwDispInputNo', DWORD),
    ('dwEDIDFileNo', DWORD),
    ('byRes', BYTE * 32),
])

NET_DVR_DISPINPUT_CFG = struct_tagNET_DVR_DISPINPUT_CFG
LPNET_DVR_DISPINPUT_CFG = POINTER(struct_tagNET_DVR_DISPINPUT_CFG)
tagNET_DVR_DISPINPUT_CFG = struct_tagNET_DVR_DISPINPUT_CFG
