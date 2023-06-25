import tkinter as tk
from typing import List
import collections
from solution import Solution

class GroupAnagramsGUI:
    def __init__(self):
        self.solution = Solution()

        self.window = tk.Tk()
        self.window.title('Group Anagrams')

        self.input_label = tk.Label(self.window, text='Enter a comma-separated list of words:')
        self.input_box = tk.Entry(self.window)

        self.output_label = tk.Label(self.window, text='Grouped anagrams:')
        self.output_box = tk.Text(self.window)

        self.group_button = tk.Button(self.window, text='Group', command=self.group_anagrams)

        self.input_label.pack()
        self.input_box.pack()
        self.output_label.pack()
        self.output_box.pack()
        self.group_button.pack()

    def group_anagrams(self):
        input_str = self.input_box.get().strip()
        if not input_str:
            self.output_box.delete('1.0', tk.END)
            return
        words = input_str.split(',')
        groups = self.solution.groupAnagrams(words)
        output_str = '\n'.join(','.join(group) for group in groups)
        self.output_box.delete('1.0', tk.END)
        self.output_box.insert('1.0', output_str)

if __name__ == '__main__':
    gui = GroupAnagramsGUI()
    gui.window.mainloop()