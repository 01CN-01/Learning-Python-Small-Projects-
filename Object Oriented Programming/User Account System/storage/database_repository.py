import sqlite3
from typing import List

from models.user import User
from storage.repository import UserRepository


class DatabaseUserRepository(UserRepository):
    """SQLite-backed user repository (schema is created externally)."""

    def __init__(self, db_path: str) -> None:
        self._db_path = db_path

    def load_all(self) -> List[User]:
        with sqlite3.connect(self._db_path) as conn:
            cursor = conn.execute(
                """
                SELECT 
                    social, first_name, last_name, email, password
                FROM 
                    users
                ORDER BY 
                    id ASC
                """
            )
            rows = cursor.fetchall()
        return [User(social, first, last, email, pw) for social, first, last, email, pw in rows]

    def load_by_social(self, social: str) -> List[User]:
        with sqlite3.connect(self._db_path) as conn:
            cursor = conn.execute(
                """
                SELECT 
                    social, first_name, last_name, email, password
                FROM 
                    users
                WHERE 
                    LOWER(social) = LOWER(?)
                ORDER BY 
                    id ASC
                """,
                (social,),
            )
            rows = cursor.fetchall()
        return [User(social, first, last, email, pw) for social, first, last, email, pw in rows]

    def load_by_name_wildcard(self, name: str) -> List[User]:
        wildcard = f"%{name}%"
        with sqlite3.connect(self._db_path) as conn:
            cursor = conn.execute(
                """
                SELECT 
                    social, first_name, last_name, email, password
                FROM 
                    users
                WHERE 
                    LOWER(first_name) LIKE LOWER(?) OR
                    LOWER(last_name) LIKE LOWER(?)
                ORDER BY 
                    id ASC
                """,
                (wildcard, wildcard),
            )
            rows = cursor.fetchall()
        return [User(social, first, last, email, pw) for social, first, last, email, pw in rows]

    def delete_all(self) -> None:
        with sqlite3.connect(self._db_path) as conn:
            conn.execute("DELETE FROM users")
            conn.commit()

    def save_all(self, users: List[User]) -> None:
        """Persist all users (replace existing records)."""
        self.delete_all()
        with sqlite3.connect(self._db_path) as conn:
            conn.executemany(
                """
                INSERT INTO users (social, first_name, last_name, email, password)
                VALUES (?, ?, ?, ?, ?)
                """,
                [(u.social, u.first_name, u.last_name, u.email, u.password) for u in users],
            )
            conn.commit()

    # Alias to clarify intent for updates.
    def update_all(self, users: List[User]) -> None:
        self.save_all(users)

