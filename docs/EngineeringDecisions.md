## Engineering Decisions

### Decision 1

Decision:
Project will follow the Software Development Life Cycle (SDLC) instead of being developed as a tutorial project.

Reason:
The goal is to learn professional software engineering practices while building a production-quality AI application.

Status:
Accepted

### Decision 2

Decision:
We will use Git from the very beginning of the project.

Reason:
Version control should track the entire software development lifecycle, including documentation, planning, code, testing, and deployment—not just source code. This preserves the complete history of the project from its inception.

Status:
Accepted

### Decision 3

Decision:
The project will establish a complete and reproducible development environment before application development begins.

Reason:
A properly configured development environment ensures consistency, reproducibility, and a stable foundation for future development. Setting up version control, the virtual environment, and project dependencies first reduces integration issues and allows future sprints to focus entirely on building features.

Status:
Accepted

### Decision 4

The project will use a dedicated Python virtual environment (`venv`) and a `requirements.txt` file for dependency management.

Reason:
Every contributor should work with the same Python dependencies without affecting the system-wide Python installation.

Status:
Accepted
