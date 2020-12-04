# DATA MODELING WITH POSTGRES

This project creates a postgres database "sparkifydb" for a music app, Sparkify. The purpose of the database is to model song and log datasets (originaly stored in JSON format) with a star schema optimised for queries on song play analysis.

## Schema design and ETL Pipeline

The star schema for Sparkify Database has 1 Fact Table (songplays) and 4 Dimension Tables (users, artists, time, songs). 
The create_tables.py file contains functions to CREATE DATABASE, CREATE TABLE and DROP TABLE which runs the Postgres SQL queries from sql_queries.py file.
The etl.py inturn inserts the data into the schema using insert statements from sql_queries.py file.



