class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_string = ""
        t_string = ""

        string_stack = []

        for i in s:
            if i == "#":
                if(string_stack):
                    string_stack.pop()
            else:
                string_stack.append(i)
        
        s_string = "".join(string_stack)

        string_stack = []

        for i in t:
            if i == "#":
                if(string_stack):
                    string_stack.pop()
            else:
                string_stack.append(i)
        
        t_string = "".join()

        return (t_string==s_string)