# Visualize-SQL-queries-in-python
This repository contains a simple method to visualize SQL queries in Python. The visualizaiton is already available in many SQL platforms, but I have not seen such in Python. Since one might have more leverage to run SQL queries in python, I figured it might be a helpful addition to make things simpler in Python, as well. Before coming up with this, I just intended to practice with some SQL queries in Python using the 'chinook' database. 

Using sqlite3 packcage in python, there is no straightforward method to see what selection query's output is. To address this, I wrote a simple function that utilizes pandas dataframes and some regex search to have meaningful table structures.

The regex search is utilized to extract column names form an SQL query. The regex expression were tested under various conditions. However, seach task is not yet over since I am sure there are situations where the available searching is not sufficient.
