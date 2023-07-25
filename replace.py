path = r'C:\Users\David\Desktop\cso2pack_csgo\leet.txt'

with open(path, 'r') as fin, open(r'C:\Users\David\Desktop\output.txt', 'w') as fout:
    for path in fin:
        if "models" in path:
            fout.write(f'AddFileToDownloadsTable("{path.strip()}");\n')
