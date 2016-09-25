#!/usr/bin/python3.4
__Author__ = "Danny Mcwaves"


class HTML:
    """
    i am trying so hard to nail this thing once and for all. to be able to write simple html tags thing and then to
    write this tags thing and then put in this attributes and all that stuff.
    """
    ROOT = """
<!DOCTYPE html>
<html>
<head>
    %(headTags)s
</head>
<body>
    %%(bodyTags)s
</body>
</html>
    """

    def __init__(self, htmlHead):
        self.__head(htmlHead)

    def __head(self, content):
        self.ROOT = self.ROOT % {'headTags': content}

    def body(self, content):
        content = "\n\t" + content + "%(bodyTags)s"
        self.ROOT = self.ROOT % {'bodyTags': content}

    def __str__(self):
        return str(self.ROOT % {'bodyTags': ""})

    class Element:
        """
        this is supposed to implement the writing of the elements and the element stuff.
        """
        def __init__(self, name, *args):
            self.__elementName = name
            self.__singleTags = ["link", "meta", "img", "br", "hr", "input"]

            if list(args).__len__() != 0:
                attributes = " ".join(list(args))
                self.__startTag = "<"+self.__elementName+" "+attributes+">"
            else:
                self.__startTag = "<"+self.__elementName+"> "

            if self.__elementName in self.__singleTags:
                self.element = self.__startTag.replace(self.__startTag[-2::], "/> ")
            else:
                self.element = "\n\t" + self.__startTag + "%s" + "\n\t</"+self.__elementName+">\n"

        def innerHTML(self, content):
            content = "\n\t\t" + content + "%s"
            self.element = self.element % content
            return self

        def __str__(self):
            return str(self.element % "")


if __name__ == '__main__':
    headTag = """<meta charset='utf-8'/>
    <link href='index.css' rel='stylesheet'>"""
    html = HTML(headTag)
    html.body("what the fuck am i doing over here now")
    html.body("Am i sure i can really get this done easily")

    div = html.Element("div", "class='myClass'")
    div.innerHTML("yhs this is me doing my shit stuff and all that crap").innerHTML("what is this")
    div.innerHTML("creating some more shit right now").innerHTML("and some more too over here").innerHTML("blow")
    div.innerHTML("some errors")

    html.body(div.__str__())
    html.body("who the fuck am i")
    html.body("I think i just might have an idea over here now")
    html.body("Or what am i going to now")
    print(html)