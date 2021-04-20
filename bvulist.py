class bvulist(list):
    def prepend(self, data):
        self.insert(0, data)

    def pop_front(self):
        return self.pop(0)

    def pop_back(self):
        return self.pop()
