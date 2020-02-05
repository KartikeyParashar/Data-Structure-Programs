class Deque:
    def __init__(self):
        self.deque = []

    def add_at_front(self,item):
        self.deque.insert(0,item)

    def add_at_rear(self,item):
        self.deque.append(item)

    def remove_from_front(self):
        return self.deque.pop(0)

    def remove_from_rear(self):
        return self.deque.pop()

    def isEmpty(self):
        return self.deque == []

    def size(self):
        return  len(self.deque)

    def check_pallindrome_or_not(self,string):
        for character in string.lower():
            self.add_at_rear(character)
        if self.deque == self.deque[::-1]:
            print(f"Yes, {string} is a Pallindrome")
        else:
            print(f"No, {string} is not a Pallindrome")

