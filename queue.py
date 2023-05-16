# queue Data structure
print('queue ds is imported')


class Queue:
    def __init__(self):
        self.q = list()

    def queue_isempty(self):
        if len(self.q) == 0:
            return True
        else:
            return False

    def queue_push(self, x):
        self.q.append(x)

    def queue_pop(self):
        if len(self.q) == 0:
            print('Empty queue')
            return None
        else:
            del (self.q[0])
            return None

    def front(self):
        if len(self.q) != 0:
            return self.q[0]
        else:
            print('Empty Queue')
            return None
