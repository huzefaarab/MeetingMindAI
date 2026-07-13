# Software Requirements Specification (SRS)

# MeetingMind AI

---

## 1. Project Overview

MeetingMind AI is an AI-powered meeting memory assistant designed to help users retrieve important information from meeting transcripts using natural language questions.

The application stores meeting knowledge and allows users to quickly recall discussions without manually reading lengthy transcripts.

---

## 2. Problem Statement

People frequently forget important discussions after meetings.

Important information such as:

- Assigned tasks
- Deadlines
- Decisions
- Responsibilities
- Technical discussions

often gets buried inside long meeting transcripts, making it difficult and time-consuming to retrieve later.

---

## 3. Proposed Solution

MeetingMind AI allows users to upload meeting transcripts.

The system processes and stores the transcript and later answers user questions using only the uploaded meeting content.

Instead of searching manually, users simply ask questions such as:

- Who was assigned the backend?
- What deadline was decided?
- What did we decide about authentication?

---

## 4. Target Users

- Students
- Software Development Teams
- Project Managers
- Startup Teams
- Business Teams

---

## 5. Objectives

The objective of MeetingMind AI is to reduce the effort required to remember information discussed during meetings.

The system should allow users to retrieve meeting information quickly using natural language.

---

## 6. Functional Requirements

Version 1 should allow users to:

- Upload meeting transcripts
- Store transcript information
- Ask questions about the meeting
- Retrieve accurate answers from the transcript

---

## 7. Non-Functional Requirements

The system should:

- Provide accurate answers
- Respond within a reasonable time
- Be easy to use
- Be modular and scalable
- Maintain transcript integrity

---

## 8. Scope

Included in Version 1:

- Transcript upload
- AI Question Answering
- Meeting memory retrieval

---

## 9. Out of Scope

Version 1 will NOT include:

- Live meeting participation
- Speech-to-text
- Zoom/Google Meet integration
- Calendar integration
- Email reminders

---

## 10. Future Scope

Possible future improvements include:

- Live meeting assistant
- Real-time transcription
- Action item extraction
- Deadline extraction
- Meeting summaries
- Calendar integration
- Multi-meeting memory
- Agentic AI features

## Technology Stack (Version 1)

| Component | Technology |
|-----------|------------|
| Programming Language | Python 3.13 |
| User Interface | Streamlit |
| Large Language Model | Google Gemini |
| Version Control | Git |
| Remote Repository | GitHub |
| Python Environment | venv |
| Package Manager | pip |