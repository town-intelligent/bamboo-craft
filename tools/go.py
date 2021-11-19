import os

def replace(filename):
    file_target = open(filename, "r")
    list_source = file_target.readlines()
    file_target.close()

    for index in range(len(list_source)):

        if "h2 font-weight-bold" in list_source[index].rstrip("\n"):
            del list_source[index]
            list_source.insert(index, "<p class=\"h2 font-weight-bold\"><a href=\"../index.html\">竹山竹藝</a></p>")

            # File
            textfile = open("output/" + filename, "w")
            for element in list_source:
                textfile.write(element.rstrip("\n") + "\n")
        
            textfile.close()

            return


# List dir
list_file = os.listdir("./")

for str_filename in list_file:
  if ".html" in str_filename:
      replace(str_filename)
