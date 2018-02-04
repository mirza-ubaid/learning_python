from User import User as U
from Privileges import Privileges as P

class Admin(U):
    def __init__(self, first, last, dob, edu, adrs, cnmbr):
        super().__init__(first, last, dob, edu, adrs, cnmbr)
        self.privileges = P()


admin = Admin("Mirza Ubaidullah", "Baig", "05/05/ 95", "Computer System Engineer(BE)", "F.B. area block-1",
              +9234627123654)
admin.privileges.show_privilegs()
