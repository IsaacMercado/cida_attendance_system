from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .net_dvr_dispinfo import NET_DVR_DISPINFO


class struct_tagNET_DVR_SCREENCONTROL_ABILITY(Structure):
    pass

_S(struct_tagNET_DVR_SCREENCONTROL_ABILITY, [
    ('dwSize', DWORD),
    ('byLayoutNum', BYTE),
    ('byWinNum', BYTE),
    ('byOsdNum', BYTE),
    ('byLogoNum', BYTE),
    ('byInputStreamNum', BYTE),
    ('byOutputChanNum', BYTE),
    ('byCamGroupNum', BYTE),
    ('byPlanNum', BYTE),
    ('byRes1', BYTE * 5),
    ('byIsSupportPlayBack', BYTE),
    ('byMatrixInputNum', BYTE),
    ('byMatrixOutputNum', BYTE),
    ('struVgaInfo', NET_DVR_DISPINFO),
    ('struBncInfo', NET_DVR_DISPINFO),
    ('struHdmiInfo', NET_DVR_DISPINFO),
    ('struDviInfo', NET_DVR_DISPINFO),
    ('byMaxUserNums', BYTE),
    ('byPicSpan', BYTE),
    ('wDVCSDevNum', WORD),
    ('wNetSignalNum', WORD),
    ('wBaseCoordinateX', WORD),
    ('wBaseCoordinateY', WORD),
    ('byExternalMatrixNum', BYTE),
    ('byRes2', BYTE * 49),
])

NET_DVR_SCREENCONTROL_ABILITY = struct_tagNET_DVR_SCREENCONTROL_ABILITY
LPNET_DVR_SCREENCONTROL_ABILITY = POINTER(struct_tagNET_DVR_SCREENCONTROL_ABILITY)
tagNET_DVR_SCREENCONTROL_ABILITY = struct_tagNET_DVR_SCREENCONTROL_ABILITY
