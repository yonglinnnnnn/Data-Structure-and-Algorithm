# Name: Xu Yong Lin
# Admin no: 212033J
# Tutorial group: IT2153-01

# additional feature: handle small caps, mix caps

# class for doing encryption and decryption using a Caesar cipher
class CaesarCipher:
    # construct Caesar cipher using given integer shift for rotation
    def __init__(self, shift):
        encoder = [None] * 26  # temp array for encryption
        decoder = [None] * 26  # temp array for decryption

        for k in range(26):
            encoder[k] = chr((k + shift) % 26 + ord('A'))
            decoder[k] = chr((k - shift) % 26 + ord('A'))

        self._forward = ''.join(encoder)  # convert the encoder and
        self._backward = ''.join(decoder)  # decoder arrays as strings

    # return string representing encrypted message
    def encrypt(self, message):
        return self._transform(message, self._forward)

    # return decrypted message given encrypted secret
    def decrypt(self, secret):
        return self._transform(secret, self._backward)

    # utility to perform transformation based on given code string
    def _transform(self, original, code):
        msg = list(original)  # convert msg into a list of characters

        # additional: able to handle both capital and small caps letters
        for k in range(len(msg)):
            # original: capital letters only
            if msg[k].isupper():
                j = ord(msg[k]) - ord('A')  # index from 0 to 25
                msg[k] = code[j]  # replace this character
            # additional: handle small caps
            elif msg[k].islower():
                j = ord(msg[k]) - ord('a')  # index from 0 to 25
                msg[k] = code[j].lower()
        return ''.join(msg)


# test code -- Mix caps
print('===For Mix Caps===')
cipher = CaesarCipher(3)
message = "The Eagle Is In Play; Meet At Joe's"
coded = cipher.encrypt(message)
print('Secret: ', coded)
answer = cipher.decrypt(coded)
print('Message: ', answer)

# test code -- small caps
print('\n===For Small Caps===')
cipher2 = CaesarCipher(3)
message2 = "the eagle is in play; meet at joe's"
coded2 = cipher2.encrypt(message2)
print('Secret: ', coded2)
answer2 = cipher2.decrypt(coded2)
print('Message: ', answer2)
