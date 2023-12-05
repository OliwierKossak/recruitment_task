import json


class JsonFileLoader:
    """
    Enables to load and modify a JSON file.
    """

    def __init__(self, file_path):
        """
        Initializes new instance of 'JsonFileLoader'

        :param file_path: Path to csv file.
        """
        self.file_path = file_path

    def load_file(self):
        """
        Load json file.

        :returns: json file.
        """
        with open(f'{self.file_path}') as json_file:
            json_data = json.load(json_file)
        return json_data

    def convert_empty_children_list_to_none(self):
        """
        Change value for key = children to None when list of children is empty.

        :return: List of dictionaries with users information with change value for "children" key.
        """
        users = self.load_file()
        for user in users:
            if len(user['children']) == 0:
                user['children'] = None
        return users

    def load_cleaned_file(self):
        """
        Return a cleansed data set with user information.

        :return: List with dictionaries with users information.
        """
        users = self.convert_empty_children_list_to_none()
        return users
