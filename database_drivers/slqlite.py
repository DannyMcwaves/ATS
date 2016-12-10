
"""
sqlite database driver.
"""
import sqlite3


class SqlInterface:

    def __init__(self, base_name):
        """
        define some basic functions for reading and writing data to the database.
        """
        self._connect = sqlite3.connect(base_name)
        cursor = self._connect.cursor()
        self.execute = cursor.execute
        self.execute_many = cursor.executemany
        self.fetchall = cursor.fetchall
        self.fetchone = cursor.fetchone
        self.Error = self._connect.Error

    def __table_schema(self, name):
        """
        the format of saving data in the database.
        """
        table = """
        create table {tablename}(
            id int auto_increment,
            name varchar(50) not null default "log",
            data MEDIUMTEXT not null
        )
        """.format(tablename=name)
        try:
            self.execute(table)
        except self._connect.DatabaseError as err:
            return err
        except self._connect.Error as err:
            return err
        finally:
            return True

    def create_table(self):
        """
        creating a table with the name provided
        """
        state = self.__table_schema("pdfData")
        if state is True:
            return state
        else:
            raise state

    def insert(self, identity, name, data):
        """
        insert data into the database.
        """
        insert_command = "insert into pdfData(id, name, data) values ({}, '{}', '{}')".format(identity, name, data)
        try:
            self.execute(insert_command)
        except self.Error as err:
            raise err
        else:
            return True

    def update(self, name, data):
        """
        we are updating the data where the name. overriding pre-existent data.
        """
        update_command = "update pdfData set data={} where name={}".format(data, name)
        try:
            self.execute(update_command)
        except self.Error as err:
            raise err
        else:
            return True

    def read(self):
        self.execute("select * from pdfData")
        return self.fetchall()

