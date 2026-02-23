from ctypes import Union

from ..base_classes import _S
from .net_dvr_mb_gps_status import NET_DVR_MB_GPS_STATUS
from .net_dvr_mb_gsensor_status import NET_DVR_MB_GSENSOR_STATUS
from .net_dvr_mb_platform_status import NET_DVR_MB_PLATFORM_STATUS
from .net_dvr_mb_wifi_status import NET_DVR_MB_WIFI_STATUS


class union_anon_351(Union):
    pass

_S(union_anon_351, [
    ('struGPSStatus', NET_DVR_MB_GPS_STATUS),
    ('struGSensorStatus', NET_DVR_MB_GSENSOR_STATUS),
    ('struWiFiStatus', NET_DVR_MB_WIFI_STATUS),
    ('struPlatformStatus', NET_DVR_MB_PLATFORM_STATUS),
])

