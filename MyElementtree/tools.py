
#this class is for myelementparser to operator string
#https://github.com/huangshaowei/myxmlparser.git

import re

#data must be string
class Mytools:
   def IsChildrenExist(self,data):
       
       return data.count("/") > 1
   def splitChildrenData(self,data,tag_name):
       p = re.compile(r"<\s*[^/]\w*\s*[^>]*>+")
       begin = p.findall(data)
       p = re.compile(r"<\s*/\w*\s*[^>]*>+")
       end = p.findall(data)
       if len(begin) != len(end):
          return None
       res = []
       res +=begin
       for item in res:
          if item.find(tag_name) == -1:
              begin.remove(item)
       res = []
       res +=end
       for item in res:
          if item.find(tag_name) == -1:
              end.remove(item)
       res =[]
       for i in range(0,len(begin)):
          index = data.find(begin[i])
          bindex = data.find(end[i]) + len(end[i])
          res.append(data[index:bindex])
          data=data[bindex:]
       return res
   def getChildrenData(self,data):
       p = re.compile(r"<\s*[^/]\w*\s*[^>]*>+")
       begin = p.findall(data)
       p = re.compile(r"<\s*/\w*\s*[^>]*>+")
       end   = p.findall(data)
       end.reverse()
       index = data.find(begin[0])+len(begin[0])
       bindex= data.find(end[0])
       while data[index:bindex].find(begin[0]) != -1:
          bindex = data.find(end[0],bindex+1)
       return data[index:bindex]
   def getTagName(self,data):
       p = re.compile(r"<\s*(\w*)")
       s = p.findall(data)
       return s[0]
   def getAttributes(self,data):
       p = re.compile(r"<\s*(\S+)(\s[^>]*)?>[\s\S]*<\s*\/\1\s*>")
       fileds = p.findall(data)[0]
       if len(fileds) == 1:
           return None
       res = {}
       p = re.compile(r"\s*(\w*)\s*=\s*(\S*)")
       tem_list = p.findall(fileds[1])
       for tem in tem_list:
           res[tem[0]]=tem[1]
       return res
   def GetText(self,data):
       p = re.compile(r"<[\s\S]*>([\s\S]*)<\s*/[\s\S]*>")
       s = p.findall(data)[0]
       return s.strip()


