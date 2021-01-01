def transformClient(file):
    transformed_lines = []
    with open(file) as fp:
        line = fp.readline()
        while line:
            line = line.strip()
            line = line.replace('"', "'")
            line = 'client.println("'+line+'");'
            line = line.replace('\n', '')
            transformed_lines.append(line)
            line = fp.readline()
    return transformed_lines

def createNewFile(transformed, finalFile):
    final_text_file = open(finalFile, 'w+')
    for line_ in transformed:
        final_text_file.write(line_+'\n')

createNewFile(transformClient('index.html'), 'control.ino')
