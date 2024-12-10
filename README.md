# HFOV_24_FlexSquad

This repository contains the code we implemented based on the highest-priority user stories identified during Sprint 1. These priorities were set collaboratively, and the user stories were translated into actionable development tasks.

On our GitHub page, under **Projects** -> **Product Backlog**, you can find a visual representation of our progress and planning.

---

## Information about Sprint 1

We implemented the following User Stories as independent functions:

- US1: As a gym member I want to be able to see available classes so i can plan what class i want to attend
- US2: As a gym member, I want to be able to attend virtual classes, so I can keep working on my health and well-being, even though I can’t physically be there
- US3: As a gym member I want more flexible subscription plans, such as one month or a single class, so that I can easily find the best subscription that suits me
- US4: As a fitness instructor I want to see how many members are attending my class so that I can be better prepared for each class
- US5: As a manager I want an overview of class attendance to understand class popularity

Initially, we interpreted that each User Story could be implemented as an independent function. During the feedback session with Shalini, we were informed that the program should run as a cohesive, integrated unit.

As a result, in **Sprint 2**, we focus on connecting all the independent functions into a unified program with a user interface (UI).

Side note: in a few places the user_id is hardcoded so the app can show the functions.

---

## Information about Sprint 2

In Sprint 2, we extended the functionality of our project by addressing the following user stories:

- US6: As a gym member I want to be able to book classes easily through platforms such as an app
- US7: As an owner I want to motivate members to attend classes to meet fitness goals by promoting motivational quotes
- US8: As a long-term gym member, I want to be rewarded for being a loyal customer to help me stay motivated on my fitness journey

Beyond implementing these new features, we integrated the previously independent functionalities from Sprint 1 into a unified, cohesive application with a user-friendly interface (UI) using [npyscreen](https://npyscreen.readthedocs.io/).

Additionally, we categorized the preparation of the final presentation as part of Sprint 2 activities.

---

## Installing Requirements

**Python version used:**

- Python 3.13

To set up the development environment, follow these steps:

1. **Create a virtual environment**:
   Run the following command to create a virtual environment in the current directory:

   ```bash
   python -m venv .venv
   ```

2. **Activate the virtual environment**:

- On macOS/Linux, use:
  ```bash
  source .venv/bin/activate
  ```
- On Windows, use:
  ```bash
  .venv\Scripts\activate
  ```

3. **Install required libraries**:
   With the virtual environment activated, run:
   ```bash
   pip install -r requirements.txt
   ```

## Run the Application

Once the requirements are installed and the virtual environment is activated, you can run the application using the following command:

```bash
python3 main.py
```
