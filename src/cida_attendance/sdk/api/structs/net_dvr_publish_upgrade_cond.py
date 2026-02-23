from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_PUBLISH_UPGRADE_COND(Structure):
    pass

_S(struct_tagNET_DVR_PUBLISH_UPGRADE_COND, [
    ('dwSize', DWORD),
    ('dwUpgradeType', DWORD),
    ('dwTerminalNum', DWORD),
    ('pTerminalNo', POINTER(DWORD)),
    ('dwGroupNo', DWORD),
    ('byRes', BYTE * 32),
])

NET_DVR_PUBLISH_UPGRADE_COND = struct_tagNET_DVR_PUBLISH_UPGRADE_COND
LPNET_DVR_PUBLISH_UPGRADE_COND = POINTER(struct_tagNET_DVR_PUBLISH_UPGRADE_COND)
tagNET_DVR_PUBLISH_UPGRADE_COND = struct_tagNET_DVR_PUBLISH_UPGRADE_COND
