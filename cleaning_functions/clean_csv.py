import pandas as pd
from pandas._libs import OutOfBoundsDatetime
from pandas._libs.internals import defaultdict
from unidecode import unidecode
from collections.abc import Callable
import re
from typing import Optional, Any
import uuid
import random
from numbers import Number


# convert a csv into utf8 format
def convert_utf8(original_file_path: str, new_file_path: str):
    df = pd.read_csv(original_file_path, converters=defaultdict(lambda i: str))
    for column in df.columns:
        df[column] = df[column].apply(lambda x: unidecode(str(x)))
    df.to_csv(new_file_path, encoding='utf-8')

#########################
# Single Entry Functions#
#########################

# Remove special characters when dealing with words
# transforms removed characters into spaces, removes . and -
def remove_special_for_words(entry: str | Number):
    return re.sub(r"[^a-zA-Z0-9]+", ' ', str(entry))

# Remove special characters when dealing with numbers
# No spaces, does not remove - and .
def remove_special_for_numbers(entry: str | Number):
    return re.sub(r"[^a-zA-Z0-9-.]+", '', str(entry))

# Remove leading and trailing spaces
def truncate(entry: str | Number):
    return str(entry).strip()

# Replace spaces with underscores
def snake_case(entry: str | Number):
    return str(entry).replace(" ", "_")

# Make all letters lowercase
def lower_case(entry: str | Number):
    return str(entry).lower()

def remove_spaces(entry: str | Number):
    return str(entry).replace(" ", "")


def cast_to_datetime(entry: str | Number):
    return pd.to_datetime(str(entry)).to_period(freq="D")

########################
# DataFrame Functions #
#######################

# Apply a list of functions to the column headers
def clean_headers(df: pd.DataFrame,
                  cleaning_functions_list: list[Callable]) -> pd.DataFrame:
    column_name_map = {item: item for item in df.columns}
    for item in column_name_map:
        for function in cleaning_functions_list:
            column_name_map[item] = function(column_name_map[item])
    df.rename(columns=column_name_map, inplace=True)
    return df


# Apply a list of functions to selected columns
def clean_columns(df: pd.DataFrame,
                  selected_columns: list[str],
                  cleaning_functions_list: list[Callable]) -> pd.DataFrame:
    for col in selected_columns:
        for function in cleaning_functions_list:
            df[col] = df[col].apply(lambda x: function(x))
    return df


# Apply a list of functions to every single entry in the dataframe
def clean_entries(df: pd.DataFrame,
                  cleaning_functions_list: list[Callable]) -> pd.DataFrame:
    for function in cleaning_functions_list:
        df = df.apply(lambda x: function(x))
        return df


def cast_data_types(df: pd.DataFrame, names_to_types: dict) -> pd.DataFrame:
    return df.astype(names_to_types)

def try_cast_data_types(df: pd.DataFrame, names_to_types: dict) -> pd.DataFrame:
    successful_casts = []
    failed_casts = {}
    for key, value in names_to_types.items():
        try:
            df = df.astype(names_to_types)
            successful_casts.append(key)
        except Exception as error:
            failed_casts[key] = error
    print (f"Successfully casted the following variables to their desired data types")
    print(successful_casts)
    print("Failed to cast the following variables ")
    print(failed_casts)
    return df, failed_casts

    return df



# Get a deterministic hash of a string, dependent only on the seed
# (for creating unique id columns which will always be consistent when fed the same data and seed, even if generated at different times)
def deterministic_uuid(entry: str | Number):
    random.seed(str(entry))
    id = uuid.UUID(bytes=bytes(random.getrandbits(8) for _ in range(16)), version=4)
    id = str(id).replace("-", "")
    return id

# Create a unique index column by taking a deterministic hash of values in selected identifier columns
def set_unique_index(df: pd.DataFrame,
                     columns_to_hash: list[str],
                     index_name="id",
                     index_length_limit: Optional[int] = None,
                     set_index: Optional[bool]=True):
    df[index_name] = list(
        map(lambda x: deterministic_uuid(''.join([str(col_value) for col_value in x]))[0:index_length_limit],
            df[columns_to_hash].values))
    if set_index:
        df.set_index(index_name, inplace=True)
    return df

# Define a function for replacing a cell with only "-" with None, as this should be a missing value
def convert_only_dash_to_missing(entry: Any) -> None:
    entry = str(entry)
    if entry =="-":
        return None
    else:
        return entry

def pilot_terminated_to_indicator(entry: any):
    entry = str(entry)
    if entry == "NO":
        return 0
    elif entry == "YES":
        return 1
    else:
        return None

def convert_dictionary(data_dict: dict) -> dict:
    converted_dict = {}
    for key, value in data_dict.items():
        for item in value:
            converted_dict[item] = key
    return converted_dict

def replace_nan_with_none(entry):
    lower_entry = str(entry).lower()
    if lower_entry in ['nan', 'none', 'nat', '-', '<na>', '<nat>']:
        return None
    else:
        return entry

def fix_list_columns(entry):
    if entry is not None:
        return str(entry).split(",")
    else:
        return None