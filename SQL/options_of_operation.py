# hello=# \c test_user 
# You are now connected to database "test_user" as user "hello".
# test_user=# create type positions as enum ('mentor', 'tracker', 'scrum
# test_user'# ');
# CREATE TYPE
# test_user=# create table makers(
# test_user(# mentor_id serial primary key,
# test_user(# name varchar(50)  not null,
# test_user(# position positions not null,
# test_user(# birthdate date,
# test_user(# salary int);
# CREATE TABLE
# test_user=# insert into makers ( name, position, birthdate, salary) values ('Alice', 'mentor', '1996-04-09', '6000');
# INSERT 0 1
# test_user=# select * from makers;
#  mentor_id | name  | position | birthdate  | salary 
# -----------+-------+----------+------------+--------
#          1 | Alice | mentor   | 1996-04-09 |   6000
# (1 row)
# test_user=# insert into makers (name, position, birthdate, salary) values ('Anton', 'tracker', '1990-04-03', '3000');
# INSERT 0 1

# test_user=# insert into makers (name, position, birthdate, salary) values ('Josh', 'mentor', '2004-08-02', '10000');
# INSERT 0 1

# test_user=# insert into makers (name, position, birthdate, salary) values ('Argen', 'mentor', '2004-08-07', '100000000');
# INSERT 0 1

# test_user=# insert into makers (name , position, birthdate, salary) values ('Anton', 'tracker', '1890-04-29', '2999')
# ;
# INSERT 0 1

# test_user=# insert into makers( name, position, birthdate, salary) values ('Alex', 'mentor', '1989-06-11', '20000');
# INSERT 0 1

# test_user=# insert into makers (name, position, birthdate, salary) values ('Samara', 'tracker', '2004-08-11', '2843349');
# INSERT 0 1

# test_user=# insert into makers (name, position, birthdate, salary) values ('Sasha', 'mentor', '2000-08-23', '222221');
# INSERT 0 1


# test_user=# select * from makers;
#  mentor_id |  name  | position | birthdate  |  salary   
# -----------+--------+----------+------------+-----------
#          1 | Alice  | mentor   | 1996-04-09 |      6000
#          2 | Anton  | tracker  | 1990-04-03 |      3000
#          3 | Josh   | mentor   | 2004-08-02 |     10000
#          4 | Argen  | mentor   | 2004-08-07 | 100000000
#          5 | Anton  | tracker  | 1890-04-29 |      2999
#          6 | Alex   | mentor   | 1989-06-11 |     20000
#          7 | Samara | tracker  | 2004-08-11 |   2843349
#          8 | Sasha  | mentor   | 2000-08-23 |    222221
# (8 rows)

# test_user=# insert into makers (name, position, birthdate, salary) values ('Jecica', 'mentor', '2001-01-12', '50000');
# INSERT 0 1
# test_user=# insert into makers (name, position, birthdate, salary) values ('Alan', 'tracker', '2001-04-16', '6000');
# INSERT 0 1
# test_user=# select * from makers;
#  mentor_id |  name  | position | birthdate  |  salary   
# -----------+--------+----------+------------+-----------
#          1 | Alice  | mentor   | 1996-04-09 |      6000
#          2 | Anton  | tracker  | 1990-04-03 |      3000
#          3 | Josh   | mentor   | 2004-08-02 |     10000
#          4 | Argen  | mentor   | 2004-08-07 | 100000000
#          5 | Anton  | tracker  | 1890-04-29 |      2999
#          6 | Alex   | mentor   | 1989-06-11 |     20000
#          7 | Samara | tracker  | 2004-08-11 |   2843349
#          8 | Sasha  | mentor   | 2000-08-23 |    222221
#          9 | Jecica | mentor   | 2001-01-12 |     50000
#         10 | Alan   | tracker  | 2001-04-16 |      6000
# (10 rows)

# test_user=# select position || ' ' || name as mentors from makers;
#     mentors     
# ----------------
#  mentor Alice
#  tracker Anton
#  mentor Josh
#  mentor Argen
#  tracker Anton
#  mentor Alex
#  tracker Samara
#  mentor Sasha
#  mentor Jecica
#  tracker Alan
# (10 rows)

