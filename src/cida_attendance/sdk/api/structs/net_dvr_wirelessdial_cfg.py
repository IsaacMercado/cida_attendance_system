from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_WIRELESSDIAL_CFG(Structure):
    pass

_S(struct_tagNET_DVR_WIRELESSDIAL_CFG, [
    ('dwSize', DWORD),
    ('byEnabled', BYTE),
    ('byDialMode', BYTE),
    ('byNetworkMode', BYTE),
    ('byRes1', BYTE),
    ('byDialNum', BYTE * 32),
    ('byUserName', BYTE * 32),
    ('byPassword', BYTE * 32),
    ('byAPNName', BYTE * 32),
    ('byUIMCardNum', BYTE * 32),
    ('byVerifProtocol', BYTE),
    ('byRes2', BYTE),
    ('wMTU', WORD),
    ('dwOffineTime', DWORD),
    ('byNetAPN', BYTE * 32),
    ('byEnabled4G', BYTE),
    ('byEnabledDNS', BYTE),
    ('byRes3', BYTE * 30),
])

NET_DVR_WIRELESSDIAL_CFG = struct_tagNET_DVR_WIRELESSDIAL_CFG
LPNET_DVR_WIRELESSDIAL_CFG = POINTER(struct_tagNET_DVR_WIRELESSDIAL_CFG)
tagNET_DVR_WIRELESSDIAL_CFG = struct_tagNET_DVR_WIRELESSDIAL_CFG
