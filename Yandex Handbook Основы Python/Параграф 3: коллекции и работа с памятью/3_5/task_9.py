file1_name = input().strip()
file2_name = input().strip()
result = []
with open(file1_name, encoding="UTF-8") as file_in:
    for line in file_in.readlines():
        line_without_tabs = line.replace('\t', '')        
        clean_words = line_without_tabs.split() 
        if clean_words: 
                glued_line = ' '.join(clean_words)
                result.append(glued_line)
with open(file2_name, "w", encoding="UTF-8") as file_out:
    print(*result, sep='\n', file=file_out)