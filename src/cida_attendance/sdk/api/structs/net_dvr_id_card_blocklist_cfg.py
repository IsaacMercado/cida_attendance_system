from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER, String
from .net_dvr_id_card_info import NET_DVR_ID_CARD_INFO


class struct_tagNET_DVR_ID_CARD_BLOCKLIST_CFG(Structure):
    pass

_S(struct_tagNET_DVR_ID_CARD_BLOCKLIST_CFG, [
    ('dwSize', DWORD),
    ('struIDCardCfg', NET_DVR_ID_CARD_INFO),
    ('dwFingerPrintDataLen', DWORD),
    ('pFingerPrintData', String),
    ('dwPicDataLen', DWORD),
    ('pPicData', String),
    ('byRes', BYTE * 128),
])

NET_DVR_ID_CARD_BLOCKLIST_CFG = struct_tagNET_DVR_ID_CARD_BLOCKLIST_CFG
LPNET_DVR_ID_CARD_BLOCKLIST_CFG = POINTER(struct_tagNET_DVR_ID_CARD_BLOCKLIST_CFG)
tagNET_DVR_ID_CARD_BLOCKLIST_CFG = struct_tagNET_DVR_ID_CARD_BLOCKLIST_CFG
