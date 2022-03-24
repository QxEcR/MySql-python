import mysql.connector


class MySql:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.connection.cursor()

    def excute(self, command):
        self.cursor.execute(command)
        self.connection.commit()

    def createTable(self, table, fields: list):
        # example of fields:
        # fields = ["id INT NOT NULL AUTO_INCREMENT PRIMARY KEY", "name VARCHAR(255)", "age INT"]
        command = f"CREATE TABLE IF NOT EXISTS {table} ({','.join(fields) if len(fields) > 1 else fields[0]})"
        self.excute(command)
        print(f"Created table {table}")

    def showTables(self):
        self.cursor.execute("SHOW TABLES")
        return self.cursor.fetchall()

    def selectAll(self, table, fields: list):
        # example of fields:
        # fields = ["id", "name", "age"]
        # fields = ["*"]

        if len(fields) > 1:
            command = f"SELECT {', '.join(fields) if len(fields) > 1 else fields[0]} FROM {table}"
        else:
            command = f"SELECT {fields[0]} FROM {table}"

        self.cursor.execute(command)
        return self.cursor.fetchall()
