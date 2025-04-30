from lxml import etree 

xml_file = "bookstore.xml" 
dtd_file = "bookstore.dtd" 
xml_doc = etree.parse(xml_file) 
dtd = etree.DTD(dtd_file) 
if dtd.validate(xml_doc): 
    print("XML is valid according to DTD") 
else: 
    print("DTD Validation failed") 

xsd_file = "bookstore.xsd" 
xmlschema_doc = etree.parse(xsd_file) 
xmlschema = etree.XMLSchema(xmlschema_doc)
if xmlschema.validate(xml_doc): 
    print("XML is valid according to XSD") 
else: 
    print("XSD Validation failed")
