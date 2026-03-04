# Expense Splitter MVP

A simple, clean, human-written expense splitter for hackathons.

## Features

✓ Create users with unique IDs  
✓ Add expenses with equal splitting  
✓ View all expenses  
✓ Calculate who owes whom  
✓ Explicit, readable logic

## Project Structure

```
expense_spilliter/
├── user.py              # User class (userid, name)
├── expense.py           # Expense class (manages expense data and equal splitting)
├── expense_manager.py   # ExpenseManager class (core business logic)
├── main.py             # Demo/example usage
└── README.md           # This file
```

## Running the Application

### Prerequisites
- Python 3.x installed

### Run the demo:
```bash
python main.py
```

Or:
```bash
python3 main.py
```

## Code Standards

✓ All variable/method names are **lowercase** (no camelCase)  
✓ Uses underscores for compound names (e.g., `add_user`, `get_share_per_person`)  
✓ Explicit logic - no streams, lambdas, or advanced patterns  
✓ Easy to read, easy to explain, easy to demo  
✓ Only 3 mandatory classes - no extra abstractions  

## Example Usage

```python
from expense_manager import ExpenseManager

# Create manager
manager = ExpenseManager()

# Add users
manager.add_user("alice_001", "Alice")
manager.add_user("bob_001", "Bob")

# Add expense (Alice paid 300 for dinner, split with Bob)
manager.add_expense(
    expenseid="exp_001",
    description="Dinner",
    totalamount=300,
    paidby_userid="alice_001",
    participant_userids=["alice_001", "bob_001"]
)

# Show results
manager.show_expenses()
manager.show_who_owes_whom()
```

## Balance Calculation Logic

For each expense:
1. **Payer gets +totalamount** (they paid it)
2. **Each participant gets -share** (their equal portion)

Example:
- Alice pays $300 for dinner (Alice, Bob, Charlie split it)
- Share per person = $300 / 3 = $100
- Alice: +300 - 100 = +200 (owed to Alice)
- Bob: -100 (owes money)
- Charlie: -100 (owes money)

Final balances are summed across all expenses to determine net settlement.

## What's NOT Included (By Design)

- No authentication/login
- No UI frameworks
- No database (in-memory only)
- No payment processing
- No advanced patterns
- Only equal splitting (no custom splits)

---

**This is a hackathon MVP - simple, clean, and easy to understand.**
