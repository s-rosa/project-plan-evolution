# Project Plan Evolution
Author: Sofia Rosa
<br>
Collaborators: Alex Coles, Bekki Connolly, Miguel Angel
## Project Description
This challenge was set by Nplan, a UK-based software company which utilises machine learning and AI analytics to forecast outcomes of construction projects and mitigate risk.
## Problem Statement
The client wanted to understand the impact of project schedule updates and monitor these updates when they happen.
## Solution
Our solution provides a general overview of the activities, milestones and links for the project. The client can then dive down into actual acitivity information 



Then goes into detail regarding the variance between planned and actual start / end dates for activities and milestones. Finally, it demonstrates a feature we would want to add had the data not be anonymised where we highlight key ‘high risk’ or ‘mission critical’ activities such as cranage and finds the average delay of any of these activities across multiple projects, which can then be used to derive an average cost for this risk.



## Methodology
### 1. Data Cleansing
We merged all data files into one using Python
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
# Separate categories of the files
def get_file_metadata(filename: str) -> Tuple[str, str]:
    """ Detect whether the csv concerns activities, links or milestones """
    # [0] - revision key
    # [1] - type (e.g. activity, milestone, link)
    tokenised_name = filename.split('.')
    return tokenised_name[1], tokenised_name[0]
```
## Future Development

## More Information
To learn more, please visit: https://www.youtube.com/watch?v=_ZPRI1GVmEw&list=PLM0EU9nRaeVAAdF2xO_BZK00a8fN7ki1P&index=3
