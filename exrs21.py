"""
https://www.codewars.com/kata/550527b108b86f700000073f

https://www.codewars.com/kata/55f4a44eb72a0fa91600001e
"""


class CreateMessage(str):
    def __call__(self, string=''):
        return CreateMessage(f'{self} {string}'.strip())


print(CreateMessage("Hello")("World!")("how")("are")("you?")() == "Hello World! how are you?")
