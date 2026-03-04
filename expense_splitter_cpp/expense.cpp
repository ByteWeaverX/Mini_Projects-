#include "expense.h"

expense::expense(int id, string desc, double amount, int paid_by, vector<int> parts) {
    expenseid = id;
    description = desc;
    totalamount = amount;
    paidby = paid_by;
    participants = parts;
}