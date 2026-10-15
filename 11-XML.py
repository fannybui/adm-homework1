# ==================================================
# EXERCISE 1 : XML 1 - Find the Score
# ==================================================

import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    score = len(node.attrib)

    for child in node:
        score += get_attr_number(child)

    return score

def f_get_attr_number():
    n = int(input("Enter N the number of XML code lines : "))
    lines = []
    for _ in range(n):
        lines.append(input("Enter the N lines of your XML document : "))
    xml = '\n'.join(lines)
    root = etree.fromstring(xml)
    print(get_attr_number(root))

# ==================================================
# EXERCISE 2 : XML2 - Find the Maximum Depth
# ==================================================

import xml.etree.ElementTree as etree

maxdepth = 0
def depth(elem, level):
    global maxdepth
    level += 1
    if level > maxdepth:
        maxdepth = level
    for child in elem:
        depth(child, level)

def max_depth():
    n = int(input("Enter N the number of XML code lines : "))
    xml = ""
    for i in range(n):
        xml =  xml + input("Enter the N lines of your XML document : ") + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)

# ==================================================
# MAIN MENU
# ==================================================

def main():
    while True:
        print("\n================================")
        print("XML")
        print("================================")
        print("1. XML 1 - Find the Score")
        print("2. XML2 - Find the Maximum Depth")
        print("0. Exit")
        print("================================")

        choice = input("Choose an exercise: ")

        if choice == "1":
            f_get_attr_number()

        elif choice == "2":
            max_depth()

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


# Start the program
if __name__ == "__main__":
    main()