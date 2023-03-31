#if the applicant has high income and good credit then it is eligible for loan otherwise not

has_high_income=True
has_good_credit=True

if has_high_income and has_good_credit:
    print("Eligible For loan")

else:
    print("Not Eligible for loan") 

#if applicant has good credit And doesn't have a criminal record then it is eligible for loan

has_criminal_record=False
if has_good_credit and not has_criminal_record: #not operator makes true to false and vice-versa hence both the condition in the if statement becomes true then the print statement will be executed.
    print("Eligible for loan")

