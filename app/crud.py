import sqlite3 as sq

db_name = 'cun_students.db'
table_name = 'estudiante'


# CRUD OPERATIONS

def create_student(student):
    execute_query(query='INSERT INTO {} VALUES (?,?,?,?)'.format(table_name), parameters=student)


def get_students():
    return execute_query(query='SELECT * FROM {}'.format(table_name))


def update_student(student):
    execute_query(query='''
                UPDATE {}
                SET doc=?, nombre=?, fecha=?, genero=?
                WHERE doc=?
            '''.format(table_name), parameters=student + (student[0],))


def delete_student(document_number):
    execute_query(query='DELETE FROM {} WHERE doc=?'.format(table_name), parameters=(document_number,))


def get_student(document_number):
    return execute_query(query='SELECT * FROM {} WHERE doc=?'.format(table_name), parameters=(document_number,))


def create_table():
    if not is_table_exists():
        query = '''
                CREATE TABLE {} (
                    doc INT UNIQUE,
                    nombre VARCHAR(40),
                    fecha DATE,
                    genero CHAR(1) 
                )
                '''.format(table_name)

        execute_query(query)


def execute_query(query, parameters=()):
    with sq.connect(db_name) as connection:
        cursor = connection.cursor()
        result = cursor.execute(query, parameters)
        connection.commit()
    return result


def is_table_exists():
    return execute_query('''SELECT count(name) FROM sqlite_master WHERE type='table' AND name=?''',
                         parameters=(table_name,)).fetchone()[0] == 1


def run_crud():
    create_table()
