file = open("/workspace/Zuri_python/zuri.text", "rt")
data = file.read()
words = data.split()

print('Number of words in text file :', len(words))
