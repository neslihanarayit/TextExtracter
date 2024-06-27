import easyocr
reader = easyocr.Reader(['en'])
with open("result-text.txt") as resultText:
    latestresult = resultText.read()
result = reader.readtext('image-to-text-online.png')
for i in range(len(result)):
    with open("result-text.txt", mode="a") as resultText:
        resultText.write(result[i][1])
