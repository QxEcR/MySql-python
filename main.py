from MySql import MySql


def main():
    host = "localhost"  # enter your host
    user = "root"  # enter username
    password = ""  # enter password if needed
    database = "test"  # enter database name
    db = MySql(host, user, password, database)

    # show all tables in database
    tables = db.showTables()
    print(tables)

    # create a table
    fields = ["id INT NOT NULL AUTO_INCREMENT PRIMARY KEY",
              "firstname VARCHAR(255)", "lastname VARCHAR(255)"]
    db.createTable("Human", fields)

    # select a row
    fields = ["firstname", "lastname"]
    row = db.selectAll("Human", fields)
    print(row)

    # if you want to use another command, you can use excute method
    db.excute(
        "INSERT INTO human (firstname, lastname) VALUES ('ghaidaa', 'alharbi')")


if __name__ == "__main__":
    main()
