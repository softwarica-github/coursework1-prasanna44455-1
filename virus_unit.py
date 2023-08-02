import unittest
import tkinter as tk
from tkinter import messagebox
from unittest.mock import patch

import virus_scanner

class TestVirusScanner(unittest.TestCase):

    @patch('virus_scanner.filedialog.askopenfilename', return_value='/path/to/file.exe')
    def test_scan_file(self, mock_askopenfilename):
        # Create the main window
        window = tk.Tk()
        window.title("Antivirus Scanner")
        window.geometry("500x300")

        # Create label to display the scan result
        result_label = tk.Label(window, text="", font=("Arial", 18))

        # Mock the loading_screen() function
        with patch('virus_scanner.loading_screen') as mock_loading_screen:
            # Call the scan_file() function
            virus_scanner.scan_file()

            # Assert that loading_screen() was called
            mock_loading_screen.assert_called_once()

            # Mock the process_file() function
            with patch('virus_scanner.process_file') as mock_process_file:
                # Simulate the after() callback
                window.after(3000, lambda: mock_process_file('/path/to/file.exe'))

                # Assert that process_file() was called with the correct file path
                mock_process_file.assert_called_once_with('/path/to/file.exe')

        # Cleanup
        window.destroy()