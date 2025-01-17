def romanToInt(s):
        d = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        counter = 0
        counterpart = 0
        st = []
        
        for i in range(len(s) - 1):  
            if d.get(s[i]) < d.get(s[i + 1]):
                st.append(s[i] + s[i + 1])
                
        for i in range(len(st)):
            counter += abs(d.get(st[i][0]) - d.get(st[i][1]))
        
        for i in range(len(s) - 1):
            for x in st:
                if s[i : i + 2] == x:
                    s = s.replace(s[i : i + 2] , '')
                    
        for i in s:
            counterpart += d.get(i)
                
        return counter + counterpart