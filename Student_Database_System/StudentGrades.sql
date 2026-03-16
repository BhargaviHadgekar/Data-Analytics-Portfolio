/*
CREATE DATABASE StudentGrades;
GO

USE StudentGrades;
GO


-- Students Table
CREATE TABLE Students (
    student_id INT IDENTITY(1,1) PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL
);

-- Courses Table
CREATE TABLE Courses (
    course_id INT IDENTITY(1,1) PRIMARY KEY,
    course_name VARCHAR(50) UNIQUE NOT NULL
);

-- Grades Table
CREATE TABLE Grades (
    grade_id INT IDENTITY(1,1) PRIMARY KEY,
    student_id INT,
    course_id INT,
    grade FLOAT CHECK (grade BETWEEN 0 AND 100),
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (course_id) REFERENCES Courses(course_id)
);


INSERT INTO Courses (course_name) VALUES
('Python'),
('Java'),
('C++'),
('MySQL');



INSERT INTO Students (name, email) VALUES
('Ishita', 'ishita@gmail.com'),
('Manav', 'manav@gmail.com'),
('Tanya', 'tanya@gmail.com');



INSERT INTO Grades (student_id, course_id, grade) VALUES
(1, 1, 88),  -- Ishita - Python
(1, 2, 91),  -- Ishita - Java
(2, 4, 76),  -- Manav - MySQL
(3, 2, 95);  -- Tanya - Java
(2, 1, 84),  -- Manav - Python
(3, 3, 90),  -- Tanya - C++
(1, 4, 89),  -- Ishita - MySQL
(2, 2, 78),  -- Manav - Java
(3, 1, 92);  -- Tanya - Python



SELECT * FROM Students;
SELECT * FROM Courses;
SELECT * FROM Grades;
*/

SELECT s.name, c.course_name, g.grade
FROM Grades g
JOIN Students s ON g.student_id = s.student_id
JOIN Courses c ON g.course_id = c.course_id;



