from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .net_dvr_subsystem_ability import NET_DVR_SUBSYSTEM_ABILITY


class struct_tagNET_DVR_VIDEOPLATFORM_ABILITY_V40(Structure):
    pass

_S(struct_tagNET_DVR_VIDEOPLATFORM_ABILITY_V40, [
    ('dwSize', DWORD),
    ('byCodeSubSystemNums', BYTE),
    ('byDecodeSubSystemNums', BYTE),
    ('bySupportNat', BYTE),
    ('byInputSubSystemNums', BYTE),
    ('byOutputSubSystemNums', BYTE),
    ('byCodeSpitterSubSystemNums', BYTE),
    ('byAlarmHostSubSystemNums', BYTE),
    ('bySupportBigScreenNum', BYTE),
    ('byVCASubSystemNums', BYTE),
    ('byV6SubSystemNums', BYTE),
    ('byV6DecoderSubSystemNums', BYTE),
    ('bySupportBigScreenX', BYTE),
    ('bySupportBigScreenY', BYTE),
    ('bySupportSceneNums', BYTE),
    ('byVcaSupportChanMode', BYTE),
    ('bySupportScreenNums', BYTE),
    ('bySupportLayerNums', BYTE),
    ('byNotSupportPreview', BYTE),
    ('byNotSupportStorage', BYTE),
    ('byUploadLogoMode', BYTE),
    ('struSubSystemAbility', NET_DVR_SUBSYSTEM_ABILITY * 120),
    ('by485Nums', BYTE),
    ('by232Nums', BYTE),
    ('bySerieStartChan', BYTE),
    ('byScreenMode', BYTE),
    ('byDevVersion', BYTE),
    ('bySupportBaseMapNums', BYTE),
    ('wBaseLengthX', WORD),
    ('wBaseLengthY', WORD),
    ('bySupportPictureTrans', BYTE),
    ('bySupportPreAllocDec', BYTE),
    ('bySupportDecAutoManage', BYTE),
    ('byTranDevSubSystemNums', BYTE),
    ('byFiberSwitchNums', BYTE),
    ('byRes2', BYTE * 625),
])

NET_DVR_VIDEOPLATFORM_ABILITY_V40 = struct_tagNET_DVR_VIDEOPLATFORM_ABILITY_V40
LPNET_DVR_VIDEOPLATFORM_ABILITY_V40 = POINTER(struct_tagNET_DVR_VIDEOPLATFORM_ABILITY_V40)
tagNET_DVR_VIDEOPLATFORM_ABILITY_V40 = struct_tagNET_DVR_VIDEOPLATFORM_ABILITY_V40
