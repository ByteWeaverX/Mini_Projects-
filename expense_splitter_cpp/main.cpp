#include <iostream>
#include <vector>
#include "expense_manager.h"
using namespace std;

int main() {
    cout << "Expense Splitter Application\n" << endl;

    expense_manager manager;
    int choice = 0;

    while (true) {
        cout << "Menu:" << endl;
        cout << "1. Add User" << endl;
        cout << "2. Add Expense" << endl;
        cout << "3. Show All Expenses" << endl;
        cout << "4. Show Balances" << endl;
        cout << "5. Exit" << endl;
        cout << "Enter choice: ";
        cin >> choice;

        if (choice == 1) {
            int userid;
            string name;

            cout << "Enter User ID: ";
            cin >> userid;
            cin.ignore();

            cout << "Enter User Name: ";
            getline(cin, name);

            manager.add_user(userid, name);
        }
        else if (choice == 2) {
            int expenseid;
            string description;
            double totalamount;
            int paidby;
            int num_participants;
            vector<int> participants;

            cout << "Enter Expense ID: ";
            cin >> expenseid;
            cin.ignore();

            cout << "Enter Description: ";
            getline(cin, description);

            cout << "Enter Total Amount: ";
            cin >> totalamount;

            cout << "Enter Payer User ID: ";
            cin >> paidby;

            cout << "Enter Number of Participants: ";
            cin >> num_participants;

            cout << "Enter Participant User IDs: ";
            for (int i = 0; i < num_participants; i++) {
                int participant_id;
                cin >> participant_id;
                participants.push_back(participant_id);
            }

            manager.add_expense(expenseid, description, totalamount, paidby, participants);
        }
        else if (choice == 3) {
            manager.show_expenses();
        }
        else if (choice == 4) {
            manager.show_balances();
        }
        else if (choice == 5) {
            cout << "Goodbye!" << endl;
            break;
        }
        else {
            cout << "Invalid choice!" << endl;
        }
    }

    return 0;
}