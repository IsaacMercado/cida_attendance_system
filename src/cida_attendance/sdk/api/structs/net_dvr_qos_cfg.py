from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_QOS_CFG(Structure):
    pass

_S(struct_tagNET_DVR_QOS_CFG, [
    ('dwSize', DWORD),
    ('byManageDscp', BYTE),
    ('byAlarmDscp', BYTE),
    ('byVideoDscp', BYTE),
    ('byAudioDscp', BYTE),
    ('byFlag', BYTE),
    ('byEnable', BYTE),
    ('byRes', BYTE * 126),
])

NET_DVR_QOS_CFG = struct_tagNET_DVR_QOS_CFG
LPNET_DVR_QOS_CFG = POINTER(struct_tagNET_DVR_QOS_CFG)
tagNET_DVR_QOS_CFG = struct_tagNET_DVR_QOS_CFG
