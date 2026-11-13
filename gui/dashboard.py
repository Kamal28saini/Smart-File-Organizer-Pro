
import os
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

from src.file_scanner import scan_files
from src.duplicate_detector import find_duplicates
from src.organizer import organize_files, undo_last_move
from src.database import get_history


class FileOrganizerApp:

    def __init__(self, root):

        self.root = root

        self.root.title("Smart File Organizer Pro")
        self.root.geometry("1100x700")
        self.root.minsize(850, 550)

        self.selected_folder = tk.StringVar()
        self.files = []

        self.setup_style()
        self.create_widgets()

    # ---------------- STYLE ----------------

    def setup_style(self):

        style = ttk.Style()

        style.theme_use("clam")

        style.configure(
            "Treeview",
            rowheight=28,
            font=("Arial", 10)
        )

        style.configure(
            "Treeview.Heading",
            font=("Arial", 10, "bold")
        )

    # ---------------- GUI ----------------

    def create_widgets(self):

        header = ttk.Frame(
            self.root,
            padding=15
        )

        header.pack(fill="x")

        ttk.Label(
            header,
            text="Smart File Organizer Pro",
            font=("Arial", 22, "bold")
        ).pack(anchor="w")

        ttk.Label(
            header,
            text="Organize files • Detect duplicates • Track history"
        ).pack(anchor="w", pady=5)

        # Folder selection

        folder_frame = ttk.LabelFrame(
            self.root,
            text="Folder Selection",
            padding=10
        )

        folder_frame.pack(
            fill="x",
            padx=15,
            pady=10
        )

        ttk.Entry(
            folder_frame,
            textvariable=self.selected_folder
        ).pack(
            side="left",
            fill="x",
            expand=True,
            padx=5
        )

        ttk.Button(
            folder_frame,
            text="Browse",
            command=self.browse_folder
        ).pack(side="left", padx=5)

        ttk.Button(
            folder_frame,
            text="Scan Files",
            command=self.scan_folder
        ).pack(side="left", padx=5)

        # File table

        table_frame = ttk.Frame(
            self.root,
            padding=10
        )

        table_frame.pack(
            fill="both",
            expand=True,
            padx=15
        )

        columns = (
            "name",
            "category",
            "size",
            "path"
        )

        self.tree = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings",
            selectmode="extended"
        )

        self.tree.heading(
            "name",
            text="File Name"
        )

        self.tree.heading(
            "category",
            text="Category"
        )

        self.tree.heading(
            "size",
            text="Size (KB)"
        )

        self.tree.heading(
            "path",
            text="Path"
        )

        self.tree.column(
            "name",
            width=200
        )

        self.tree.column(
            "category",
            width=120
        )

        self.tree.column(
            "size",
            width=100
        )

        self.tree.column(
            "path",
            width=500
        )

        scrollbar = ttk.Scrollbar(
            table_frame,
            orient="vertical",
            command=self.tree.yview
        )

        self.tree.configure(
            yscrollcommand=scrollbar.set
        )

        self.tree.pack(
            side="left",
            fill="both",
            expand=True
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

        # Buttons

        action_frame = ttk.Frame(
            self.root,
            padding=15
        )

        action_frame.pack(fill="x")

        ttk.Button(
            action_frame,
            text="Organize Files",
            command=self.organize
        ).pack(side="left", padx=5)

        ttk.Button(
            action_frame,
            text="Find Duplicates",
            command=self.show_duplicates
        ).pack(side="left", padx=5)

        ttk.Button(
            action_frame,
            text="Undo Last Move",
            command=self.undo
        ).pack(side="left", padx=5)

        ttk.Button(
            action_frame,
            text="View History",
            command=self.show_history
        ).pack(side="left", padx=5)

        ttk.Button(
            action_frame,
            text="Preview File",
            command=self.preview_file
        ).pack(side="left", padx=5)

        # Status bar

        self.status = ttk.Label(
            self.root,
            text="Ready",
            relief="sunken",
            anchor="w"
        )

        self.status.pack(
            fill="x",
            side="bottom"
        )

    # ---------------- BROWSE ----------------

    def browse_folder(self):

        folder = filedialog.askdirectory()

        if folder:

            self.selected_folder.set(folder)

            self.scan_folder()

    # ---------------- SCAN ----------------

    def scan_folder(self):

        folder = self.selected_folder.get()

        if not folder:

            messagebox.showwarning(
                "Folder Required",
                "Please select a folder first."
            )

            return

        try:

            self.files = scan_files(folder)

            self.refresh_table()

            self.status.config(
                text=f"Found {len(self.files)} files"
            )

        except Exception as error:

            messagebox.showerror(
                "Scan Error",
                str(error)
            )

    def refresh_table(self):

        for item in self.tree.get_children():

            self.tree.delete(item)

        for file in self.files:

            size_kb = round(
                file["size"] / 1024,
                2
            )

            self.tree.insert(
                "",
                "end",
                values=(
                    file["name"],
                    file["category"],
                    size_kb,
                    file["path"]
                )
            )

    # ---------------- PREVIEW ----------------

    def preview_file(self):

        selected = self.tree.selection()

        if not selected:

            messagebox.showwarning(
                "Select File",
                "Please select a file from the table."
            )

            return

        values = self.tree.item(
            selected[0],
            "values"
        )

        file_path = values[3]

        messagebox.showinfo(
            "File Preview",
            f"Name: {values[0]}\n"
            f"Category: {values[1]}\n"
            f"Size: {values[2]} KB\n"
            f"Path: {file_path}"
        )

    # ---------------- ORGANIZE ----------------

    def organize(self):

        if not self.files:

            messagebox.showwarning(
                "No Files",
                "Please scan a folder first."
            )

            return

        selected = self.tree.selection()

        if selected:

            file_paths = [
                self.tree.item(item, "values")[3]
                for item in selected
            ]

        else:

            file_paths = [
                file["path"]
                for file in self.files
            ]

        confirm = messagebox.askyesno(
            "Confirm Organization",
            f"Organize {len(file_paths)} files?"
        )

        if not confirm:

            return

        moved_count, errors = organize_files(
            file_paths
        )

        self.status.config(
            text=f"Organized {moved_count} files"
        )

        message = (
            f"{moved_count} files organized successfully."
        )

        if errors:

            message += (
                f"\n\n{len(errors)} files could not be moved."
            )

        messagebox.showinfo(
            "Organization Complete",
            message
        )

        self.scan_folder()

    # ---------------- DUPLICATES ----------------

    def show_duplicates(self):

        folder = self.selected_folder.get()

        if not folder:

            messagebox.showwarning(
                "Folder Required",
                "Please select a folder first."
            )

            return

        paths = []

        for root, _, filenames in os.walk(folder):

            for filename in filenames:

                paths.append(
                    os.path.join(root, filename)
                )

        duplicates = find_duplicates(paths)

        if not duplicates:

            messagebox.showinfo(
                "Duplicates",
                "No duplicate files found."
            )

            return

        result = []

        for file_hash, duplicate_paths in duplicates.items():

            result.append(
                f"SHA-256: {file_hash[:16]}..."
            )

            result.extend(duplicate_paths)

            result.append("")

        self.show_text_window(
            "Duplicate Files",
            "\n".join(result)
        )

    # ---------------- UNDO ----------------

    def undo(self):

        confirm = messagebox.askyesno(
            "Undo",
            "Restore the last moved file?"
        )

        if not confirm:

            return

        result = undo_last_move()

        if result:

            messagebox.showinfo(
                "Undo",
                "Last file move successfully undone."
            )

            self.scan_folder()

        else:

            messagebox.showwarning(
                "Undo",
                "No undoable operation found."
            )

    # ---------------- HISTORY ----------------

    def show_history(self):

        history = get_history()

        window = tk.Toplevel(self.root)

        window.title("Operation History")
        window.geometry("1000x450")

        columns = (
            "id",
            "source",
            "destination",
            "date",
            "status"
        )

        tree = ttk.Treeview(
            window,
            columns=columns,
            show="headings"
        )

        tree.heading("id", text="ID")
        tree.heading("source", text="Original Path")
        tree.heading("destination", text="Destination")
        tree.heading("date", text="Date")
        tree.heading("status", text="Status")

        tree.column("id", width=50)
        tree.column("source", width=300)
        tree.column("destination", width=300)
        tree.column("date", width=180)
        tree.column("status", width=100)

        for record in history:

            operation_id, source, destination, date, undone = record

            tree.insert(
                "",
                "end",
                values=(
                    operation_id,
                    source,
                    destination,
                    date,
                    "Undone" if undone else "Moved"
                )
            )

        tree.pack(
            fill="both",
            expand=True
        )

    # ---------------- TEXT WINDOW ----------------

    def show_text_window(self, title, content):

        window = tk.Toplevel(self.root)

        window.title(title)
        window.geometry("850x450")

        text = tk.Text(
            window,
            wrap="word"
        )

        scrollbar = ttk.Scrollbar(
            window,
            command=text.yview
        )

        text.configure(
            yscrollcommand=scrollbar.set
        )

        text.insert(
            "1.0",
            content
        )

        text.configure(
            state="disabled"
        )

        text.pack(
            side="left",
            fill="both",
            expand=True
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )


def launch_app():

    root = tk.Tk()

    FileOrganizerApp(root)

    root.mainloop()
