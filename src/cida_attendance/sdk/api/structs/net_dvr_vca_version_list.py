from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_vca_version import NET_DVR_VCA_VERSION


class struct_tagNET_DVR_VCA_VERSION_LIST(Structure):
    pass

_S(struct_tagNET_DVR_VCA_VERSION_LIST, [
    ('dwSize', DWORD),
    ('struVcaVersion', NET_DVR_VCA_VERSION * 64),
    ('byRes', BYTE * 128),
])

NET_DVR_VCA_VERSION_LIST = struct_tagNET_DVR_VCA_VERSION_LIST
LPNET_DVR_VCA_VERSION_LIST = POINTER(struct_tagNET_DVR_VCA_VERSION_LIST)
tagNET_DVR_VCA_VERSION_LIST = struct_tagNET_DVR_VCA_VERSION_LIST
