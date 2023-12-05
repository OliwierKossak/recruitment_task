import csv
import re


class CsvFileLoader:
    """
    Enables to load and modify a CSV file.
    """

    def __init__(self, file_path):
        """
        Initializes new instance of 'CsvFileLoader'

        :param file_path: Path to csv file.
        """
        self.file_path = file_path

    def load_csv_file(self):
        """
        Load csv file and convert it to list with dictionaries.

        :returns: Csv file converted to list with rows converted to dictionaries.
        """
        with open(f'{self.file_path}', 'r') as file:
            csv_file = csv.DictReader(file, delimiter=';')
            data = [row for row in csv_file]
        return data

    def clean_children_data(self):
        """
        Format information about child to same format for every user.

        :return: formatted list with dictionaries with information about users.
        """
        users = self.load_csv_file()
        for user in users:
            children = user['children'].split(',')
            user_children_list = []

            for child in children:
                child_dictionary = self.create_child_dictionary(child)
                user_children_list.append(child_dictionary)
                if len(child) == 0:
                    user_children_list = None
                    break

            user['children'] = user_children_list

        return users

    def create_child_dictionary(self, text):
        """
        Create dictionary with information about child in format: {name:value, age:value}

        :param text:
        :return: dictionary with information about child  name and age
        """
        child_dictionary = {}
        match_string = re.match(r'(^\w+) \((\d+)\)$', text)
        if match_string:
            name = match_string.group(1)
            age = match_string.group(2)
            child_dictionary['name'] = name
            child_dictionary['age'] = age

        return child_dictionary

    def load_cleaned_file(self):
        """
        Return a cleansed data set with user information.
        :return: list with dictionaries with users information.
        """
        users = self.clean_children_data()
        return users