# test_user=# select * from makers order by birthdate desc;
#  mentor_id |  name  | position | birthdate  |  salary   
# -----------+--------+----------+------------+-----------
#          7 | Samara | tracker  | 2004-08-11 |   2843349
#          4 | Argen  | mentor   | 2004-08-07 | 100000000
#          3 | Josh   | mentor   | 2004-08-02 |     10000
#         10 | Alan   | tracker  | 2001-04-16 |      6000
#          9 | Jecica | mentor   | 2001-01-12 |     50000
#          8 | Sasha  | mentor   | 2000-08-23 |    222221
#          1 | Alice  | mentor   | 1996-04-09 |      6000
#          2 | Anton  | tracker  | 1990-04-03 |      3000
#          6 | Alex   | mentor   | 1989-06-11 |     20000
#          5 | Anton  | tracker  | 1890-04-29 |      2999
# (10 rows)

# test_user=# select * from makers order by birthdate;
#  mentor_id |  name  | position | birthdate  |  salary   
# -----------+--------+----------+------------+-----------
#          5 | Anton  | tracker  | 1890-04-29 |      2999
#          6 | Alex   | mentor   | 1989-06-11 |     20000
#          2 | Anton  | tracker  | 1990-04-03 |      3000
#          1 | Alice  | mentor   | 1996-04-09 |      6000
#          8 | Sasha  | mentor   | 2000-08-23 |    222221
#          9 | Jecica | mentor   | 2001-01-12 |     50000
#         10 | Alan   | tracker  | 2001-04-16 |      6000
#          3 | Josh   | mentor   | 2004-08-02 |     10000
#          4 | Argen  | mentor   | 2004-08-07 | 100000000
#          7 | Samara | tracker  | 2004-08-11 |   2843349
# (10 rows)

# test_user=# select * from makers where (position = 'mentor' or position = 'tracker') and (name like 'A%' or name like 'S%');
#  mentor_id |  name  | position | birthdate  |  salary   
# -----------+--------+----------+------------+-----------
#          1 | Alice  | mentor   | 1996-04-09 |      6000
#          2 | Anton  | tracker  | 1990-04-03 |      3000
#          4 | Argen  | mentor   | 2004-08-07 | 100000000
#          5 | Anton  | tracker  | 1890-04-29 |      2999
#          6 | Alex   | mentor   | 1989-06-11 |     20000
#          7 | Samara | tracker  | 2004-08-11 |   2843349
#          8 | Sasha  | mentor   | 2000-08-23 |    222221
#         10 | Alan   | tracker  | 2001-04-16 |      6000
# (8 rows)

# test_user=# SELECT * FROM makers WHERE salary between 5000 and 8000;
#  mentor_id | name  | position | birthdate  | salary 
# -----------+-------+----------+------------+--------
#          1 | Alice | mentor   | 1996-04-09 |   6000
#         10 | Alan  | tracker  | 2001-04-16 |   6000
# (2 rows)

# test_user=# select * from makers order by salary desc;
#  mentor_id |  name  | position | birthdate  |  salary   
# -----------+--------+----------+------------+-----------
#          4 | Argen  | mentor   | 2004-08-07 | 100000000
#          7 | Samara | tracker  | 2004-08-11 |   2843349
#          8 | Sasha  | mentor   | 2000-08-23 |    222221
#          9 | Jecica | mentor   | 2001-01-12 |     50000
#          6 | Alex   | mentor   | 1989-06-11 |     20000
#          3 | Josh   | mentor   | 2004-08-02 |     10000
#         10 | Alan   | tracker  | 2001-04-16 |      6000
#          1 | Alice  | mentor   | 1996-04-09 |      6000
#          2 | Anton  | tracker  | 1990-04-03 |      3000
#          5 | Anton  | tracker  | 1890-04-29 |      2999
# (10 rows)

# test_user=# select * from makers order by salary desc fetch first (3) row only;
#  mentor_id |  name  | position | birthdate  |  salary   
# -----------+--------+----------+------------+-----------
#          4 | Argen  | mentor   | 2004-08-07 | 100000000
#          7 | Samara | tracker  | 2004-08-11 |   2843349
#          8 | Sasha  | mentor   | 2000-08-23 |    222221
# (3 rows)

# test_user=# select position, count(mentor_id) from makers group by position;
#  position | count 
# ----------+-------
#  tracker  |     4
#  mentor   |     6
# (2 rows)

# test_user=# select avg(salary) from makers where position = 'mentor'; 
#           avg          
# -----------------------
#  16718036.833333333333
# (1 row)

