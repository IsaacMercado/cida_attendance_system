from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_vca_picmodel_result import NET_VCA_PICMODEL_RESULT


class struct_tagNET_VCA_BLOCKLIST_PIC(Structure):
    pass

_S(struct_tagNET_VCA_BLOCKLIST_PIC, [
    ('dwSize', DWORD),
    ('dwFacePicNum', DWORD),
    ('byRes', BYTE * 20),
    ('struBlockListPic', NET_VCA_PICMODEL_RESULT * 10),
])

NET_VCA_BLOCKLIST_PIC = struct_tagNET_VCA_BLOCKLIST_PIC
LPNET_VCA_BLOCKLIST_PIC = POINTER(struct_tagNET_VCA_BLOCKLIST_PIC)
tagNET_VCA_BLOCKLIST_PIC = struct_tagNET_VCA_BLOCKLIST_PIC
