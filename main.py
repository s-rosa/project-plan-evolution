# 1. Import all data files
# 2. For each activity, links, milestones, condense into the same file
# 3. Write out those files to local system
import os
import pandas as pd
from typing import Tuple

def get_file_metadata(filename: str) -> Tuple[str, str]:
    """ Detect whether the csv concerns activities, links or milestones """
    # [0] - revision key
    # [1] - type (e.g. activity, milestone, link)
    tokenised_name = filename.split('.')
    return tokenised_name[1], tokenised_name[0]

def append_files(
    file_dataframe: pd.DataFrame,
    master_dataframe: pd.DataFrame,
    revision_name: str
):
    """ Append a csv into a master csv that is collating the data """
    # Need to add a column at the start with revision ID
    column_id = 'revision_name'
    file_dataframe[column_id] = revision_name
    return pd.concat([file_dataframe, master_dataframe])

def save_master_csv(dataframe: pd.DataFrame, name: str):
    """ Write out master csv with collated data"""
    base_path = os.path.abspath(os.path.dirname(__file__))
    save_path = base_path + '/' + 'results' + '/' + name + '.csv'
    print('save path: ', save_path)
    dataframe.to_csv(save_path)

def main():
    base_path = os.path.abspath(os.path.dirname(__file__))
    data_directory = base_path + '/' + 'data'

    # Need an initial csv to start with
    master_activity_csv = pd.DataFrame()
    master_link_csv = pd.DataFrame()
    master_milestone_csv = pd.DataFrame()

    for index, file_name in enumerate(os.listdir(data_directory)):
        print('File number: ', index)
        file_type, revision_name = get_file_metadata(file_name)
        print('file type: ', file_type)
        file_path = data_directory + '/' + file_name
        print('file_path: ', file_path)
        file_dataframe = pd.read_csv(file_path)


        if file_type == 'activity-actv':
            master_activity_csv = append_files(file_dataframe, master_activity_csv, revision_name)

        elif file_type == 'link-link':
            master_link_csv = append_files(file_dataframe, master_link_csv, revision_name)

        elif file_type == 'milestone-mstn':
            master_milestone_csv = append_files(file_dataframe, master_milestone_csv, revision_name)

    save_master_csv(master_activity_csv, 'master_activity')
    save_master_csv(master_link_csv, 'master_link')
    save_master_csv(master_milestone_csv, 'master_milestone')
    print('Saved all files')

main()
