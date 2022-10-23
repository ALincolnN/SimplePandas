from Configs import *

import pandas as pd
from DatabaseConnection import *


class Loader:

    def __init__(self):

        self.conf = os.environ.get('Database Object')

    def main(self):
        test_sql = 'select usename as role_name from pg_catalog.pg_user'

        result = DatabaseConnection(database_configuration=self.conf, sql_statement=test_sql)

        conn = result.connection()

        return conn


x = Loader()
print(x.main())


