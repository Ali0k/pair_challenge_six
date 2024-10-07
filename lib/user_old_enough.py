from datetime import datetime
from dateutil.relativedelta import relativedelta # type: ignore

def user_old_enough(DOB):
    
    if DOB == None or DOB == int or DOB == float or DOB == bool or DOB == []:
        raise Exception("DOB must be given. Please enter DOB like so `YYYY-MM-DD`")
    
    todays_datetime = datetime.now()
    dob_object = datetime.strptime(DOB, '%Y-%m-%d')
    
    age = relativedelta(todays_datetime, dob_object)
    
    
    if age.years >= 16 and age.days > 0:
        return f"Access granted"
    elif age.years < 16:
        return f"You are {age.years} years old which is underage. You must be 16." 
    elif age.years == 16 and age.months == 0 and age.days == 0:
        return f"Happy 16th! In you go!"
    
    
print(user_old_enough('2008-10-07'))