-- phpMyAdmin SQL Dump
-- version 5.2.2
-- https://www.phpmyadmin.net/
--
-- Host: 172.18.0.2
-- Generation Time: Mar 31, 2025 at 03:50 PM
-- Server version: 9.2.0
-- PHP Version: 8.2.27

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `student_management_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `grades`
--

CREATE TABLE `grades` (
  `id` int NOT NULL,
  `student_id` varchar(10) DEFAULT NULL,
  `module_name` varchar(100) DEFAULT NULL,
  `module_grade` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `grades`
--

INSERT INTO `grades` (`id`, `student_id`, `module_name`, `module_grade`) VALUES
(68, 'STU001', 'Algebra', 45),
(69, 'STU001', 'Calculus', 50),
(70, 'STU001', 'Geometry', 55),
(71, 'STU002', 'Physics I', 65),
(72, 'STU002', 'Mechanics', 62),
(73, 'STU002', 'Electromagnetism', 58),
(74, 'STU003', 'Organic Chemistry', 72),
(75, 'STU003', 'Inorganic Chemistry', 80),
(76, 'STU003', 'Physical Chemistry', 85),
(77, 'STU004', 'Biology I', 39),
(78, 'STU004', 'Anatomy', 42),
(79, 'STU004', 'Microbiology', 37),
(80, 'STU005', 'Linear Algebra', 78),
(81, 'STU005', 'Calculus II', 74),
(82, 'STU006', 'Quantum Mechanics', 60),
(83, 'STU006', 'Classical Mechanics', 65),
(84, 'STU006', 'Optics', 55),
(85, 'STU007', 'Biochemistry', 50),
(86, 'STU007', 'Genetics', 45),
(87, 'STU007', 'Physiology', 52),
(88, 'STU008', 'Chemistry Lab', 85),
(89, 'STU008', 'Chemical Thermodynamics', 78),
(90, 'STU009', 'Number Theory', 40),
(91, 'STU009', 'Statistics', 42),
(92, 'STU010', 'Physics II', 55),
(93, 'STU010', 'Electronics', 48),
(94, 'STU011', 'Ecology', 66),
(95, 'STU011', 'Botany', 60),
(96, 'STU012', 'Chemistry Lab II', 81),
(97, 'STU012', 'Physical Chemistry II', 79),
(98, 'STU013', 'Physics Lab', 38),
(99, 'STU013', 'Thermodynamics', 42),
(100, 'STU014', 'Cell Biology', 62),
(101, 'STU014', 'Immunology', 64),
(102, 'STU015', 'Discrete Mathematics', 72),
(103, 'STU015', 'Algebra II', 75),
(104, 'STU016', 'Thermodynamics', NULL),
(105, 'STU017', 'Microbiology', NULL),
(106, 'STU018', 'Physics Lab', NULL),
(107, 'STU019', 'Biology Lab', NULL),
(108, 'STU020', 'Chemistry Lab', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `students`
--

CREATE TABLE `students` (
  `id` int NOT NULL,
  `student_id` varchar(10) NOT NULL,
  `first_name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `dob` date NOT NULL,
  `email` varchar(100) DEFAULT NULL,
  `course_enrolled` varchar(100) DEFAULT NULL,
  `year_of_study` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `students`
--

INSERT INTO `students` (`id`, `student_id`, `first_name`, `last_name`, `dob`, `email`, `course_enrolled`, `year_of_study`) VALUES
(23, 'STU001', 'Alice', 'Johnson', '2002-05-15', 'alice.johnson@example.com', 'Mathematics', 2),
(24, 'STU002', 'Bob', 'Smith', '2001-08-23', 'bob.smith@example.com', 'Physics', 1),
(25, 'STU003', 'Charlie', 'Brown', '2003-01-10', 'charlie.brown@example.com', 'Chemistry', 3),
(26, 'STU004', 'David', 'Wilson', '2001-11-30', 'david.wilson@example.com', 'Biology', 2),
(27, 'STU005', 'Eve', 'Davis', '2002-04-20', 'eve.davis@example.com', 'Mathematics', 1),
(28, 'STU006', 'Frank', 'Miller', '2003-09-05', 'frank.miller@example.com', 'Physics', 3),
(29, 'STU007', 'Grace', 'Lee', '2002-07-12', 'grace.lee@example.com', 'Biology', 2),
(30, 'STU008', 'Hank', 'Kim', '2000-12-01', 'hank.kim@example.com', 'Chemistry', 4),
(31, 'STU009', 'Ivy', 'Wong', '2001-02-17', 'ivy.wong@example.com', 'Mathematics', 3),
(32, 'STU010', 'Jake', 'Li', '2002-11-11', 'jake.li@example.com', 'Physics', 2),
(33, 'STU011', 'Karen', 'White', '2003-06-25', 'karen.white@example.com', 'Biology', 1),
(34, 'STU012', 'Leo', 'Green', '2002-03-14', 'leo.green@example.com', 'Chemistry', 3),
(35, 'STU013', 'Mia', 'Black', '2001-05-30', 'mia.black@example.com', 'Physics', 4),
(36, 'STU014', 'Nina', 'Clark', '2003-09-20', 'nina.clark@example.com', 'Biology', 2),
(37, 'STU015', 'Omar', 'Adams', '2000-10-05', 'omar.adams@example.com', 'Mathematics', 4),
(38, 'STU016', 'Paula', 'Lopez', '2001-01-23', 'paula.lopez@example.com', 'Physics', 3),
(39, 'STU017', 'Quinn', 'Scott', '2003-12-18', 'quinn.scott@example.com', 'Biology', 1),
(40, 'STU018', 'Rita', 'Perez', '2002-04-08', 'rita.perez@example.com', 'Chemistry', 2),
(41, 'STU019', 'Sam', 'Turner', '2001-08-15', 'sam.turner@example.com', 'Physics', 3),
(42, 'STU020', 'Tina', 'Nguyen', '2000-11-22', 'tina.nguyen@example.com', 'Biology', 4);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `grades`
--
ALTER TABLE `grades`
  ADD PRIMARY KEY (`id`),
  ADD KEY `student_id` (`student_id`);

--
-- Indexes for table `students`
--
ALTER TABLE `students`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `student_id` (`student_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `grades`
--
ALTER TABLE `grades`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=113;

--
-- AUTO_INCREMENT for table `students`
--
ALTER TABLE `students`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=44;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `grades`
--
ALTER TABLE `grades`
  ADD CONSTRAINT `grades_ibfk_1` FOREIGN KEY (`student_id`) REFERENCES `students` (`student_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
