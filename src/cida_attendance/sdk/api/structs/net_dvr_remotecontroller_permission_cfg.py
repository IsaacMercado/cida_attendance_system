from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_REMOTECONTROLLER_PERMISSION_CFG(Structure):
    pass

_S(struct_tagNET_DVR_REMOTECONTROLLER_PERMISSION_CFG, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byAssociateNetUser', BYTE),
    ('wRemoteCtrllerID', WORD),
    ('sDevSn', BYTE * 16),
    ('byArmRight', BYTE),
    ('byDisArmRight', BYTE),
    ('byArmReportRight', BYTE),
    ('byDisArmReportRight', BYTE),
    ('byClearAlarmRight', BYTE),
    ('bySubSystemID', BYTE),
    ('byKeyboardAddr', BYTE),
    ('byEnableDel', BYTE),
    ('byAlwaysOpenRight', BYTE),
    ('byOpeningDirection', BYTE),
    ('byRes3', BYTE * 2),
    ('byName', BYTE * 32),
    ('byRes2', BYTE * 28),
])

NET_DVR_REMOTECONTROLLER_PERMISSION_CFG = struct_tagNET_DVR_REMOTECONTROLLER_PERMISSION_CFG
LPNET_DVR_REMOTECONTROLLER_PERMISSION_CFG = POINTER(struct_tagNET_DVR_REMOTECONTROLLER_PERMISSION_CFG)
tagNET_DVR_REMOTECONTROLLER_PERMISSION_CFG = struct_tagNET_DVR_REMOTECONTROLLER_PERMISSION_CFG
