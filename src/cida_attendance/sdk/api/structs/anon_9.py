from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_anon_9(Structure):
    pass

_S(struct_anon_9, [
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
])

NET_DVR_DEVICECFG = struct_anon_9
LPNET_DVR_DEVICECFG = POINTER(struct_anon_9)
