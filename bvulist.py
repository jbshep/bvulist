class bvulist(list):
    ''' Documentation will go here! '''

    def prepend(self, data):
        self.insert(0, data)

    def pop_front(self):
        #return self.pop(0)
        # This will make the test fail.
        return self.pop()

    def pop_back(self):
        return self.pop()
