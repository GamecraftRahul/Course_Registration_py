-- Create database
CREATE DATABASE course_management;

USE course_management;

-- Table for subjects
CREATE TABLE subjects (
    subject_id INT AUTO_INCREMENT PRIMARY KEY,
    subject_name VARCHAR(100) NOT NULL
);

-- Table for teachers
CREATE TABLE teachers (
    teacher_id INT AUTO_INCREMENT PRIMARY KEY,
    teacher_name VARCHAR(100) NOT NULL,
    subject_id INT,
    FOREIGN KEY (subject_id) REFERENCES subjects(subject_id)
);

-- Table for students
CREATE TABLE students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    student_name VARCHAR(100) NOT NULL,
    subject_id INT,
    FOREIGN KEY (subject_id) REFERENCES subjects(subject_id)
);

-- Sample subjects
INSERT INTO subjects (subject_name) VALUES 
('Mathematics'), 
('Physics'), 
('Chemistry'), 
('Biology'), 
('English');

-- Sample teachers
INSERT INTO teachers (teacher_name, subject_id) VALUES
('Alice Johnson', 1),
('Bob Smith', 2),
('Carol Lee', 3),
('David Brown', 4),
('Eva White', 5);

-- Sample students
INSERT INTO students (student_name, subject_id) VALUES
('John Doe', 1),
('Jane Doe', 2),
('Mike Ross', 3),
('Rachel Zane', 4),
('Harvey Specter', 5),
('Louis Litt', 1),
('Donna Paulsen', 2),
('Jessica Pearson', 3),
('Katrina Bennett', 4),
('Samantha Wheeler', 5);
