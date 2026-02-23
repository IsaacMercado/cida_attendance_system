from ctypes import Union

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .anon_51 import NET_DVR_SINGLE_RS232
from .anon_420 import NET_DVR_NET_RECEIVE
from .net_dvr_address import NET_DVR_ADDRESS
from .net_dvr_monitor_info import NET_DVR_MONITOR_INFO
from .net_dvr_net_sniff import NET_DVR_NET_SNIFF
from .net_dvr_usb_rs232 import NET_DVR_USB_RS232


class union_tagNET_DVR_POS_CONNECTMODE_UNION(Union):
    pass

_S(union_tagNET_DVR_POS_CONNECTMODE_UNION, [
    ('byLen', BYTE * 312),
    ('struNetRecv', NET_DVR_NET_RECEIVE),
    ('struTcpMonitor', NET_DVR_MONITOR_INFO),
    ('struRS232', NET_DVR_SINGLE_RS232),
    ('struUdpMonitor', NET_DVR_MONITOR_INFO),
    ('struSniff', NET_DVR_NET_SNIFF),
    ('struMcast', NET_DVR_ADDRESS),
    ('struUSBRS232', NET_DVR_USB_RS232),
])

NET_DVR_POS_CONNECTMODE_UNION = union_tagNET_DVR_POS_CONNECTMODE_UNION
LPNET_DVR_POS_CONNECTMODE_UNION = POINTER(union_tagNET_DVR_POS_CONNECTMODE_UNION)
tagNET_DVR_POS_CONNECTMODE_UNION = union_tagNET_DVR_POS_CONNECTMODE_UNION
