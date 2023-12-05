import xmltodict


class XmlFileLoader:
    """
    Enables to load and modify an XML file.
    """

    def __init__(self, file_path):
        """
        Initializes new instance of 'XMLFileLoader'

        :param file_path: Path to xml file.
        """
        self.file_path = file_path

    def load_xml_file(self):
        """
        Load xml file.

        :returns: xml file as dictionary.
        """
        with open(f'{self.file_path}', 'r', encoding='utf-8') as xml_file:
            my_xml = xml_file.read()
        xml_dictionary = xmltodict.parse(my_xml)

        return xml_dictionary

    def remove_markups(self):
        """
        Remove "users" and "user" markups.

        :return: list with dictionaries with users information.
        """
        xml_file = self.load_xml_file()
        formatted_file = xml_file['users']['user']

        return formatted_file

    def remove_child_markup(self):
        """
        Remove "child" markup.

        :return: list with dictionaries with users information.
        """
        xml_file = self.remove_markups()
        for user in range(len(xml_file)):
            children = xml_file[user]['children']
            if not children == None:
                child_markup = xml_file[user]['children']['child']
                if isinstance(child_markup, list):
                    xml_file[user]['children'] = child_markup
                elif isinstance(child_markup, dict):
                    child_list = []
                    child_list.append(child_markup)
                    xml_file[user]['children'] = child_list
        return xml_file

    def load_cleaned_file(self):
        """
        Return list with dictionaries with users information without markups.

        :return: list with dictionaries with users information.
        """
        users = self.remove_child_markup()
        return users
