import sqlite3

class Schema:
    def __init__(self):
        self.conn = sqlite3.connect('todo.db')
        self.create_user_table()
        self.create_to_do_table()

    def create_to_do_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS "Todo" (
            id INTEGER PRIMARY KEY,
            Title TEXT,
            Description TEXT,
            _is_done boolean,
            _is_deleted boolean,
            CreatedOn Date DEFAULT CURRENT_DATE,
            DueDate Date,
            UserId INTEGER FOREIGNKEY REFERENCES User(_id)
        );
        """

        self.conn.execute(query)

    def create_user_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS "User" (
            id INTEGER PRIMARY KEY,
            Name TEXT,
            Email TEXT
        );
        """
        self.conn.execute(query)

class ToDoModel:
    TABLENAME = "TODO"

    def __init__(self):
        self.conn = sqlite3.connect('todo.db')

    def create(self, text, description):
        query = f'insert into {TABLENAME} ' \
                f'(Title, Description) ' \
                f'values ("{text}","{description}")'

        result = self.conn.execute(query)
        return result

    def update(self, text, description, id):
        query = f'update  {TABLENAME} ' \
                f'set Title = "{text}", Description = "{description}" ' \
                f'where id = "{id}"'

        result = self.conn.execute(query)
        return result

    def delete(self, id):
        query = f'delete from {TABLENAME} ' \
                f'where id = "{id}"'

        result = self.conn.execute(query)
        return result

    def list(self):
        query = f'select * from {TABLENAME}'

        result = self.conn.execute(query)
        return result

if __name__ == "__main__":
    Schema()
    app.run(debug=True)
