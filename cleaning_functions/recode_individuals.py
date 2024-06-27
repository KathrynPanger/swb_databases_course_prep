import math
import numpy as np

rename_dict={
    "s1q2": "scheduled_interview_date",
    "s1q3": "phone_answer_status",
    "s1q5": "is_household_member",
    "call_id": "call_attempt_number",
    "hhid": "household_id",
    "s1q1": "phone_number_id",
    "s1q8": "agree_to_be_interviewed",
    'indiv': "person_id",
    's2q7a': 'is_household_head_still_member',
    's2q8': 'why_person_join_household',
    's2q2': 'is_new_household_member',
    's2q3': 'is_still_household_member',
    's2q5': 'sex',
    's2q6': 'age',
    's2q7': 'relationship_to_head',
    's2q7_os': 'other_relationship',
    's2q8': 'why_join_household',
    's2q4': 'why_leave_household',
    's2q8_os':'other_reason_for_joining',
    's2q14': 'is_covid_vaccinated',
    's6q0b_1': 'is_available_to_respond',
    's6q1_1': 'worked_for_pay_last_week',
    's6q1a_1': 'has_business_was_absent_last_week',
    's6q1b_1': 'when_expected_to_return_to_work',
    's6q1c_1': 'why_not_work_last_week',
    's6q1c_os_1': 'other_reason_not_work',
    's6q3a_1': 'tried_to_earn_pay_last_month',
    's6q3b_1': 'how_tried_to_earn_pay_last_month',
    's6q3b_os_1': 'other_way_tried_to_earn_pay_last_month',
    's6q5b_1': 'main_activity_of_employers_business_last_week',
    's6q6a_1': "family_farm_food_fate",
    "s6q8b1_1": 'hours_worked_last_week_main_business_activity',
    's6q9a_1': 'worked_december_2021',
    's6q9b_1': 'worked_january_2022',
    's6q9c_1': 'worked_february_2022',
    's6q9d_1': 'worked_march_2022',
    's6cq1_1': 'age_started_working',
    's6cqe2_1': 'is_employed',
    's6cq5_1': 'years_worked_first_job',
    's6cq6_1': 'why_left_first_job',
    's2q15': 'how_many_shots'


}



dtype = {'household_id': 'string',
              'is_new_household_member': 'str',
              'is_still_household_member': 'str',
              'why_leave_household': 'str',
              'sex': 'str',
              'age': 'Int64',
              'relationship_to_head': 'str',
              'other_relationship': 'str',
              'why_join_household': 'str',
              'other_reason_for_joining':'str',
              'is_selected_farmer': 'str',
              'is_covid_vaccinated': 'str',
              'is_available_to_respond': 'str',
              'worked_for_pay_last_week': 'str',
              'has_business_was_absent_last_week': 'str',
              'when_expected_to_return_to_work': 'str',
              'why_not_work_last_week': 'str',
              'other_reason_not_work': 'str',
              'tried_to_earn_pay_last_month': 'str',
              'how_tried_to_earn_pay_last_month': 'str',
              'other_way_tried_to_earn_pay_last_month': 'str',
              'main_activity_of_employers_business_last_week': 'str',
              'family_farm_food_fate': "str",
              "hours_worked_last_week_main_business_activity": 'Int64',
              'worked_december_2021': 'str',
              'worked_january_2022': 'str',
              'worked_february_2022': 'str',
              'worked_march_2022': 'str',
              'age_started_working': 'Int64',
              'is_employed': 'str',
              'years_worked_first_job': 'Int64',
              'why_left_first_job': 'str',
               'how_many_shots': 'Int64',

               }


def recode_agree_to_be_interviewed(entry):
    if math.isnan(entry):
        return entry
    else:
        value = int(entry)
        if value == 1:
            return "YES"
        elif value == 2:
            return "NO"

def recode_phone_answer_status(entry):
    if math.isnan(entry):
        return entry
    else:
        value = int(entry)
        if value == 1:
            return "YES, ANSWERED"
        elif value == 2:
            return "NO, NOT ANSWERED"
        elif value == 3:
            return "NO, NUMBER DOES NOT EXIST"
        elif value == 4:
            return "NO, PHONE SWITCHED OFF"


def recode_speaker_is_household_member(entry):
    # If the entry has missing data, skip it
    if math.isnan(entry):
        return entry
    #If not, recode the variable this way
    else:
        value = int(entry)
        if value == 1:
            return "YES"
        elif value == 2:
            return "NO"
        elif value == 3:
            return "UNKNOWN, LANGUAGE BARRIER"


