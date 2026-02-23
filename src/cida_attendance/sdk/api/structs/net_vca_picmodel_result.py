from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_VCA_PICMODEL_RESULT(Structure):
    pass

_S(struct_tagNET_VCA_PICMODEL_RESULT, [
    ('dwImageLen', DWORD),
    ('dwModelLen', DWORD),
    ('byRes', BYTE * 20),
    ('pImage', POINTER(BYTE)),
    ('pModel', POINTER(BYTE)),
])

NET_VCA_PICMODEL_RESULT = struct_tagNET_VCA_PICMODEL_RESULT
LPNET_VCA_PICMODEL_RESULT = POINTER(struct_tagNET_VCA_PICMODEL_RESULT)
tagNET_VCA_PICMODEL_RESULT = struct_tagNET_VCA_PICMODEL_RESULT
