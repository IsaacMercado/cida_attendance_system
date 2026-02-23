from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .net_vca_facesnap_result import NET_VCA_FACESNAP_RESULT


class struct_tagNET_ITS_GATE_FACE(Structure):
    pass

_S(struct_tagNET_ITS_GATE_FACE, [
    ('dwSize', DWORD),
    ('byGroupNum', BYTE),
    ('byPicNo', BYTE),
    ('byFeaturePicNo', BYTE),
    ('byRes', BYTE),
    ('wLaneid', WORD),
    ('byCamLaneId', BYTE),
    ('byDir', BYTE),
    ('dwChanIndex', DWORD),
    ('byMonitoringSiteID', BYTE * 48),
    ('byDeviceID', BYTE * 48),
    ('struFaceInfo', NET_VCA_FACESNAP_RESULT),
    ('byRes2', BYTE * 256),
])

NET_ITS_GATE_FACE = struct_tagNET_ITS_GATE_FACE
LPNET_ITS_GATE_FACE = POINTER(struct_tagNET_ITS_GATE_FACE)
tagNET_ITS_GATE_FACE = struct_tagNET_ITS_GATE_FACE
