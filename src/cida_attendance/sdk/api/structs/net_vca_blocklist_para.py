from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_vca_blocklist_info import NET_VCA_BLOCKLIST_INFO
from .net_vca_picmodel_result import NET_VCA_PICMODEL_RESULT


class struct_tagNET_VCA_BLOCKLIST_PARA(Structure):
    pass

_S(struct_tagNET_VCA_BLOCKLIST_PARA, [
    ('dwSize', DWORD),
    ('struBlockListInfo', NET_VCA_BLOCKLIST_INFO),
    ('dwRegisterPicNum', DWORD),
    ('struRegisterPic', NET_VCA_PICMODEL_RESULT * 10),
    ('byRes', BYTE * 40),
])

NET_VCA_BLOCKLIST_PARA = struct_tagNET_VCA_BLOCKLIST_PARA
LPNET_VCA_BLOCKLIST_PARA = POINTER(struct_tagNET_VCA_BLOCKLIST_PARA)
tagNET_VCA_BLOCKLIST_PARA = struct_tagNET_VCA_BLOCKLIST_PARA
