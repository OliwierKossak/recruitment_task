import re

from datetime import datetime


class DataValidation:
    """
    Used to validate data and display information about users.
    """

    def validate_email_address_format(self, email):
        """
        Check if format of email address is correct.

        :param email: address email.
        :return: true if format of email is correct else return false.
        """
        is_email_correct = False

        if re.match(r'^[^@]+@[^@]+\.[^@]\w{1,4}$', email):
            is_email_correct = True

        return is_email_correct

    def format_telephone_number(self, telephone_number):
        """
        Removes redundant characters from a phone number.

        :param telephone_number: telephone number.
        :return: nine-digit number.
        """
        telephone_number = telephone_number.replace(' ', '')
        telephone_number = telephone_number[len(telephone_number) - 9::]
        return telephone_number

    def change_user_telephone_number_format(self, users):
        """
        Changes the format of the user's phone number.

        :param users: list with dictionaries with users information.
        :return: list with dictionaries with users information about users updated with the new mobile number format.
        """
        user_index = 0
        while user_index < len(users):
            user_telephone_number = users[user_index]['telephone_number']
            corrected_number = self.format_telephone_number(
                user_telephone_number)
            users[user_index]['telephone_number'] = corrected_number
            user_index += 1
        return users

    def convert_str_to_datetime(self, date_time):
        """
        Converts datetime in string format to datetime format.

        :param date_time: string in format %Y-%m-%d %H:%M:%S.
        :return: datetime.
        """
        converted_date_time = datetime.strptime(date_time, '%Y-%m-%d %H:%M:%S')
        return converted_date_time

    def check_if_first_datetime_is_older(self, date_time_1, date_time_2):
        """
        Checks if first date is older than second.

        :param date_time_1:  string in format %Y-%m-%d %H:%M:%S.
        :param date_time_2: string in format %Y-%m-%d %H:%M:%S.
        :return: True when first datetime is older else False.
        """
        date_time_converted_1 = self.convert_str_to_datetime(date_time_1)
        date_time_converted_2 = self.convert_str_to_datetime(date_time_2)
        is_datetime_older = False

        if date_time_converted_1 < date_time_converted_2:
            is_datetime_older = True

        return is_datetime_older

    def check_if_telephone_number_exists(self, users, telephone_number):
        """
        Check if telephone number exists.

        :param users: list with dictionaries with users information.
        :param telephone_number: user telephone number.
        :return: True if telephone number exists else False.
        """
        telephone_number_exists = False
        for user in users:
            if user['telephone_number'] == telephone_number:
                telephone_number_exists = True
                break
        return telephone_number_exists

    def check_if_password_exists(self, users, password):
        """
        Check if password exists.

        :param users: list with dictionaries with users information.
        :param password: user password.
        :return: True if password exists else False.
        """
        password_exists = False

        for user in users:
            if user['password'] == password:
                password_exists = True
                break
        return password_exists

    def check_if_email_exists(self, users, email):
        """
        Check if email exists.

        :param users: list with dictionaries with users information.
        :param email: user email address.
        :return: True if email address exists else False.
        """

        email_exists = False
        for user in users:
            if user['email'] == email:
                email_exists = True
                break
        return email_exists

    def check_if_user_is_admin(self, users, email, telephone_number, password):
        """
        Check if user have admin role.

        :param users: list with dictionaries with users information.
        :param email: user email address.
        :param telephone_number: user telephone number.
        :param password: user password.
        :return: True if user have admin role else False.
        """
        user_is_admin = False
        for user in users:
            if user['telephone_number'] == telephone_number and user['password'] == password:
                if user['role'] == 'admin':
                    user_is_admin = True
                    break
            elif user['email'] == email and user['password'] == password:
                if user['role'] == 'admin':
                    user_is_admin = True
                    break
        return user_is_admin

    def print_number_of_users(self, users):
        """
        Display number of users.

        :param users: list with dictionaries with users information.
        """
        print(len(users))

    def find_user_index(self, users, email_or_telephone_number):
        """
        Search for user index.

        :param users: list with dictionaries with users information.
        :param email_or_telephone_number: user email address or telephone number.
        :return: user index.
        """
        user_index = 0
        for user in range(len(users)):
            if email_or_telephone_number == users[user]['email']:
                user_index = user
                break
            elif email_or_telephone_number == users[user]['telephone_number']:
                user_index = user
                break
            else:
                user_index = None
        return user_index

    def find_oldest_user_index(self, users):
        """
        Search for user index with the longest existing account.

        :param users: list with dictionaries with users information.
        :return: index of user with the longest existing account.
        """
        oldest_user_index = 0
        current_user_index = None
        for user_index in range(1, len(users)):
            current_user_index = user_index
            oldest_user_date = users[oldest_user_index]['created_at']
            current_user_index = users[current_user_index]['created_at']
            if not self.check_if_first_datetime_is_older(oldest_user_date, current_user_index):
                oldest_user_index = current_user_index

        return oldest_user_index

    def find_users_with_children_of_same_age(self, users, user_index):
        """
        Search for users whose children have the same age and display them.

        :param users: list with dictionaries with users information.
        :param user_index: user index for which we are looking for users who have children of the same age.
        """
        user_children_age = []
        user_children = users[user_index]['children']
        if user_children == None:
            print("the user has no children")
        else:
            for child_age in range(len(user_children)):
                user_children_age.append(user_children[child_age]['age'])
            for user in range(len(users)):
                if user_index == user:
                    continue
                else:
                    other_user_children = users[user]['children']
                    other_user_children_age = []
                    if other_user_children is not None:
                        for child_age in range(len(other_user_children)):
                            other_user_children_age.append(
                                other_user_children[child_age]['age'])
                        for child_age in user_children_age:
                            if child_age in other_user_children_age:
                                self.print_user_information_children_sorted_by_name(
                                    users, user)
                                break

    def print_user_information_children_sorted_by_name(self, users, user_index):
        """
        Display user information: firstname, telephone number and children sorted by name.

        :param users: list with dictionaries with users information.
        :param user_index: index of the user whose information will be displayed.
        """
        user = users[user_index]
        children = users[user_index]['children']
        children_information = ""
        children_sorted_by_name = sorted(children, key=lambda x: x['name'])
        for child in range(len(children_sorted_by_name)):
            children_information += f"{children_sorted_by_name[child]['name']}, {children_sorted_by_name[child]['age']}"
            if not child + 1 == len(children_sorted_by_name):
                children_information += "; "
        print(
            f"{user['firstname']}, {user['telephone_number']}: {children_information}")

    def print_user_information_name_email_created_at(self, users, user_index):
        """
        Display user information: firstname, email address, created account date.

        :param users: list with dictionaries with users information.
        :param user_index: index of the user whose information will be displayed.
        """
        user_email = users[user_index]['email']
        user_name = users[user_index]['firstname']
        user_created_at = users[user_index]['created_at']
        print(
            f"""name: {user_name} \nemail_address: {user_email} \ncreated_at: {user_created_at}""")

    def print_user_children(self, users, user_index):
        """
        Display information about user children.

        :param users: list with dictionaries with users information.
        :param user_index: index of the user whose information about children will be displayed.
        """
        children = users[user_index]['children']
        if children == None:
            print('The user has no children')
        elif len(children) == 1:
            child = children[0]
            print(f"{child['name']}, {child['age']}")
        else:
            children_sorted_by_name = sorted(children, key=lambda x: x['name'])
            for child in children_sorted_by_name:
                print(f"{child['name']}, {child['age']}")

    def create_list_with_children_age(self, users):
        """
        Create list with children age.

        :param users: list with dictionaries with users information.
        :return: list with children age.
        """
        children_age_list = []
        for user in range(len(users)):
            children = users[user]['children']
            if children == None:
                continue
            else:
                for child in children:
                    children_age_list.append(int(child['age']))
        return children_age_list

    def count_children_by_age(self, children_age_list):
        """
        Display counted children by age and sorted by number of children in group age.

        :param children_age_list: list with children age.
        """
        children_age_dictionary = {}
        for age in children_age_list:
            if age not in children_age_dictionary.keys():
                children_age_dictionary[age] = 1
            else:
                children_age_dictionary[age] += 1

        children_age_dictionary_sorted = {k: v for k, v in sorted(
            children_age_dictionary.items(), key=lambda x: x[1])}

        for age, count in children_age_dictionary_sorted.items():
            print(f"age: {age}, count: {count}")
