from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_SIGNAL_JOINT_CFG(Structure):
    pass

_S(struct_tagNET_DVR_SIGNAL_JOINT_CFG, [
    ('dwSize', DWORD),
    ('sCamName', BYTE * 32),
    ('byEnable', BYTE),
    ('byCamMode', BYTE),
    ('byRows', BYTE),
    ('byColumns', BYTE),
    ('dwSignalNo', DWORD * 64),
    ('dwJointNo', DWORD),
    ('dwSignalNoJoint', DWORD),
    ('byRes', BYTE * 64),
])

NET_DVR_SIGNAL_JOINT_CFG = struct_tagNET_DVR_SIGNAL_JOINT_CFG
LPNET_DVR_SIGNAL_JOINT_CFG = POINTER(struct_tagNET_DVR_SIGNAL_JOINT_CFG)
tagNET_DVR_SIGNAL_JOINT_CFG = struct_tagNET_DVR_SIGNAL_JOINT_CFG