def recode_why_leave_household(entry):
    if math.isnan(entry):
        return entry
    # If not, recode the variable this way
    else:
        value = int(entry)
        if value == 1:
            return "DIVORCE OR SEPORATION"
        elif value == 2:
            return "EDUCATIONAL OPPORTUNITY"
        elif value == 3:
            return "WORK"
        elif value == 4:
            return "FIND BETTER LAND"
        elif value == 5:
            return "HEALTH REASONS"
        elif value == 6:
            return "SECURITY REASONS"
        elif value == 7:
            return "MARRIAGE OR COHABITATION"
        elif value == 8:
            return 'JOIN OTHER FAMILY'
        elif value == 9:
            return "MOVED WITH OWN FAMILY"
        elif value == 10:
            return "SET UP OWN HOME"
        elif value == 11:
            return "CONFLICT OR INSURGENCY"
        elif value == 12:
            return "DISPUTE WITH OTHERS"
        elif value == 13:
            return "ABDUCTED OR KIDNAPPED"
        elif value == 14:
            return "DECEASED"
        elif value == 15:
            return "DISPLACED DUE TO DROUGHT"
        elif value == 16:
            return 'HARVEST LOSS'
        elif value == 17:
            return 'DISPLACED DUE TO FLOOD'
        elif value == 96:
            return 'OTHER'
        else:
            return np.nan

def recode_binary(entry):
    if math.isnan(entry):
        return entry
    #If not, recode the variable this way
    else:
        value = int(entry)
        if value == 1:
            return "YES"
        elif value == 2:
            return "NO"
        else:
            return np.nan

def recode_sex(entry):
    if math.isnan(entry):
        return entry
    #If not, recode the variable this way
    else:
        value = int(entry)
        if value == 1:
            return "MALE"
        elif value == 2:
            return "FEMALE"
        else:
            return np.nan

def recode_relationship_to_head(entry):
    if math.isnan(entry):
        return entry
    #If not, recode the variable this way
    else:
        value = int(entry)
        if value == 1:
            return "HEAD"
        elif value == 2:
            return "SPOUSE"
        elif value == 3:
            return "OWN CHILD"
        elif value == 4:
            return "STEP CHILD"
        elif value == 5:
            return "ADOPTED CHILD"
        elif value == 6:
            return "GRANDCHILD"
        elif value == 7:
            return "SIBLING"
        elif value == 8:
            return 'NIECE OR NEPHEW'
        elif value == 9:
            return "SIBLING-IN-LAW"
        elif value == 10:
            return "PARENT"
        elif value == 11:
            return "PARENT-IN-LAW"
        elif value == 12:
            return "DOMESTIC HELP"
        elif value == 14:
            return "OTHER RELATION"
        elif value == 15:
            return "OTHER NON-RELATION"
        elif value == 16:
            return "CHILD-IN-LAW"
        elif value == 98:
            return 'FORMER_HEAD'
        else:
            return np.nan

def recode_why_join_household(entry):
    if math.isnan(entry):
        return entry
    #If not, recode the variable this way
    else:
        value = int(entry)
        if value == 1:
            return "NEW BORN"
        elif value == 2:
            return "ADOPTED CHILD"
        elif value == 3:
            return "MARRIAGE OR COHABITATION"
        elif value == 4:
            return "DIVORCE OR SEPARATION"
        elif value == 5:
            return "RETURNED FROM COLLEGE"
        elif value == 6:
            return "RETURNED FROM INSTITUTION"
        elif value == 7:
            return "MOVED IN WITH RELATIVE"
        elif value == 8:
            return 'SHARED ACCOMMODATION'
        elif value == 9:
            return "RETURN FROM WORK MIGRATION"
        elif value == 10:
            return "MISTAKENLY NOT REPORTED OR FORGOTTEN LAST VISIT"
        elif value == 11:
            return "DISPLACED DUE TO CONFLICT"
        elif value == 12:
            return "CORONAVIRUS RELATED"
        elif value == 15:
            return "DISPLACED DUE TO DROUGHT"
        elif value == 16:
            return "HARVEST LOSS"
        elif value == 17:
            return "DISPLACED DUE TO FLOOD"
        elif value == 96:
            return 'OTHER'
        else:
            return np.nan


def recode_why_leave_household(entry):
    if math.isnan(entry):
        return entry
    # If not, recode the variable this way
    else:
        value = int(entry)
        if value == 1:
            return "DIVORCE OR SEPORATION"
        elif value == 2:
            return "EDUCATIONAL OPPORTUNITY"
        elif value == 3:
            return "WORK"
        elif value == 4:
            return "FIND BETTER LAND"
        elif value == 5:
            return "HEALTH REASONS"
        elif value == 6:
            return "SECURITY REASONS"
        elif value == 7:
            return "MARRIAGE OR COHABITATION"
        elif value == 8:
            return 'JOIN OTHER FAMILY'
        elif value == 9:
            return "MOVED WITH OWN FAMILY"
        elif value == 10:
            return "SET UP OWN HOME"
        elif value == 11:
            return "CONFLICT OR INSURGENCY"
        elif value == 12:
            return "DISPUTE WITH OTHERS"
        elif value == 13:
            return "ABDUCTED OR KIDNAPPED"
        elif value == 14:
            return "DECEASED"
        elif value == 15:
            return "DISPLACED DUE TO DROUGHT"
        elif value == 16:
            return 'HARVEST LOSS'
        elif value == 17:
            return 'DISPLACED DUE TO FLOOD'
        elif value == 96:
            return 'OTHER'
        else:
            return np.nan

