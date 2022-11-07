#
# Learning in Tamil - Python 
# Example file - HTML
#

from html.parser import HTMLParser

class MyParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.start_tags = []
        self.end_tags = []
        self.all_data = []
        self.p_tag_data = []
        self.comments = []
        self.capture = False

    # function to handle HTML start tags
    def handle_starttag(self, tag, attrs):
        print("Tag: ",tag)
        self.start_tags.append(tag)

        if attrs.__len__() > 0:
            print ("Attributes in :",tag)
            for a in attrs:
                print ("", a[0],"=",a[1])
                
        # find line number and position
        position = self.getpos() 
        print (tag, "at line: ", position[0], " & position ", position[1])

        if tag in ('p','h1'):
            self.capture = True
        
    # function to handle HTML  end tags
    def handle_endtag(self, tag):
        self.end_tags.append(tag)
        if tag in ('p','h1'):
            self.capture = False
    # function to handle text data or the tag contents
    def handle_data(self, data):
        if not data.isspace():
            self.all_data.append(data)
            if self.capture:
                self.p_tag_data.append(data)
        
    # function to handle HTML comments
    def handle_comment(self, data):
        self.comments.append(data)

def main():
    # Create an instance for the parser and feed the HTML data
    parser = MyParser()
      
    # open the HTML 
    htmlFile = open("input.html","r")
    if htmlFile.mode == "r":
        contents = htmlFile.read() # read the HTML file contents
        parser.feed(contents)
    
    print("start_tags: ", parser.start_tags)
    print("end_tags: ", parser.end_tags)
    print("all_data: ", parser.all_data)
    print("p_tag_data: ", parser.p_tag_data)
    print("comments: ", parser.comments)
    print ("Paragraph tags:", parser.p_tag_data)

if __name__ == "__main__":
    main()
  
