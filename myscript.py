#!/usr/bin/python
import pathos 
c = pathos.core.copy('test.py', destination='ubuntu@ec2-34-227-200-184.compute-1.amazonaws.com:~/test.py'
s = pathos.core.execute('python test.py',host='ubuntu@ec2-34-227-200-184.compute-1.amazonaws.com')
print s.response() 
