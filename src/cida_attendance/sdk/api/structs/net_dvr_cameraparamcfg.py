from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_backlight import NET_DVR_BACKLIGHT
from .net_dvr_cmosmodcfg import NET_DVR_CMOSMODECFG
from .net_dvr_daynight import NET_DVR_DAYNIGHT
from .net_dvr_exposure import NET_DVR_EXPOSURE
from .net_dvr_gain import NET_DVR_GAIN
from .net_dvr_gammacorrect import NET_DVR_GAMMACORRECT
from .net_dvr_noiseremove import NET_DVR_NOISEREMOVE
from .net_dvr_videoeffect import NET_DVR_VIDEOEFFECT
from .net_dvr_wdr import NET_DVR_WDR
from .net_dvr_whitebalance import NET_DVR_WHITEBALANCE


class struct_tagNET_DVR_CAMERAPARAMCFG(Structure):
    pass

_S(struct_tagNET_DVR_CAMERAPARAMCFG, [
    ('dwSize', DWORD),
    ('struVideoEffect', NET_DVR_VIDEOEFFECT),
    ('struGain', NET_DVR_GAIN),
    ('struWhiteBalance', NET_DVR_WHITEBALANCE),
    ('struExposure', NET_DVR_EXPOSURE),
    ('struGammaCorrect', NET_DVR_GAMMACORRECT),
    ('struWdr', NET_DVR_WDR),
    ('struDayNight', NET_DVR_DAYNIGHT),
    ('struBackLight', NET_DVR_BACKLIGHT),
    ('struNoiseRemove', NET_DVR_NOISEREMOVE),
    ('byPowerLineFrequencyMode', BYTE),
    ('byIrisMode', BYTE),
    ('byMirror', BYTE),
    ('byDigitalZoom', BYTE),
    ('byDeadPixelDetect', BYTE),
    ('byBlackPwl', BYTE),
    ('byEptzGate', BYTE),
    ('byLocalOutputGate', BYTE),
    ('byCoderOutputMode', BYTE),
    ('byLineCoding', BYTE),
    ('byDimmerMode', BYTE),
    ('byPaletteMode', BYTE),
    ('byEnhancedMode', BYTE),
    ('byDynamicContrastEN', BYTE),
    ('byDynamicContrast', BYTE),
    ('byJPEGQuality', BYTE),
    ('struCmosModeCfg', NET_DVR_CMOSMODECFG),
    ('byFilterSwitch', BYTE),
    ('byFocusSpeed', BYTE),
    ('byAutoCompensationInterval', BYTE),
    ('bySceneMode', BYTE),
])

NET_DVR_CAMERAPARAMCFG = struct_tagNET_DVR_CAMERAPARAMCFG
LPNET_DVR_CAMERAPARAMCFG = POINTER(struct_tagNET_DVR_CAMERAPARAMCFG)
tagNET_DVR_CAMERAPARAMCFG = struct_tagNET_DVR_CAMERAPARAMCFG
