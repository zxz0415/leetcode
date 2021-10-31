from unittest import TestCase

from data_source import get_leetcode_question_everyday


class Test(TestCase):
    def test_get_leetcode_question_every_day(self):
        get_leetcode_question_everyday()
        #self.fail()
