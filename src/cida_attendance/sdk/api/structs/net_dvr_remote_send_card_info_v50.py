from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_dvr_card_port_info import NET_DVR_CARD_PORT_INFO


class struct_tagNET_DVR_REMOTE_SEND_CARD_INFO_V50(Structure):
    pass

_S(struct_tagNET_DVR_REMOTE_SEND_CARD_INFO_V50, [
    ('byCardNo', BYTE),
    ('byMainSlotNo', BYTE),
    ('byRes1', BYTE * 2),
    ('byTypeName', BYTE * 32),
    ('bySoftwareVersion', BYTE * 32),
    ('byIsVerMismatch', BYTE),
    ('byRes2', BYTE * 3),
    ('byNewestSoftwareVersion', BYTE * 32),
    ('byHardwareVersion', BYTE * 32),
    ('struPortInfo', NET_DVR_CARD_PORT_INFO * 4),
    ('byRes3', BYTE * 64),
])

NET_DVR_REMOTE_SEND_CARD_INFO_V50 = struct_tagNET_DVR_REMOTE_SEND_CARD_INFO_V50
LPNET_DVR_REMOTE_SEND_CARD_INFO_V50 = POINTER(struct_tagNET_DVR_REMOTE_SEND_CARD_INFO_V50)
tagNET_DVR_REMOTE_SEND_CARD_INFO_V50 = struct_tagNET_DVR_REMOTE_SEND_CARD_INFO_V50
