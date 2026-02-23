from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, UINT64
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_LOCAL_GENERAL_CFG(Structure):
    pass

_S(struct_tagNET_DVR_LOCAL_GENERAL_CFG, [
    ('byExceptionCbDirectly', BYTE),
    ('byNotSplitRecordFile', BYTE),
    ('byResumeUpgradeEnable', BYTE),
    ('byAlarmJsonPictureSeparate', BYTE),
    ('byRes', BYTE * 4),
    ('i64FileSize', UINT64),
    ('dwResumeUpgradeTimeout', DWORD),
    ('byAlarmReconnectMode', BYTE),
    ('byStdXmlBufferSize', BYTE),
    ('byMultiplexing', BYTE),
    ('byFastUpgrade', BYTE),
    ('byRes1', BYTE * 232),
])

NET_DVR_LOCAL_GENERAL_CFG = struct_tagNET_DVR_LOCAL_GENERAL_CFG
LPNET_DVR_LOCAL_GENERAL_CFG = POINTER(struct_tagNET_DVR_LOCAL_GENERAL_CFG)
tagNET_DVR_LOCAL_GENERAL_CFG = struct_tagNET_DVR_LOCAL_GENERAL_CFG
