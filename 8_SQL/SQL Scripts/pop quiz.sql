USE advance;
-- Students
CREATE TABLE Students
(StudentId INT, StudentName VARCHAR(10));
INSERT INTO Students (StudentId, StudentName)
SELECT 1,'John'
UNION ALL
SELECT 2,'Matt'
UNION ALL
SELECT 3,'James';

-- Classes
CREATE TABLE Classes
(ClassId INT, ClassName VARCHAR(10));
INSERT INTO Classes (ClassId, ClassName)
SELECT 1,'Maths'
UNION ALL
SELECT 2,'Arts'
UNION ALL
SELECT 3,'History';

-- StudentClass
CREATE TABLE StudentClass
(StudentId INT, ClassId INT);
INSERT INTO StudentClass (StudentId, ClassId)
SELECT 1,1
UNION ALL
SELECT 1,2
UNION ALL
SELECT 3,1
UNION ALL
SELECT 3,2
UNION ALL
SELECT 3,3;

-- Select data
SELECT *
FROM Students;
SELECT *
FROM Classes;
SELECT *
FROM StudentClass;

/* Question 1:  What will be the best possible join if we want to retrieve 
all the students who have signed up for the classes in the summer? */
select st.StudentName, cl.ClassName
from StudentClass sc
inner join Classes cl ON cl.ClassID = sc.ClassID
inner join Students st ON st.StudentID = sc.StudentID;

/* Question 2:  What will be the best possible join if we want to retrieve 
all the students who have signed up for no classes in summer? */
select st.StudentName, cl.ClassName
from students st
left join StudentClass sc ON st.StudentId = sc.StudentId
left join Classes cl ON cl.ClassID = sc.ClassID
where cl.ClassName IS NULL;

select st.StudentName
from students st
left join StudentClass sc ON st.StudentId = sc.StudentId
where sc.ClassID IS NULL;

-- Clean up
DROP TABLE Students;
DROP TABLE Classes;
DROP TABLE StudentClass;




