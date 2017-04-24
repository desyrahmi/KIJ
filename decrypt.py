# Script to encrypt plaintext using 64bit key (8 character length)
# using given simple symmetrict block encryption method

# Set global variable
key= '';
plain_text = '';

# Read plain text from file
file = open("cipher_text.dat", "r");
cipher_text = file.read();

# Read key from file
file = open("key.dat", "r");
key = file.read();

# Start Decrypting
print "[log] start derypting....";
for i in range(0, len(cipher_text), 4):
    print "[log] processing block " + str((i / 4) + 1) + " with string range [" + str(i) + ":" + str(i + 3) + "]";

    # Ambil substring index ke-i sampai index ke-i+3
    currentString = cipher_text[i:i+4];
    print "[log] current string: " + currentString;

    # Pecah key menjadi 2
    leftMost32BitKey = key[0:4];
    rightMost32BitKey = key[4:8];

    # Process C - K1
    print "[log] processing C - K1"
    currentBlockPlainText = ''.join(chr(((ord(a) - ord(b)) + (1 << 64)) % (1 << 64)) for a,b in zip(currentString, rightMost32BitKey));
    print "[process log] " + currentString + " - " + rightMost32BitKey + " = " + currentBlockPlainText;

    # Process (C - K1) xor K0
    print "[log] processing (C - K1) xor K0"
    currentBlockPlainTextOld = currentBlockPlainText;
    currentBlockPlainText = ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(currentBlockPlainText, leftMost32BitKey));
    print "[process log] " + currentBlockPlainText + " - " + leftMost32BitKey + " = " + currentBlockPlainText;

    # Concat current block plain text to main answer
    plain_text += currentBlockPlainText;

print "cipher text length = " + str(len(cipher_text));
print "Plain Text: " + plain_text + " with length " + str(len(plain_text)) + " characters";

file = open("plain_text_decrypt_result.dat", "w");
file.write(plain_text);

