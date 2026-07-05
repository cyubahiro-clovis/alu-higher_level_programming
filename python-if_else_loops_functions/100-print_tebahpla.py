#!/usr/bin/python3
print('{}'.format(''.join(chr(122 - i) if i % 2 == 0 else chr(122 - i - 32) for i in range(26))), end='')  # noqa: E501
