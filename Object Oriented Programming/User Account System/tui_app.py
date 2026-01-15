from typing import List

from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Button, DataTable, Footer, Header, Input, Label, Select, Static

from models.user import User
from services.account_service import AccountService
from storage.json_repository import JsonUserRepository
from storage.database_repository import DatabaseUserRepository
from storage.repository import UserRepository


_ALLOWED_SOCIALS = {"instagram": "Instagram", "facebook": "Facebook", "twitter": "Twitter"}


class UserAccountTUI(App):
    """Textual TUI for the User Account System."""

    BINDINGS = [
        ("ctrl+c", "quit", "Quit"),
        ("f1", "focus_add", "Add form"),
        ("f2", "focus_search", "Search"),
        ("f3", "focus_table", "Table"),
    ]

    CSS = """
    Screen {
        align: center middle;
    }
    #app {
        width: 100%;
        height: 100%;
        padding: 1 2;
    }
    #title {
        text-style: bold;
        color: $text;
        padding: 0 0 1 0;
    }
    .panel {
        border: round $primary;
        padding: 1;
        margin: 0 0 1 0;
        background: $boost;
    }
    .panel-half {
        width: 1fr;
        min-width: 40;
    }
    .panel-title {
        text-style: bold;
        color: $accent;
        padding: 0 0 1 0;
    }
    .field {
        width: 1fr;
        margin: 0 1 0 0;
        min-height: 1;
    }
    .row {
        height: auto;
        padding: 0 0 1 0;
    }
    #status_message {
        height: auto;
        padding: 0 1;
    }
    #table {
        height: 1fr;
        margin: 1 0 0 0;
    }
    """

    def __init__(self) -> None:
        """Initialize the TUI and the service dependency."""
        super().__init__()

        databasePath = "data_stores/user_accounts.db"
        jsonFilePath = "data_stores/user_accounts.json"

        use_db = True
        if use_db:
            repository: UserRepository = DatabaseUserRepository(databasePath)
        else:
            repository = JsonUserRepository(JsonUserRepository)
            
        self._service = AccountService(repository)
        self._current_users: List[User] = []

    def compose(self) -> ComposeResult:
        """Build the Textual layout."""
        yield Header()
        with Vertical(id="app"):
            yield Label("User Account System (Textual TUI)", id="title")
            with Horizontal():
                with Vertical(classes="panel panel-half"):
                    yield Static("Add Account", classes="panel-title")
                    with Horizontal(classes="row"):
                        yield Input(placeholder="Social (Instagram/Facebook/Twitter)", id="social_input", classes="field")
                        yield Input(placeholder="First name", id="first_name_input", classes="field")
                        yield Input(placeholder="Last name", id="last_name_input", classes="field")
                    with Horizontal(classes="row"):
                        yield Input(placeholder="Email (name@domain.com)", id="email_input", classes="field")
                        yield Input(placeholder="Password", id="password_input", password=True, classes="field")
                        yield Button("Add", id="add_button", variant="success")
                        yield Button("Exit", id="exit_button", variant="error")
                with Vertical(classes="panel panel-half"):
                    yield Static("Search / Remove", classes="panel-title")
                    with Horizontal(classes="row"):
                        yield Select(
                            options=[("Social", "social"), ("Name", "name")],
                            value="social",
                            id="search_type",
                        )
                        yield Input(placeholder="Search term", id="search_input", classes="field")
                        yield Button("Search", id="search_button", variant="primary")
                        yield Button("View All", id="view_all_button", variant="default")
                    with Horizontal(classes="row"):
                        yield Input(placeholder="Remove index (e.g., 1)", id="remove_input", classes="field")
                        yield Button("Remove", id="remove_button", variant="warning")
            yield DataTable(id="table")
            yield Label("", id="status_message")
        yield Footer()

    def on_mount(self) -> None:
        """Configure table columns and load data."""
        table = self.query_one("#table", DataTable)
        table.add_columns("Index", "Social", "First Name", "Last Name", "Email")
        self._refresh_table(self._service.list_users())
        # Focus first field for quick entry.
        self.set_focus(self.query_one("#social_input", Input))

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button actions in the TUI."""
        if event.button.id == "add_button":
            self._handle_add()
        elif event.button.id == "search_button":
            self._handle_search()
        elif event.button.id == "view_all_button":
            self._handle_view_all()
        elif event.button.id == "remove_button":
            self._handle_remove()
        elif event.button.id == "exit_button":
            self.exit()

    def action_focus_add(self) -> None:
        """Focus the add form."""
        self.set_focus(self.query_one("#social_input", Input))

    def action_focus_search(self) -> None:
        """Focus the search input."""
        self.set_focus(self.query_one("#search_input", Input))

    def action_focus_table(self) -> None:
        """Focus the data table."""
        self.set_focus(self.query_one("#table", DataTable))

    def _handle_add(self) -> None:
        """Add a new user from the input fields using existing service logic."""
        social_raw = self.query_one("#social_input", Input).value.strip()
        first_name = self.query_one("#first_name_input", Input).value.strip()
        last_name = self.query_one("#last_name_input", Input).value.strip()
        email = self.query_one("#email_input", Input).value.strip()
        password = self.query_one("#password_input", Input).value.strip()

        social = _ALLOWED_SOCIALS.get(social_raw.lower())
        if social is None:
            self._set_status("Social must be Instagram, Facebook, or Twitter.", is_error=True)
            return

        if not first_name or not last_name:
            self._set_status("First and last name are required.", is_error=True)
            return

        if not self._is_email_like(email):
            self._set_status("Email must look like name@domain.com.", is_error=True)
            return

        if not password:
            self._set_status("Password is required.", is_error=True)
            return

        self._service.add_user(User(social, first_name, last_name, email, password))
        self._clear_add_inputs()
        self._refresh_table(self._service.list_users())
        self._set_status("Account added.", is_error=False)

    def _handle_search(self) -> None:
        """Search by social or name and refresh the table."""
        search_type = self.query_one("#search_type", Select).value
        term = self.query_one("#search_input", Input).value.strip()
        if not term:
            self._set_status("Enter a search term.", is_error=True)
            return

        if search_type == "social":
            results = self._service.search_by_social(term)
        else:
            results = self._service.search_by_name(term)

        if not results:
            self._set_status("No matching records found.", is_error=True)
        else:
            self._set_status(f"Found {len(results)} record(s).", is_error=False)
        self._refresh_table(results)

    def _handle_view_all(self) -> None:
        """Show all records in the table."""
        self._refresh_table(self._service.list_users())
        self._set_status("Showing all records.", is_error=False)

    def _handle_remove(self) -> None:
        """Remove a user by index entered in the remove input."""
        raw_value = self.query_one("#remove_input", Input).value.strip()
        if not raw_value.isdigit():
            self._set_status("Enter a numeric index to remove.", is_error=True)
            return

        index = int(raw_value) - 1
        removed = self._service.remove_user_by_index(index)
        if removed:
            self._set_status("Account removed.", is_error=False)
            self._refresh_table(self._service.list_users())
        else:
            self._set_status("Index out of range.", is_error=True)

    def _refresh_table(self, users: List[User]) -> None:
        """Refresh the table with the provided users."""
        table = self.query_one("#table", DataTable)
        table.clear()
        self._current_users = list(users)
        for index, user in enumerate(self._current_users, start=1):
            table.add_row(
                str(index),
                user.social,
                user.first_name,
                user.last_name,
                user.email,
            )

    def _set_status(self, message: str, is_error: bool) -> None:
        """Display a status message with optional error styling."""
        label = self.query_one("#status_message", Label)
        label.update(message)
        label.styles.color = "red" if is_error else "green"

    def _is_email_like(self, value: str) -> bool:
        """Basic email validation requiring '@' and a dot in the domain."""
        if value.count("@") != 1:
            return False
        local_part, domain_part = value.split("@", 1)
        if not local_part or not domain_part:
            return False
        if "." not in domain_part:
            return False
        if any(not section for section in domain_part.split(".")):
            return False
        return True

    def _clear_add_inputs(self) -> None:
        """Clear add-account inputs after a successful add."""
        self.query_one("#social_input", Input).value = ""
        self.query_one("#first_name_input", Input).value = ""
        self.query_one("#last_name_input", Input).value = ""
        self.query_one("#email_input", Input).value = ""
        self.query_one("#password_input", Input).value = ""


if __name__ == "__main__":
    UserAccountTUI().run()

