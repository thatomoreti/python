# Task & Workflow Management API

A RESTful API built with Flask for managing tasks and workflows.  
This project demonstrates backend reliability, CRUD operations, and role-based task assignment.  
Designed with scalability and maintainability in mind, it supports both **Admins** and **Workers**.

---

## Features

### Core Functionality
- **Create Tasks**  
  - Prevent duplicates using unique `Heading` and `Task_ID`.
- **Edit Tasks**  
  - Validate existence before editing attributes.
- **Delete Tasks**  
  - Remove tasks by `Heading` or `Description`.
- **Mark Task Status**  
  - Update status: `Completed`, `Incomplete`, or `In Progress`.
- **Assign Tasks to Workers**  
  - Link tasks to specific users for accountability.

---

## Data Models

### Task
- `Task_ID` (INT, AUTO_INCREMENT, UNIQUE)  
- `Heading` (VARCHAR(100), UNIQUE, NOT NULL)  
- `Description` (VARCHAR(200))  
- `Status` (VARCHAR, default `"Incomplete"`)  
- `Type` (VARCHAR, NOT NULL)
- `Creator_id` (INT) 
- `Worker_id` (INT)

### User
- `U_ID` (INT, AUTO_INCREMENT, UNIQUE)  
- `Name` (VARCHAR(100), NOT NULL)  
- `Surname` (VARCHAR, NOT NULL)  
- `Type` (VARCHAR(10), NOT NULL)  
  - `Admin` → manages tasks  
  - `Worker` → completes tasks  

---

## Roles & Relationships

- **Admin**
  - Can create, edit, delete, assign tasks, and count task statuses.
  - Relationship: `Admin (1:N Tasks)`
- **Worker**
  - Can mark task status (complete/incomplete/in progress).
  - Relationship: `Worker (1:1 Task)`

---

## API Endpoints

| Endpoint        | Method | Description                          |
|-----------------|--------|--------------------------------------|
| `/getTask`      | GET    | Retrieve all tasks                   |
| `/task`         | POST   | Create and assign new task to a worker|
| `/delete/task/'`| DELETE | Delete a task by ID/Heading          |
| `/editTask  `   | PUT    | Edit a task                          |
| `/completeTask` | PUT    | Mark task status as completed        |
| `/user        ` | POST   | Create a user                        |

---

## Workflow

1. **Identify User Role**  
   - Admin → Manage tasks (create, edit, delete, assign).  
   - Worker → Complete tasks (mark status).  

2. **Admin Flow**  
   - Create tasks with heading, description, type.  
   - Edit tasks by heading.  
   - Delete tasks by heading.  
     

3. **Worker Flow**  
   - View assigned tasks.  
   - Mark status (`Completed`, `Incomplete`, `In Progress`).  
   - Loop until all tasks are completed.  

---

## Tech Stack
- **Backend**: Flask (Python)  
- **Database**: SQLAlchemy (SQLite/MySQL/Postgres)  
- **Auth (Future)**: JWT for secure user sessions  
- **Deployment (Future)**: DigitalOcean / Heroku  

---

## Future Improvements
- JWT authentication for secure role-based access.  
- Cloud deployment with CI/CD pipeline.  
- Frontend dashboard for task visualization.  
- Unit tests for endpoints.
- Add filtered count functionality based on task status

---

## How to Run
```bash
# Clone repo
git clone https://github.com/thatomoreti/task_manager.git
cd task_manager

# Install dependencies
pip install -r requirements.txt

# Run server
python app.py
