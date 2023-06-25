gui.py
This file contains the implementation of the Graphical User Interface (GUI) for the Group Anagrams application. The GUI allows the user to enter a comma-separated list of words and groups the anagrams together.

Dependencies
tkinter: a standard Python library for creating GUI applications.
Classes
GroupAnagramsGUI: the main class that creates the GUI window and handles the user input and output.
Methods
init(self): initializes the GUI window and creates the input, output, and button widgets.
group_anagrams(self): groups the anagrams entered by the user and displays the output in the output box.
Usage
To run the application, execute the gui.py file in the command line:

Copy
python gui.py
solution.py
This file contains the implementation of the Solution class that performs the actual grouping of anagrams. The groupAnagrams method takes a list of words and groups the anagrams together.

Classes
Solution: a class that contains the groupAnagrams method.
Methods
groupAnagrams(self, strs: List[str]) -> List[List[str]]: groups the anagrams in the given list of words and returns a list of grouped anagrams.
Usage
To use the Solution class, import it into your Python code and create an instance of the class:

python
Copy
from solution import Solution

solution = Solution()
Then, call the groupAnagrams method with a list of words to group the anagrams:

python
Copy
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
groups = solution.groupAnagrams(words)
print(groups)  # [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
I hope this helps! Let me know if you have any further questions.
