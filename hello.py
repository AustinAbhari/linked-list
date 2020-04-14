#!/usr/bin/python
"idk lol"
class Node:
    'Node linked lists!'

    def __init__(self, value):
        self.value = value
        self.next = None

    def displayValue(self):
        print self.value


class linkedListForward:
    'linked List!'
    first = None
    last = None
    current = None
    nodeCount = 0

    def __init__(self):
        'thanks'

    def printAll(self):
        "Print all the Nodes"
        if self.first is None:
            print "There are no Nodes in the list\n"
        else:
            print "[" + str(self.first.value) + "]",
            current = self.first
            index = 1
            while current.next is not None:
                print "->",
                index += 1
                print "[" + str(current.next.value) + "]",
                current = current.next
        print ''

    def printFL(self):
        "Print the first and last"
        if self.first != None:
            print "first:"
            print self.first.value
        else:
            print "There are no Nodes in the list\n"
            return 1
        if self.last != None:
            print "last:"
            print self.last.value
        else:
            print "There are no Nodes in the list\n"
            return 1


    def addNode(self, node):
        "Add that node!"
        if self.first is None:
            self.first = node
            self.nodeCount = 1
            self.last = self.first
        else:
            self.last.next = node
            self.last = node
            self.nodeCount += 1

    def printNodeCount(self):
        "Print the node amount!"
        print "Node Count:"
        print self.nodeCount

    def deleteNode(self, index):
        "Delete that node!"
        i = 1
        current = self.first
        previous = None
        print index
        if self.nodeCount == 1 and index == 1:
            self.first = None
            print "Successfully Deleted"
            self.nodeCount -= 1
            self.printAll()
            return
        elif self.nodeCount < index:
            print "Invalid Index nodeCount < index"
            return
        elif index <= 0:
            print "Invalid Index"
            return
        while current.next is not None and i < index:
            temp = current.next
            previous = current
            current = temp
            i += 1
        if previous != None and current.next != None:
            previous.next = current.next
            print "Successfully Deleted"
            self.nodeCount -= 1
            self.printAll()
        elif previous is None and current.next != None:
            self.first = current.next
            print "Successfully Deleted"
            self.nodeCount -= 1
            current = None
            self.printAll()
        elif previous != None and current.next is None:
            previous.next = None
            print "Successfully Deleted"
            self.nodeCount -= 1
            self.printAll()

    def swap(self, index1, index2):
        "Swappin"
        if index1 < 0 or index1 > self.nodeCount:
            print 'Invalid index 1'
            return
        if index2 < 0 or index2 > self.nodeCount:
            print 'Invalid index 2'
            return
        current1 = self.first
        current2 = self.first
        for x in range(1, index1):
            temp1 = current1.next
            previous1 = current1
            current1 = temp1
        for y in range(1, index2):
            temp2 = current2.next
            previous2 = current2
            current2 = temp2
        previous1.next = current2
        current2.next = current1.next
        previous2.next = current1
        current1.next = current2.next

def main():
    "run it breh lol"
    command = ''
    print "--------------------------------------\n"
    print "Welcome to your own linked list!"
    print 'Commands:\n -quit\n -print all\n -print last\n -print fl\n -test\n -delete\n -add\n'
    print "--------------------------------------"
    ll = linkedListForward()
    while True:
        command = raw_input("Please enter an Input: ")
        if command == "quit" or command == 'q' or command == "Quit":
            break
        elif command == "add":
            print "\nWhat value do you want to add?\n"
            value = raw_input("Value:")
            node = Node(value)
            ll.addNode(node)
            print "Successfully Added!\n"
        elif command == "print all":
            print ''
            ll.printAll()
            print ''
        elif command == "node count":
            print ''
            ll.printNodeCount()
            print ''
        elif command == "print fl":
            print ''
            ll.printFL()
            print ''
        elif command == 'test':
            value = int(raw_input("Amount of nodes?:"))
            for x in range(1, value+1):
                node = Node(x)
                ll.addNode(node)
            print '\nAdded test nodes\n'
            ll.printAll()
            print ''
        elif command == 'commands':
            print '\nCommands:\n -quit\n -print all\n -print last\n -print fl\n -test\n -delete\n -add\n'
        elif command == "delete":
            print ''
            index = int(raw_input("index:"))
            ll.deleteNode(index)
            print ''
        elif command == 'swap':
            index1 = int(raw_input("First Index: "))
            index2 = int(raw_input("second Index: "))
            ll.swap(index1, index2)
        else:
            print "Invalid Command"
    print "left"
main()
