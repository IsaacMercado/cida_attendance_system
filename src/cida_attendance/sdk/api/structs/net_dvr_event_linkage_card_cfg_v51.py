from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .net_dvr_evetn_card_linkage_union import NET_DVR_EVETN_CARD_LINKAGE_UNION


class struct_tagNET_DVR_EVENT_LINKAGE_CARD_CFG_V51(Structure):
    pass

_S(struct_tagNET_DVR_EVENT_LINKAGE_CARD_CFG_V51, [
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
    ('byMainDevStopBuzzer', BYTE),
    ('wAudioDisplayID', WORD),
    ('byAudioDisplayMode', BYTE),
    ('byRes3', BYTE * 25),
    ('byReaderBuzzer', BYTE * 512),
    ('byAlarmOutClose', BYTE * 512),
    ('byAlarmInSetup', BYTE * 512),
    ('byAlarmInClose', BYTE * 512),
    ('byReaderStopBuzzer', BYTE * 512),
    ('byRes', BYTE * 512),
])

NET_DVR_EVENT_CARD_LINKAGE_CFG_V51 = struct_tagNET_DVR_EVENT_LINKAGE_CARD_CFG_V51
LPNET_DVR_EVENT_CARD_LINKAGE_CFG_V51 = POINTER(struct_tagNET_DVR_EVENT_LINKAGE_CARD_CFG_V51)
tagNET_DVR_EVENT_LINKAGE_CARD_CFG_V51 = struct_tagNET_DVR_EVENT_LINKAGE_CARD_CFG_V51
