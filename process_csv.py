from scripts.process_data import ProcessData


class ProcessCSV(ProcessData):
    def _process_line(self, line):
        return line.split(';')
