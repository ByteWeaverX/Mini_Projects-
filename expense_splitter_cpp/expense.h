#ifndef EXPENSE_H
#define EXPENSE_H

#include <string>
#include <vector>
using namespace std;

class expense {
public:
    int expenseid;
    string description;
    double totalamount;
    int paidby;
    vector<int> participants;

    expense(int id, string desc, double amount, int paid_by, vector<int> parts);
};

#endif