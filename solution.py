import unittest
from typing import List
import collections
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s.lower():
                count[ord(c) - ord("a")] += 1
            ans[tuple(count)].append(s)
        return list(ans.values())


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://example.com')
        self.solution = Solution()

    def tearDown(self):
        self.driver.quit()

    def test_empty_input_gui(self):
        input_element = self.driver.find_element_by_id('input')
        input_element.send_keys('')
        submit_button = self.driver.find_element_by_id('submit')
        submit_button.click()
        output_element = self.driver.find_element_by_id('output')
        actual_output = output_element.text.strip().split('\n')
        self.assertEqual(actual_output, [''])

    def test_single_word_input_gui(self):
        input_element = self.driver.find_element_by_id('input')
        input_element.send_keys('abc')
        submit_button = self.driver.find_element_by_id('submit')
        submit_button.click()
        output_element = self.driver.find_element_by_id('output')
        actual_output = output_element.text.strip().split('\n')
        self.assertEqual(actual_output, [['abc']])

    def test_multiple_groups_gui(self):
        input_element = self.driver.find_element_by_id('input')
        input_element.send_keys('eat,tea,tan,ate,nat,bat')
        submit_button = self.driver.find_element_by_id('submit')
        submit_button.click()
        output_element = self.driver.find_element_by_id('output')
        actual_output = output_element.text.strip().split('\n')
        expected_output = [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
        self.assertEqual(len(expected_output), len(actual_output))
        for group in expected_output:
            with self.subTest(group=group):
                self.assertIn(group, actual_output)

    def test_case_sensitivity_gui(self):
        input_element = self.driver.find_element_by_id('input')
        input_element.send_keys('a,A')
        submit_button = self.driver.find_element_by_id('submit')
        submit_button.click()
        output_element = self.driver.find_element_by_id('output')
        actual_output = output_element.text.strip().split('\n')
        expected_output = [['a', 'A']]
        self.assertEqual(len(expected_output), len(actual_output))
        for group in expected_output:
            with self.subTest(group=group):
                self.assertIn(group, actual_output)

    def test_single_character_input_gui(self):
        input_element = self.driver.find_element_by_id('input')
        input_element.send_keys('a,b,c')
        submit_button = self.driver.find_element_by_id('submit')
        submit_button.click()
        output_element = self.driver.find_element_by_id('output')
        actual_output = output_element.text.strip().split('\n')
        expected_output = [['a'], ['b'], ['c']]
        self.assertEqual(len(expected_output), len(actual_output))
        for group in expected_output:
            with self.subTest(group=group):
                self.assertIn(group, actual_output)

    def test_max_length_input_gui(self):
        input_element = self.driver.find_element_by_id('input')
        input_element.send_keys('a'*100 + ',' + 'b'*100 + ',' + 'c'*100)
        submit_button = self.driver.find_element_by_id('submit')
        submit_button.click()
        output_element = self.driver.find_element_by_id('output')
        actual_output = output_element.text.strip().split('\n')
        expected_output = [[('a'*100), ('b'*100), ('c'*100)]]
        self.assertEqual(len(expected_output), len(actual_output))
        for group in expected_output:
            with self.subTest(group=group):
                self.assertIn(group, actual_output)

    def test_higher_boundary_gui(self):
        input_element = self.driver.find_element_by_id('input')
        input_element.send_keys(('a'*5000 + ',')*2000)
        submit_button = self.driver.find_element_by_id('submit')
        submit_button.click()
        output_element = self.driver.find_element_by_id('output')
        actual_output = output_element.text.strip().split('\n')
        expected_output = [[('a'*5000)*2000]]
        self.assertEqual(len(expected_output), len(actual_output))
        for group in expected_output:
            with self.subTest(group=group):
                self.assertIn(group, actual_output)


if __name__ == '__main__':
    unittest.main(failfast=True)