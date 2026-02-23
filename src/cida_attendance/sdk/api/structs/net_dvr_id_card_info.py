from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_date import NET_DVR_DATE


class struct_tagNET_DVR_ID_CARD_INFO(Structure):
    pass

_S(struct_tagNET_DVR_ID_CARD_INFO, [
    ('dwSize', DWORD),
    ('byName', BYTE * 128),
    ('struBirth', NET_DVR_DATE),
    ('byAddr', BYTE * 280),
    ('byIDNum', BYTE * 32),
    ('byIssuingAuthority', BYTE * 128),
    ('struStartDate', NET_DVR_DATE),
    ('struEndDate', NET_DVR_DATE),
    ('byTermOfValidity', BYTE),
    ('bySex', BYTE),
    ('byNation', BYTE),
    ('byRes', BYTE * 101),
])

NET_DVR_ID_CARD_INFO = struct_tagNET_DVR_ID_CARD_INFO
LPNET_DVR_ID_CARD_INFO = POINTER(struct_tagNET_DVR_ID_CARD_INFO)
tagNET_DVR_ID_CARD_INFO = struct_tagNET_DVR_ID_CARD_INFO
