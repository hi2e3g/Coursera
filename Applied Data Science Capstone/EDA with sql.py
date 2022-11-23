"""
Assignment: SQL Notebook for Peer Assignment
Estimated time needed: 60 minutes.

Introduction
Using this Python notebook you will:

Understand the Spacex DataSet
Load the dataset into the corresponding table in a Db2 database
Execute SQL queries to answer assignment questions
Overview of the DataSet
SpaceX has gained worldwide attention for a series of historic milestones.

It is the only private company ever to return a spacecraft from low-earth orbit, which it first accomplished in December 2010. SpaceX advertises Falcon 9 rocket launches on its website with a cost of 62 million dollars wheras other providers cost upward of 165 million dollars each, much of the savings is because Space X can reuse the first stage.

Therefore if we can determine if the first stage will land, we can determine the cost of a launch.

This information can be used if an alternate company wants to bid against SpaceX for a rocket launch.

This dataset includes a record for each payload carried during a SpaceX mission into outer space.

Download the datasets
This assignment requires you to load the spacex dataset.

In many cases the dataset to be analyzed is available as a .CSV (comma separated values) file, perhaps on the internet. Click on the link below to download and save the dataset (.CSV file):

Spacex DataSet

Store the dataset in database table
it is highly recommended to manually load the table using the database console LOAD tool in DB2.
"""
!pip install sqlalchemy==1.3.9
!pip install ibm_db_sa
!pip install ipython-sql
%load_ext sql
%sql ibm_db_sa://mmp08973:xxxx@54a2f15b-5c0f-46df-8954-7e38e612c2bd.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud:32733/BLUDB?security=SSL
%sql select * from SPACEXTBL
#Task 1
#Display the names of the unique launch sites in the space mission
%sql select DISTINCT LAUNCH_SITE from SPACEXTBL
#Task 2
#Display 5 records where launch sites begin with the string 'CCA'
%sql select * from SPACEXTBL where launch_site like 'CCA%' limit 5
#Task 3
#Display the total payload mass carried by boosters launched by NASA (CRS)
%sql select sum(payload_mass__kg_) as sum from SPACEXTBL where customer like 'NASA (CRS)'

#Task 4
#Display average payload mass carried by booster version F9 v1.1
%sql select avg(payload_mass__kg_) as Average from SPACEXTBL where booster_version like 'F9 v1.1%'
#Task 5
#List the date when the first succesful landing outcome in ground pad was acheived.
Hint:Use min function

%sql select min(date) as Date from SPACEXTBL where mission_outcome like 'Success'
#Task 6
#List the names of the boosters which have success in drone ship and have payload mass greater than 4000 but less than 6000
%sql select booster_version from SPACEXTBL where (mission_outcome like 'Success') AND (payload_mass__kg_ BETWEEN 40
#Task 7
#List the total number of successful and failure mission outcomes
%sql SELECT mission_outcome, count(*) as Count FROM SPACEXTBL GROUP by mission_outcome ORDER BY mission_outcome


#Task 8
#List the names of the booster_versions which have carried the maximum payload mass. Use a subquery
maxm = %sql select max(payload_mass__kg_) from SPACEXTBL
maxv = maxm[0][0]

%sql select booster_version from SPACEXTBL where payload_mass__kg_=(select max(payload_mass__kg_) from SPACEXTBL)

#Task 9
#List the failed landing_outcomes in drone ship, their booster versions, and launch site names for the in year 2015
%sql select MONTHNAME(DATE) as Month, landing__outcome, booster_version, launch_site from SPACEXTBL where DATE like '2015%' AND landing__outcome like 'Failure (drone ship)'

#Task 10
#Rank the count of landing outcomes (such as Failure (drone ship) or Success (ground pad)) between the date 2010-06-04 and 2017-03-20, in descending order
%sql select landing__outcome, count(*) as count from SPACEXTBL where Date >= '2010-06-04' AND Date <= '2017-03-20'
