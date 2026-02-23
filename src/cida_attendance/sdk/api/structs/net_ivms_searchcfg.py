from ctypes import Structure

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER
from .anon_169 import NET_DVR_MATRIX_DEC_REMOTE_PLAY
from .net_ivms_alarm_jpeg import NET_IVMS_ALARM_JPEG
from .net_ivms_rulecfg import NET_IVMS_RULECFG


class struct_tagNET_IVMS_SEARCHCFG(Structure):
    pass

_S(struct_tagNET_IVMS_SEARCHCFG, [
    ('dwSize', DWORD),
    ('struRemotePlay', NET_DVR_MATRIX_DEC_REMOTE_PLAY),
    ('struAlarmJpeg', NET_IVMS_ALARM_JPEG),
    ('struRuleCfg', NET_IVMS_RULECFG),
])

NET_IVMS_SEARCHCFG = struct_tagNET_IVMS_SEARCHCFG
LPNET_IVMS_SEARCHCFG = POINTER(struct_tagNET_IVMS_SEARCHCFG)
tagNET_IVMS_SEARCHCFG = struct_tagNET_IVMS_SEARCHCFG
