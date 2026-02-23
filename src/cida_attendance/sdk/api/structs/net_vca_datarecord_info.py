from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_vca_human_attribute import NET_VCA_HUMAN_ATTRIBUTE
from .net_vca_register_pic import NET_VCA_REGISTER_PIC


class struct_tagNET_VCA_DATARECORD_INFO(Structure):
    pass

_S(struct_tagNET_VCA_DATARECORD_INFO, [
    ('dwSize', DWORD),
    ('dwRecordID', DWORD),
    ('struAttribute', NET_VCA_HUMAN_ATTRIBUTE),
    ('struRegisterPic', NET_VCA_REGISTER_PIC),
    ('byRemark1', BYTE * 32),
    ('byRemark2', BYTE * 64),
    ('byRes', BYTE * 32),
])

NET_VCA_DATARECORD_INFO = struct_tagNET_VCA_DATARECORD_INFO
LPNET_VCA_DATARECORD_INFO = POINTER(struct_tagNET_VCA_DATARECORD_INFO)
tagNET_VCA_DATARECORD_INFO = struct_tagNET_VCA_DATARECORD_INFO
