import sqlite3


class ProcessData:
    def __init__(self, file_path, db_name, table_name, chunk_size=100000):
        self.file_path = file_path
        self.db_name = db_name
        self.table_name = table_name
        self.chunk_size = chunk_size

    def process_data(self):
        """
        public method, manages the process of data extraction
        and saving into database
        """
        con = sqlite3.connect(f'{self.db_name}.db')
        cur = con.cursor()
        for data_block in self._extract_data():
            for items in data_block:
                # NULL is used for primary key, it will be generated then automatically by SQLite
                cur.execute(f"INSERT INTO {self.table_name} VALUES (NULL, {', '.join(items)})")
                con.commit()
        con.close()

    def _process_line(self, line):
        """
        _process_line is specific to file format, here it just returns input param
        override this method to implement data parsing for your particular case

        :param str line: line from plain text file
        :return list: list of items parsed from line
        """
        return line

    def _extract_data(self):
        """
        parse data line by line applying _process_line

        :yield list: list of lists with items extracted from chunk of strings
        """
        with open(self.file_path, 'r') as fr:
            for chunk in self._read_file(file_handler=fr,
                                         lines_to_read=self.chunk_size):
                chunk_processed = list(map(lambda line:
                                       self._process_line(line), chunk))
                yield chunk_processed

    def _read_file(self, file_handler, lines_to_read):
        """
        read file line by line in chunks (chunks of lines from file)
        so large files can be processed without memory issues 

        :yield list: chunk of lines from plain text file
        """
        lines = []
        for line in file_handler:
            lines.append(line.strip())
            if len(lines) == lines_to_read:
                yield lines
                lines = []
        if lines:
            yield lines
