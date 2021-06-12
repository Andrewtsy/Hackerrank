

def get_attr_number(node):
    score = len(node.attrib)
    elements = node.findall('.//')
    for ele in elements:
        score += len(ele.attrib)
    return score

