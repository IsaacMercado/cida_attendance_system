from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_dvr_led_registor_value import NET_DVR_LED_REGISTOR_VALUE


class struct_tagNET_DVR_LED_RECV_REGISTOR(Structure):
    pass

_S(struct_tagNET_DVR_LED_RECV_REGISTOR, [
    ('byEliminateGhostShadowLevel', BYTE),
    ('byEliminateShadowy', BYTE),
    ('byGrayEqualize1', BYTE),
    ('byGrayEqualize2', BYTE),
    ('byEnableGrayUniformity', BYTE),
    ('byDisableHGrayStripes', BYTE),
    ('byGhostShadowEnhancedMode1', BYTE),
    ('byGhostShadowEnhancedMode2', BYTE),
    ('byClearBadPoint', BYTE),
    ('byEnableSelfDefineRegistor', BYTE),
    ('byRes1', BYTE * 2),
    ('struRegistorValue', NET_DVR_LED_REGISTOR_VALUE),
    ('byEnabledExGradientOptimition', BYTE),
    ('byDummyGClockCycle', BYTE),
    ('byDummyGClockHighTime', BYTE),
    ('byFirstGClockExtendedTime', BYTE),
    ('byRes', BYTE * 28),
])

NET_DVR_LED_RECV_REGISTOR = struct_tagNET_DVR_LED_RECV_REGISTOR
LPNET_DVR_LED_RECV_REGISTOR = POINTER(struct_tagNET_DVR_LED_RECV_REGISTOR)
tagNET_DVR_LED_RECV_REGISTOR = struct_tagNET_DVR_LED_RECV_REGISTOR
