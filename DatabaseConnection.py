import json
import psycopg2


class DatabaseConnection:

    def __init__(self, sql_statement, database_configuration, database_version):
        self.sql = sql_statement
        self.config = json.loads(database_configuration)
        self.version = database_version

    def connection(self):
        try:
            connection = psycopg2.connect()

            cursor = connection.cursor()

            cursor.execute(self.sql)

            record = cursor.fetchall()

            return record

        except (Exception, psycopg2.Error) as error:
            print('Error while connecting to the database', error)

        finally:
            try:
                cursor.close()

                connection.close()

            except NameError:
                return 'The connection had a failure while trying to connect to the database', NameError




