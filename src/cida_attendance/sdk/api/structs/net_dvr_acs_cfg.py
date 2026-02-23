from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_ACS_CFG(Structure):
    pass

_S(struct_tagNET_DVR_ACS_CFG, [
    ('dwSize', DWORD),
    ('byRS485Backup', BYTE),
    ('byShowCapPic', BYTE),
    ('byShowCardNo', BYTE),
    ('byShowUserInfo', BYTE),
    ('byOverlayUserInfo', BYTE),
    ('byVoicePrompt', BYTE),
    ('byUploadCapPic', BYTE),
    ('bySaveCapPic', BYTE),
    ('byInputCardNo', BYTE),
    ('byEnableWifiDetect', BYTE),
    ('byEnable3G4G', BYTE),
    ('byProtocol', BYTE),
    ('byRes', BYTE * 500),
])

NET_DVR_ACS_CFG = struct_tagNET_DVR_ACS_CFG
LPNET_DVR_ACS_CFG = POINTER(struct_tagNET_DVR_ACS_CFG)
tagNET_DVR_ACS_CFG = struct_tagNET_DVR_ACS_CFG
