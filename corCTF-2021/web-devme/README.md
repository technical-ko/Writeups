# web-devme (web, 323pts, 264 solved)

## Description

```
an ex-google, ex-facebook tech lead recommended me this book!

https://devme.be.ax
```

## Task Analysis
The link given in the description presents us with the following webpage:

![Intro](/corCTF-2021/web-devme/screenshots/siteintro.PNG)

The two buttons that are immediately present did not appear to do anything useful for us, as the "Buy for $20" button simply redirected us to the same page, and the "Learn more" button simply scrolled the page down. Upon scrolling downward, however, we found a field for user input that required further investigation: 

![User Input](/corCTF-2021/web-devme/screenshots/userinput.PNG)

Examining the request sent when using the "Submit email" button showed that the endpoint is using Graphql:

![Find Graphql](/corCTF-2021/web-devme/screenshots/burpfindgraphql.PNG)

We checked to see if there were 
Graphql supports introspection, which 

![Introspection](/corCTF-2021/web-devme/screenshots/introspection1.PNG)

![Query types](/corCTF-2021/web-devme/screenshots/query_query_types.PNG)

![Token_Required](/corCTF-2021/web-devme/screenshots/flag_requires_token.PNG)

![Token](/corCTF-2021/web-devme/screenshots/query_token.PNG)

![Flag](/corCTF-2021/web-devme/screenshots/foundflag.PNG)
