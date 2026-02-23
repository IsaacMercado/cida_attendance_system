from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_vca_blocklist_info import NET_VCA_BLOCKLIST_INFO


class struct_tagNET_VCA_BLOCKLIST_FASTREGISTER_PARA(Structure):
    pass

_S(struct_tagNET_VCA_BLOCKLIST_FASTREGISTER_PARA, [
    ('dwSize', DWORD),
    ('struBlockListInfo', NET_VCA_BLOCKLIST_INFO),
    ('dwImageLen', DWORD),
    ('byRes', BYTE * 124),
    ('pImage', POINTER(BYTE)),
])

NET_VCA_BLOCKLIST_FASTREGISTER_PARA = struct_tagNET_VCA_BLOCKLIST_FASTREGISTER_PARA
LPNET_VCA_BLOCKLIST_FASTREGISTER_PARA = POINTER(struct_tagNET_VCA_BLOCKLIST_FASTREGISTER_PARA)
tagNET_VCA_BLOCKLIST_FASTREGISTER_PARA = struct_tagNET_VCA_BLOCKLIST_FASTREGISTER_PARA
