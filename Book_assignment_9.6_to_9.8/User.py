class User:
    def __init__(self, first, last, dob, edu, adrs, cnmbr):
        self.first_name = first
        self.last_name = last
        self.address = adrs
        self.contact_no = cnmbr
        self.date_of_birth = dob
        self.education = edu
    def describ_user(self):
        print("# Printing User Information:")
        print("\t~Name: ",self.first_name+self.last_name)
        print("\t~Address: ",self.address)
        print("\t~Qualification: ",self.education)
        print("\t~Born on: ",self.date_of_birth)
        print("\t~Contact number: ",self.contact_no)
    def greet_user(self):
        print('"We Welcome you ', self.first_name+self.last_name)
