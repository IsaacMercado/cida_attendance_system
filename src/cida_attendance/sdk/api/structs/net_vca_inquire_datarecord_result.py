from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_vca_human_attribute import NET_VCA_HUMAN_ATTRIBUTE


class struct_tagNET_VCA_INQUIRE_DATARECORD_RESULT(Structure):
    pass

_S(struct_tagNET_VCA_INQUIRE_DATARECORD_RESULT, [
    ('dwSize', DWORD),
    ('dwDataBaseID', DWORD),
    ('dwRecordID', DWORD),
    ('struAttribute', NET_VCA_HUMAN_ATTRIBUTE),
    ('byRemark1', BYTE * 32),
    ('byRemark2', BYTE * 64),
    ('dwFacePicID', DWORD),
    ('dwFacePicLen', DWORD),
    ('byRes', BYTE * 80),
    ('pFacePic', POINTER(BYTE)),
])

NET_VCA_INQUIRE_DATARECORD_RESULT = struct_tagNET_VCA_INQUIRE_DATARECORD_RESULT
LPNET_VCA_INQUIRE_DATARECORD_RESULT = POINTER(struct_tagNET_VCA_INQUIRE_DATARECORD_RESULT)
tagNET_VCA_INQUIRE_DATARECORD_RESULT = struct_tagNET_VCA_INQUIRE_DATARECORD_RESULT
