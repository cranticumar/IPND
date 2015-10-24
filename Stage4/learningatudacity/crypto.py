import string
import random
import hmac
import hashlib

def make_salt():
    '''
    In cryptography, a salt is random data that is used as an additional input
    to a one-way function that hashes a password or passphrase. The primary 
    function of salts is to defend against dictionary attacks versus a list of
    password hashes and against pre-computed rainbow table attacks
    '''
    return ''.join(random.sample(list(string.ascii_letters), 5))

def encrypto(word, salt=None):
    '''
    HMAC - hash message authentication code (HMAC)
    This fucntion encrypts input string into hash string with help of SALT inorder
    to avoid secure database even if it is cracked.
    '''
    if salt is None:
        salt = make_salt()
    hashed_word = hmac.new(salt, word).hexdigest()
    return "{s}|{h}".format(s = salt, h = hashed_word)

def decrypto(actual_word, encrypted_string):
    '''
    This function actually takes encrypted string and actual word as input
    Then reencrypts the actual word with salt part of the encrypted string
    and matches to authenticate the trueness of the actual word
    '''
    (s, h) = encrypted_string.split('|')
    if encrypted_string == encrypto(actual_word, str(s)):
        return True

def encrypto_wo_salt(word):
    '''
    This function encrypts the provided word/input with specific algorithms of
    hashlibs
    '''
    algo_index = len(word) + string.letters.find(word[0]) * string.letters.find(word[-1])
    algo_index = algo_index % len(hashlib.algorithms)
    return hmac.new(word, digestmod = getattr(hashlib, hashlib.algorithms[algo_index])).hexdigest()