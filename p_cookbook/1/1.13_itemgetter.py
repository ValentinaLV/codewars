from operator import itemgetter

rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

# working faster
rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))
print(rows_by_fname)
print(rows_by_uid)
rows_by_lfname = sorted(rows, key=itemgetter('lname', 'fname'))
print(rows_by_lfname)

# min-max
max_row_uid = max(rows, key=itemgetter('uid'))
min_row_uid = min(rows, key=itemgetter('uid'))
print(max_row_uid)
print(min_row_uid)

# working slowly
rows_by_fname2 = sorted(rows, key=lambda r: r['fname'])
rows_by_uid2 = sorted(rows, key=lambda r: r['uid'])
print(rows_by_fname2)
print(rows_by_uid2)

max_row_uid2 = max(rows, key=lambda r: r['uid'])
min_row_uid2 = min(rows, key=lambda r: r['uid'])
print(max_row_uid2)
print(min_row_uid2)
