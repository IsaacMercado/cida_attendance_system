from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .net_dvr_snmpv3_user import NET_DVR_SNMPv3_USER


class struct_tagNET_DVR_SNMPCFG_V30(Structure):
    pass

_S(struct_tagNET_DVR_SNMPCFG_V30, [
    ('dwSize', DWORD),
    ('byEnableV1', BYTE),
    ('byEnableV2', BYTE),
    ('byEnableV3', BYTE),
    ('byRes1', BYTE * 3),
    ('wServerPort', WORD),
    ('byReadCommunity', BYTE * 32),
    ('byWriteCommunity', BYTE * 32),
    ('byTrapHostIP', BYTE * 64),
    ('wTrapHostPort', WORD),
    ('byRes2', BYTE * 2),
    ('struRWUser', NET_DVR_SNMPv3_USER),
    ('struROUser', NET_DVR_SNMPv3_USER),
    ('byTrapName', BYTE * 32),
])

NET_DVR_SNMPCFG_V30 = struct_tagNET_DVR_SNMPCFG_V30
LPNET_DVR_SNMPCFG_V30 = POINTER(struct_tagNET_DVR_SNMPCFG_V30)
tagNET_DVR_SNMPCFG_V30 = struct_tagNET_DVR_SNMPCFG_V30
