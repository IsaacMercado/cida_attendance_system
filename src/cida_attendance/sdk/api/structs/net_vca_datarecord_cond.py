from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_vca_humanattribute_cond import NET_VCA_HUMANATTRIBUTE_COND


class struct_tagNET_VCA_DATARECORD_COND(Structure):
    pass

_S(struct_tagNET_VCA_DATARECORD_COND, [
    ('dwDataBaseID', DWORD),
    ('struAttribute', NET_VCA_HUMANATTRIBUTE_COND),
    ('byRes', BYTE * 80),
])

NET_VCA_DATARECORD_COND = struct_tagNET_VCA_DATARECORD_COND
LPNET_VCA_DATARECORD_COND = POINTER(struct_tagNET_VCA_DATARECORD_COND)
tagNET_VCA_DATARECORD_COND = struct_tagNET_VCA_DATARECORD_COND
