from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_anon_301(Structure):
    pass

_S(struct_anon_301, [
    ('dwSize', DWORD),
    ('sDVRName', BYTE * 32),
    ('dwDVRID', DWORD),
    ('dwRecycleRecord', DWORD),
    ('sSerialNumber', BYTE * 48),
    ('dwSoftwareVersion', DWORD),
    ('dwSoftwareBuildDate', DWORD),
    ('dwDSPSoftwareVersion', DWORD),
    ('dwDSPSoftwareBuildDate', DWORD),
    ('dwPanelVersion', DWORD),
    ('dwHardwareVersion', DWORD),
    ('byAlarmInPortNum', BYTE),
    ('byAlarmOutPortNum', BYTE),
    ('byRS232Num', BYTE),
    ('byRS485Num', BYTE),
    ('byNetworkPortNum', BYTE),
    ('byDiskCtrlNum', BYTE),
    ('byDiskNum', BYTE),
    ('byDVRType', BYTE),
    ('byChanNum', BYTE),
    ('byStartChan', BYTE),
    ('byDecordChans', BYTE),
    ('byVGANum', BYTE),
    ('byUSBNum', BYTE),
    ('byAuxoutNum', BYTE),
    ('byAudioNum', BYTE),
    ('byIPChanNum', BYTE),
    ('byZeroChanNum', BYTE),
    ('bySupport', BYTE),
    ('byEsataUseage', BYTE),
    ('byIPCPlug', BYTE),
    ('byStorageMode', BYTE),
    ('bySupport1', BYTE),
    ('wDevType', WORD),
    ('byDevTypeName', BYTE * 24),
    ('bySupport2', BYTE),
    ('byAnalogAlarmInPortNum', BYTE),
    ('byStartAlarmInNo', BYTE),
    ('byStartAlarmOutNo', BYTE),
    ('byStartIPAlarmInNo', BYTE),
    ('byStartIPAlarmOutNo', BYTE),
    ('byHighIPChanNum', BYTE),
    ('byEnableRemotePowerOn', BYTE),
    ('wDevClass', WORD),
    ('byRes2', BYTE * 6),
])

NET_DVR_DEVICECFG_V40 = struct_anon_301
LPNET_DVR_DEVICECFG_V40 = POINTER(struct_anon_301)
