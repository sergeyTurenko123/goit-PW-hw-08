from models import Authors, Quotes
from abc import ABC, abstractmethod
import connect
import redis
from redis_lru import RedisLRU

client = redis.StrictRedis(host="localhost", port=6379, password=None)
cache = RedisLRU(client)
@cache
def name(args):
    for author in Authors.objects(fullname__startswith=' '.join(args)):
        return([quot.tags for quot in Quotes.objects(author=author)])

def tag(args):
    for quot in Quotes.objects(tags__startswith=' '.join(args)):
        return quot.quote

def tags(args):
    for quot in Quotes.objects(tags__in=(args)):
        print (quot.quote)
    
def parse_input(user_input):
    name, *args = user_input.split()
    name = name.strip().lower()
    return name, *args

class AbstractBot(ABC):
    @abstractmethod
    def return_help(self):
        raise NotImplementedError()

class SimpleBot(AbstractBot):

    def return_help(self, commands):
        print("Available commands:")
        for command in commands:
            print(f"- {command}")

def main():

    view = SimpleBot()
    view.return_help(['name', 'tag', 'tags', 'close', 'exit', 'hello'])

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "name":
            print (name(args))
        elif command == "tag":
            print (tag(args))
        elif command == "tags":
            return (tags(args))

if __name__ == "__main__":
    
    main()