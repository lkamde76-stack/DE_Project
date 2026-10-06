import mysql.connector

def get_db_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="1234",
        database="expense_manager"
    )
    if connection.is_connected():
        print("Connection is successfully established")
        print(connection.get_server_info())
    else:
        print("Connection failed")

    cursor = connection.cursor(dictionary=True)
    return connection,cursor

def fetch_all_records(cursor):
    connection ,cursor = get_db_connection()
    cursor.execute("select * from expense_manager.expenses limit 10")

    expenses = cursor.fetchall()
    for expense in expenses:
        print(expense)

    cursor.close()
    connection.close()

def fetch_expenses_for_date(expense_date):
    connection,cursor = get_db_connection()
    cursor.execute("select * from expenses where expense_date=%s",(expense_date,))
    expenses = cursor.fetchall()
    for expense in expenses:
        print(expense)

    cursor.close()
    connection.close()

if __name__ == "__main__":
    # fetch_all_records(get_db_connection())
    fetch_expenses_for_date('2024-09-01')
