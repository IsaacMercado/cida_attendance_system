from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_led_port_backup import NET_DVR_LED_PORT_BACKUP
from .net_dvr_led_recv_card_info import NET_DVR_LED_RECV_CARD_INFO


class struct_tagNET_DVR_LED_PORT_CFG(Structure):
    pass

_S(struct_tagNET_DVR_LED_PORT_CFG, [
    ('dwSize', DWORD),
    ('byEnabled', BYTE),
    ('byRes1', BYTE * 3),
    ('struLedPortBackup', NET_DVR_LED_PORT_BACKUP),
    ('dwRecvCardNum', DWORD),
    ('struRecvCard', NET_DVR_LED_RECV_CARD_INFO * 64),
    ('dwPortNo', DWORD),
    ('byRes2', BYTE * 64),
])

NET_DVR_LED_PORT_CFG = struct_tagNET_DVR_LED_PORT_CFG
LPNET_DVR_LED_PORT_CFG = POINTER(struct_tagNET_DVR_LED_PORT_CFG)
tagNET_DVR_LED_PORT_CFG = struct_tagNET_DVR_LED_PORT_CFG
