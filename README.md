# LOG ANALYSIS

This is a reporting tool that prints out reports (in plain text) based on the data in the database using PostgreSQL and Python.

## Getting Started

To get started on this, you will need to install the PostgreSQL database software on your preferred machine. 

## Preparing Your Data

- You need the data to analyze - you can download that [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
- You will need to unzip this file after downloading it. The file inside is called newsdata.sql
- To build the reporting tool, you'll need to load the site's data into your local database.
- To load the data use `psql -d news -f newsdata.sql`.
- Running this command will connect to your installed database server and execute the SQL commands in the downloaded file, creating tables and populating them with data.

## Running the Report

To run the reporting tool - download the pythoon file in the same directory as the database data and run `python news.py`