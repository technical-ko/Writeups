# web-devme (web, 323pts, 264 solved)

## Description

```
an ex-google, ex-facebook tech lead recommended me this book!

https://devme.be.ax
```

## Task Analysis
The link given in the description presents us with the following webpage:

![Intro](/corCTF-2021/web-devme/screenshots/siteintro.PNG)

The two buttons that are immediately present did not appear to do anything useful, as the "Buy for $20" button simply redirected us to the same page, and the "Learn more" button simply scrolled the page down. Upon scrolling downward, however, I found a field for user input that required further investigation: 

![User Input](/corCTF-2021/web-devme/screenshots/userinput.PNG)


## Solution:
Examining the request sent when clicking the "Submit email" button using Burp showed that the endpoint is using GraphQL:

![Find Graphql](/corCTF-2021/web-devme/screenshots/burpfindgraphql.PNG)

GraphiQL is a simple program for writing and sending GraphQL queries.
We used it here to test to see if introspection has been turned off in the with the following query:

![Introspection](/corCTF-2021/web-devme/screenshots/introspection1.PNG)

[Introspection](https://graphql.org/learn/introspection/) allows users to query the database about its internal structure, such as what types and queries it supports. This may be useful in some scenarios, 
but it comes at a cost to security by giving potential attackers an opportunity to find and exploit the database's vulnerabilities. The query above listed the names of all the types defined in the schema.
The fact that introspection was turned on allowed me to gather information about the queries that were being used:

![Query types](/corCTF-2021/web-devme/screenshots/query_query_types.PNG)

Here I found that there are two types of queries that have been defined for this database. The one named "flag" of course stood out.

![Token_Required](/corCTF-2021/web-devme/screenshots/flag_requires_token.PNG)

We can see from the above attempt that the "flag" query recquires a token parameter. I guessed these would likely be assigned to each user and stored as a field on the "user" type, so I executed the following query:

![Token](/corCTF-2021/web-devme/screenshots/query_token.PNG)

The above query returned a list of tokens. I took the first one in the list and applied it to the "flag" query as a parameter: 

![Flag](/corCTF-2021/web-devme/screenshots/foundflag.PNG)

And I found the flag: "corctf{ex_g0013_3x_fac3b00k_t3ch_l3ad_as_a_s3rvice}"
