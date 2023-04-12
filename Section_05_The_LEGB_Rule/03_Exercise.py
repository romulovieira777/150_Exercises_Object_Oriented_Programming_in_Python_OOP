"""
Exercise No. 03

A global variable counter is given with an incorrectly implemented update_counter() function. Correct the implementation
of the update_counter() function so that you can modify the counter variable from this function. Then call the
update_counter() function.

Tip:
    Use the global statement.

Expected result:

    2
"""
counter = 1


def update_counter():
    global counter
    counter += 1
    print(counter)


update_counter()