def recode_is_covid_vaccinated(entry):
    if math.isnan(entry):
        return entry
    #If not, recode the variable this way
    else:
        value = int(entry)
        if value == 1:
            return "YES"
        elif value == 2:
            return "NO"
        elif value == 99:
            return "UNKNOWN"
        else:
            return np.nan

def recode_when_expected_to_return_to_work(entry):
    if math.isnan(entry):
        return entry
    #If not, recode the variable this way
    else:
        value = int(entry)
        if value == 1:
            return "WITHIN ONE WEEK"
        elif value == 2:
            return "WITHIN ONE MONTH"
        elif value == 3:
            return "WITHIN THREE MONTHS"
        elif value == 4:
            return "MORE THAN THREE MONTHS"
        elif value == 5:
            return "ONCE RESTRICTIONS ARE LIFTED"
        elif value == 98:
            return "UKNOWN"
        else:
            return np.nan

def recode_why_not_work_last_week(entry):
    if math.isnan(entry):
        return entry
    #If not, recode the variable this way
    else:
        value = int(entry)
        if value == 1:
            return "CORONAVIRUS CLOSURE"
        elif value == 2:
            return "CLOSURE FOR NON-CORONAVIRUS REASON"
        elif value == 3:
            return "LAID OFF"
        elif value == 4:
            return "FURLOUGHED"
        elif value == 5:
            return "VACATION"
        elif value == 6:
            return "SICK"
        elif value == 7:
            return "CARE FOR ILL RELATIVE"
        elif value == 8:
            return 'SEASONAL WORKER'
        elif value == 9:
            return "RETIRED"
        elif value == 10:
            return "MOVEMENT RESTRICTIONS"
        elif value == 11:
            return "LACK OF INPUTS FOR FARMING"
        elif value == 12:
            return "NOT FARMING SEASON"
        elif value == 13:
            return "PERSONNEL ROTATION DUE TO CORONAVIRUS"
        elif value == 14:
            return "CONFLICT OR INSURGENCY"
        elif value == 15:
            return "CLOSED DUE TO ENDSARS PROTESTS"
        elif value == 17:
            return 'LACK OF BUSINESS INPUTS'
        elif value == 18:
            return "MATERNITY LEAVE"
        elif value == 96:
            return 'OTHER'
        else:
            return np.nan

def recode_how_tried_to_earn_pay_last_month(entry):
    if math.isnan(entry):
        return entry
    #If not, recode the variable this way
    else:
        value = int(entry)
        if value == 1:
            return "APPLY TO PROSPECTIVE EMPLOYERS"
        elif value == 2:
            return "ANSWER JOB ADVERTISEMENTS"
        elif value == 3:
            return "STUDY JOB ADVERTISEMENTS"
        elif value == 4:
            return "REGISTER WITH UNEMPLOYMENT CENTER"
        elif value == 5:
            return "REGISTER WITH PRIVATE RECRUITMENT OFFICE"
        elif value == 6:
            return "TAKE A TEST OR INTERVIEDW"
        elif value == 7:
            return "SEEK HELP FROM RELATIVES, FRIENDS, OTHERS"
        elif value == 8:
            return 'CHECK AT WORK SITES'
        elif value == 9:
            return "WAIT ON TEH STREET TO BE RECRUITED"
        elif value == 10:
            return "SEEK FINANCIAL HELP TO START A BUSINESS"
        elif value == 11:
            return "LOOK FOR NON-FINANCIAL RESOURCES TO START A BUSINESS"
        elif value == 12:
            return "APPLY FOR PERMIT TO START A BUSINESS"
        elif value == 96:
            return "OTHER"
        else:
            return np.nan

def recode_main_activity_of_employers_business_last_week(entry):
    if math.isnan(entry):
        return entry
    #If not, recode the variable this way
    else:
        value = int(entry)
        if value == 1:
            return "AGRICULTURE, HUNTING, FISHING"
        elif value == 2:
            return "MINING, MANUFACTURING"
        elif value == 3:
            return "ELECTRICITY, GAS, WATER SUPPLY"
        elif value == 4:
            return "CONSTRUCTION"
        elif value == 5:
            return "BUYING & SELLING GOODS, REPAIR OF GOODS, HOTELS & RESTAURANTS"
        elif value == 6:
            return "TRANSPORT, DRIVING, POST, TRAVEL AGENCIES"
        elif value == 7:
            return "PROFESSIONAL ACTIVITIES: FINANCE, LEGAL, ANALYSIS, COMPUTER, REAL ESTATE"
        elif value == 8:
            return 'PUBLIC ADMINISTRATION'
        elif value == 9:
            return "PERSONAL SERVICES, EDUCATION, HEALTH, CULTURE, SPORT, DOMESTIC WORK, OTHER"
        else:
            return np.nan

