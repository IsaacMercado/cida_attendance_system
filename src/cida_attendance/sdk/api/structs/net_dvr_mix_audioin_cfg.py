from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_auto_limit_wave_cfg import NET_DVR_AUTO_LIMIT_WAVE_CFG
from .net_dvr_dsp_parameter_cfg import NET_DVR_DSP_PARAMETER_CFG


class struct_tagNET_DVR_MIX_AUDIOIN_CFG(Structure):
    pass

_S(struct_tagNET_DVR_MIX_AUDIOIN_CFG, [
    ('dwSize', DWORD),
    ('dwHighPassFilter', DWORD),
    ('dwNoiseMargin', DWORD),
    ('struLimitWave', NET_DVR_AUTO_LIMIT_WAVE_CFG),
    ('struDSPParameter', NET_DVR_DSP_PARAMETER_CFG),
    ('byRes', BYTE * 40),
])

NET_DVR_MIX_AUDIOIN_CFG = struct_tagNET_DVR_MIX_AUDIOIN_CFG
LPNET_DVR_MIX_AUDIOIN_CFG = POINTER(struct_tagNET_DVR_MIX_AUDIOIN_CFG)
tagNET_DVR_MIX_AUDIOIN_CFG = struct_tagNET_DVR_MIX_AUDIOIN_CFG
