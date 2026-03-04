#ifndef EXPENSE_MANAGER_H
#define EXPENSE_MANAGER_H

#include <vector>
#include <map>
#include <string>
#include "user.h"
#include "expense.h"
using namespace std;

class expense_manager {
private:
    vector<user> users;
    vector<expense> expenses;

    string get_user_name(int userid);

public:
    void add_user(int userid, string name);
    void add_expense(int expenseid, string description, double totalamount, int paidby, vector<int> participants);
    void show_expenses();
    void show_balances();
};

#endif