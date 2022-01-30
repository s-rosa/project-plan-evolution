# Project Plan Evolution
Author: Sofia Rosa
<br>Collaborators: Alex Coles, Bekki Connolly, Miguel Angel

## Project Description
This challenge was set by Nplan, a UK-based software company which utilises machine learning and AI analytics to forecast outcomes of construction projects and mitigate risk.

## Problem Statement
The client wanted to understand the impact of updates and changes to project schedule plans.

## Solution
Our solution consists of a Power BI dashboard which provides a general overview of the activities and milestones required to complete a project. It allows to closely manage activities on the critical path and ensure the project is finished in time. The client can dive down and look at some of the specific information around activities and milestones including a list of tasks required to complete the project, an estimate of time that each activity / milestone will take to complete, and a graph neural network which allows to indentify dependencies between activities and milestones.

## Methodology

### 1. Collate data using Python
We have merged all the data files using Python.
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
Once the data was combined, we have built a dashboard in Power BI to help the client visualise the output. The first page gives an overview of the activities, milestones and links for the project. 
![Part1](https://user-images.githubusercontent.com/68342642/151710962-516aa8ff-a124-49a9-b743-49577c4a7277.gif)

The second page shows the status of each activity (also available for milestones). 
![Part2](https://user-images.githubusercontent.com/68342642/151712470-15f99c0b-0644-4043-920d-9b04addc1253.gif)

The third page allows to deep dive into a specific activity (also available for milestones).
![Part3](https://user-images.githubusercontent.com/68342642/151712476-5ff2a929-7c3a-411e-8ce6-6f689b4b6831.gif)

The fourth page shows dependencies between activities and milestones.
![Part4](https://user-images.githubusercontent.com/68342642/151712479-dacfea15-ab14-4d61-a73e-b3928e076e29.gif)

## Recommendations
In the future, we would want to use predictive modeling to forecast slippage and help the client avoid project delays.

## More Information
For a quick demo ouf our solution, please click here: (https://www.youtube.com/watch?v=_ZPRI1GVmEw&list=PLM0EU9nRaeVAAdF2xO_BZK00a8fN7ki1P&index=3)
