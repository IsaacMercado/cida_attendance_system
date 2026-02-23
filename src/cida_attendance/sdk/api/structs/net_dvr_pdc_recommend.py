from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_PDC_RECOMMEND(Structure):
    pass

_S(struct_tagNET_DVR_PDC_RECOMMEND, [
    ('dwSize', DWORD),
    ('wWidth', WORD),
    ('byRes', BYTE * 126),
])

NET_DVR_PDC_RECOMMEND = struct_tagNET_DVR_PDC_RECOMMEND
LPNET_DVR_PDC_RECOMMEND = POINTER(struct_tagNET_DVR_PDC_RECOMMEND)
tagNET_DVR_PDC_RECOMMEND = struct_tagNET_DVR_PDC_RECOMMEND
