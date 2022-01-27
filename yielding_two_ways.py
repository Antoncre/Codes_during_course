from collections import deque
from types import coroutine


friends = deque(('Antoni', 'Dawid', 'Olek', 'Jakub'))


@coroutine
def friend_upper():
    while friends:
        friend = friends.popleft().upper()
        greeting = yield
        print(f'{greeting} {friend}')


async def greet(g):
    print("starting...")
    await g
    print("Ending...")
greeter = greet(friend_upper())
greeter.send(None)
greeter.send('Cześć')
print("Rewriting all greetings data...")
listss = 5 ** 37000
print(listss)
greeter.send('Cześć')

