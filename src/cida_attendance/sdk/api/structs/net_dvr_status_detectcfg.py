from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_STATUS_DETECTCFG(Structure):
    pass

_S(struct_tagNET_DVR_STATUS_DETECTCFG, [
    ('dwSize', DWORD),
    ('byEnableTrigIODetect', BYTE),
    ('byEnableFlashOutDetect', BYTE),
    ('byEnableRS485Detect', BYTE),
    ('byEnableTrafficLightDetect', BYTE),
    ('byRes', BYTE * 28),
])

NET_DVR_STATUS_DETECTCFG = struct_tagNET_DVR_STATUS_DETECTCFG
LPNET_DVR_STATUS_DETECTCFG = POINTER(struct_tagNET_DVR_STATUS_DETECTCFG)
tagNET_DVR_STATUS_DETECTCFG = struct_tagNET_DVR_STATUS_DETECTCFG
