from services.account_service import AccountService
from models.user import User
from utils import validators


_COLOR_RESET = "\033[0m"
_COLOR_TITLE = "\033[95m"
_COLOR_SECTION = "\033[94m"
_COLOR_SUCCESS = "\033[92m"
_COLOR_WARNING = "\033[93m"
_COLOR_ERROR = "\033[91m"
_COLOR_DIM = "\033[90m"


def _color(text: str, color_code: str) -> str:
    """Wrap text with a color code for CLI output."""
    return f"{color_code}{text}{_COLOR_RESET}"


def _print_header(title: str) -> None:
    """Print a styled section header with spacing."""
    print()
    print(_color("=" * 34, _COLOR_TITLE))
    print(_color(f"{title:^34}", _COLOR_TITLE))
    print(_color("=" * 34, _COLOR_TITLE))


def _print_subheader(title: str) -> None:
    """Print a smaller section header."""
    print()
    print(_color(title, _COLOR_SECTION))
    print(_color("-" * len(title), _COLOR_SECTION))


def run_menu(service: AccountService) -> None:
    """Run the main menu loop that interacts with the user."""
    while True:
        _print_header("User Account System")
        print(_color("1) Add Account", _COLOR_SECTION))
        print(_color("2) Remove Account", _COLOR_SECTION))
        print(_color("3) View All Accounts", _COLOR_SECTION))
        print(_color("4) Search", _COLOR_SECTION))
        print(_color("5) Exit", _COLOR_SECTION))

        option_menu = validators.get_int_in_range("Choose an option: ", 1, 5)
        if option_menu == 1:
            _add_account_flow(service)
        elif option_menu == 2:
            _remove_account_flow(service)
        elif option_menu == 3:
            _view_all_accounts_flow(service)
        elif option_menu == 4:
            _search_flow(service)
        elif option_menu == 5:
            print(_color("Goodbye.", _COLOR_DIM))
            break


def _add_account_flow(service: AccountService) -> None:
    """Prompt the user for account details and save them."""
    _print_subheader("Add Account")
    count = validators.get_int_in_range("How many accounts do you want to add?: ", 1, 100)
    for _ in range(count):
        social = validators.get_social("Enter social name (Instagram/Facebook/Twitter): ")
        first_name = validators.get_non_empty("Enter first name: ")
        last_name = validators.get_non_empty("Enter last name: ")
        email = validators.get_email("Enter email address: ")
        password = _confirm_password()
        service.add_user(User(social, first_name, last_name, email, password))
        print(_color("Account added.", _COLOR_SUCCESS))
        print()


def _remove_account_flow(service: AccountService) -> None:
    """Show accounts, then prompt for which one to remove."""
    _print_subheader("Remove Account")
    users = service.list_users()
    if not users:
        print(_color("No accounts to remove.", _COLOR_WARNING))
        return

    _print_users(users)
    selection = validators.get_int_in_range(
        "Select the number corresponding to the user to delete: ",
        1,
        len(users),
    )
    removed = service.remove_user_by_index(selection - 1)
    if removed:
        print(_color("Account removed.", _COLOR_SUCCESS))
    else:
        print(_color("Invalid selection.", _COLOR_ERROR))


def _view_all_accounts_flow(service: AccountService) -> None:
    """Display all stored accounts."""
    _print_subheader("All Accounts")
    users = service.list_users()
    if not users:
        print(_color("No accounts found.", _COLOR_WARNING))
        return
    _print_users(users)


def _search_flow(service: AccountService) -> None:
    """Prompt for a search type and display matches."""
    _print_subheader("Search Accounts")
    print(_color("1) Search by Social", _COLOR_SECTION))
    print(_color("2) Search by Name", _COLOR_SECTION))
    option = validators.get_int_in_range("Select one option: ", 1, 2)
    if option == 1:
        social = validators.get_non_empty("Enter social name to search: ")
        results = service.search_by_social(social)
    else:
        name = validators.get_non_empty("Enter name to search: ")
        results = service.search_by_name(name)

    if not results:
        print(_color("No accounts found.", _COLOR_WARNING))
        return
    _print_users(results)


def _confirm_password() -> str:
    """Prompt for a password twice and return the confirmed value."""
    while True:
        password = validators.get_non_empty("Enter password: ")
        confirmation = validators.get_non_empty("Confirm password: ")
        if password == confirmation:
            return password
        print(_color("Passwords do not match. Try again.", _COLOR_ERROR))


def _print_users(users: list[User]) -> None:
    """Print user details in a consistent format."""
    print(_color(f"Total records: {len(users)}", _COLOR_DIM))
    for index, user in enumerate(users, start=1):
        print()
        print(_color(f"Record {index}", _COLOR_SECTION))
        print(_color("-" * 30, _COLOR_DIM))
        print(f"Social: {user.social}")
        print(f"Name: {user.first_name} {user.last_name}")
        print(f"Email: {user.email}")
        print(f"Password: {user.password}")
        print(_color("-" * 30, _COLOR_DIM))
