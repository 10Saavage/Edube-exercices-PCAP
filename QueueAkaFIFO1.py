class QueueError(Exception):  # Choose base class for the new exception.
    def __init__(self):
        Exception.__init__(self)
    #
    #  Write code here
    #


class Queue:
    def __init__(self):
        self.__Queue_list = []
        #
        # Write code here
        #

    def put(self, elem):
        self.__Queue_list.insert(0, elem)
        #
        # Write code here
        #

    def get(self):
        try:
            val = self.__Queue_list[-1]
            del self.__Queue_list[-1]
            return val
        except QueueError:
            print("Queue error")
        #
        # Write code here
        #


que = Queue()
que.put(1)
que.put("dog")
que.put(False)
try:
    for i in range(4):
        print(que.get())
except:
    print("Queue error")
