from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from ..enums import VCA_DELETE_RECORD_TYPE
from .net_vca_delete_record_cond_union import NET_VCA_DELETE_RECORD_COND_UNION


class struct_tagNET_VCA_DELETE_RECORD_COND(Structure):
    pass

_S(struct_tagNET_VCA_DELETE_RECORD_COND, [
    ('dwDeleteType', VCA_DELETE_RECORD_TYPE),
    ('uDeleteCond', NET_VCA_DELETE_RECORD_COND_UNION),
    ('byRes', BYTE * 40),
])

NET_VCA_DELETE_RECORD_COND = struct_tagNET_VCA_DELETE_RECORD_COND
LPNET_VCA_DELETE_RECORD_COND = POINTER(struct_tagNET_VCA_DELETE_RECORD_COND)
tagNET_VCA_DELETE_RECORD_COND = struct_tagNET_VCA_DELETE_RECORD_COND
