from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_vca_sub_procimg_v50 import NET_VCA_SUB_PROCIMG_V50


class struct_tagNET_VCA_FD_PROCIMG_RESULT_V50(Structure):
    pass

_S(struct_tagNET_VCA_FD_PROCIMG_RESULT_V50, [
    ('dwSize', DWORD),
    ('dwImageId', DWORD),
    ('byRes', BYTE * 20),
    ('dwSubImageNum', DWORD),
    ('struProcImg', NET_VCA_SUB_PROCIMG_V50 * 30),
])

NET_VCA_FD_PROCIMG_RESULT_V50 = struct_tagNET_VCA_FD_PROCIMG_RESULT_V50
LPNET_VCA_FD_PROCIMG_RESULT_V50 = POINTER(struct_tagNET_VCA_FD_PROCIMG_RESULT_V50)
tagNET_VCA_FD_PROCIMG_RESULT_V50 = struct_tagNET_VCA_FD_PROCIMG_RESULT_V50
