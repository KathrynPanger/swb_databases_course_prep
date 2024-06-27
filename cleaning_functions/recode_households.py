import math
import numpy as np
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

def recode_someone_left(entry):
    pass

def recode_someone_joined(entry):
    pass
def recode_ghs_state(entry):
    pass
def recode_household_stil_in_state(entry):
    pass

def recode_someone_moved_away(entry):
    pass


def recode_health_services_last_month(entry):
    pass

def recode_bought_petrol_ever(entry):
    pass

def recode_when_bought_petrol(entry):
    if math.isnan(entry):
        return entry
        # If not, recode the variable this way
    else:
        value = int(entry)
        if value == 1:
            return "PAST 7 DAYS"
        elif value == 2:
            return "BETWEEN 7 AND 30 DAYS"
        elif value == 3:
            return "MORE THAN 30 DAYS"
        else:
            return np.nan

# def recode_recode_liters_petrol_last_bought(entry):
#     pass

# def recode_cost_of_petrol_last_bought(entry):
#     pass

def recode_changed_price_of_petrol_last_month(entry):
    if math.isnan(entry):
        return entry
        # If not, recode the variable this way
    else:
        value = int(entry)
        if value == 1:
            return "INCREASED"
        elif value == 2:
            return "SAME"
        elif value == 3:
            return "DECREASED"
        elif value == 99:
            return "UNKNOWN"
        else:
            return np.nan

def recode_adequate_last_month(entry):
    if math.isnan(entry):
        return entry
        # If not, recode the variable this way
    else:
        value = int(entry)
        if value == 1:
            return "NOT ENOUGH"
        elif value == 2:
            return "ADEQUATE"
        elif value == 3:
            return "MORE THAN ENOUGH"
        else:
            return np.nan

def recode_adequate_healthcare_last_month(entry):
    if math.isnan(entry):
        return entry
        # If not, recode the variable this way
    else:
        value = int(entry)
        if value == 1:
            return "NOT ENOUGH"
        elif value == 2:
            return "ADEQUATE"
        elif value == 3:
            return "MORE THAN ENOUGH"
        elif value == 4:
            return "NO HEALTHCARE NEEDED"
        else:
            return np.nan


def recode_how_getting_by_financially(entry):
    if math.isnan(entry):
        return entry
        # If not, recode the variable this way
    else:
        value = int(entry)
        if value == 1:
            return "EXCELLENT"
        elif value == 2:
            return "GOOD"
        elif value == 3:
            return "FAIR"
        elif value == 4:
            return "POORLY"
        else:
            return np.nan
