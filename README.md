# LIBRARY MANAGEMENT SYSTEM (PYTHON CLI) (no AI used anywhere)
- A Terminal based library management system using oop in python
- supports adding/removing books members , borrowing and returing books and loggig actions

- build from scratch to practice core python , OOP concepts and creating a costom logger for library.py , book.py 

## Features
- Add books and members with unique IDs
- Borrow and return books (with stock update)
- View all members and their borrowed books
- Search books by title
- Logging using Python's `logging` module
- Decorators: retry, timeit, logger, secure
 
## Concepts Practiced
- Object-Oriented Programming (classes, objects)
- File handling and CLI interaction
- Exception handling
- Custom decorators (`@retry`, `@secure`, etc.)
- Logging and modular code design

## File structure
 "Python Files"
- `core.py` - contains classes Book , Member
- `libary.py` - contains class library
- `use.py` - contains python CLI
 "Log Files" - these will be created once you run it 
 - `Entries.log` - logs entries from core.py
 - `Library.log` - logs action performed in library like borrowed, returned ...

## How to Run
1. Clone this repo or download the files
2. Open terminal in project folder
3. Run the main file:

## Notes
- All passwords in this system are set to `"02042007"` by default (used with `@secure`)
- Logging files will be created automatically on first run
- This project is a raw skill-building tool — not meant for production use

'''i know the naming of variables is messy but i am working on it , i built this when i had 1.5 months left to start in my first semister of college'''