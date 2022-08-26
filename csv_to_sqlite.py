from process_csv import ProcessCSV
import os

if __name__ == '__main__':
    PATH = f'{os.path.dirname(os.path.realpath(__file__))}/sample.csv'
    csv_to_sqlite = ProcessCSV(file_path=PATH,
                               db_name='sample',
                               table_name='csv_data',
                               chunk_size=200)
    csv_to_sqlite.process_data()
