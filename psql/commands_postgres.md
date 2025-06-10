# # commands: // directly from pratham@pratham-HP-EliteBook-840-G3:~$ 

# create database:
createdb test
#delete db:
deletedb test
# check database list:
psql #space #tab
# connect to database:
psql test

# show list of databases: \l
# quit/exit: \q
# show list of existing roles in db: \du
# show content of the table: \dl  -  large object table
# switch working database: \c
# display all the tables of the current db: \d or \dt
# help for syntax of Sql commands: \h -  * for all commands
# view table names: \dp


# CREATE TABLE:
CREATE TABLE table-name(
id int,
name varchar(100),
city varchar(100));
// creates table into the database your in 

# adding data in Table
insert into table-name( column1-name, column2-name, column3-name) values (value1, value2, value3)
eg: insert into person values (101,'Rahul','Delhi')
eg: insert into person(id,name,city) values (101,'Raju','Delhi')

# reading data table:
select * from table-name
// * means all 
# to view only a single/multiple/specific column:
select column1-name, column2-name from person

# update data table:
update table-name set column-name = 'New value' where column-name = 'value'
# multiple values:
update table-name set column1='value1' , column2='value2' where condition
eg: update person set city='London' where id=2 
// where is called clause/position.

# alter table - add new column
ALTER TABLE table_name ADD COLUMN column_name data_type;
# alter table-modify column:
ALTER TABLE table_name ALTER COLUMN column_name SET DATA TYPE new_data_type;
# alter table- rename column:
ALTER TABLE table_name RENAME COLUMN old_column_name TO new_column_name;
# alter table- rename table :
ALTER TABLE old_table_name RENAME TO new_table_name;
# alter table- drop column:
ALTER TABLE table_name DROP COLUMN column_name;
# alter table- set and remove default values for a table:
set- ALTER TABLE table_name ALTER COLUMN column_name SET DEFAULT default_value;
remove- ALTER TABLE table_name ALTER COLUMN column_name DROP DEFAULT;
# alter table- set and remove a column to NOT NULL:
set- ALTER TABLE table_name ALTER COLUMN column_name SET NOT NULL;
remove- ALTER TABLE table_name ALTER COLUMN column_name DROP NOT NULL;

# delete data row from table:
delete from table-name where condition/identification(id=4);
delete from table-name where condition1 and condition2;
# delete all rows from table :
delete from table-name;
# delete using IN clause:
DELETE FROM table_name WHERE column_name IN (value1, value2, ...);

# Create Schema: (used to partition a single table into 2 diff tables under same name.
list all schema- SELECT schema_name FROM information_schema.schemata;
access schema- schema_name.object_Name
alter schema schema_name rename to new_schema_name;
create schema- CREATE SCHEMA schema_name;
create table in a schema- CREATE TABLE schema_name.table_name ( 
    column1 datatype PRIMARY KEY, column2 datatype NOT NULL, column3 datatype );
create a view in schema- CREATE VIEW schema_name.view_name AS SELECT column1, column2 FROM schema_name.table_name WHERE condition;
dropa schema- DROP SCHEMA schema_name; (add CASCADE at the end to drop schema and all its objects and RESTRICT to ensure schema is only dropped when it is empty)

# group by:
basic- SELECT column_name, aggregate_function(column_name) FROM table_name GROUP BY column_name;
multiple- SELECT column1, column2, aggregate_function(column3) FROM table_name GROUP BY column1, column2;

# group by + order by: kinda sorting
SELECT department, COUNT(*) 
FROM employees 
GROUP BY department 
ORDER BY COUNT(*) DESC;

# order by: (exactly sorting.)
basic- SELECT column_name FROM table_name ORDER BY column_name [ASC|DESC];
sort in sort- SELECT name, department, salary FROM employees  ORDER BY department ASC, salary DESC;
// (Sorts by department in ascending order, then by salary in descending order within each department.)
// add- NULLS first/last to keep the null values at start or end.
first 5 or first n- SELECT name, salary FROM employees ORDER BY salary DESC LIMIT 5;
// can be edited to get highest or least n employees.
pagination or 5 after first 5- using offset:
SELECT name, salary FROM employees ORDER BY salary DESC LIMIT 5 OFFSET 5;

# having function: - unlike 'where' it works after aggregated functions
SELECT column_name, aggregate_function(column_name) FROM table_name GROUP BY column_name HAVING condition;
# where function: - unlike 'having' it works before aggregated functions
SELECT column_name,aggregate_function(column_name) FROM table_name GROUP BY column_name HAVING condition;
SELECT * FROM employees WHERE salary > 50000;

# psql operators:
1. Arithmetic Operators: + , - , * , / , %
2. Comparison Operators: = , != or <> , > , < , >= , <=
3. Logical Operators: AND , OR , NOT
4. Bitwise Operators:   // not so important
    Operator	Description	    Example
    &	        Bitwise AND	    SELECT 5 & 3; → 1
    |	        Bitwise OR      SELECT 5 | 3; → 7
    #	        Bitwise XOR	    SELECT 5 # 3; → 6
    ~	        Bitwise NOT	    SELECT ~5; → -6 // will increment and negate and give
    <<	        Left shift	    SELECT 5 << 2; → 20
    >>	        Right shift	    SELECT 5 >> 1; → 2
5. String Operators:
    Operator	    Description
    LIKE	        Pattern matching
    ILIKE	        Case-insensitive LIKE
    SIMILAR TO	    Similar to regex matching
6. Array Operators: when working on and operator
    Operator	Description
    @>	        Contains
    <@	        Contained by
    &&	        Overlaps	
7. Special Operators:
    Operator	    Description	                            Example
    IS NULL	        Checks if value is NULL	                SELECT * FROM employees WHERE salary IS NULL;
    IS NOT NULL	    Checks if value is NOT NULL	            SELECT * FROM employees WHERE salary IS NOT NULL;
    DISTINCT	    Removes duplicates	                    SELECT DISTINCT department FROM employees;
    IN	Checks      if value exists in list	                SELECT * FROM employees WHERE department IN ('HR', 'IT');
    NOT IN	        Excludes values from list	            SELECT * FROM employees WHERE department NOT IN ('HR', 'IT');
    EXISTS	        Checks if subquery returns results	    SELECT * FROM employees WHERE EXISTS (SELECT 1 FROM departments WHERE employees.department_id = departments.id);

# Conditions:
WHERE -basic
WHERE with COMPARISION / LOGICAL OPERATORS
WHERE with BETWEEN, IN, LIKE (Pattern Matching), ILIKE (Case-Insensitive Search)
WHERE with IS NULL & IS NOT NULL
HAVING
CASE
EXISTS , NOT EXISTS
ORDER BY
LIMIT
OFFSET
JOIN
WITH

# JOINS -used to join tables, usually with primary key of the first table and foreign key of the other table
    Types of joins:
    1. INNER JOIN- joins tables using common values in column. (A intersection B)
    2. LEFT JOIN- joins tables with dominance of the first/left table. if similar value not found,it will return null in the right/second table
    3. RIGHT JOIN- joins tables with dominance of the second/right table. if similar value not found,it will return null in the left/first table
    4. FULL OUTER JOIN- if no common exists it will keep the respective opposite values null for both the tables.














## CONSTRAINS - rules applied to a column - can give multiple constrains
# primary key- unique identification - not null - cannot repeat - only one primary key per table.
# not null - given after datatype at the time of creation
# default value- gives a default value to a particular column. like account type= 'Savings'
# auto_increment - key word is 'serial'.
