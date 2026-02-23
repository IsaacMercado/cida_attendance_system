from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_vca_sub_procimg import NET_VCA_SUB_PROCIMG


class struct_tagNET_VCA_FD_PROCIMG_RESULT(Structure):
    pass

_S(struct_tagNET_VCA_FD_PROCIMG_RESULT, [
    ('dwSize', DWORD),
    ('dwImageId', DWORD),
    ('byRes', BYTE * 20),
    ('dwSubImageNum', DWORD),
    ('struProcImg', NET_VCA_SUB_PROCIMG * 30),
])

NET_VCA_FD_PROCIMG_RESULT = struct_tagNET_VCA_FD_PROCIMG_RESULT
LPNET_VCA_FD_PROCIMG_RESULT = POINTER(struct_tagNET_VCA_FD_PROCIMG_RESULT)
tagNET_VCA_FD_PROCIMG_RESULT = struct_tagNET_VCA_FD_PROCIMG_RESULT
