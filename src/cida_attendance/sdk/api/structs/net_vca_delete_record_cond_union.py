from ctypes import Union

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER
from .net_vca_humanattribute_cond import NET_VCA_HUMANATTRIBUTE_COND


class union_tagNET_VCA_DELETE_RECORD_COND_UNION(Union):
    pass

_S(union_tagNET_VCA_DELETE_RECORD_COND_UNION, [
    ('struAttribute', NET_VCA_HUMANATTRIBUTE_COND),
    ('dwRecordID', DWORD),
])

NET_VCA_DELETE_RECORD_COND_UNION = union_tagNET_VCA_DELETE_RECORD_COND_UNION
LPNET_VCA_DELETE_RECORD_COND_UNION = POINTER(union_tagNET_VCA_DELETE_RECORD_COND_UNION)
tagNET_VCA_DELETE_RECORD_COND_UNION = union_tagNET_VCA_DELETE_RECORD_COND_UNION
