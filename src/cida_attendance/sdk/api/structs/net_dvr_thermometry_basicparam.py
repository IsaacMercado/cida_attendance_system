from ctypes import Structure, c_float, c_int

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .net_dvr_temperature_color import NET_DVR_TEMPERATURE_COLOR


class struct_tagNET_DVR_THERMOMETRY_BASICPARAM(Structure):
    pass

_S(struct_tagNET_DVR_THERMOMETRY_BASICPARAM, [
    ('dwSize', DWORD),
    ('byEnabled', BYTE),
    ('byStreamOverlay', BYTE),
    ('byPictureOverlay', BYTE),
    ('byThermometryRange', BYTE),
    ('byThermometryUnit', BYTE),
    ('byThermometryCurve', BYTE),
    ('byFireImageModea', BYTE),
    ('byShowTempStripEnable', BYTE),
    ('fEmissivity', c_float),
    ('byDistanceUnit', BYTE),
    ('byEnviroHumidity', BYTE),
    ('byRes2', BYTE * 2),
    ('struTempColor', NET_DVR_TEMPERATURE_COLOR),
    ('iEnviroTemperature', c_int),
    ('iCorrectionVolume', c_int),
    ('bySpecialPointThermType', BYTE),
    ('byReflectiveEnabled', BYTE),
    ('wDistance', WORD),
    ('fReflectiveTemperature', c_float),
    ('fAlert', c_float),
    ('fAlarm', c_float),
    ('fThermalOpticalTransmittance', c_float),
    ('fExternalOpticsWindowCorrection', c_float),
    ('byDisplayMaxTemperatureEnabled', BYTE),
    ('byDisplayMinTemperatureEnabled', BYTE),
    ('byDisplayAverageTemperatureEnabled', BYTE),
    ('byThermometryInfoDisplayposition', BYTE),
    ('dwAlertFilteringTime', DWORD),
    ('dwAlarmFilteringTime', DWORD),
    ('byemissivityMode', BYTE),
    ('bydisplayTemperatureInOpticalChannelEnabled', BYTE),
    ('byDisplayCentreTemperatureEnabled', BYTE),
    ('byRes', BYTE * 49),
])

NET_DVR_THERMOMETRY_BASICPARAM = struct_tagNET_DVR_THERMOMETRY_BASICPARAM
LPNET_DVR_THERMOMETRY_BASICPARAM = POINTER(struct_tagNET_DVR_THERMOMETRY_BASICPARAM)
tagNET_DVR_THERMOMETRY_BASICPARAM = struct_tagNET_DVR_THERMOMETRY_BASICPARAM
