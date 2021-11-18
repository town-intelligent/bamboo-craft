def replace(item, list_content):
    f = open("./source.html")
    list_source = f.readlines()
    f.close()

    counters = 0
    for index in range(len(list_source)):
        if "CONTENT" == list_source[index].rstrip("\n"):
            del list_source[index]


            counter  = index
            items = 0
            for obj in list_content:
                items = items + 1
                list_source.insert(counter, "<p>" + obj.rstrip("\n"))
                counter = counter + 1

            # File
            textfile = open("output/" + str(item-1) + ".html", "w")
            for element in list_source:
                textfile.write(element.rstrip("\n") + "\n")
            textfile.close()

            return

# Read input
f = open("./input.txt")
lines_input = f.readlines()
f.close()

items = 1
for index in range(len(lines_input)):
    if lines_input[index].rstrip("\n") == str(items):
        content = []
        items = items + 1

        counter = index
        while lines_input[counter].rstrip("\n") != str(items):
            content.append(lines_input[counter].rstrip("\n"))
            counter = counter + 1

        # Replace
        replace(items-1, content)
