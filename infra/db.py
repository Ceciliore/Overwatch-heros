import psycopg2


class ConectaPostgres:
    def __init__(self, config):
        self.config = config
        self.user = config.user
        self.password = config.password
        self.host = config.host
        self.port = config.port
        self.database = config.database
        self.dsn = f"postgres://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"
        self.connection = self.create_connection()

    def do_select_database(self, query, *args):
        cursor = self.connection.cursor()
        cursor.execute(query, *args)


    def do_delete_database(self, query, *args):
        self.connection.fetchall_cursor(query, args)
        return

    def do_insert_database(self, query, *args):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, *args)
            
            self.connection.commit()
            count = cursor.rowcount

            print(count, "Record inserted successfully into table")

        except (Exception, psycopg2.Error) as error:
            print("Failed to insert record into mobile table", error)

    def create_connection(self):
        return psycopg2.connect(dsn=self.dsn)
