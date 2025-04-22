
from BankDatabase import BankDatabase, SQLCursor
from BankDatabaseInfo import DATABASENAME

create_accounts_table_formula = """
CREATE TABLE IF NOT EXISTS Accounts (
    User_ID VARCHAR(255) PRIMARY KEY,
    name VARCHAR(255),
    lastname VARCHAR(255),
    Year INT,
    mail VARCHAR(255),
    password VARCHAR(255)
);
"""

create_cards_table_formula = """
CREATE TABLE IF NOT EXISTS cards (
    User_ID VARCHAR(255),
    card_ID VARCHAR(255) PRIMARY KEY,
    card_type VARCHAR(255),
    balance DECIMAL(10,2),
    FOREIGN KEY(User_ID) REFERENCES Accounts(User_ID)
);
"""

def Create_tables_if_not_exsists():
    SQLCursor.execute(f"SELECT COUNT(*) FROM information_schema.tables WHERE table_schema = '{DATABASENAME}' AND table_name = 'accounts'")

    accounts_table_exsists = SQLCursor.fetchone()[0]

    if accounts_table_exsists == 0:

        SQLCursor.execute(create_accounts_table_formula)

        BankDatabase.commit()

        print('Accounts Database created!')
    
    else:
        print('Accounts Database already exsists')

    SQLCursor.execute(f"SELECT COUNT(*) FROM information_schema.tables WHERE table_schema = '{DATABASENAME}' AND table_name = 'cards'")

    cards_table_exsists = SQLCursor.fetchone()[0]

    if cards_table_exsists == 0:

        SQLCursor.execute(create_cards_table_formula)

        BankDatabase.commit()

        print('Cards Database created!')
    
    else:
        print('Cards Database already exsists')       

Create_tables_if_not_exsists()