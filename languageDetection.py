# importing library
from langdetect import detect

text = input("Input any text in any language:")

# print output according to list of ISO 639-1 codes
print(detect(text))
