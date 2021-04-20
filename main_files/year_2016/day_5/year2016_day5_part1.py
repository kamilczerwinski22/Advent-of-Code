# --- Day 5: How About a Nice Game of Chess? ---
# You are faced with a security door designed by Easter Bunny engineers that seem to have acquired most of their
# security knowledge by watching hacking movies.
#
# The eight-character password for the door is generated one character at a time by finding the MD5 hash of some
# Door ID (your puzzle input) and an increasing integer index (starting with 0).
#
# A hash indicates the next character in the password if its hexadecimal representation starts with five zeroes.
# If it does, the sixth character in the hash is the next character of the password.
#
# For example, if the Door ID is abc:
#
# - The first index which produces a hash that starts with five zeroes is 3231929, which we find by hashing
# abc3231929; the sixth character of the hash, and thus the first character of the password, is 1.
# - 5017308 produces the next interesting hash, which starts with 000008f82..., so the second character of the
# password is 8.
# - The third time a hash starts with five zeroes is for abc5278568, discovering the character f.

# In this example, after continuing this search a total of eight times, the password is 18f47a30.
#
# Given the actual Door ID, what is the password?

from hashlib import md5
from itertools import count as iter_counter


def decrypt_door(door_id: str) -> str:
    # initial variables
    result_password = ""

    # main logic - for each generated MD5 hash check if it starts with 00000
    for i in iter_counter():
        encoded = md5((door_id + str(i)).encode()).hexdigest()

        if encoded.startswith('00000'):
            result_password += encoded[5]  # take 6th element
            print(result_password)
            if len(result_password) == 8:  # if password length is 8, return it
                return result_password


if __name__ == '__main__':
    my_door_id = "uqwqemis"
    result = decrypt_door(my_door_id)
    print(f"Password for Door Id {my_door_id} is: {result}")
