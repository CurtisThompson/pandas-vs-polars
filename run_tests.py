from src import test_read, test_filter_select, test_group_aggregation


# TEST: Load Data
test_read.run_tests()
print()

# TEST: Filter Data and Select Columns
test_filter_select.run_tests()
print()

# TEST: Group And Aggregate
test_group_aggregation.run_tests()
print()