from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_GBT28181_ACCESS_CFG(Structure):
    pass

_S(struct_tagNET_DVR_GBT28181_ACCESS_CFG, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byTransProtocol', BYTE),
    ('wLocalSipPort', WORD),
    ('szServerID', c_char * 64),
    ('szServerDomain', c_char * 128),
    ('szSipServerAddress', c_char * 128),
    ('wServerSipPort', WORD),
    ('byProtocolVersion', BYTE),
    ('byTCPConnectMod', BYTE),
    ('szSipUserName', c_char * 64),
    ('szSipAuthenticateID', c_char * 64),
    ('szSipAuthenticatePasswd', c_char * 32),
    ('dwRegisterValid', DWORD),
    ('byHeartbeatInterval', BYTE),
    ('byMaxHeartbeatTimeOut', BYTE),
    ('byStreamType', BYTE),
    ('byDeviceStatus', BYTE),
    ('dwRegisterInterval', DWORD),
    ('dwAutoAllocChannelID', DWORD),
    ('szDeviceDomain', c_char * 128),
    ('byRes4', BYTE * 116),
])

NET_DVR_GBT28181_ACCESS_CFG = struct_tagNET_DVR_GBT28181_ACCESS_CFG
LPNET_DVR_GBT28181_ACCESS_CFG = POINTER(struct_tagNET_DVR_GBT28181_ACCESS_CFG)
tagNET_DVR_GBT28181_ACCESS_CFG = struct_tagNET_DVR_GBT28181_ACCESS_CFG
