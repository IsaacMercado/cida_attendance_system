from ctypes import Structure

from ..base_classes import _S, BYTE, LONG
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_ALARMHOST_ENVIRONMENTAL_LOGGER(Structure):
    pass

_S(struct_tagNET_DVR_ALARMHOST_ENVIRONMENTAL_LOGGER, [
    ('iAmmoniaNitrogen', LONG),
    ('iCOD', LONG),
    ('iPH', LONG),
    ('iOxygen', LONG),
    ('iSulfurDioxide', LONG),
    ('iSoot', LONG),
    ('iFluoride', LONG),
    ('iPollutedWater', LONG),
    ('iTotalPhosphorus', LONG),
    ('iExhaust', LONG),
    ('iNitrogenOxides', LONG),
    ('iFlueGasTemperature', LONG),
    ('iFlueGasPressure', LONG),
    ('iDustThickness', LONG),
    ('iAirCleanLevel', LONG),
    ('iPm10Thickness', LONG),
    ('byRes', BYTE * 448),
])

NET_DVR_ALARMHOST_ENVIRONMENTAL_LOGGER = struct_tagNET_DVR_ALARMHOST_ENVIRONMENTAL_LOGGER
LPNET_DVR_ALARMHOST_ENVIRONMENTAL_LOGGER = POINTER(struct_tagNET_DVR_ALARMHOST_ENVIRONMENTAL_LOGGER)
tagNET_DVR_ALARMHOST_ENVIRONMENTAL_LOGGER = struct_tagNET_DVR_ALARMHOST_ENVIRONMENTAL_LOGGER
