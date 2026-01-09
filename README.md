# Python Quiz Application

## Overview

This project is a terminal-based Python quiz application designed to test users on:

- Unit conversion knowledge  
- General computing and mathematics topics  

The program demonstrates the use of **functions, modular code, input validation, and structured program flow**, in line with professional software development practices.

It has been developed using **Python 3.9+** and follows a simple software lifecycle:  
**Design -> Implementation -> Testing -> Refinement**.

## Features

- Menu-based user interface  
- Multiple quiz categories  
- Randomised questions  
- Automatic score tracking  
- Input validation  
- Modular function-based design  
- Replay and exit options  

## How to Run the Program (User Guide)

### Requirements

- Python **3.9 or above**
- Terminal / Command Prompt

### Steps

1. Download or clone the GitHub repository  
2. Open a terminal in the project folder  
3. Run the program:

```bash
python quiz_app.py
```
4. Choose a quiz option from the menu
5. Answer the questions
6. View your final score

## How the Code Works (Technical Documentation)

### Program Structure

The program is built using modular functions:

| Function | Purpose |
|---------|---------|
| `display_menu()` | Displays the quiz menu |
| `get_user_choice()` | Collects user input |
| `ask_question()` | Asks and checks answers |
| `run_quiz()` | Runs a quiz session |
| `main()` | Controls program flow |

### Execution Control

The program uses the following line to control when the quiz runs:

```python
if __name__ == "__main__":
    main()
```

This ensures the ```main()``` function only runs when the file is executed directly, not when it is imported into another file. This supports modular design and prevents the program from running automatically in unintended situations.

### Design Approach

- Question banks are stored as lists of tuples  
- Randomisation ensures different quizzes each run  
- User input is validated  
- Scoring is tracked  

### Testing & Debugging

The program was tested using:
- Invalid menu inputs
- Incorrect answers
- Multiple quiz attempts
- Exit conditions

Any errors found were corrected to ensure stable program behaviour.

## Legal, Ethical & Professional Considerations

- No personal data is collected  
- Accessible via terminal (low hardware requirements)  
- Clear instructions provided  
- No copyrighted material used

## Future Improvements

- Add difficulty levels  
- Add GUI  
- Store scores  
- Add more categories   
