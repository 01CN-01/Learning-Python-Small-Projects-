from services.account_service import AccountService
from storage.database_repository import DatabaseUserRepository
from storage.json_repository import JsonUserRepository
from ui.menu import run_menu

def main() -> None:
    """Create app services and start the menu loop."""

    databasePath = "data_stores/user_accounts.db"
    jsonFilePath = "data_stores/user_accounts.json"

    # Toggle repository implementation here:
    use_db = True
    if use_db:
        repository = DatabaseUserRepository(databasePath)
    else:
        repository = JsonUserRepository(jsonFilePath)

    service = AccountService(repository)
    run_menu(service)

if __name__ == "__main__":
    main()