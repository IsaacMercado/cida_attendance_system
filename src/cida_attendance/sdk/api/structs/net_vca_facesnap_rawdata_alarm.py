from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_vca_dev_info import NET_VCA_DEV_INFO


class struct_tagNET_VCA_FACESNAP_RAWDATA_ALARM_(Structure):
    pass

_S(struct_tagNET_VCA_FACESNAP_RAWDATA_ALARM_, [
    ('dwSize', DWORD),
    ('dwRelativeTime', DWORD),
    ('dwAbsTime', DWORD),
    ('struDevInfo', NET_VCA_DEV_INFO),
    ('dwJsonDataLen', DWORD),
    ('pJsonBuff', POINTER(BYTE)),
    ('byRes', BYTE * 256),
])

NET_VCA_FACESNAP_RAWDATA_ALARM = struct_tagNET_VCA_FACESNAP_RAWDATA_ALARM_
LPNET_VCA_FACESNAP_RAWDATA_ALARM = POINTER(struct_tagNET_VCA_FACESNAP_RAWDATA_ALARM_)
tagNET_VCA_FACESNAP_RAWDATA_ALARM_ = struct_tagNET_VCA_FACESNAP_RAWDATA_ALARM_
