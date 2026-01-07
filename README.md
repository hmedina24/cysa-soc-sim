# cysa-soc-sim

# CySA+ SOC-Sim: AI-Driven Security Analyst Trainer

## 🛠 Tech Stack
* **Language:** Python 3.10+
* **AI Orchestration:** Google Gemini API (or OpenAI)
* **Database:** SQLite (via SQLAlchemy) for persistent player state
* **Security Frameworks:** CompTIA CySA+ (CS0-003) Exam Objectives, MITRE ATT&CK
* **Environment:** Python-dotenv for secure API management

---

## 📖 Description & Overview
**CySA+ SOC-Sim** is an interactive, gamified learning agent designed to prepare cybersecurity professionals for the CompTIA CySA+ certification. Unlike static practice exams, this tool uses a Large Language Model (LLM) to act as a **Senior SOC Lead**, generating dynamic, real-world scenarios across three difficulty tiers.

The agent focuses on the four core domains of the CS0-003 exam:
1.  **Security Operations:** 33%
2.  **Vulnerability Management:** 30%
3.  **Incident Response:** 20%
4.  **Reporting & Communication:** 17%

The project bridges the gap between theoretical knowledge and hands-on analysis by forcing users to interpret raw logs and justify their defense strategies in a simulated "SOC environment."

---

## 🗂 Table of Contents
1. [Tech Stack](#-tech-stack)
2. [Project Overview](#-description--overview)
3. [Architecture & Levels](#-architecture--levels)
4. [Installation & Usage](#-usage)
5. [Roadmap & Timeline](#-project-timeline)
6. [Credits](#-creditsauthor)

---

## 🕹 Architecture & Levels
The simulation is structured into three progressive difficulty tiers:
* **Level 1 (Triage Analyst):** Focuses on Multiple Choice Questions (MCQs) to build foundational vocabulary.
* **Level 2 (Responder):** Requires the user to analyze raw log snippets and identify Indicators of Compromise (IoCs) via string input.
* **Level 3 (Threat Hunter):** Complex, multi-stage breach scenarios requiring containment strategy explanations.

The engine uses a **Weighted Randomizer** to ensure questions are distributed according to the actual CompTIA exam domain weights.

---

## 🚀 Usage
1. **Clone the repo:**
   `git clone https://github.com/yourusername/cysa-soc-sim.git`
2. **Install dependencies:**
   `pip install -r requirements.txt`
3. **Set up environment variables:**
   Create a `.env` file and add your API key:
   `API_KEY=your_llm_api_key_here`
4. **Run the Simulation:**
   `python main.py`

---

## ⏳ Project Timeline
* **Phase 1 (Week 1):** Repository setup, SQLite schema design, and LLM API integration.
* **Phase 2 (Week 2):** Development of Level 1 (MCQ) logic and weighted domain randomizer.
* **Phase 3 (Week 3):** Implementation of Level 2 & 3 (Log analysis and scenario-based PBQs).
* **Phase 4 (Week 4):** Testing, prompt refinement, and final documentation for portfolio display.

---

## ✍️ Credits/Author
* **Developer:** Hector Medina 
* **Role:** Cybersecurity Student & Software Engineer
