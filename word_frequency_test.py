#!/usr/bin/python

from collections import Counter
from collections import deque
import word_frequency
import unittest


class WordFrequencyTests(unittest.TestCase):

  def setUp(self):
    self.records = [
      'red,yellow,green,black',
      'red,green,blue,black',
      'yellow,green,blue',
      'yellow,blue,black'
    ]

    record1 = set(['red', 'yellow', 'green', 'black'])
    record2 = set(['red', 'green', 'blue', 'black'])
    record3 = set(['yellow', 'green', 'blue'])
    record4 = set(['yellow', 'blue', 'black'])

    self.parsed_records = {
      'blue' : deque([record2, record3, record4]),
      'black' : deque([record1, record2, record4]),
      'green' : deque([record1, record2, record3]),
      'yellow' : deque([record1, record3, record4]),
      'red' : deque([record1, record2])
    }

    self.queries = [
      'blue,yellow',
      'black,green'
    ]

    self.parsed_queries = [
      set(['blue', 'yellow']),
      set(['black', 'green'])
    ]

  def testParseRecords(self):
    result = word_frequency.parse_records(self.records)
    self.assertEquals(result, self.parsed_records)

  def testParseQueries(self):
    result = word_frequency.parse_queries(self.queries)
    self.assertEquals(result, self.parsed_queries)

  def testQueryRecords(self):
    query_1, query_2 = self.parsed_queries

    expected_result_1 = Counter({"black": 1, "green": 1})
    expected_result_2 = Counter({"blue": 1, "red": 2, "yellow": 1})

    result_1 = word_frequency.query_records(query_1, self.parsed_records)
    result_2 = word_frequency.query_records(query_2, self.parsed_records)

    self.assertEquals(result_1, expected_result_1)
    self.assertEquals(result_2, expected_result_2)

if __name__ == '__main__':
  unittest.main()
