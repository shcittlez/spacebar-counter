import keyboard
from tkinter import Tk, Label, Toplevel, Button

class CounterApp:
    def __init__(self, root):
        self.count = 0
        self.counts = []  # To store previous counts

        # Set up the main window
        self.root = root
        self.root.title("Space Bar Counter")
        self.root.geometry("300x200")

        # Keep the window always on top
        self.root.attributes("-topmost", True)

        # Label to display the count
        self.label = Label(root, text=f"Count: {self.count}", font=("Helvetica", 24))
        self.label.pack(pady=20)

        # Button to open the history window
        self.history_button = Button(root, text="View History", command=self.toggle_history_window)
        self.history_button.pack(pady=10)

        # Set up the new window for displaying previous counts
        self.history_window = None
        self.history_label = None

        # Bind global hotkeys
        keyboard.on_press_key("space", self.increment_count)  # Space key to increment
        keyboard.add_hotkey("ctrl+r", self.reset_count)  # Ctrl+R to reset the count

    def increment_count(self, event=None):
        self.count += 1
        self.update_label()

    def reset_count(self):
        # Save the current count before resetting
        self.counts.append(self.count)

        # Reset the counter
        self.count = 0
        self.update_label()

    def toggle_history_window(self):
        # If the history window is already open, close it
        if self.history_window and self.history_window.winfo_exists():
            self.history_window.destroy()
        else:
            # Open the history window if it's not already open
            self.display_sample_history()

    def display_sample_history(self):
        # Create the history window to the right of the main window
        self.history_window = Toplevel(self.root)
        self.history_window.title("Count History")
        self.history_window.geometry("300x300+{}+{}".format(self.root.winfo_x() + self.root.winfo_width(), self.root.winfo_y()))
        self.history_window.attributes("-topmost", True)

        # Create header labels for the columns
        self.history_label = Label(self.history_window, text="Previous Counts", font=("Helvetica", 14))
        self.history_label.pack(pady=10)

        # Now add the counts to the history window, one by one
        for count in self.counts:
            # Display the counts
            label = Label(self.history_window, text=f"Count: {count}", font=("Helvetica", 12))
            label.pack(pady=5)

    def update_label(self):
        self.label.config(text=f"Count: {self.count}")

    def on_closing(self):
        # Unhook all hotkeys before closing
        keyboard.unhook_all()
        self.root.destroy()

if __name__ == "__main__":
    root = Tk()
    app = CounterApp(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()








