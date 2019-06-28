'''
Caesar's Cipher

In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's code or Caesar shift, is one of the simplest and most widely known encryption techniques. 
It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. 
For example, with a left shift of 3, D would be replaced by A, E would become B, and so on.
The method is named after Julius Caesar, who used it in his private correspondence.
'''

def caesarCipher(inputText, step):
	outputText = []

	uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

	for letterText in inputText:
		if letterText in uppercase:

			cryptindex = uppercase.index(letterText)
			newcryptindex = (cryptindex + step)%26
			newLetter = uppercase[newcryptindex]
			outputText.append(newLetter)

		elif letterText in lowercase:

			cryptindex = lowercase.index(letterText)
			newcryptindex = (cryptindex + step)%26
			newLetter = lowercase[newcryptindex]
			outputText.append(newLetter)

	outtext = "".join(outputText)
	return outtext

# Main Program
if __name__== "__main__":
	print("Caesar Cipher Encoder")
	print()
	inputText = input("Enter the text you want to encode using Caesar's Cipher: ")
	print()
	step = int(input("Enter the step index for encoding: "))
	print()
	outputText = caesarCipher(inputText,step)
	print()
	print("Encoded String:", outputText)