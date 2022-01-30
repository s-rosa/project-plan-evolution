# Project Plan Evolution
Author: Sofia Rosa
<br>
Collaborators: Alex Coles, Bekki Connolly, Miguel Angel
## Project Description
This challenge was set by Nplan, a UK-based software company which utilises machine learning and AI analytics to forecast outcomes of construction projects and mitigate risk.
## Problem Statement
The client wanted to understand the impact of project schedule updates and monitor these updates when they happen.
## Solution
Our solution consists of a Power BI dashboard which provides a general overview of the activities, milestones and links for the project. The client can dive down and look at some of the specific information around activities and milestones (including planned and actual start / end dates, 


which shows the complexity of the project


Then goes into detail regarding the variance between planned and actual start / end dates for activities and milestones. Finally, it demonstrates a feature we would want to add had the data not be anonymised where we highlight key ‘high risk’ or ‘mission critical’ activities such as cranage and finds the average delay of any of these activities across multiple projects, which can then be used to derive an average cost for this risk.



## Methodology
### 1. Collate data using Python
We have merged all the data files into one using Python.
```python
# Import Python libraries
import os
import pandas as pd
from typing import Tuple
```
```python
# Separate categories of the files
def get_file_metadata(filename: str) -> Tuple[str, str]:
    """ Detect whether the csv concerns activities, links or milestones """
    # [0] - revision key
    # [1] - type (e.g. activity, milestone, link)
    tokenised_name = filename.split('.')
    return tokenised_name[1], tokenised_name[0]
```
```python
# Concatenate the files
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
```
```python
# Save tables
def save_master_csv(dataframe: pd.DataFrame, name: str):
    """ Write out master csv with collated data"""
    base_path = os.path.abspath(os.path.dirname(__file__))
    save_path = base_path + '/' + 'results' + '/' + name + '.csv'
    print('save path: ', save_path)
    dataframe.to_csv(save_path)
```
```python
# Combines all functions and create 3 .CSV files to be used in Power Bi
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
```
### 2. Build a dashboard in Power BI
Finally, we have built a Power BI dashboard to help visualise the combined data.
https://gfycat.com/unkemptfriendlyicelandichorse
## Recommendations
In the future, we would want to use predictive modeling to forecast slippage and help the client avoid delays in schedule.
## More Information
To learn more, please visit: https://www.youtube.com/watch?v=_ZPRI1GVmEw&list=PLM0EU9nRaeVAAdF2xO_BZK00a8fN7ki1P&index=3
