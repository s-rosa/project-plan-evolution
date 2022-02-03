# Project Plan Evolution
Author: Sofia Rosa
<br>Collaborators: Alex Coles, Bekki Connolly, Miguel Angel


## Project Description
My team participated in Project:Hack 11, a competition hosted by Project Data Analytics Community. We took on a challenge set by Nplan, a UK-based software company which utilises machine learning and AI analytics to forecast outcomes of construction projects and mitigate risk. Nplan needed some help understand the impact of changes made to project schedule plans. We delivered a solution in 2 days and achieved the 3rd place out of 24 teams present.

## Problem Statement
It is important for project managers to be able to monitor and closely manage schedule updates when they happen to ensure projects are delivered on time. If some activities or milestones slip as a result of these changes, the whole project can be delayed and cause a financial loss. Project managers need to understand the impact of schedule updates and intervene, if necessary, to get their project back on schedule. 

## Solution
Our solution consists of a Power BI dashboard which provides a general overview of the activities and milestones required to complete a project. It allows to identify project delays early on and take immediate action to get the project back on schedule. The client can dive down and look at some of the specific information around activities and milestones including a list of tasks required to complete the project, an estimate of time that each task will take to complete, and task dependencies.

## Methodology

### 1. Collate data using Python
The client provided us with 130+ .CSV files. We have merged all the data files using Python.
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
# Combine all functions and create 3 .CSV files to be used in Power Bi
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
Once the data was combined, we have built a dashboard in Power BI to help the client visualise the output. The Programme Revision Summary page gives an overview of the activities, milestones, and links between activities and milestones. It allows the client to evaluate the complexity of the project and possibly change project scope or re-allocate resources.

![Part1](https://user-images.githubusercontent.com/68342642/151710962-516aa8ff-a124-49a9-b743-49577c4a7277.gif)

The Activity Status Summary page provides a summary of actual vs planned status of all project activities. It allows to identify high risk activities that must be closely managed to avoid project delays. A similar summary is also available for milestones.

![Part2](https://user-images.githubusercontent.com/68342642/151712470-15f99c0b-0644-4043-920d-9b04addc1253.gif)

The Activity Detail page allows to deep dive into one specific activity and compare planned vs actual start and end dates. A similar summary is also available for milestones.

![Part3](https://user-images.githubusercontent.com/68342642/151712476-5ff2a929-7c3a-411e-8ce6-6f689b4b6831.gif)

The Programme Network Explorer page shows dependencies between activities and milestones. It allows to identify activities and milestones that are critical to the successful delivery of the project.

![Part4](https://user-images.githubusercontent.com/68342642/151712479-dacfea15-ab14-4d61-a73e-b3928e076e29.gif)

## Recommendations
In the future, we would want to use predictive modeling to forecast slippage and help the client avoid project delays.

## More Information
For a quick demo, please click [here](https://www.youtube.com/watch?v=_ZPRI1GVmEw&list=PLM0EU9nRaeVAAdF2xO_BZK00a8fN7ki1P&index=3).
