from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_DEC_VCA_ALARM_LOGO(Structure):
    pass

_S(struct_tagNET_DVR_DEC_VCA_ALARM_LOGO, [
    ('byEnableLogo', BYTE),
    ('byFlash', BYTE),
    ('wFlashTime', WORD),
    ('dwLogoX', DWORD),
    ('dwLogoY', DWORD),
    ('byRes', BYTE * 32),
])

NET_DVR_DEC_VCA_ALARM_LOGO = struct_tagNET_DVR_DEC_VCA_ALARM_LOGO
LPNET_DVR_DEC_VCA_ALARM_LOGO = POINTER(struct_tagNET_DVR_DEC_VCA_ALARM_LOGO)
tagNET_DVR_DEC_VCA_ALARM_LOGO = struct_tagNET_DVR_DEC_VCA_ALARM_LOGO
