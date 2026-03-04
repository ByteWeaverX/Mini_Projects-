# Implementation Notes

## Design Philosophy

This MVP is built with **simplicity and clarity** as the primary goals:
- No advanced patterns
- No clever tricks
- Explicit, readable logic
- Human-written style code
- Easy to explain and verify

## Class Details

### User Class
```
Fields:
  - userid (string)
  - name (string)

Methods:
  - __init__(userid, name): Constructor
  - __str__(): Returns the user's name
  - __repr__(): Returns formatted representation
```

**Purpose**: Simple data holder for user identity.

---

### Expense Class
```
Fields:
  - expenseid (string): Unique expense identifier
  - description (string): What the expense was for
  - totalamount (number): Total cost before splitting
  - paidby (User object): The user who paid
  - participants (list of User objects): All users who should pay their share

Methods:
  - __init__(...): Constructor
  - get_share_per_person(): Calculates equal split amount
  - __str__(): Returns formatted expense description
```

**Purpose**: Encapsulates expense data and provides equal-split calculation.

---

### ExpenseManager Class
```
Fields:
  - users (dict): userid -> User object mapping
  - expenses (list): All Expense objects
  - balances (dict): userid -> balance (float)

Methods:
  - add_user(userid, name): Register a new user
  - add_expense(expenseid, description, totalamount, paidby_userid, participant_userids)
  - calculate_balances(): Recalculate all user balances
  - show_expenses(): Print all expenses
  - show_balances(): Print raw balances (debug view)
  - show_who_owes_whom(): Print settlement requirements
```

**Purpose**: Main orchestrator managing users, expenses, and balance calculations.

---

## Balance Calculation Algorithm

### Step 1: Initialize
- All user balances = 0

### Step 2: For Each Expense
```
paidby_balance += totalamount  [payer gets full amount]

For each participant:
  participant_balance -= share_amount  [each person subtracts their share]
```

### Step 3: Interpretation
- **Positive balance**: User is owed money by others
- **Negative balance**: User owes money to others
- **Zero balance**: Settled

### Step 4: Settlement (who_owes_whom)
```
Create two lists:
  1. Creditors: users with positive balance (owed money)
  2. Debtors: users with negative balance (owes money)

Match debtors with creditors:
  - For each debtor, settle against creditors in order
  - Amount settled = min(debtor_amount, creditor_amount)
  - Print: "X owes Y <amount>"
```

---

## Example Walkthrough

**Scenario:**
- Alice, Bob, Charlie split expenses
- Alice pays $300 for dinner (3 people)
- Bob pays $200 for movie (2 people)
- Charlie pays $150 for gas (2 people)

**Calculation:**

Expense 1: Dinner ($300, paidby Alice, participants: Alice, Bob, Charlie)
```
Share = 300 / 3 = 100
Alice: 0 + 300 - 100 = 200
Bob:   0 - 100 = -100
Charlie: 0 - 100 = -100
```

Expense 2: Movie ($200, paidby Bob, participants: Bob, Charlie)
```
Share = 200 / 2 = 100
Alice:   200 - 0 = 200
Bob:     -100 + 200 - 100 = 0
Charlie: -100 - 100 = -200
```

Expense 3: Gas ($150, paidby Charlie, participants: Alice, Charlie)
```
Share = 150 / 2 = 75
Alice:   200 - 75 = 125
Bob:     0 - 0 = 0
Charlie: -200 + 150 - 75 = -125
```

**Final Balances:**
- Alice: +125 (owed to Alice)
- Bob: 0 (settled)
- Charlie: -125 (Charlie owes)

**Settlement:**
- Charlie owes Alice 125

---

## Code Quality Checklist

- [x] All variable names are lowercase
- [x] Method names use underscores (snake_case)
- [x] No lambda functions
- [x] No stream operations
- [x] No advanced patterns (no strategies, no decorators, no meta-programming)
- [x] Explicit loops instead of map/filter
- [x] Simple if-else statements
- [x] Comments for non-obvious logic
- [x] No deep nesting (max 2-3 levels)
- [x] Only 3 mandatory classes
- [x] No extra abstractions or helper classes
- [x] Reads like human-written code

---

## Testing the MVP

Run `main.py` to see the full demonstration with 3 users and 3 expenses. The output shows:
1. All expenses added
2. Raw balances (for verification)
3. Settlement (who owes whom)
4. Detailed explanation of balance calculations

---

## What's NOT Included

- No authentication
- No UI/web framework
- No database persistence
- No API
- No custom split logic (equal only)
- No payment processing
- No logging framework
- No error recovery

**This is by design.** The MVP is intentionally minimal to focus on core logic and code quality.
