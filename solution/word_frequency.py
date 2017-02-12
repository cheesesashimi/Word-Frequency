#!/usr/bin/python

from collections import Counter
from collections import defaultdict
from collections import deque
from json import dumps

def parse_queries(queries):
  """Parses queries from a given list.

  Args:
    queries; list: A list of words to query for, separated by commas.

  Returns:
    A list of sets containing the words to query for.
  """
  return [set(query.split(',')) for query in queries]

def parse_records(records):
  """Parses records from a given list.

  Args:
    records; list: A list of records to parse. Words are comma-separated.

  Returns:
    A dictionary whose keys are the words to query for and whose values
    are a deque of sets which contain that word.
  """
  parsed_records = defaultdict(deque)
  for record in records:
    word_set = set(record.split(','))
    for word in word_set:
      parsed_records[word].append(word_set)
  return parsed_records

def query_records(query, parsed_records):
  """Queries records for a given query.

  Args:
    query; set: The words to query for.

  Returns:
    A Counter object (dictionary) containing the difference of the words in
    the query as keys and the number of their occurances as values. 
  """
  query_results = Counter()
  
  word = list(query)[0]

  for record in parsed_records[word]:
    if query.issubset(record):
      for word_difference in record.difference(query):
        query_results[word_difference] += 1
  return query_results

def output(dictionary):
  """Prints the given dictionary object as a JSON dump.

  Args:
    dictionary; The dictionary to print.
  """
  print(dumps(dictionary, sort_keys=True))

def main():
  """The main body of the program."""
  record_file = open('records.txt', 'ro')
  query_file = open('queries.txt', 'ro')

  print('Parsing records and queries.')

  parsed_queries = parse_queries(query_file.read().splitlines())
  parsed_records = parse_records(record_file.read().splitlines())

  print('Finished parsing, running queries.')

  record_file.close()
  query_file.close()

  for query in parsed_queries:
    output(query_records(query, parsed_records))

if __name__ == '__main__':
  main()
