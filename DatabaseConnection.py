import json
import psycopg2


class DatabaseConnection:

    def __init__(self, sql_statement, database_configuration, database_version):
        self.sql = sql_statement
        self.config = json.loads(database_configuration)
        self.version = database_version

    def connection(self):
        try:
            connection = psycopg2.connect(user=self.config['user'],
                                          password=self.config['password'],
                                          host=self.config['host'],
                                          port=self.config['port'],
                                          database=self.config['database'])

            cursor = connection.cursor()

            cursor.execute(self.sql)

            record = cursor.fetchall()

            return record

        except (Exception, psycopg2.Error) as error:
            return 'Error while connecting to the database', error

        finally:
            try:
                cursor.close()

                connection.close()

            except NameError:
                return 'The connection had a failure while trying to connect to the database', NameError

    def createupdate(self):
        try:
            connection = psycopg2.connect(user=self.config['user'],
                                          password=self.config['password'],
                                          host=self.config['host'],
                                          port=self.config['port'],
                                          database=self.config['database'])

            cursor = connection.cursor()

            cursor.execute(self.sql)

            connection.commit()

        except (Exception, psycopg2.Error) as error:
            return 'Error while connecting to the database', error

        finally:
            try:
                cursor.close()

                connection.close()

            except NameError:
                return 'The connection had a failure while trying to connect to the database', NameError


if __name__ == '__main__':
    print('Now go back to coding, ;)')
