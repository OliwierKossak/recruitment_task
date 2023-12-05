from data_validation import DataValidation


class DataProcessor(DataValidation):
    """
    Used to remove the incorrect values in users data set.
    """

    def merge_data_from_list(self, data_list):
        """
        Merge lists into one list.

        :param data_list: list contains lists to merge.
        :return: merged list.
        """
        merged_list = []
        for data in data_list:
            merged_list.extend(data)

        return merged_list

    def delete_user_without_telephone_number(self, users):
        """
        Remove users without telephone number.

        :param users: list with dictionaries with users information.
        :return: list of dictionaries with users who have a phone number.
        """
        user_index = 0
        while user_index < len(users):
            user_telephone_number_length = len(
                users[user_index]['telephone_number'])
            if user_telephone_number_length < 1:
                del users[user_index]
                user_index -= 1
            user_index += 1
        return users

    def delete_users_with_incorrect_email_address(self, users):
        """
        Remove users with incorrect email address.

        :param users: list with dictionaries with users information.
        :return: list of dictionaries with users who have a correct email address.
        """

        user_index = 0
        while user_index < len(users):
            user_email = users[user_index]['email']
            if not self.validate_email_address_format(user_email):
                del users[user_index]
                user_index -= 1
            user_index += 1
        return users

    def removes_users_with_incorrect_data(self, users):
        """
        Removes users with incorrect email or telephone number.
        :param users: list with dictionaries with users information.
        :return: list of dictionaries with users who have a correct email address or phone number.
        """
        self.delete_users_with_incorrect_email_address(users)
        self.delete_user_without_telephone_number(users)
        self.change_user_telephone_number_format(users)
        return users

    def check_is_same_telephone_number(self, number_1, number_2):
        """
        Check if two telephone numbers are same.

        :param number_1: first telephone number.
        :param number_2: second telephone number.
        :return: True if telephone numbers are same else False.
        """
        if number_1 == number_2:
            return True
        else:
            return False

    def delete_user_with_duplicate_telephone_number(self, users):
        """
        Remove older user when two users have same telephone number.

        :param users: list with dictionaries with users information.
        :return: list with dictionaries with users information without duplicate telephone numbers.
        """
        users = self.removes_users_with_incorrect_data(users)
        first_user_index = 0
        loop_index = len(users)
        while first_user_index < loop_index - 1:
            second_user_index = first_user_index + 1
            first_user_phone_number = users[first_user_index]['telephone_number']
            while second_user_index < loop_index:
                second_user_phone_number = users[second_user_index]['telephone_number']
                if second_user_index == first_user_index:
                    first_user_index += 1
                    continue
                if self.check_is_same_telephone_number(first_user_phone_number, second_user_phone_number):
                    first_user_created_at = users[first_user_index]['created_at']
                    second_user_created_at = users[second_user_index]['created_at']
                    if self.check_if_first_datetime_is_older(first_user_created_at, second_user_created_at):
                        del users[first_user_index]
                        first_user_index -= 1
                        loop_index -= 1
                        break
                    else:
                        del users[second_user_index]
                        second_user_index -= 1
                        loop_index -= 1
                second_user_index += 1
            first_user_index += 1
        return users

    def delete_user_with_duplicate_email(self, users):
        """
        Remove older user when two users have same email address.

        :param users: list with dictionaries with users information.
        :return: list with dictionaries with users information without duplicate email addresses.
        """
        users = self.removes_users_with_incorrect_data(users)
        first_user_index = 0
        loop_index = len(users)
        while first_user_index < loop_index - 1:
            second_user_index = first_user_index + 1
            first_user_email = users[first_user_index]['email']
            while second_user_index < loop_index:
                second_user_email = users[second_user_index]['email']
                if second_user_index == first_user_index:
                    first_user_index += 1
                    continue
                if self.check_is_same_telephone_number(first_user_email, second_user_email):
                    first_user_created_at = users[first_user_index]['created_at']
                    second_user_created_at = users[second_user_index]['created_at']
                    if self.check_if_first_datetime_is_older(first_user_created_at, second_user_created_at):
                        del users[first_user_index]
                        first_user_index -= 1
                        loop_index -= 1
                        break
                    else:
                        del users[second_user_index]
                        second_user_index -= 1
                        loop_index -= 1
                second_user_index += 1
            first_user_index += 1
        return users

    def clear_users_data(self, users):
        """
        Remove users with duplicate telephone numbers or email address.
        :param users: list with dictionaries with users information.
        :return:  list with dictionaries with users information without duplicate email addresses or telephone numbers.
        """

        self.delete_user_with_duplicate_telephone_number(users)
        self.delete_user_with_duplicate_email(users)
        return users
