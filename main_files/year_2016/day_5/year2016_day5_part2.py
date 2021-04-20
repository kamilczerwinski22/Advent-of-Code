# --- Part Two ---
# As the door slides open, you are presented with a second door that uses a slightly more inspired security mechanism.
# Clearly unimpressed by the last version (in what movie is the password decrypted in order?!), the Easter Bunny
# engineers have worked out a better solution.
#
# Instead of simply filling in the password from left to right, the hash now also indicates the position within the
# password to fill. You still look for hashes that begin with five zeroes; however, now, the sixth character
# represents the position (0-7), and the seventh character is the character to put in that position.
#
# A hash result of 000001f means that f is the second character in the password. Use only the first result for each
# position, and ignore invalid positions.
#
# For example, if the Door ID is abc:
#
# - The first interesting hash is from abc3231929, which produces 0000015...; so, 5 goes in position 1: _5______.
# - In the previous method, 5017308 produced an interesting hash; however, it is ignored, because it specifies an
# invalid position (8).
# - The second interesting hash is at index 5357525, which produces 000004e...; so, e goes in position 4: _5__e___.
#
# You almost choke on your popcorn as the final character falls into place, producing the password 05ace8e3.
#
# Given the actual Door ID and this new method, what is the password? Be extra proud of your solution if it uses a
# cinematic "decrypting" animation.


from hashlib import md5
from itertools import count as iter_counter


def decrypt_door(door_id: str) -> str:
    # initial variables
    result_password = []

    # main logic - for each generated MD5 hash check if it starts with 00000<digit_lees_that_eight>
    for i in iter_counter():
        encoded = md5((door_id + str(i)).encode()).hexdigest()

        if encoded.startswith('00000') and encoded[5].isdigit():
            # check if digit (0-7) and not already present
            if int(encoded[5]) < 8 and int(encoded[5]) not in [num for num, _ in result_password]:
                result_password.append((int(encoded[5]), encoded[6]))  # take 7th element with position
                print(result_password)
                if len(result_password) == 8:  # if password length is 8, put it together and return
                    return "".join(char for _, char in sorted(result_password))


if __name__ == '__main__':
    my_door_id = "uqwqemis"
    result = decrypt_door(my_door_id)
    print(f"Second password for Door Id {my_door_id} is: {result}")
