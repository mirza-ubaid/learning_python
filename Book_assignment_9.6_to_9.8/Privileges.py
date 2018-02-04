class Privileges:
    def __init__(self):
        self.privileges = ["can add post", "can delete post",
                           "can ban user", "can add user",
                           "can pin posts", "can close comment section"]
    def show_privilegs(self):
        print("Admin is entitled the following privileges:")
        for privilege in self.privileges:
            print("\t# ", privilege.title())
