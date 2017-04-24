# Script to encrypt plaintext using 64bit key (8 character length)
# using given simple symmetrict block encryption method

# Set global variable
key= '';
cipherText = '';

# Read plain text from file
file = open("plain_text.dat", "r");
plain_text = file.read();

# Read key from file
file = open("key.dat", "r");
key = file.read();

# Start encrypting
print "[log] start encrypting....";
for i in range(0, len(plain_text), 4):
    print "[log] processing block " + str((i / 4) + 1) + " with string range [" + str(i) + ":" + str(i + 3) + "]";

    # Ambil substring index ke-i sampai index ke-i+3
    currentString = plain_text[i:i+4];
    print "[log] current string: " + currentString;

    # Pecah key menjadi 2
    leftMost32BitKey = key[0:4];
    rightMost32BitKey = key[4:8];

    # Proses P xor K0 (leftMost64BitKey)
    print "[log] processing P xor K0 (leftMost32BitKey)";
    currentBlockCipherText = ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(currentString, leftMost32BitKey));
    print "[process log] " + currentString + " xor " + leftMost32BitKey + " = " + currentBlockCipherText;

    # Process currentBlockCihperText + K1 (rightMost32BitKey)
    print "[log] processing (P xor K0) + K1 (rightMost32BitKey)";
    currentBlockCipherTextOld = currentBlockCipherText;
    currentBlockCipherText = ''.join(chr((ord(a) + ord(b)) % (1 << 64)) for a,b in zip(currentBlockCipherText, rightMost32BitKey));
    print "[process log] " + currentBlockCipherTextOld + " + " + rightMost32BitKey + " = " + currentBlockCipherText;

    # Concat current block result to main answer
    cipherText += currentBlockCipherText;

print "plain text length = " + str(len(plain_text));
print "Cipher Text: " + cipherText + " with length " + str(len(cipherText)) + " characters";

file = open("cipher_text.dat", "w");
file.write(cipherText);
