#
# Learning in Tamil - Python 
# Example file - XML
#

import xml.dom.minidom

def getUserNodeValue(user, elementName):
    rc = []
    for element in user.getElementsByTagName(elementName):
        for node in element.childNodes:
            if node.nodeType == node.TEXT_NODE:
                rc.append(node.data)
        return ''.join(rc)

def main():
    # load and parse the input XML file using parse function
    xmlDocument = xml.dom.minidom.parse("input.xml")

    print(xmlDocument.firstChild.tagName)
    print(xmlDocument.firstChild.getAttribute("name"))
    print(xmlDocument.toxml(encoding=None, standalone=None))
    print(xmlDocument.toprettyxml(indent='  ', newl=''))

    users = xmlDocument.getElementsByTagName("user")
    print ("Found %d users in the XML" % users.length)

    for user in users:
        for childNode in user.childNodes:
            print(childNode.nodeName)
        print("id: ", user.getAttribute("id"))
        print("\tfirstname: ",getUserNodeValue(user, "firstname"))
        print("\tlastname: ",getUserNodeValue(user, "lastname"))
        print("\tlocation: ",getUserNodeValue(user, "location"))
        print("\trole: ",getUserNodeValue(user, "role"))
        pages = user.getElementsByTagName("page")
        print("No of pages: ",pages.length)
        for page in pages:
            print("\t\t",page.getAttribute("link"))

        if user.getAttribute("id") == "001":
            print("Adding new page to the user")
            newPage = xmlDocument.createElement("page")
            newPage.setAttribute("link", "payroll")
            pages = user.getElementsByTagName('pages')
            pages[0].appendChild(newPage)
            pages = user.getElementsByTagName("page")
            print("No of pages: ",pages.length)
            for page in pages:
                print("\t\t",page.getAttribute("link"))
        
if __name__ == "__main__":
    main()
