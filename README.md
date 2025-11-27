A simple interactive budgeting tool built using Python + Pygame.
The app helps users enter monthly income and expenses, then calculates spending distribution across the 50-30-20 budgeting rule:

- 50% Necessities
- 30% Luxury / Wants
- 20% Savings / Investments


1. Features


1.1 Welcome Screen
- App title and branding
- “Next” + “Exit” buttons

1.2 Personal Details Page
Users enter:
- Name
- Age
- Monthly Income
- Job Type (via custom dropdown menu)

Navigation:
- Back, Next, Exit

1.3 Necessity Expenses Page
Users input mandatory monthly expenses:
- Rent
- Electricity
- Home Loan
- Telephone / Internet
- Food
- Education
- Stationary
- Clothes (essential)
- Daily expenses
- Commute

Displays:
- Total necessity spending
- Recommended 50% budget
- Actual percentage of income spent
- All summary text is centered

1.4 Luxury Expenses Page
Users input non-essential spending such as:
- Luxury clothes
- Appliances
- Makeup / Jewelry
- Outing
- Vehicle

Shows:
- Total luxury spending
- Recommended 30% budget
- Actual % spent

1.5 Savings & Investments Page
Users enter:
- Health insurance
- Mutual funds
- Savings account deposits
- Stock market investments

Shows:
- Total savings
- Recommended 20%
- Actual % spent

1.6 Final Summary Page
Shows:
- Total income
- Total expenses
- Remaining balance
- Category-wise breakdown (Necessity / Luxury / Savings)
- Variance vs. ideal budgeting percentages

Navigation:
- Back, Exit


2. Project Structure


BudgetApp/
    main.py        - Main game loop, screen flow, calculations
    GUI.py         - Button creation, backgrounds, layout helpers
    INPUT.py       - Custom textbox function without internal loops
    dropdown.py    - Reusable dropdown component (single select)
    BG2.png        - Background for all data pages
    Background.png - Welcome screen background
    LOGO.png       - Window icon
    budgeting.xlsx - Reference structure for categories


3. Navigation Logic


Each page uses:

    Back | Next | Exit

Except the welcome screen which uses:

    Next | Exit

Back sends the user to the previous page.
Next moves to the next budgeting section.


4. Custom Components


4.1 Text Input Box
- No while-loops inside the input function
- Controlled through the main event loop
- Supports active/inactive states

4.2 Dropdown Component
- Fully reusable
- Single-select
- No background so it blends into any screen
- Works with:
  - drop_down()
  - draw_dropdown()
  - working_dropdown()


5. Requirements

Python Libraries:
- pygame

Install using:

    pip install pygame

Python Version:
- Python 3.8+


6. How to Run

From the project folder, run:

    python main.py


7. Future Improvements

- Add bar charts or pie charts for summary visualization
- Add animations or highlighting for invalid input
- Export results to PDF or Excel
- Add dark mode
- Add user profiles or save/load functionality
