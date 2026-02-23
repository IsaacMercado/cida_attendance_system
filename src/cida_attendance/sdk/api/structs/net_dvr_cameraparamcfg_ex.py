from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_agc_param import NET_DVR_AGC_PARAM
from .net_dvr_backlight import NET_DVR_BACKLIGHT
from .net_dvr_cmosmodcfg import NET_DVR_CMOSMODECFG
from .net_dvr_corridor_mode_ccd import NET_DVR_CORRIDOR_MODE_CCD
from .net_dvr_daynight import NET_DVR_DAYNIGHT
from .net_dvr_dde_param import NET_DVR_DDE_PARAM
from .net_dvr_defogcfg import NET_DVR_DEFOGCFG
from .net_dvr_electronicstabilization import NET_DVR_ELECTRONICSTABILIZATION
from .net_dvr_exposure import NET_DVR_EXPOSURE
from .net_dvr_ffc_param import NET_DVR_FFC_PARAM
from .net_dvr_gain import NET_DVR_GAIN
from .net_dvr_gammacorrect import NET_DVR_GAMMACORRECT
from .net_dvr_laser_param_cfg import NET_DVR_LASER_PARAM_CFG
from .net_dvr_noiseremove import NET_DVR_NOISEREMOVE
from .net_dvr_optical_dehaze import NET_DVR_OPTICAL_DEHAZE
from .net_dvr_piris_param import NET_DVR_PIRIS_PARAM
from .net_dvr_smartir_param import NET_DVR_SMARTIR_PARAM
from .net_dvr_snap_cameraparamcfg import NET_DVR_SNAP_CAMERAPARAMCFG
from .net_dvr_thermometry_agc import NET_DVR_THERMOMETRY_AGC
from .net_dvr_videoeffect import NET_DVR_VIDEOEFFECT
from .net_dvr_wdr import NET_DVR_WDR
from .net_dvr_whitebalance import NET_DVR_WHITEBALANCE


class struct_tagNET_DVR_CAMERAPARAMCFG_EX(Structure):
    pass

_S(struct_tagNET_DVR_CAMERAPARAMCFG_EX, [
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
    ('struDefogCfg', NET_DVR_DEFOGCFG),
    ('struElectronicStabilization', NET_DVR_ELECTRONICSTABILIZATION),
    ('struCorridorMode', NET_DVR_CORRIDOR_MODE_CCD),
    ('byExposureSegmentEnable', BYTE),
    ('byBrightCompensate', BYTE),
    ('byCaptureModeN', BYTE),
    ('byCaptureModeP', BYTE),
    ('struSmartIRParam', NET_DVR_SMARTIR_PARAM),
    ('struPIrisParam', NET_DVR_PIRIS_PARAM),
    ('struLaserParam', NET_DVR_LASER_PARAM_CFG),
    ('struFFCParam', NET_DVR_FFC_PARAM),
    ('struDDEParam', NET_DVR_DDE_PARAM),
    ('struAGCParam', NET_DVR_AGC_PARAM),
    ('byLensDistortionCorrection', BYTE),
    ('byDistortionCorrectionLevel', BYTE),
    ('byCalibrationAccurateLevel', BYTE),
    ('byZoomedInDistantViewLevel', BYTE),
    ('struSnapCCD', NET_DVR_SNAP_CAMERAPARAMCFG),
    ('struOpticalDehaze', NET_DVR_OPTICAL_DEHAZE),
    ('struThermAGC', NET_DVR_THERMOMETRY_AGC),
    ('byFusionMode', BYTE),
    ('byHorizontalFOV', BYTE),
    ('byVerticalFOV', BYTE),
    ('byBrightnessSuddenChangeSuppression', BYTE),
    ('byGPSEnabled', BYTE),
    ('byRes2', BYTE * 155),
])

NET_DVR_CAMERAPARAMCFG_EX = struct_tagNET_DVR_CAMERAPARAMCFG_EX
LPNET_DVR_CAMERAPARAMCFG_EX = POINTER(struct_tagNET_DVR_CAMERAPARAMCFG_EX)
tagNET_DVR_CAMERAPARAMCFG_EX = struct_tagNET_DVR_CAMERAPARAMCFG_EX
