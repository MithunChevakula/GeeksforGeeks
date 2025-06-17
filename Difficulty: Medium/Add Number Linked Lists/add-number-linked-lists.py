class Solution:
    def reverse(self,head):
        orinext = None
        prev = None
        while head:
            orinext = head.next
            head.next = prev
            prev = head
            head = orinext
        return prev
    def addTwoLists(self, num1, num2):
        # code here
        # 1.remove 0 from num1,num2

        while num1:
            if num1.data != 0:
                break
            num1 = num1.next
            
        while num2:
            if num2.data != 0:
                break
            num2 = num2.next

        # 2.reverse num1,num2
        num1 = self.reverse(num1)
        num2 = self.reverse(num2)

        # 3.add and buid answer        
        prev = None
        carry = 0
        while num1 and num2:
            add = num1.data + num2.data + carry
            carry = add//10
            add = add%10
            n = Node(add)
            n.next = prev
            prev = n
            num1 = num1.next
            num2 = num2.next
        
        while num1:
            add = num1.data + carry
            carry = add//10
            add = add%10
            n = Node(add)
            n.next = prev
            prev = n
            num1 = num1.next
        
        while num2:
            add = num2.data + carry
            carry = add//10
            add = add%10
            n = Node(add)
            n.next = prev
            prev = n
            num2 = num2.next
        
        while carry != 0:
            add = carry
            carry = add//10
            add = add%10
            n = Node(add)
            n.next = prev
            prev = n
        
        return prev