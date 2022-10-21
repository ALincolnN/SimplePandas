import os
import json

os.environ['PandasDbLite'] = json.dumps({'user': 'postgres',
                                         'password': 'gotohell',
                                         'database': 'PandasLite',
                                         'host': 'localhost',
                                         'port': '5432'
                                        })


if __name__ == '__main__':
    print(type(os.environ.get('PandasDbLite')))
