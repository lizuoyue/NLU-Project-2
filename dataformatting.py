def readData(filePath, sourcePath, targetPath):
	f = open(filePath, 'r')
	sourceWriter = open(sourcePath, 'w')
	targetWriter = open(targetPath, 'w')
	line = f.readline()
	while line:
		sentences = line.strip().split('\t')
		sourceWriter.write(sentences[0]+"\n")
		targetWriter.write(sentences[1]+"\n")
		sourceWriter.write(sentences[1]+"\n")
		targetWriter.write(sentences[2]+"\n")
		line = f.readline()
	f.close()
	sourceWriter.close()
	targetWriter.close()

print("training data...\n")
readData("../data/Training_Shuffled_Dataset.txt","../data/train/source.txt","../data/train/target.txt")
print("validation data...\n")
readData("../data/Validation_Shuffled_Dataset.txt","../data/validation/source.txt","../data/validation/target.txt")