def recode_family_farm_food_fate(entry):
    if math.isnan(entry):
        return entry
    #If not, recode the variable this way
    else:
        value = int(entry)
        if value == 1:
            return "ONLY FOR SALE"
        elif value == 2:
            return "ONLY FOR FAMILY CONSUMPTION"
        elif value == 3:
            return "BOTH FAMILY AND SALE"
        else:
            return np.nan


def recode_hours_worked_last_week_main_business_activity(entry):
    if math.isnan(entry) or int(entry) != 998:
        return entry
    #If not, recode the variable this way
    else:
        return "UNKNOWN"

def recode_why_left_first_job(entry):
    if math.isnan(entry):
        return entry
    #If not, recode the variable this way
    else:
        value = int(entry)
        if value == 1:
            return "TEMPORARY CONTRACT"
        elif value == 2:
            return "TO HAVE A BETTER PAID JOB"
        elif value == 3:
            return "TO HAVE MORE CLIENTS OR BUSINESS"
        elif value == 4:
            return "TO WORK MORE HOURS"
        elif value == 5:
            return "TO WORK FEWER HOURS"
        elif value == 6:
            return "TO BETTER MATCH SKILLS"
        elif value == 7:
            return "TO WORK CLOSER TO HOME"
        elif value == 8:
            return "TO IMPROVE OTHER WORKING CONDITIONS"
        elif value == 9:
            return "LAID OFF"
        elif value == 10:
            return "BUSINESS CLOSED"
        elif value == 11:
            return "TO RELOCATE"
        elif value == 12:
            return "TO STUDY OR GAIN NEW SKILLS"
        elif value == 96:
            return "OTHER"
        else:
            return np.nan

def recode_how_many_shots(entry):
    if math.isnan(entry):
        return entry
    #If not, recode the variable this way
    else:
        value = int(entry)
        if value == 1:
            return "ONE DOSE"
        elif value == 2:
            return "TWO DOSES"
        elif value == 3:
            return "BOOSTER"
        elif value == 99:
            return "UNKNOWN"
        else:
            return np.nan

def recode_age_started_working(entry):
    if entry != 99:
        return entry
    else:
        return np.nan

def recode_hours_worked_last_week_main_business_activity(entry):
    try:
        return int(entry)
    except ValueError:
        return entry

recode_dict = {
    "scheduled_interview_date": "scheduled_interview_date",
    "phone_answer_status": "phone_answer_status",
    "is_household_member": recode_binary,
    "agree_to_be_interviewed": recode_binary,
    'is_new_household_member': recode_binary,
    'is_still_household_member': recode_binary,
    'is_selected_farmer': recode_binary,
    'sex': recode_sex,
    'age': 'age',
    'relationship_to_head': recode_relationship_to_head,
 #   'other_relationship': 'other_relationship',
    'why_join_household': recode_why_join_household,
    'why_leave_household': recode_why_leave_household,
#    'other_reason_for_joining':'other_reason_for_joining',
    'is_covid_vaccinated': recode_is_covid_vaccinated,
    'is_available_to_respond': recode_binary,
    'worked_for_pay_last_week': recode_binary,
    'has_business_was_absent_last_week': recode_binary,
    'when_expected_to_return_to_work': recode_when_expected_to_return_to_work,
    'why_not_work_last_week': recode_why_not_work_last_week,
#    'other_reason_not_work': 'other_reason_not_work',
    'tried_to_earn_pay_last_month': recode_binary,
    'how_tried_to_earn_pay_last_month': recode_how_tried_to_earn_pay_last_month,
#   'other_way_tried_to_earn_pay_last_month': 'other_way_tried_to_earn_pay_last_month',
    'main_activity_of_employers_business_last_week': recode_main_activity_of_employers_business_last_week,
    'family_farm_food_fate': recode_family_farm_food_fate,
    "hours_worked_last_week_main_business_activity": recode_hours_worked_last_week_main_business_activity,
    'worked_december_2021': recode_binary,
    'worked_january_2022': recode_binary,
    'worked_february_2022': recode_binary,
    'worked_march_2022': recode_binary,
    'age_started_working': recode_age_started_working,
    'is_employed': recode_binary,
#    'years_worked_first_job': 'years_worked_first_job',
    'why_left_first_job': recode_why_left_first_job,
    'how_many_shots': recode_how_many_shots

}
