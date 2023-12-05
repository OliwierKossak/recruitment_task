from actions import Actions
from csv_file_loader import CsvFileLoader
from data_processor import DataProcessor
from json_file_loader import JsonFileLoader
from xml_file_loader import XmlFileLoader


if __name__ == "__main__":
    json_loader = JsonFileLoader('data/a/users.json')
    json_file = json_loader.load_cleaned_file()

    xml_loader = XmlFileLoader('data/a/b/users_1.xml')
    xml_file = xml_loader.load_cleaned_file()

    csv_loader = CsvFileLoader('data/a/b/users_1.csv')
    csv_file = csv_loader.load_cleaned_file()

    csv_loader_2 = CsvFileLoader('data/a/c/users_2.csv')
    csv_file_2 = csv_loader_2.load_cleaned_file()

    files_list = [json_file, xml_file, csv_file, csv_file_2]

    data_processor = DataProcessor()
    users = data_processor.merge_data_from_list(files_list)
    data_processor.clear_users_data(users)
    actions = Actions(users)
    actions.main()