# test_user=# select name, length(name) as len from makers order by len ;
#   name  | len 
# --------+-----
#  Alan   |   4
#  Josh   |   4
#  Alex   |   4
#  Anton  |   5
#  Anton  |   5
#  Alice  |   5
#  Argen  |   5
#  Sasha  |   5
#  Samara |   6
#  Jecica |   6
# (10 rows)

# test_user=# select * from makers;
#  mentor_id |  name  | position | birthdate  |  salary   
# -----------+--------+----------+------------+-----------
#          1 | Alice  | mentor   | 1996-04-09 |      6000
#          2 | Anton  | tracker  | 1990-04-03 |      3000
#          3 | Josh   | mentor   | 2004-08-02 |     10000
#          4 | Argen  | mentor   | 2004-08-07 | 100000000
#          5 | Anton  | tracker  | 1890-04-29 |      2999
#          6 | Alex   | mentor   | 1989-06-11 |     20000
#          7 | Samara | tracker  | 2004-08-11 |   2843349
#          8 | Sasha  | mentor   | 2000-08-23 |    222221
#          9 | Jecica | mentor   | 2001-01-12 |     50000
#         10 | Alan   | tracker  | 2001-04-16 |      6000
# (10 rows)

# test_user=# update makers set salary = 10000 where mentor_id = 10; 
# UPDATE 1
# test_user=# select * from makers;
#  mentor_id |  name  | position | birthdate  |  salary   
# -----------+--------+----------+------------+-----------
#          1 | Alice  | mentor   | 1996-04-09 |      6000
#          2 | Anton  | tracker  | 1990-04-03 |      3000
#          3 | Josh   | mentor   | 2004-08-02 |     10000
#          4 | Argen  | mentor   | 2004-08-07 | 100000000
#          5 | Anton  | tracker  | 1890-04-29 |      2999
#          6 | Alex   | mentor   | 1989-06-11 |     20000
#          7 | Samara | tracker  | 2004-08-11 |   2843349
#          8 | Sasha  | mentor   | 2000-08-23 |    222221
#          9 | Jecica | mentor   | 2001-01-12 |     50000
#         10 | Alan   | tracker  | 2001-04-16 |     10000
# (10 rows)

# test_user=# delete from makers where mentor_id = 3;
# DELETE 1
# test_user=# select * from makers;
#  mentor_id |  name  | position | birthdate  |  salary   
# -----------+--------+----------+------------+-----------
#          1 | Alice  | mentor   | 1996-04-09 |      6000
#          2 | Anton  | tracker  | 1990-04-03 |      3000
#          4 | Argen  | mentor   | 2004-08-07 | 100000000
#          5 | Anton  | tracker  | 1890-04-29 |      2999
#          6 | Alex   | mentor   | 1989-06-11 |     20000
#          7 | Samara | tracker  | 2004-08-11 |   2843349
#          8 | Sasha  | mentor   | 2000-08-23 |    222221
#          9 | Jecica | mentor   | 2001-01-12 |     50000
#         10 | Alan   | tracker  | 2001-04-16 |     10000
# (9 rows)

# test_user=# alter table makers drop salary;
# ALTER TABLE
# test_user=# select * from makers;
#  mentor_id |  name  | position | birthdate  
# -----------+--------+----------+------------
#          1 | Alice  | mentor   | 1996-04-09
#          2 | Anton  | tracker  | 1990-04-03
#          4 | Argen  | mentor   | 2004-08-07
#          5 | Anton  | tracker  | 1890-04-29
#          6 | Alex   | mentor   | 1989-06-11
#          7 | Samara | tracker  | 2004-08-11
#          8 | Sasha  | mentor   | 2000-08-23
#          9 | Jecica | mentor   | 2001-01-12
#         10 | Alan   | tracker  | 2001-04-16
# (9 rows)

# test_user=# alter table makers rename column birthdate to date;
# ALTER TABLE
# test_user=# select * from makers;
#  mentor_id |  name  | position |    date    
# -----------+--------+----------+------------
#          1 | Alice  | mentor   | 1996-04-09
#          2 | Anton  | tracker  | 1990-04-03
#          4 | Argen  | mentor   | 2004-08-07
#          5 | Anton  | tracker  | 1890-04-29
#          6 | Alex   | mentor   | 1989-06-11
#          7 | Samara | tracker  | 2004-08-11
#          8 | Sasha  | mentor   | 2000-08-23
#          9 | Jecica | mentor   | 2001-01-12
#         10 | Alan   | tracker  | 2001-04-16
# (9 rows)