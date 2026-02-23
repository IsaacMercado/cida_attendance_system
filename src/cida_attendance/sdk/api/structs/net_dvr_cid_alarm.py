from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .net_dvr_time_ex import NET_DVR_TIME_EX


class struct_tagNET_DVR_CID_ALARM(Structure):
    pass

_S(struct_tagNET_DVR_CID_ALARM, [
    ('dwSize', DWORD),
    ('sCIDCode', BYTE * 4),
    ('sCIDDescribe', BYTE * 32),
    ('struTriggerTime', NET_DVR_TIME_EX),
    ('struUploadTime', NET_DVR_TIME_EX),
    ('sCenterAccount', BYTE * 6),
    ('byReportType', BYTE),
    ('byUserType', BYTE),
    ('sUserName', BYTE * 32),
    ('wKeyUserNo', WORD),
    ('byKeypadNo', BYTE),
    ('bySubSysNo', BYTE),
    ('wDefenceNo', WORD),
    ('byVideoChanNo', BYTE),
    ('byDiskNo', BYTE),
    ('wModuleAddr', WORD),
    ('byCenterType', BYTE),
    ('byRelativeChannel', BYTE),
    ('sCenterAccountV40', BYTE * 32),
    ('byDevSerialNo', BYTE * 9),
    ('byRepeaterNo', BYTE),
    ('wRemoteCtrllerUserNo', WORD),
    ('dwIOTChannelNo', DWORD),
    ('standardCIDcode', BYTE),
    ('byRes2', BYTE * 11),
])

NET_DVR_CID_ALARM = struct_tagNET_DVR_CID_ALARM
LPNET_DVR_CID_ALARM = POINTER(struct_tagNET_DVR_CID_ALARM)
tagNET_DVR_CID_ALARM = struct_tagNET_DVR_CID_ALARM
