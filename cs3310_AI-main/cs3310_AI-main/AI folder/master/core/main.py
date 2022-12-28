from BMR.models import BMR
from Users.models import Users

def main():
    b = BMR 
    u = Users
    choice = 'yes'
    while (choice != 'no'):
        u.setHobby()
        choice = u.setChoice()
        
    
        
main()
    