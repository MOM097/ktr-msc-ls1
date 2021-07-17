import csv
from User import User
from card import Card

def main():
    #Load Users and Cards
    users = init_users()
    cards = init_cards()

    #Main loop
    while True:
        selection = 0
        print("Welcome to BUSINESS CARD MANAGER")

        print("1. Logging into a profile")
        print("2. Create a profile")
        print("3. Exit")

        selection = int(input("Enter your selection : >"))


        if selection == 1:
            current_user = User()
            name = input("Enter you Name : > ")
            password = input("Enter your password : > ")

            not_logged = True

            while not_logged:
                name = input("Enter you Name : > ")
                password = input("Enter your password : > ")
                for user in users:
                    if user.name == name and user.validate_password(password):
                        current_user = user
                        print("Logged In ! Welcome : Mr ",current_user.name)
                        not_logged = False
                    else:
                        print("Your Name or your password is incorrect")
            

            card_b = True
            while card_b:
                print("1. Add a BUSINESS CARD")
                print("2. Log Out!")

                profile_selection = 0

                profile_selection = int(input("Enter : > "))

                if profile_selection == 1:
                    n_name = input("Enter a name : >")
                    n_company = input("Enter a Company name : >")
                    n_email = input("Enter an Email : >")
                    n_tel = input("Enter a Phone Number : >")

                    new_card =  Card(n_name, n_company, n_email, n_tel)
                    add_card(new_card)
                    card_b = False

                
                elif profile_selection == 2:
                    not_logged = True
                    card_b = False
        
        elif selection == 2:

            new_user = User()

            n_name = input("Enter a name : >")
            n_company = input("Enter a Company name : >")
            n_email = input("Enter an Email : >")
            n_tel = input("Enter a Phone Number : >")

            n_password = input("Enter a Password : >")

            new_user.name = n_name
            new_user.email = n_email
            new_user.set_password(n_password)
            new_user.telephone = n_tel
            new_user.company = n_company

            add_user(new_user)
            print("Profile has been created !")
        
        elif selection == 3:
            print("Bye !")
            exit()


#Initiate Users
def init_users():
    #Users list
    users = []
    #Read CSV file
    with open('users.csv', 'r') as file:
        reader = csv.reader(file)

        #For each row
        for row in reader:
            #Parse row
            user = User()

            if len(row) != 0:
                user.name = row[0]
                user.email = row[1]
                user.company = row[2]
                user.telephone = row[3]
                user.set_password(row[4])
                users.append(user)
    return users
        

#Intiate Cards
def init_cards():
    #Cards List
    cards = []
    #Read CSV file
    with open('cards.csv', 'r') as file:
        reader = csv.reader(file)

        #For each row
        for row in reader:
            #Parse row
            card = Card("","","","")

            card.name = row[0]
            card.email = row[1]
            card.company = row[2]
            card.telephone = row[3]
           
            cards.append(card)
    
    return cards

#append Card
def add_user(user):
    with open('users.csv', 'a+') as file:
        writer = csv.writer(file)
        writer.writerow([user.name, user.company, user.email, user.telephone, user.password]) 


#Append card
def add_card(card):
    with open('cards.csv', 'a+', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([card.name, card.email, card.company, card.telephone])




if __name__ == '__main__':
    main()