###################
# use to parse my own xml file
# https://github.com/huangshaowei/myxmlparser.git
##################

import re
import codecs
import Mytools

class MyNode:
   def __init__(self,parent,data):
      self.data = data
      self.tool = Mytools()
      self.childNodes = []
      self.parent = parent
      self.childTagName = None
      pass
   def parser(self):
      self.name = self.tool.getTagName(self.data)
      self.attr = self.tool.getAttributes(self.data)
      if not self.tool.IsChildrenExist(self.data):
         self.text = self.tool.GetText(self.data)
      pass
   def getChildren(self,tag_name):
       if self.tool.IsChildrenExist(self.data):
          childdatas = self.tool.getChildrenData(self.data)
          self.childTagName = self.tool.getTagName(childdatas)
          subdatas = self.tool.splitChildrenData(childdatas,self.childTagName)
          for subdata in subdatas:
             node = MyNode(self,subdata)
             node.parser()
             self.childNodes.append(node)
       return self.childNodes
       pass

class MyElementTree:
#input fileName or data
    def __init__(self,data):
       self.data = data
    def __init__(self,filepath,codetype):
       file = codecs.open(filepath,"r",codetype)
       text = file.read()
       __text__=text.replace("\r\n","") #remove \r\n
       try:
          __text__=__text__[text.index("?>")+2:]
       except:
          return
       self.data = __text__
    def parser(self):
       return MyNode(None,self.data)


# test
p = MyElementTree("G:\\freecad-8-26-all-success\\Mod\\Database\\1.xml","utf8")
root = p.parser()
root.parser()
nodes = root.getChildren("table")