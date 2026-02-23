from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_evetn_card_linkage_union import NET_DVR_EVETN_CARD_LINKAGE_UNION


class struct_tagNET_DVR_EVENT_CARD_LINKAGE_CFG(Structure):
    pass

_S(struct_tagNET_DVR_EVENT_CARD_LINKAGE_CFG, [
    ('dwSize', DWORD),
    ('byProMode', BYTE),
    ('byRes1', BYTE * 3),
    ('dwEventSourceID', DWORD),
    ('uLinkageInfo', NET_DVR_EVETN_CARD_LINKAGE_UNION),
    ('byAlarmout', BYTE * 512),
    ('byRes2', BYTE * 32),
    ('byOpenDoor', BYTE * 256),
    ('byCloseDoor', BYTE * 256),
    ('byNormalOpen', BYTE * 256),
    ('byNormalClose', BYTE * 256),
    ('byMainDevBuzzer', BYTE),
    ('byCapturePic', BYTE),
    ('byRecordVideo', BYTE),
    ('byRes3', BYTE * 29),
    ('byReaderBuzzer', BYTE * 512),
    ('byRes', BYTE * 128),
])

NET_DVR_EVENT_CARD_LINKAGE_CFG = struct_tagNET_DVR_EVENT_CARD_LINKAGE_CFG
LPNET_DVR_EVENT_CARD_LINKAGE_CFG = POINTER(struct_tagNET_DVR_EVENT_CARD_LINKAGE_CFG)
tagNET_DVR_EVENT_CARD_LINKAGE_CFG = struct_tagNET_DVR_EVENT_CARD_LINKAGE_CFG
