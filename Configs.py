import os
import json
from DatabaseConnection import *

PandasDbInfo = {
    'database': 'pandasdblite',
    'user': 'pandasuser',
    'password': 'Gotohell',
    'host': 'localhost',
    'port': '5432'
    }


os.environ['Database Object'] = json.dumps(PandasDbInfo)


if __name__ == '__main__':
    print(type(os.environ['pandasdbLite']))

