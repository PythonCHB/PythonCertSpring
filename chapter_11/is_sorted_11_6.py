#! /usr/bin/env python
#
# Write a function called is_sorted that takes a list as a parameter and returns
# True if the list is sorted in ascending order and False otherwise. You can
# assume (as a precondition) that the elements of the list can be compared with
# the relational operators <, >, etc.
# For example, is_sorted([1,2,2]) should return True and is_sorted(['b','a'])
# Write a function called is_sorted that takes a list as a parameter and returns
# True if the list is sorted in ascending order and False otherwise. You can
# assume (as a precondition) that the elements of the list can be compared with
# the relational operators <, >, etc.
# For example, is_sorted([1,2,2]) should return True and is_sorted(['b','a'])
# should return False.

def is_sorted(my_list) :
    """This function returns is_sorted if each element in the list is greater
than or equal to the element before it"""
    for i in range(1, len(my_list)) :
        if my_list[i] < my_list[i-1] :
            return False
    return True

if __name__ == "__main__" :
    def test_is_sorted( a_list, expected ) :
        if is_sorted(a_list) == expected :
            print "Success: ", a_list, ( "is" if expected else "is not"),\
                  "sorted, as expected"
        else :
            print "FAILURE: ", a_list, "returned", r, "expected", expected

test_is_sorted([1,2,2], True)
test_is_sorted(['b','a'], False)
test_is_sorted([1, 2, 4, 5, 4], False)
test_is_sorted([1, 2, -1, 3, 4], False)
