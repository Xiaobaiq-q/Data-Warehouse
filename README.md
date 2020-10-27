# Data Warehouse with Redshift
## Introduction
A music streaming startup, Sparkify, has grown their user base and song database and want to move their processes and data onto the cloud. Their data resides in S3, in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

As their data engineer, you are tasked with building an ETL pipeline that extracts their data from S3, stages them in Redshift, and transforms data into a set of dimensional tables for their analytics team to continue finding insights in what songs their users are listening to. You'll be able to test your database and ETL pipeline by running queries given to you by the analytics team from Sparkify and compare your results with their expected results.

## Project Description
In this project, you'll apply what you've learned on data warehouses and AWS to build an ETL pipeline for a database hosted on Redshift. To complete the project, you will need to load data from S3 to staging tables on Redshift and execute SQL statements that create the analytics tables from these staging tables.

## Datasets

The log data and song data are stored in S3 public bucket.

1. s3://udacity-dend/log_data - user activity log files. Each file contains data on user activity: artist, auth, firstName, gender, itemInSession, lastName, length, level, location, method, page, registration, sessionId, song, status, ts, userAgent and userId.

2. s3://udacity-dend/song_data - songs data file. Each file contains metadata on a single song: num_songs, artist_id, artist_latitude, artist_longitude, artist_location, artist_name, song_id, title, duration and year.
## SongPlays Analysis Schema

#### Fact Table

| songplays |
| --- |
| songplay_id |
| start_time |
| user_id |
| level |
| song_id |
| artist_id |
| session_id |
| location |
| user_agent |

#### Dimension Tables

| users  |
| --- |
| user_id |
| first_name |
| last_name |
| gender |
| level |


| songs   |
| --- |
| song_id |
| title |
| artist_id |
| year |
| duration |


| artists    |
| --- |
| artist_id |
| name |
| location |
| lattitude |
| longitude |


| time     |
| --- |
| start_time |
| hour |
| day |
| week |
| month |
| year |
| weekday |

## Data Warehouse Configuration 
1. Create a IAM role in your AWS account. 
2. Create a Redshift Cluster and allow your created a IAM role to access your cluster.
3. GET ENDPOIN (Host address) and IAM role link and fill the config file.


## ETL pipeline
1. Create staging_events and staging_songs tables to store the data from S3 public buckets.
2. Load the data from S3 public buckets to staging tables in the Redshift Cluster.
2. Insert data into fact table and dimension tables from staging tables. 


## How to run
1. Run `create_tables.py` to create the table.

2. Run `etl.py` to start the ETL pipeline.