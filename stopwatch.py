import time
import tkinter as tk


class StopwatchTimer:
    """Handle stopwatch timing independently from the GUI."""

    def __init__(self):
        self.start_time = None
        self.elapsed_time = 0.0
        self.running = False

    def start(self):
        """Start or resume the stopwatch."""
        if self.running:
            return

        self.start_time = time.monotonic() - self.elapsed_time
        self.running = True

    def stop(self):
        """Pause the stopwatch and preserve elapsed time."""
        if not self.running:
            return

        self.elapsed_time = time.monotonic() - self.start_time
        self.running = False

    def reset(self):
        """Reset the stopwatch to zero."""
        self.start_time = None
        self.elapsed_time = 0.0
        self.running = False

    def get_elapsed_time(self):
        """Return the current elapsed time in seconds."""
        if self.running:
            return time.monotonic() - self.start_time

        return self.elapsed_time


class Stopwatch:
    def __init__(self, root):
        self.root = root
        self.root.title("Stopwatch")
        self.root.resizable(False, False)

        self.timer = StopwatchTimer()

        self.time_label = tk.Label(
            root,
            text="00:00:00",
            font=("Verdana", 30, "bold"),
            width=10
        )
        self.time_label.pack(padx=20, pady=(20, 10))

        button_frame = tk.Frame(root)
        button_frame.pack(pady=(0, 20))

        self.start_button = tk.Button(
            button_frame,
            text="Start",
            width=7,
            command=self.start
        )
        self.start_button.pack(side=tk.LEFT, padx=3)

        self.stop_button = tk.Button(
            button_frame,
            text="Stop",
            width=7,
            state=tk.DISABLED,
            command=self.stop
        )
        self.stop_button.pack(side=tk.LEFT, padx=3)

        self.reset_button = tk.Button(
            button_frame,
            text="Reset",
            width=7,
            state=tk.DISABLED,
            command=self.reset
        )
        self.reset_button.pack(side=tk.LEFT, padx=3)

    def start(self):
        """Start or resume the stopwatch."""
        self.timer.start()

        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.reset_button.config(state=tk.NORMAL)

        self.update_display()

    def stop(self):
        """Pause the stopwatch."""
        self.timer.stop()

        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

        self.update_display()

    def reset(self):
        """Reset the stopwatch and update the display."""
        self.timer.reset()

        self.time_label.config(text="00:00:00")
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.reset_button.config(state=tk.DISABLED)

    def update_display(self):
        """Update the displayed elapsed time."""
        if not self.timer.running:
            return

        total_seconds = int(self.timer.get_elapsed_time())
        hours, remainder = divmod(total_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        self.time_label.config(
            text=f"{hours:02d}:{minutes:02d}:{seconds:02d}"
        )

        self.root.after(100, self.update_display)


def main():
    root = tk.Tk()
    Stopwatch(root)
    root.mainloop()


if __name__ == "__main__":
    main()
    