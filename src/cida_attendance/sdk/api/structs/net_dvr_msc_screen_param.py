from ctypes import Union

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_dvr_adc_cfg import NET_DVR_ADC_CFG
from .net_dvr_boot_logo_cfg import NET_DVR_BOOT_LOGO_CFG
from .net_dvr_color_temperature_cfg import NET_DVR_COLOR_TEMPERATURE_CFG
from .net_dvr_defog_lcd import NET_DVR_DEFOG_LCD
from .net_dvr_lcd_audio_cfg import NET_DVR_LCD_AUDIO_CFG
from .net_dvr_msc_screen_backlight_cfg import NET_DVR_MSC_SCREEN_BACKLIGHT_CFG
from .net_dvr_msc_screen_interface_cfg import NET_DVR_MSC_SCREEN_INTERFACE_CFG
from .net_dvr_msc_screen_pip_cfg import NET_DVR_MSC_SCREEN_PIP_CFG
from .net_dvr_screen_edge_cfg import NET_DVR_SCREEN_EDGE_CFG
from .net_dvr_screen_fan_work_mode_cfg import NET_DVR_SCREEN_FAN_WORK_MODE_CFG
from .net_dvr_screen_menu_cfg import NET_DVR_SCREEN_MENU_CFG
from .net_dvr_screen_vga_cfg import NET_DVR_SCREEN_VGA_CFG
from .net_dvr_screen_work_state import NET_DVR_SCREEN_WORK_STATE
from .net_dvr_video_out_cfg import NET_DVR_VIDEO_OUT_CFG


class union_tagNET_DVR_MSC_SCREEN_PARAM(Union):
    pass

_S(union_tagNET_DVR_MSC_SCREEN_PARAM, [
    ('struInterfaceCfg', NET_DVR_MSC_SCREEN_INTERFACE_CFG),
    ('struFanWorkMode', NET_DVR_SCREEN_FAN_WORK_MODE_CFG),
    ('struVgaCfg', NET_DVR_SCREEN_VGA_CFG),
    ('struMenuCfg', NET_DVR_SCREEN_MENU_CFG),
    ('struOutEffectCfg', NET_DVR_VIDEO_OUT_CFG),
    ('struColorTemperatureCfg', NET_DVR_COLOR_TEMPERATURE_CFG),
    ('struAdcCfg', NET_DVR_ADC_CFG),
    ('struScreenEdgeCfg', NET_DVR_SCREEN_EDGE_CFG),
    ('struBacklight', NET_DVR_MSC_SCREEN_BACKLIGHT_CFG),
    ('struPicInPicCfg', NET_DVR_MSC_SCREEN_PIP_CFG),
    ('struDefog', NET_DVR_DEFOG_LCD),
    ('struWorkState', NET_DVR_SCREEN_WORK_STATE),
    ('struBootLogoCfg', NET_DVR_BOOT_LOGO_CFG),
    ('struAudioCfg', NET_DVR_LCD_AUDIO_CFG),
    ('byRes', BYTE * 256),
])

NET_DVR_MSC_SCREEN_PARAM = union_tagNET_DVR_MSC_SCREEN_PARAM
LPNET_DVR_MSC_SCREEN_PARAM = POINTER(union_tagNET_DVR_MSC_SCREEN_PARAM)
tagNET_DVR_MSC_SCREEN_PARAM = union_tagNET_DVR_MSC_SCREEN_PARAM
