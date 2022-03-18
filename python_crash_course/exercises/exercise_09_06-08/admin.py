class User():
    """Represent a simple user profile."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the user."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        self.login_attempts = 0

    def describe_user(self):
        """Display a summary of the user's information."""
        print(f"\n{self.first_name} {self.last_name}")
        print(f"  Username: {self.username}")
        print(f"  Email: {self.email}")
        print(f"  Location: {self.location}")

    def greet_user(self):
        """Display a personalized greeting to the user."""
        print(f"\nWelcome back, {self.username}!")

    def increment_login_attempts(self):
        """Increment the value of login_attempts."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset login_attempts to 0."""
        self.login_attempts = 0


class Privileges():
    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        print(f"Privileges: ")
        if self.privileges:
            for privilege in self.privileges:
                print(f"\t {privilege}")
        else:
            print("User has no privileges!")


class Admin(User):
    def __init__(self, first_name, last_name, username, email, location):
        super().__init__(first_name, last_name, username, email, location)
        self.privileges = Privileges()


# administrator = Admin('john', 'smith', 'lsmith', 'xyz', 'paris')
# administrator.privileges = ['can add post', 'can delete post', 'can ban user']
# administrator.show_privileges()

admin2 = Admin('john', 'smith', 'lsmith', 'xyz', 'paris')

admin2.privileges.show_privileges()

print("Adding privileges...")

admin2.privileges.privileges = [
    'can add post', 'can delete post', 'can ban user']

admin2.privileges.show_privileges()
