from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_6 import NET_DVR_SCHEDTIME


class struct_tagNET_DVR_PLAN_VQD_CFG(Structure):
    pass

_S(struct_tagNET_DVR_PLAN_VQD_CFG, [
    ('dwSize', DWORD),
    ('sPlanID', BYTE * 32),
    ('struDetectTime', (NET_DVR_SCHEDTIME * 8) * 7),
    ('byPlanMode', BYTE),
    ('byRes1', BYTE),
    ('byCheckFlag', BYTE),
    ('bySignal', BYTE),
    ('byBlur', BYTE),
    ('byLuma', BYTE),
    ('byChroma', BYTE),
    ('bySnow', BYTE),
    ('byStreak', BYTE),
    ('byFreeze', BYTE),
    ('byPTZ', BYTE),
    ('byEnablePlanRound', BYTE),
    ('byContrast', BYTE),
    ('byMono', BYTE),
    ('byShake', BYTE),
    ('byFlash', BYTE),
    ('byCover', BYTE),
    ('byScene', BYTE),
    ('byDark', BYTE),
    ('byRes', BYTE * 13),
])

NET_DVR_PLAN_VQD_CFG = struct_tagNET_DVR_PLAN_VQD_CFG
LPNET_DVR_PLAN_VQD_CFG = POINTER(struct_tagNET_DVR_PLAN_VQD_CFG)
tagNET_DVR_PLAN_VQD_CFG = struct_tagNET_DVR_PLAN_VQD_CFG
