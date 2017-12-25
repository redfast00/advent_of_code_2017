class RoundBuffer:
    def __init__(self, buffer):
        self._buffer = buffer
    def get_next(self, idx):
        if idx == len(self._buffer) - 1:
            return self._buffer[0]
        return self._buffer[idx+1]
    def get_at_offset(self, offset):
        return self._buffer[offset%len(self._buffer)]
captcha = input()
buffer = RoundBuffer(captcha)
total = 0
for idx, element in enumerate(captcha):
    if element == buffer.get_next(idx):
        total += int(element)
print(total)
total = 0
for idx, element in enumerate(captcha):
    if element == buffer.get_at_offset(idx + len(captcha)//2):
        total += int(element)
print(total)
