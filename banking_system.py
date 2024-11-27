
# Function to deposit money into an account
accounts = {
            'John': {'balance': 1000},
            'Jane': {'balance': 500}
        }
def deposit(account: dict, amount: float) -> None:
    account['balance']+=amount

# Function to withdraw money from an account
def withdraw(account: dict, amount: float) -> None:
    if account and account['balance']>=amount:
        account['balance']-=amount
    return None

# Function to transfer money between two accounts
def transfer(from_account: dict, to_account: dict, amount: float) -> None:
    if from_account and to_account and from_account['balance']>=amount :
        from_account['balance']-=amount
        to_account['balance']+=amount
    return None
# Function to add a new account to the system
def add_account(accounts: dict, owner: str, initial_balance: float) -> None:
    if owner not in accounts:
        balance={'balance':initial_balance}
        accounts[owner]=balance
        pass

# Function to find an account by owner's name
def find_account(accounts: dict, owner: str) -> dict:
    if owner in accounts:
        return accounts[owner]
    else:
        return None

# Function to display all accounts in the system
def display_all_accounts(accounts: dict) -> str:
    return '\n'.join([f"{owner}: {account['balance']}" for owner, account in accounts.items()])
