from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_UPGRADE_FIRMWARE_INFO(Structure):
    pass

_S(struct_tagNET_DVR_UPGRADE_FIRMWARE_INFO, [
    ('dwMagicNumber', DWORD),
    ('dwCheckSum', DWORD),
    ('dwHeadLen', DWORD),
    ('dwFileNums', DWORD),
    ('dwLanguage', DWORD),
    ('dwDeviceClassID', DWORD),
    ('dwOemCode', DWORD),
    ('byUpgradeVersion', BYTE),
    ('byResFeature', BYTE * 15),
    ('byFlashSize', BYTE),
    ('byRamSize', BYTE),
    ('byDspRamSize', BYTE),
    ('byRes', BYTE * 17),
])

NET_DVR_UPGRADE_FIRMWARE_INFO = struct_tagNET_DVR_UPGRADE_FIRMWARE_INFO
LPNET_DVR_UPGRADE_FIRMWARE_INFO = POINTER(struct_tagNET_DVR_UPGRADE_FIRMWARE_INFO)
tagNET_DVR_UPGRADE_FIRMWARE_INFO = struct_tagNET_DVR_UPGRADE_FIRMWARE_INFO
