from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .net_vca_dev_info import NET_VCA_DEV_INFO
from .net_vca_rule_info import NET_VCA_RULE_INFO
from .net_vca_target_info import NET_VCA_TARGET_INFO


class struct_tagNET_VCA_RULE_ALARM(Structure):
    pass

_S(struct_tagNET_VCA_RULE_ALARM, [
    ('dwSize', DWORD),
    ('dwRelativeTime', DWORD),
    ('dwAbsTime', DWORD),
    ('struRuleInfo', NET_VCA_RULE_INFO),
    ('struTargetInfo', NET_VCA_TARGET_INFO),
    ('struDevInfo', NET_VCA_DEV_INFO),
    ('dwPicDataLen', DWORD),
    ('byPicType', BYTE),
    ('byRelAlarmPicNum', BYTE),
    ('bySmart', BYTE),
    ('byPicTransType', BYTE),
    ('dwAlarmID', DWORD),
    ('wDevInfoIvmsChannelEx', WORD),
    ('byRelativeTimeFlag', BYTE),
    ('byAppendInfoUploadEnabled', BYTE),
    ('pAppendInfo', POINTER(BYTE)),
    ('pImage', POINTER(BYTE)),
])

NET_VCA_RULE_ALARM = struct_tagNET_VCA_RULE_ALARM
LPNET_VCA_RULE_ALARM = POINTER(struct_tagNET_VCA_RULE_ALARM)
tagNET_VCA_RULE_ALARM = struct_tagNET_VCA_RULE_ALARM
