
import sqlite3
from config import DATABASE_PATH


def get_connection():
    connection = sqlite3.connect(DATABASE_PATH)
    connection.execute("PRAGMA foreign_keys = ON")
    return connection


def initialize_database():

    with get_connection() as connection:

        connection.execute("""
            CREATE TABLE IF NOT EXISTS operations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                original_path TEXT NOT NULL,
                destination_path TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                undone INTEGER DEFAULT 0
            )
        """)


def record_move(original_path, destination_path):

    with get_connection() as connection:

        cursor = connection.execute("""
            INSERT INTO operations (
                original_path,
                destination_path
            )
            VALUES (?, ?)
        """, (
            str(original_path),
            str(destination_path)
        ))

        return cursor.lastrowid


def get_last_move():

    with get_connection() as connection:

        return connection.execute("""
            SELECT id, original_path, destination_path
            FROM operations
            WHERE undone = 0
            ORDER BY id DESC
            LIMIT 1
        """).fetchone()


def mark_undone(operation_id):

    with get_connection() as connection:

        connection.execute("""
            UPDATE operations
            SET undone = 1
            WHERE id = ?
        """, (operation_id,))


def get_history():

    with get_connection() as connection:

        return connection.execute("""
            SELECT id, original_path, destination_path,
                   created_at, undone
            FROM operations
            ORDER BY id DESC
        """).fetchall()
