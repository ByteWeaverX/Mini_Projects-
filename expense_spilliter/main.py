from expense_manager import ExpenseManager


def main():
    print("====== EXPENSE SPLITTER MVP ======\n")
    
    # Create manager
    manager = ExpenseManager()
    
    # Add users
    print("Step 1: Creating Users")
    print("-" * 40)
    manager.add_user("alice_001", "Alice")
    manager.add_user("bob_001", "Bob")
    manager.add_user("charlie_001", "Charlie")
    print("Created 3 users: Alice, Bob, Charlie\n")
    
    # Add expenses
    print("Step 2: Adding Expenses")
    print("-" * 40)
    
    # Expense 1: Alice paid 300 for dinner (shared by all 3)
    manager.add_expense(
        expenseid="exp_001",
        description="Dinner",
        totalamount=300,
        paidby_userid="alice_001",
        participant_userids=["alice_001", "bob_001", "charlie_001"]
    )
    print("Expense 1: Alice paid 300 for Dinner (split: Alice, Bob, Charlie)")
    print(f"  - Each person's share: 100")
    print()
    
    # Expense 2: Bob paid 200 for movie (shared by Bob and Charlie)
    manager.add_expense(
        expenseid="exp_002",
        description="Movie",
        totalamount=200,
        paidby_userid="bob_001",
        participant_userids=["bob_001", "charlie_001"]
    )
    print("Expense 2: Bob paid 200 for Movie (split: Bob, Charlie)")
    print(f"  - Each person's share: 100")
    print()
    
    # Expense 3: Charlie paid 150 (shared by Alice and Charlie)
    manager.add_expense(
        expenseid="exp_003",
        description="Gas",
        totalamount=150,
        paidby_userid="charlie_001",
        participant_userids=["alice_001", "charlie_001"]
    )
    print("Expense 3: Charlie paid 150 for Gas (split: Alice, Charlie)")
    print(f"  - Each person's share: 75")
    print()
    
    # Show all expenses
    manager.show_expenses()
    
    # Show raw balances (for verification)
    manager.show_balances()
    
    # Show who owes whom
    manager.show_who_owes_whom()
    
    print("\n" + "=" * 40)
    print("BALANCE CALCULATION EXPLANATION:")
    print("=" * 40)
    print("\nAlice's balance calculation:")
    print("  - Paid for Dinner: +300")
    print("  - Owes for Dinner share: -100")
    print("  - Owes for Movie share: -100")
    print("  - Paid for Gas share: -75")
    print("  - Result: 300 - 100 - 100 - 75 = +25 (owed to Alice)")
    print("\nBob's balance calculation:")
    print("  - Owes for Dinner share: -100")
    print("  - Paid for Movie: +200")
    print("  - Owes for Movie share: -100")
    print("  - Owes for Gas share: -75")
    print("  - Result: -100 + 200 - 100 - 75 = -75 (Bob owes)")
    print("\nCharlie's balance calculation:")
    print("  - Owes for Dinner share: -100")
    print("  - Paid for Movie: +200")
    print("  - Paid for Gas: +150")
    print("  - Owes for Gas share: -75")
    print("  - Result: -100 + 200 + 150 - 75 = +75 (owed to Charlie)")


if __name__ == "__main__":
    main()
