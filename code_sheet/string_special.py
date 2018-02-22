#using three quotes
para_str = """this is a long string that is made up of
several lines and non-printable characters such as
TAB  \t  and they will show up that way when displayed.
NEWLINEs within the string, whether explicitly given like
this within the brackets  \n , or just a NEWLINE within
the variable assignment will also show up.
"""
print (para_str)
#using normal vs r
print ('C:\\nowhere')

print (r'C:\\nowhere')
#using string formating
template = '%.3f %s haha $%d';
str1 = template  %(4.88, 'hola', 2)
print(str1)