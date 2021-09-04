# web-devme (web, 323pts, 264 solved)

## Description

```
an ex-google, ex-facebook tech lead recommended me this book!

https://devme.be.ax
```

##Task Analysis
The link given in the description presents us with the following webpage:

![Intro](/corCTF-2021/web-devme/screenshots/siteintro.PNG)

The two buttons that are immediately present do not appear to do anything useful for us, as the "Buy for $20" button simply redirects us to the same page, and the "Learn more" button simply scrolls the page down. Upon scrolling downward, however, we can see a field for user input that requires further investigation: 

![User Input](/corCTF-2021/web-devme/screenshots/userinput.PNG)

![Find Graphql](/corCTF-2021/web-devme/screenshots/burpfindgraphql.PNG)

![Introspection](/corCTF-2021/web-devme/screenshots/introspection1.PNG)

![Query types](/corCTF-2021/web-devme/screenshots/query_query_types.PNG)

![Token_Required](/corCTF-2021/web-devme/screenshots/flag_requires_token.PNG)

![Token](/corCTF-2021/web-devme/screenshots/query_token.PNG)

![Flag](/corCTF-2021/web-devme/screenshots/foundflag.PNG)
