from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_dec_vca_alarm_logo import NET_DVR_DEC_VCA_ALARM_LOGO
from .net_dvr_dec_vca_alarm_pic import NET_DVR_DEC_VCA_ALARM_PIC


class struct_tagNET_DVR_DEC_VCA_ALARM_CFG(Structure):
    pass

_S(struct_tagNET_DVR_DEC_VCA_ALARM_CFG, [
    ('dwSize', DWORD),
    ('struAlarmLogo', NET_DVR_DEC_VCA_ALARM_LOGO),
    ('struAlarmPic', NET_DVR_DEC_VCA_ALARM_PIC),
    ('byRes', BYTE * 64),
])

NET_DVR_VCA_ALARM_CFG = struct_tagNET_DVR_DEC_VCA_ALARM_CFG
LPNET_DVR_DEC_VCA_ALARM_CFG = POINTER(struct_tagNET_DVR_DEC_VCA_ALARM_CFG)
tagNET_DVR_DEC_VCA_ALARM_CFG = struct_tagNET_DVR_DEC_VCA_ALARM_CFG
