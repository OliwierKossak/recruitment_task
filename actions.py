import argparse

from data_validation import DataValidation


class Actions(DataValidation):
    """
    Actions that users can do using script.
    """

    def __init__(self, users):
        """
        Initializes new instance of 'Actions'

        :param users: list with dictionaries with users information.
        """
        self.users = users

    def print_number_of_valid_accounts(self, args):
        """
        Display number of valid users accounts.

        :param args: A namespace object containing command-line arguments.
        """

        login = args.login
        password = args.password
        users = self.users
        function = self.print_number_of_users
        users_is_admin = self.check_if_user_is_admin(
            users, login, login, password)

        email_exists = self.check_if_email_exists(users, login)

        password_exists = self.check_if_password_exists(users, password)

        telephone_number_exists = self.check_if_telephone_number_exists(
            users, login)

        self.check_access_for_user_admin(
            email_exists, telephone_number_exists, password_exists, users_is_admin, function, users)

    def print_longest_existing_account(self, args):
        """
        Display user with the longest existing account.

        :param args: A namespace object containing command-line arguments.
        """

        users = self.users
        oldest_user_index = self.find_oldest_user_index(users)
        login = args.login
        password = args.password
        users = self.users
        function = self.print_user_information_name_email_created_at
        users_is_admin = self.check_if_user_is_admin(
            users, login, login, password)

        email_exists = self.check_if_email_exists(users, login)

        password_exists = self.check_if_password_exists(users, password)

        telephone_number_exists = self.check_if_telephone_number_exists(
            users, login)
        self.check_access_for_user_admin(email_exists, telephone_number_exists,
                                         password_exists, users_is_admin, function, users, oldest_user_index)

    def print_group_children_by_age(self, args):
        """
        Display counted children by age and sorted by number of children in group age.

        :param args: A namespace object containing command-line arguments.
        """
        login = args.login
        password = args.password
        users = self.users
        children_list = self.create_list_with_children_age(users)
        function = self.count_children_by_age
        users_is_admin = self.check_if_user_is_admin(
            users, login, login, password)

        email_exists = self.check_if_email_exists(users, login)

        password_exists = self.check_if_password_exists(users, password)

        telephone_number_exists = self.check_if_telephone_number_exists(
            users, login)

        self.check_access_for_user_admin(
            email_exists, telephone_number_exists, password_exists, users_is_admin, function, children_list)

    def print_children(self, args):
        """
        Display user's children.

        :param args: A namespace object containing command-line arguments.
        """
        users = self.users
        login = args.login
        password = args.password
        user_index = self.find_user_index(users, login)
        function = self.print_user_children

        email_exists = self.check_if_email_exists(users, login)

        password_exists = self.check_if_password_exists(users, password)

        telephone_number_exists = self.check_if_telephone_number_exists(
            users, login)
        self.check_access_for_user(
            email_exists, telephone_number_exists, password_exists, function, users, user_index)

    def print_users_with_similar_children_by_age(self, args):
        """
        Display users information and children whose children are the same age as the user's children.

        :param args: A namespace object containing command-line arguments.
        """
        users = self.users
        login = args.login
        password = args.password
        user_index = self.find_user_index(users, login)
        function = self.find_users_with_children_of_same_age

        email_exists = self.check_if_email_exists(users, login)

        password_exists = self.check_if_password_exists(users, password)

        telephone_number_exists = self.check_if_telephone_number_exists(
            users, login)
        self.check_access_for_user(
            email_exists, telephone_number_exists, password_exists, function, users, user_index)

    def check_access_for_user_admin(self, email, telephone_number, password, admin, function, *arguments):
        """
        Check if user have admin role and have access to using admin functionality.

        :param email: value of bool type confirming the existence of the email address.
        :param telephone_number: value of bool type confirming the existence of the telephone number.
        :param password: value of bool type confirming the existence of user password.
        :param admin: value of bool type confirming the user role as admin.
        :param function: function called when the activation conditions are met.
        :param arguments: arguments accepted by the called function.
        """
        if email and password:
            if admin:
                function(*arguments)
            else:
                print("Access denied, need admin account")
        elif telephone_number and password:
            if admin:
                function(*arguments)
            else:
                print("Access denied, need admin account")
        else:
            print("Invalid Login")

    def check_access_for_user(self, email, telephone_number, password, function, *arguments):
        """
        Check if user access to functionality.

        :param email: value of bool type confirming the existence of the email address.
        :param telephone_number: value of bool type confirming the existence of the telephone number.
        :param password: value of bool type confirming the existence of user password.
        :param function: function called when the activation conditions are met.
        :param arguments: arguments accepted by the called function.
        """
        if email and password:
            function(*arguments)
        elif telephone_number and password:
            function(*arguments)
        else:
            print("Invalid Login")

    def main(self):
        """
        Allows to use functions using appropriate flags on the command line.
        """
        parser = argparse.ArgumentParser()
        parser.add_argument("command")
        parser.add_argument("--login")
        parser.add_argument("--password")

        args = parser.parse_args()
        if args.command == 'print-all-accounts':
            self.print_number_of_valid_accounts(args)

        if args.command == 'print-oldest-account':
            self.print_longest_existing_account(args)

        if args.command == 'group-by-age':
            self.print_group_children_by_age(args)

        if args.command == 'print-children':
            self.print_children(args)

        if args.command == 'find-similar-children-by-age':
            self.print_users_with_similar_children_by_age(args)


