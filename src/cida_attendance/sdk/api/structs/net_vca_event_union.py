from ctypes import Union

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER
from .net_vca_adv_reach_height import NET_VCA_ADV_REACH_HEIGHT
from .net_vca_adv_traverse_plane import NET_VCA_ADV_TRAVERSE_PLANE
from .net_vca_answer import NET_VCA_ANSWER
from .net_vca_area import NET_VCA_AREA
from .net_vca_audio_abnormal import NET_VCA_AUDIO_ABNORMAL
from .net_vca_blackboard_write import NET_VCA_BLACKBOARD_WRITE
from .net_vca_combined_rule import NET_VCA_COMBINED_RULE
from .net_vca_duration import NET_VCA_DURATION
from .net_vca_fakecard import NET_VCA_FAKECARD
from .net_vca_fall_down import NET_VCA_FALL_DOWN
from .net_vca_get_up import NET_VCA_GET_UP
from .net_vca_high_density import NET_VCA_HIGH_DENSITY
from .net_vca_high_density_status import NET_VCA_HIGH_DENSITY_STATUS
from .net_vca_human_enter import NET_VCA_HUMAN_ENTER
from .net_vca_intrusion import NET_VCA_INTRUSION
from .net_vca_leave_position import NET_VCA_LEAVE_POSITION
from .net_vca_lecture import NET_VCA_LECTURE
from .net_vca_left import NET_VCA_LEFT
from .net_vca_loiter import NET_VCA_LOITER
from .net_vca_over_time import NET_VCA_OVER_TIME
from .net_vca_parking import NET_VCA_PARKING
from .net_vca_peoplenum_change import NET_VCA_PEOPLENUM_CHANGE
from .net_vca_play_cellphone import NET_VCA_PLAY_CELLPHONE
from .net_vca_reach_hight import NET_VCA_REACH_HIGHT
from .net_vca_retention import NET_VCA_RETENTION
from .net_vca_run import NET_VCA_RUN
from .net_vca_running import NET_VCA_RUNNING
from .net_vca_scanner import NET_VCA_SCANNER
from .net_vca_sit_quietly import NET_VCA_SIT_QUIETLY
from .net_vca_situation_analysis import NET_VCA_SITUATION_ANALYSIS
from .net_vca_spacing_change import NET_VCA_SPACING_CHANGE
from .net_vca_standup import NET_VCA_STANDUP
from .net_vca_stick_up import NET_VCA_STICK_UP
from .net_vca_take import NET_VCA_TAKE
from .net_vca_take_left import NET_VCA_TAKE_LEFT
from .net_vca_toilet_tarry import NET_VCA_TOILET_TARRY
from .net_vca_trail import NET_VCA_TRAIL
from .net_vca_traverse_plane import NET_VCA_TRAVERSE_PLANE
from .net_vca_violent_motion import NET_VCA_VIOLENT_MOTION
from .net_vca_yard_tarry import NET_VCA_YARD_TARRY


class union_tagNET_VCA_EVENT_UNION(Union):
    pass

_S(union_tagNET_VCA_EVENT_UNION, [
    ('uLen', DWORD * 23),
    ('struTraversePlane', NET_VCA_TRAVERSE_PLANE),
    ('struArea', NET_VCA_AREA),
    ('struIntrusion', NET_VCA_INTRUSION),
    ('struLoiter', NET_VCA_LOITER),
    ('struTakeTeft', NET_VCA_TAKE_LEFT),
    ('struParking', NET_VCA_PARKING),
    ('struRun', NET_VCA_RUN),
    ('struHighDensity', NET_VCA_HIGH_DENSITY),
    ('struViolentMotion', NET_VCA_VIOLENT_MOTION),
    ('struReachHight', NET_VCA_REACH_HIGHT),
    ('struGetUp', NET_VCA_GET_UP),
    ('struLeft', NET_VCA_LEFT),
    ('struTake', NET_VCA_TAKE),
    ('struHumanEnter', NET_VCA_HUMAN_ENTER),
    ('struOvertime', NET_VCA_OVER_TIME),
    ('struStickUp', NET_VCA_STICK_UP),
    ('struScanner', NET_VCA_SCANNER),
    ('struLeavePos', NET_VCA_LEAVE_POSITION),
    ('struTrail', NET_VCA_TRAIL),
    ('struFallDown', NET_VCA_FALL_DOWN),
    ('struAudioAbnormal', NET_VCA_AUDIO_ABNORMAL),
    ('struReachHeight', NET_VCA_ADV_REACH_HEIGHT),
    ('struToiletTarry', NET_VCA_TOILET_TARRY),
    ('struYardTarry', NET_VCA_YARD_TARRY),
    ('struAdvTraversePlane', NET_VCA_ADV_TRAVERSE_PLANE),
    ('struLecture', NET_VCA_LECTURE),
    ('struAnswer', NET_VCA_ANSWER),
    ('struStandUp', NET_VCA_STANDUP),
    ('struPeopleNumChange', NET_VCA_PEOPLENUM_CHANGE),
    ('struSpacingChange', NET_VCA_SPACING_CHANGE),
    ('struCombinedRule', NET_VCA_COMBINED_RULE),
    ('struSitQuietly', NET_VCA_SIT_QUIETLY),
    ('struHighDensityStatus', NET_VCA_HIGH_DENSITY_STATUS),
    ('struRunning', NET_VCA_RUNNING),
    ('struRetention', NET_VCA_RETENTION),
    ('struBlackboardWrite', NET_VCA_BLACKBOARD_WRITE),
    ('struSituationAnalysis', NET_VCA_SITUATION_ANALYSIS),
    ('struPlayCellphone', NET_VCA_PLAY_CELLPHONE),
    ('struDruation', NET_VCA_DURATION),
    ('struFakeCard', NET_VCA_FAKECARD),
])

NET_VCA_EVENT_UNION = union_tagNET_VCA_EVENT_UNION
LPNET_VCA_EVENT_UNION = POINTER(union_tagNET_VCA_EVENT_UNION)
tagNET_VCA_EVENT_UNION = union_tagNET_VCA_EVENT_UNION
