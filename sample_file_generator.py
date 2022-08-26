# generate large CSV files with numerical data for testing

import random

NUMBER_OF_LINES = 10000
COLS_NUM = 5
FILE_MODE = 'w'
DELIMITER = ';'
NOTIFICATION_INTERVAL = round(0.2 * NUMBER_OF_LINES)


def gen_str():
    sample = random.sample(range(10, 200), COLS_NUM)
    return DELIMITER.join(
        list(map(
            lambda x: str(round(x/random.randrange(1, 10), 2)), sample))
    ) + '\n'


with open('sample.csv', FILE_MODE) as fa:
    for i in range(NUMBER_OF_LINES):
        fa.write(gen_str())
        if (i % NOTIFICATION_INTERVAL == 0) and (i > NOTIFICATION_INTERVAL):
            print(f'{i} lines completed...')
