def output_to_file(output, content):
    if output:
        with open(output, "w", encoding="utf-8") as file:
            file.write(content + "\n")
    else:
        print(content)