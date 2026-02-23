from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_vca_human_attribute import NET_VCA_HUMAN_ATTRIBUTE


class struct_tagNET_VCA_FAST_DATARECORD_INFO(Structure):
    pass

_S(struct_tagNET_VCA_FAST_DATARECORD_INFO, [
    ('dwSize', DWORD),
    ('struAttribute', NET_VCA_HUMAN_ATTRIBUTE),
    ('byRemark1', BYTE * 32),
    ('byRemark2', BYTE * 64),
    ('dwImageLen', DWORD),
    ('byRes', BYTE * 80),
    ('pImage', POINTER(BYTE)),
])

NET_VCA_FAST_DATARECORD_INFO = struct_tagNET_VCA_FAST_DATARECORD_INFO
LPNET_VCA_FAST_DATARECORD_INFO = POINTER(struct_tagNET_VCA_FAST_DATARECORD_INFO)
tagNET_VCA_FAST_DATARECORD_INFO = struct_tagNET_VCA_FAST_DATARECORD_INFO
