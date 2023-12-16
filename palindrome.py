from collections import deque


def is_palindrome(s):
    s = ''.join(char.lower() for char in s if char.isalnum())

    char_queue = deque(s)

    while len(char_queue) > 1:
        if char_queue.popleft() != char_queue.pop():
            return False

    return True


def main():
    input_string = "A man a plan a canal Panama"
    result = is_palindrome(input_string)

    if result:
        print(f'string "{input_string}" is palindrome')
    else:
        print(f'string "{input_string}" isn\'t palindrome')

    input_string = "Palindrome"
    result = is_palindrome(input_string)

    if result:
        print(f'string "{input_string}" is palindrome')
    else:
        print(f'string "{input_string}" isn\'t palindrome')


if __name__ == "__main__":
    main()
