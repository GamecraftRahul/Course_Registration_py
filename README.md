# 🎓 Course Management System

A modern desktop-based **Course Management System** developed using **Python**, **CustomTkinter**, and **MySQL**. This application provides an efficient way to manage courses, teachers, and students through a user-friendly graphical interface.

---

## 🚀 Features

### 📚 Subject Management
- Add new subjects
- Edit existing subjects
- Delete subjects
- View all available subjects

### 👨‍🏫 Teacher Management
- Add teachers
- Assign teachers to subjects
- Edit teacher information
- Delete teacher records
- Search teachers by subject

### 👨‍🎓 Student Management
- Add students
- Assign students to subjects
- Edit student information
- Delete student records
- Search students by subject

### 📊 Dashboard
- Total number of subjects
- Total number of teachers
- Total number of students
- Real-time statistics updates

### 🎨 Modern User Interface
- Built with CustomTkinter
- Dark mode support
- Tab-based navigation
- Clean and responsive layout

---

# 🛠️ Technologies Used

| Technology | Purpose |
|------------|----------|
| Python | Core Programming Language |
| CustomTkinter | Modern GUI Framework |
| Tkinter | GUI Components |
| MySQL | Database Management |
| mysql-connector-python | Database Connectivity |

---

# 📂 Project Structure

```text
Course-Management-System/
│
├── course_registration_sys.py
├── course_registration_sys_DB.sql
├── README.md
│
└── Database
    ├── subjects
    ├── teachers
    └── students
```

---

# ⚙️ Database Setup

## Step 1: Create Database

```sql
CREATE DATABASE course_management;
```

## Step 2: Select Database

```sql
USE course_management;
```

## Step 3: Import SQL File

Import the provided SQL file:

```text
course regitration sys DB.sql
```

using MySQL Workbench or any MySQL client.

---

# 🔧 Installation

## Clone Repository

```bash
git clone https://github.com/your-username/course-management-system.git
cd course-management-system
```

## Install Required Packages

```bash
pip install customtkinter mysql-connector-python
```

---

# 🗄️ Configure Database

Open the Python file and update database credentials:

```python
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YOUR_PASSWORD",
    database="course_management"
)
```

---

# ▶️ Run Application

```bash
python course_registration_sys.py
```

---

# 📚 Subject Module

Manage all subjects offered by the institution.

### Functions
- Add Subject
- Edit Subject
- Delete Subject
- View Subject List

---

# 👨‍🏫 Teacher Module

Manage teachers and their assigned subjects.

### Functions
- Add Teacher
- Assign Subject
- Edit Teacher Information
- Delete Teacher
- Search Teachers by Subject

---

# 👨‍🎓 Student Module

Manage students and their enrolled subjects.

### Functions
- Add Student
- Assign Subject
- Edit Student Information
- Delete Student
- Search Students by Subject

---

# 📊 Dashboard Analytics

The dashboard automatically displays:

```text
Total Subjects
Total Teachers
Total Students
```

Statistics are updated instantly whenever records are added, modified, or deleted.

---

# 🔍 Search Functionality

Search and filter:

- Teachers by Subject
- Students by Subject

This helps quickly locate records within large datasets.

---

# 🔐 Database Relationships

```text
Subjects
    │
    ├── Teachers
    │
    └── Students
```

Each Teacher and Student is linked to a Subject using a Foreign Key relationship.

---

# 🎯 Future Enhancements

- Student Login System
- Teacher Login System
- Attendance Management
- Course Enrollment Module
- Marks Management
- Examination System
- PDF Report Generation
- Export to Excel
- User Authentication
- Cloud Database Integration

---

# 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to GitHub
5. Open a Pull Request

---

# 📜 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

Developed using Python, CustomTkinter, and MySQL to simplify course, teacher, and student management.

⭐ If you found this project useful, consider giving it a star on GitHub.
