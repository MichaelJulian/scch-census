# Santa Clara County Homeless Census Survey

##### The most recent homeless census (2015) polled 953 of the 7,000 homeless in Santa Clara County. 
Santa Clara County stretches from San Jose to Palo Alto, and up until recently, was home to the largest homeless encampment in America (the Jungle).

##### This repository is dedicated to exploring data,
through Python and R. 

##### understanding root problems of homelessness
by finding trends and strong statistical relationships across age, gender, health conditions, length of homelessness, reasons for homelessness, family conditions, and location.

##### and finding effective solutions.


# The Data

### SantaClaraCountyHomelessCensus.xlsx
#### [Sheet0] Final Survey

This sheet contains the responses to 240 questions across 953 respondents. The majority of columns contain categorical variables represented as integers.

#### [Sheet1] Variable Labels
This sheet links each column name to a more specific label. Unfortunately, for multipart questions, the original question is often missing but can be inferred.

#### [Sheet2] Value Labels
This sheet links the values in each cell to a more specific label / categorical variable. 


Example: (Sheet0) census['A3'] represents the answers to "What is your gender?" (found on Sheet1) and each answer is a number 1-4, representing answers Male, Female, Trans M to F, Trans F to M (found on Sheet2).


# Contribute

##### To this repo
The current dataset, a 3-sheet excel document needs to be refined to include:


1. smarter column names (240+ questions)
2. cleaner data (remove NaNs, convert to binary questions or categorical variables)
3. plotting functions for effective exploratory data analysis


##### to Homeless Directly

1. [Enjoy a meal with them every Sunday](http://www.believersinchristministry.com/)
2. [Donate to Homefirst](http://www.homefirstscc.org/)
3. [Check out the awesome, life-changing work CityTeam San Jose is doing](https://www.cityteam.org/san-jose/)