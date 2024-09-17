# To Do List App

## Description
This project was created as part of the selection round for the SRM ACM Student Chapter club in my college. It consists of two versions of a To-Do List application:

1. A **GUI-based version** built using Python, Tkinter, and ttkbootstrap.
2. A **Terminal-based version** that runs entirely in the command-line interface (CLI).

Both versions allow users to add, view, and manage tasks.

## Table of Contents
- [GUI Version](#gui-version)
  - [Features](#features)
  - [Installation](#installation)
  - [Usage](#usage)
- [Terminal Version](#terminal-version)
  - [Features](#features-1)
  - [Installation](#installation-1)
  - [Usage](#usage-1)
- [Known Issues](#known-issues)
- [Technologies Used](#technologies-used)
- [Future Improvements](#future-improvements)
- [Author](#author)
- [Contact](#contact)

## GUI Version
**Video Demo:**  
[![Watch the video](https://img.youtube.com/vi/LaeNEpqk-MU/hqdefault.jpg)](https://youtube.com/shorts/LaeNEpqk-MU?si=QmQNENuo0i36bH8Q)

### Features
- **Task Management**: Add, view, and delete tasks with ease.
- **Progress Tracker**: Integrated progress bar that updates based on task completion.
- **Task Saving**: Tasks are saved to a text file for persistence across sessions.
- **Cross-Platform**: The GUI version runs on Windows, macOS, and Linux.

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/kevgon8/to-do-list-app.git
    ```
2. Navigate into the project directory:

    ```bash
    cd to-do-list-app
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```
### Usage
To run the GUI-based To-Do List app:
```bash
    python todo_gui.py
```

1. **Add Tasks**: Type tasks in the text field and click "Add" to add them to the task list.
2. **View and Manage Tasks**: Use the "View tasks" tab to mark tasks as complete or clear all tasks.
3. **Track Progress**: The progress bar updates automatically based on the number of tasks completed.

## Terminal Version
**Video Demo:**  
[![Watch the video](https://img.youtube.com/vi/q6q1k0nFOy4/hqdefault.jpg)](https://youtu.be/q6q1k0nFOy4)

### Features
- **Simple CLI Interface**: Users can add, view, and mark tasks as completed directly from the terminal.
- **Task Saving**: Tasks are saved in a text file with an easy-to-read format.
- **Cross-Platform**: The terminal version works across any system that supports Python.

### Installation
Follow the same steps as the GUI version for installation.

### Usage
To run the terminal-based To-Do List app:

```bash
python todo_cli.py
```
1. **Add Tasks**: Select option 1, enter tasks, and press Ctrl-Z to stop adding tasks.
2. **View Tasks**: Select option 2 to display the list of tasks.

3. **Mark Tasks as Completed**: Enter the number of the task you have completed to mark it as done. Completed tasks will be marked with an [X].

## Known Issues
- **GUI Progress Alignment**: The progress bar may occasionally have alignment issues.
- **Terminal Task Number Validation**: The terminal version may not handle invalid task numbers properly.

## Technologies Used
- **Python**: The core language used for both versions.
- **Tkinter**: Used for creating the GUI version.
- **ttkbootstrap**: Adds modern themes and styles to the GUI version.
- **Terminal/CLI**: Used for the terminal version for simple user interaction.

## Future Improvements
- **GUI Enhancements**: Include the ability to edit tasks and switch between different colour themes.
- **Terminal Version Improvements**: Add better input validation for task numbering and additional features like task deletion.

## Author
Kevin Gonsalves

***Please be sure to check out my other repositories too!***
- [Instagram Followers Analyzer](https://github.com/kevgon8/Instagram-Follower-Analyzer)
- [CS50P Problem Sets](https://github.com/kevgon8/CS50P-Problem-Sets-Solutions)
- [Simple User Authentication System](https://github.com/kevgon8/User-Authentication-System)

## Contact
For any questions or feedback, feel free to reach out:

Email:
- kevgon146@gmail.com 

- kg2713@srmist.edu.in
