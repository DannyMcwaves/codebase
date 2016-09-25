"""
this is a simple locker problem thingy.
there are 100 students in a school and each of them has a locker.
One day, the first student to enter the school opened his locker and the rest of the 99
lockers and left it opened.
the next student went to his/her locker and then closed it and then closed the remaining 98.
the 3rd student goes to his locker and does opposite of what was done to it and the did opposite to every n+2 locker.
where n means the current locker, he has touched.
the rest of students did the same as the 3rd student did, starting from their locker.

After all the student, how many lockers are left opened and how many are closed.
"""
from pprint import pprint


setOfLockers = ["Lock"] * 100

for i in range(len(setOfLockers) + 1):
    if i == 1:
        for k in range(i - 1, len(setOfLockers)):
            setOfLockers[k] = "Open"

    if i == 2:
        for j in range(i - 1, len(setOfLockers)):
            setOfLockers[j] = "Lock"

    elif i > 2:
        for a in range(i - 1, len(setOfLockers), 2):
            if setOfLockers[a] == "Lock":
                setOfLockers[a] = "Open"
            else:
                setOfLockers[a] = "Lock"

pprint(setOfLockers)
print("No. of opened Lockers:", setOfLockers.count("Open"))
print("No. of closed Lockers:", setOfLockers.count("Lock"))
