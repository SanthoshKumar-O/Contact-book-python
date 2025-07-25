import json
import os
contacts={}
def load_contacts():
    global contacts
    if os.path.exists("contacts.json"):
        try:
            with open("contacts.json","r") as file:
                contacts=json.load(file)
        except json.JSONDecodeError:
            contacts={}
def save_contacts():
    with open("contacts.json","w") as file:
        json.dump(contacts,file,indent=4)
def no_empty_input(prompt):
    while True:
        value=input(prompt).strip()
        if value=="":
            print("Input cannot be empty.Type again.")
            continue
        else:
            return value
        
load_contacts()
print("--CONTACTS BOOK--")

while True:    
    print()
    print("1.Add contacts")
    print("2.Show contacts")
    print("3.List all contacts")
    print("4.Delete contacts")
    print("5.Insert contacts")
    print("6.Search contacts")
    print("7.Exit")
    print()
    oper=input("What do you need to proceed: ")
    if oper=="1":
        contact=no_empty_input("Enter name : ")
        num=no_empty_input("Enter the number : ")
        if contact in contacts:
            print("Contact already exist.To add the no. to the same contact use option 5.")
        else:
            contacts[contact]=[num]
            print(f"Contact:{contact} added successfully")
            save_contacts()
    elif oper=="2":
        name=no_empty_input("Enter the name : "  )
        if name in contacts:
           print(f"The  contacts in {name} are:{' , '.join(contacts[name])}")
        else:
            print("Contact not found.")
    elif oper =="3":
        if len(contacts) ==0:
            print("No contacts yet.")   
        else:
            for contact,num in contacts.items():
                print(f"{contact} : {' , '.join(num)}")
    elif oper=="4":
        contact=no_empty_input("Enter the contact : ")    
        req=no_empty_input("Are you sure you need to delete the contact(Y/N) : ").strip()      
        if req.upper() == "Y":
            if contact in contacts:
                contacts.pop(contact)   
                print(f"{contact} has been removed successfully") 
                save_contacts()
            else:
                print("Contact does not exist.")
        elif req.upper() == "N":
            print("Deletion is cancelled.")   
        else:
            print("Your input is not correct.")  
    elif oper=="5":
        name=no_empty_input("Enter the contact to be expanded: ").strip() 
        if name in contacts:  
            value2=no_empty_input("Enter the no. to be added : ").strip()
            if value2 in contacts[name]:
                print("The no. is already saved in a contact.")
            else:
                contacts[name].append(value2)
                print("Contact no. is added successfully.") 
                save_contacts()
        else:
            print("Contact does not exist.") 
    elif oper=="6":
        num=no_empty_input("Enter the number: ")
        found=[]
        for contact,nums in contacts.items():
            if num in nums:
                found.append(contact)
        if len(found) != 0:
            print(f"{num} : {found}")
        else:                                     
            print("Contact not found.")    
    elif oper=="7":
        print("Exiting application.")    
        break                                        
                    
    else:
        print("Invalid choice.Try again.")                    
    
