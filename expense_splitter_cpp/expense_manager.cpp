#include <iostream>
#include "expense_manager.h"

string expense_manager::get_user_name(int userid) {
    for (int i = 0; i < users.size(); i++) {
        if (users[i].userid == userid) {
            return users[i].name;
        }
    }
    return "Unknown";
}

void expense_manager::add_user(int userid, string name) {
    user new_user(userid, name);
    users.push_back(new_user);
    cout << "User added: " << name << " (ID: " << userid << ")" << endl;
}

void expense_manager::add_expense(int expenseid, string description, double totalamount, int paidby, vector<int> participants) {
    if (participants.size() == 0) {
        cout << "Error: Expense must have at least one participant." << endl;
        return;
    }

    expense new_expense(expenseid, description, totalamount, paidby, participants);
    expenses.push_back(new_expense);
    cout << "Expense added: " << description << " (Amount: " << totalamount << ")" << endl;
}

void expense_manager::show_expenses() {
    cout << "\nAll Expenses:" << endl;

    if (expenses.size() == 0) {
        cout << "No expenses recorded." << endl;
        return;
    }

    for (int i = 0; i < expenses.size(); i++) {
        expense exp = expenses[i];
        string payer_name = get_user_name(exp.paidby);

        cout << "Expense " << exp.expenseid << ": " << exp.description;
        cout << " (Amount: " << exp.totalamount << ", Paid by: " << payer_name << ")" << endl;
    }
    cout << endl;
}

void expense_manager::show_balances() {
    cout << "\nBalance Summary:" << endl;

    map<int, double> balance;
    for (int i = 0; i < users.size(); i++) {
        balance[users[i].userid] = 0;
    }

    for (int i = 0; i < expenses.size(); i++) {
        expense exp = expenses[i];
        double share_per_person = exp.totalamount / exp.participants.size();

        balance[exp.paidby] = balance[exp.paidby] + exp.totalamount;

        for (int j = 0; j < exp.participants.size(); j++) {
            int participant_id = exp.participants[j];
            balance[participant_id] = balance[participant_id] - share_per_person;
        }
    }

    vector<pair<int, double>> creditors;
    vector<pair<int, double>> debtors;

    for (int i = 0; i < users.size(); i++) {
        int userid = users[i].userid;
        double final_balance = balance[userid];

        if (final_balance > 0.01) {
            creditors.push_back(make_pair(userid, final_balance));
        } else if (final_balance < -0.01) {
            debtors.push_back(make_pair(userid, -final_balance));
        }
    }

    for (int i = 0; i < debtors.size(); i++) {
        int debtor_id = debtors[i].first;
        double debt = debtors[i].second;

        for (int j = 0; j < creditors.size(); j++) {
            int creditor_id = creditors[j].first;
            double credit = creditors[j].second;

            if (debt > 0.01 && credit > 0.01) {
                double amount = (debt < credit) ? debt : credit;

                cout << get_user_name(debtor_id) << " owes "
                     << get_user_name(creditor_id) << " "
                     << amount << endl;

                debtors[i].second -= amount;
                creditors[j].second -= amount;
                debt -= amount;
            }
        }
    }
    cout << endl;
}