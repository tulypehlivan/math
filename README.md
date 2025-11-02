# math
math Al+ random forest ML

# 🚀 Math Adventures — AI-Powered Adaptive Learning Prototype

## Project Overview
This project presents a minimal adaptive math learning prototype built upon the principles of Adaptive Learning (AL). The core objective is to dynamically adjust puzzle difficulty based on user performance (accuracy and response time) to maintain the learner within their optimal **Challenge Zone**.

The prototype uses **Rule-Based Logic** for its adaptive engine, aligning with the core requirements of the assignment. 

### 🎯 Core Features
* **3 Difficulty Levels:** Easy (0), Medium (1), Hard (2).
* **Adaptive Engine:** Automatically determines the next difficulty based on two key metrics: **Streak** (Mastery) and **Time-to-Answer** (Fluency).
* **Performance Tracking:** Logs metrics for every attempt, including correctness, time taken, and the active difficulty level.
* **Progress Summary:** Displays end-of-session statistics (accuracy, average time).

---

## 🏗️ Project Architecture (Core Components)

The project adheres to the recommended modular structure:

| File | Component Name | Responsibility |
| :--- | :--- | :--- |
| `puzzle_generator.py` | Puzzle Generator | Creates dynamic math problems based on the current difficulty level. |
| `tracker.py` | Performance Tracker | Logs all metrics (correctness, time, difficulty) for session history. |
| `adaptive_engine.py`| Adaptive Engine | Implements **Rule-Based Logic** to decide the optimal next difficulty. |
| `main.py` | Main Driver & Summary | Manages the session flow, handles user input, and displays the final report. |

---

## 🛠️ Setup and Execution

The prototype utilizes only standard Python libraries, requiring no external packages.

### Requirements
* Python 3.x

### Steps

1.  **Clone the Repository:**
    ```bash
    git clone [INSERT YOUR GITHUB REPO URL HERE]
    cd math-adaptive-prototype/
    ```

2.  **Run the Prototype:**
    Navigate into the `src` directory and execute the main driver file.

    ```bash
    cd src
    python main.py
    ```

### Example Flow
1.  The system prompts for your name and initial difficulty (0, 1, or 2).
2.  The program cycles through 10 puzzles, automatically adjusting the difficulty level based on your performance.
3.  A session summary is displayed at the end.

---

## 🧠 Adaptive Logic Summary (The Core Value - 60% Weight)

The adaptation relies on a strategic rule set implemented in the **`adaptive_engine.py`**. The system assesses not just accuracy, but also **fluency**, which is crucial for mastering fundamental skills.

| Rule | Condition | Outcome |
| :--- | :--- | :--- |
| **Mastery & Fluency** | **3 Consecutive Corrects** **AND** Time $\le$ Time Threshold | **Increase Difficulty** (The Flow Zone) |
| **Struggling** | **Incorrect Answer** | **Decrease Difficulty** |
| **Slow Mastery** | **3 Consecutive Corrects** **BUT** Time $>$ Time Threshold | **Stay at Current Level** (Practice for Automaticity) |
