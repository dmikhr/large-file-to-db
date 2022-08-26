from scripts.process_data import ProcessData


class ProcessCSV(ProcessData):
    def _process_line(self, line):
        return line.split(';')


if __name__ == '__main__':
    csv_to_sqlite = ProcessCSV(file_path='sample.csv',
                               db_name='sample',
                               table_name='csv_data',
                               chunk_size=200)
    csv_to_sqlite.process_data()
