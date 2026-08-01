# SQL - More Queries

This project is part of the ALU Higher Level Programming curriculum. It
covers MySQL users and privileges, table constraints, and retrieving
data from multiple tables using subqueries and joins.

## Learning Objectives

* How to create a new MySQL user
* How to manage privileges for a user on a database or table
* What a PRIMARY KEY and a FOREIGN KEY are
* How to use the NOT NULL and UNIQUE constraints
* How to retrieve data from multiple tables in one request
* What subqueries are
* What JOIN and UNION are

## Requirements

* Allowed editors: `vi`, `vim`, `emacs`
* All files are executed on Ubuntu 20.04 LTS using MySQL 8.0 (8.0.25)
* All files end with a new line
* Every SQL query has a comment just before it
* Every file starts with a comment describing the task
* All SQL keywords are in uppercase

## Tasks

| File | Description |
| ---- | ----------- |
| `0-privileges.sql` | Lists the privileges of two users |
| `1-create_user.sql` | Creates a user with all privileges |
| `2-create_read_user.sql` | Creates a database and a read-only user |
| `3-force_name.sql` | Table where the name cannot be null |
| `4-never_empty.sql` | Table where the id defaults to 1 |
| `5-unique_id.sql` | Table where the id must be unique |
| `6-states.sql` | Creates the states table with a primary key |
| `7-cities.sql` | Creates the cities table with a foreign key |
| `8-cities_of_california_subquery.sql` | Cities of California using a subquery |
| `9-cities_by_state_join.sql` | Cities with their state name using a join |
| `10-genre_id_by_show.sql` | Shows that have at least one genre |
| `11-genre_id_all_shows.sql` | All shows with their genre id or NULL |
| `12-no_genre.sql` | Shows without a genre linked |
| `13-count_shows_by_genre.sql` | Number of shows for each genre |
| `14-my_genres.sql` | All genres of the show Dexter |
| `15-comedy_only.sql` | All Comedy shows |
| `16-shows_by_genre.sql` | All shows with their genre name or NULL |

## Author

Clovis — ALU Higher Level Programming
