from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_GB28181_SERVICE_CFG(Structure):
    pass

_S(struct_tagNET_DVR_GB28181_SERVICE_CFG, [
    ('dwSize', DWORD),
    ('byServerID', BYTE * 32),
    ('wPort', WORD),
    ('byRes1', BYTE * 2),
    ('byAuthPasswd', BYTE * 16),
    ('dwRegisterValid', DWORD),
    ('byMaxHeartbeatTimeOut', BYTE),
    ('byAutoAddIpc', BYTE),
    ('byAuthPasswdEx', BYTE * 64),
    ('byRes', BYTE * 190),
])

NET_DVR_GB28181_SERVICE_CFG = struct_tagNET_DVR_GB28181_SERVICE_CFG
LPNET_DVR_GB28181_SERVICE_CFG = POINTER(struct_tagNET_DVR_GB28181_SERVICE_CFG)
tagNET_DVR_GB28181_SERVICE_CFG = struct_tagNET_DVR_GB28181_SERVICE_CFG
