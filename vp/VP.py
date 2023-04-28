import xml.etree.ElementTree as ET

def parse_revision_xml(file_path):
    mytree = ET.parse(file_path)
    myroot = mytree.getroot()

    revisions = {}

    for tag in myroot:
        user = tag.attrib.get("user")
        if user in revisions:
            revisions[user] += 1
        else:
            revisions[user] = 1

    return revisions

def sort_revisions(revisions):
    return sorted(revisions.items(), key=lambda x: x[1], reverse=True)
