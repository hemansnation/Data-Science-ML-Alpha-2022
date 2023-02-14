SHOW databases;

create database alpha;

show databases;

use alpha;

create table students(
	id int,
    firstname varchar(20),
    lastname varchar(20),
    phonenumber varchar(10)
);

show tables;

desc students;

select * from students;

insert into students
(id, firstname, lastname, phonenumber) 
values (1,'Abhinav', 'jain', '12345678');

select * from students;

insert into students
(id, firstname, lastname, phonenumber) 
values 
(2,'Avi', 'jain', '987654'),
(3,'Rishabh', 'rathore', '9876543'),
(4,'Ravi', 'Sharma', '987654'),
(5,'Abhinav', 'jain', '567887')
;

select * from students;

show tables;

select * from homeprices;