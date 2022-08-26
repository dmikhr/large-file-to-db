Read very large files (1GB or more), parse data and save into database (files where data is presented line by line, e.g. .csv, .log) <br>
Parsing and saving data are implemented as extensions, so different extensions can be used depending on source file format and target database.
Initially script was developed to convert large *.csv files with numerical data into SQLite database (see example). 

Try example from `csv_example` directory.<br>
To run example apply sample SQLite3 schema run `sqlite3`:<br>
```
sqlite3 sample.db < sample_schema.sql
```
Generate sample .csv file. If you want to change number of columns make changes in database schema accordingly.<br>
By default it generates only 10000 lines, so you can try it quickly and see how it works. When you become comfortable with code set it to 10M+ to generate large files.
```
python file_generator_test.py
```

Then run `csv_to_sqlite.py`
```
python csv_to_sqlite.py
```