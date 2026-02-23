from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_vca_dev_info import NET_VCA_DEV_INFO


class struct_tagNET_VCA_FACESNAP_INFO_ALARM_LOG(Structure):
    pass

_S(struct_tagNET_VCA_FACESNAP_INFO_ALARM_LOG, [
    ('dwRelativeTime', DWORD),
    ('dwAbsTime', DWORD),
    ('dwSnapFacePicID', DWORD),
    ('struDevInfo', NET_VCA_DEV_INFO),
    ('byRes', BYTE * 20),
])

NET_VCA_FACESNAP_INFO_ALARM_LOG = struct_tagNET_VCA_FACESNAP_INFO_ALARM_LOG
LPNET_VCA_FACESNAP_INFO_ALARM_LOG = POINTER(struct_tagNET_VCA_FACESNAP_INFO_ALARM_LOG)
tagNET_VCA_FACESNAP_INFO_ALARM_LOG = struct_tagNET_VCA_FACESNAP_INFO_ALARM_LOG
