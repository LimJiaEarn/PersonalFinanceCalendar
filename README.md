# Personal Finance Calendar


## Table of contents
- [Introduction](#introduction)
- [Features](#features)
- [Samples / Examples](#samples-/-examples)
    - [For Students](#for-students)
    - [For Working Adults](#for-working-adults)
- [Installation and Build Guide](#installation-and-build-guide)
- [Customisation Guide](#customisation-guide)
    - [Themes](#themes)
    - [Data Dictionary](#data-dictionary) 
- [Feedback](#feedback)
- [Technologies Used](#technologies-used)



## Introduction

This project is a inspired by the numerous excel financial trackers available online but lack personalisation and customisability.
Your finances are recorded on [accounting rows](https://github.com/LimJiaEarn/PersonalFinanceTracker/blob/main/README.md#accounting-rows) where they can be
summed (more features such as calculating %, savings will be added). The design mimics a calendar for a more aesthetic interface with up to 3 [themes](https://github.com/LimJiaEarn/PersonalFinanceTracker/blob/main/README.md#themes) to choose from!

You are highly recommended to read the [Customisation Guide](#customisation-guide) to fully utilise the customisation features built in this program!



## Features

A few of the things you can do with this project

* Customise the categorisation of your incomes & expenses 
* Personalise the color theme of your calendar
* View your daily/monthly incomes & expenses 
* Collate your daily/monthly incomes & expenses 
* Review your incomes & expenses 
<br /><br />
## Samples / Examples


### For Students



Overview Page:

![plot](https://github.com/LimJiaEarn/PersonalFinanceTracker/blob/main/README_docs/Student%20Sample%20Overview.PNG)


Monthly Page:

![plot](https://github.com/LimJiaEarn/PersonalFinanceTracker/blob/main/README_docs/Student%20Sample%20Monthly.PNG)




### For Working Adults


Overview Page:

![plot](https://github.com/LimJiaEarn/PersonalFinanceTracker/blob/main/README_docs/Working%20Adult%20Sample%20Overview.PNG)


Monthly Page:

![plot](https://github.com/LimJiaEarn/PersonalFinanceTracker/blob/main/README_docs/Working%20Adult%20Sample%20Monthly.PNG)
<br /><br />
## Installation and Build Guide



### Installing in Windows:

* [Download](https://download-directory.github.io/?url=https%3A%2F%2Fgithub.com%2FLimJiaEarn%2FPersonalFinanceCalendar%2Ftree%2Fmain%2FDownloadMe) or clone this repository's [DownloadMe](https://github.com/LimJiaEarn/PersonalFinanceCalendar/tree/main/DownloadMe). 
* You are highly encouraged to extract/store the downloaded files in a single folder
* Launch Command Prompt and change directory to the folder you have installed the files in. 
![plot](https://github.com/LimJiaEarn/PersonalFinanceCalendar/blob/main/README_docs/InstallBuildGuidePic1.PNG)

* `pip install openpyxl` to install Openpyxl Library, you may read how to [install packages](https://packaging.python.org/en/latest/tutorials/installing-packages/) should you need more assistance
* You are ready to start building your calendar after this!


### Building in Windows:

Note: Before you start building, please read the [Customisation Guide](#customisation-guide) so you can fully utilise the customisation features!

* `python CalendarSettingEditor.py` to starting running the python script
* Enter 1 (Loading previous Calendar Settings is still under construction)
* Enter the year of your Calendar
* Enter the [theme](#themes) for your Calendar
* You may go through each selection to edit your [Header and Weekly Titles](#data-dictionary) (Some default titles are set for you).
* Once done, enter 0 to proceed
* You may go through each selection to edit your [Accounting Rows](#accounting-rows)
* Once done, enter 0 to proceed
* You may go through each selection to edit your [Overview Page](#overview-page)
* Once done, enter 0 to proceed

=== At this point, your setting has been saved under a text file titled "YourCalendarSettings" ===

Initialise Calendar Now:
* Enter 1
* Enter your file name you would like (e.g. MyCalendar, MyFinances)

Initialise Calendar In Future:
* `python PFC_CalendarInitialiser.py` to starting running the python script
* Enter your file name you would like (e.g. MyCalendar, MyFinances)

=== Congratulations you have successfully built your Calendar! ===
<br /><br />
## Customisation Guide 



### Themes

#### Tropical Theme (Overview Page)
![plot](https://github.com/LimJiaEarn/PersonalFinanceCalendar/blob/main/README_docs/Overview%20Theme%20Tropical.PNG)

#### Tropical Theme (Monthly Page)
![plot](https://github.com/LimJiaEarn/PersonalFinanceCalendar/blob/main/README_docs/Monthly%20Theme%20Tropical.PNG)


#### Modern Theme (Overview Page)
![plot](https://github.com/LimJiaEarn/PersonalFinanceCalendar/blob/main/README_docs/Overview%20Theme%20Modern.PNG)

#### Modern Theme (Monthly Page)
![plot](https://github.com/LimJiaEarn/PersonalFinanceCalendar/blob/main/README_docs/Monthly%20Theme%20Modern.PNG)


#### Desert Theme (Overview Page)
![plot](https://github.com/LimJiaEarn/PersonalFinanceCalendar/blob/main/README_docs/Overview%20Theme%20Desert.PNG)

#### Desert Theme (Monthly Page)
![plot](https://github.com/LimJiaEarn/PersonalFinanceCalendar/blob/main/README_docs/Monthly%20Theme%20Desert.PNG)
<br /><br />
### Data Dictionary 



#### Visual representation of terms used:



#### Overview Page:

![plot](https://github.com/LimJiaEarn/PersonalFinanceTracker/blob/main/README_docs/Annotated%20Overview%20Page.PNG)

#### Inflow Overview (/ Titles) - First tab

#### Expenses Overview (/ Titles) - Second tab

#### Inflow Breakdown (/ Titles) - Third tab

#### Expenses Breakdown (/ Titles) - Fourth tab


#### Monthly Page:

![plot](https://github.com/LimJiaEarn/PersonalFinanceTracker/blob/main/README_docs/Annotated%20Monthly%20Page.PNG)


#### Left Header (/ Titles) -  Top left 

#### Right Header  (/ Titles) - Top right

#### Weekly Rows (/ Titles) - Left main section
<br /><br />
#### Accounting Rows
Accounting Rows are preset rows where you will enter the numerical value of your money movements (e.g. Rent, Meals).
Accounting Rows are split to two types
1) Inflow - Adds to your financials (Salary)
2) Expenses - Deducts from your financials (Meals)


#### Summation Rows
Summation Rows are customised rows where you choose the titles you want to add together for a more personalised overview page.
Example: Miscellaneous row can be added to sum up rows not chosen to presented in overview tab
<br /><br />
## Feedback
If you would like to report bugs or file feature requests, you are welcomed to do so [here](https://github.com/LimJiaEarn/PersonalFinanceCalendar/issues/new)
<br /><br />
## Technologies Used
This script is written 100% in python with the assistance of Openpyxl and a subset of json library.
To read more on openpyxl, its documentation is available at https://openpyxl.readthedocs.io/en/stable/


