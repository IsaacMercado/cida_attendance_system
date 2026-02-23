from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_ITS_GATE_LANE_CFG(Structure):
    pass

_S(struct_tagNET_ITS_GATE_LANE_CFG, [
    ('byGateSiteID', BYTE * 48),
    ('byGateInfo', BYTE * 48),
    ('byLaneName', BYTE * 32),
    ('byValid', BYTE),
    ('byCamLaneId', BYTE),
    ('wLaneid', WORD),
    ('byRelativeIoNum', BYTE),
    ('byDirection', BYTE),
    ('byLprMode', BYTE),
    ('byCardMode', BYTE),
    ('byGateLaneMode', BYTE),
    ('byCharge', BYTE),
    ('byChargeMode', BYTE),
    ('byRes1', BYTE),
    ('byLedRelativeIndex', BYTE * 8),
    ('byGateRelativeIndex', BYTE),
    ('byFarRrRelativeIndex', BYTE),
    ('byRes', BYTE * 82),
])

NET_ITS_GATE_LANE_CFG = struct_tagNET_ITS_GATE_LANE_CFG
LPNET_ITS_GATE_LANE_CFG = POINTER(struct_tagNET_ITS_GATE_LANE_CFG)
tagNET_ITS_GATE_LANE_CFG = struct_tagNET_ITS_GATE_LANE_CFG
