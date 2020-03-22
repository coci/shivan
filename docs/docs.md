# How Shivan works?

Before we jump right into technical detail, I must say something about the idea behind the Shivan project and maybe further projects.

after sometimes that I work in a back-end career, I figured out that I am interested in knowing about how systematic programs work like git, databases, etc. , and some thought spinning around my head, for example :

- how does git work?

- How I create a database from scratch?

- How do download managers work?

- How Nginx handle requests?

- How can I write frameworks like flask or django?

- How do frameworks work?

- How can I write something like them ( mentioned earlier)?

- And like many of these tricky questions

after some thinking about those topics, I found the best way to learn about them is to write them. But not the same as a commercial version with tons of features that they have or what complexity on them, simply write them.

So, I began my journey with writing a key-value database like Redis, but I left that in the middle, and some days ago, I started again with writing download manager, that because Shivan was here.

## how Shivan works ( in other words, how download managers work ) :

the way that download mangers work was very stunning me, they can split up the original file in some parts and download them separately in parallel time, but how they do that?

To download the file in separate parts, only we need to tell a web server (Nginx or apache) that we need a specific part of the original file instead of a complete file, is it simple? that's it :))

I going to cover this topic in much more detail, just follow :)

As the first step, download managers send a request to a web server and grab headers only as a response, and then in the header of the response, you can find useful detail about file size.

( this is sample header from the response)

```
{
 'Date': 'Fri, 20 Mar 2020 15:41:41 GMT', 
'Content-Type': 'image/png',
'Content-Length': '159732'
'Connection': 'keep-alive', 
'Vary': 'Accept-Encoding', 
'Server': 'GitHub.com', 
'Content-Encoding': 'gzip'
 }
```

if you see in reponse there is a key-value ( 'Content-Length' ) :

```
{

 ....

 'Content-Length' : '159732'

 ....

 }
```

This is what we need; that key-value says about how big the file is ( in byte term ). It's time to download, but how?

After grab file size we can tell to web server we need a specific part of file, consider I need download file in 8 parts, I can divide the file size by the number of parts :

```
159732 / 8 =~ 19966 
```

now I know if I need download file in 8 parts I must send 8 requests and specify size ( each part must be 19966 part), I can do this only if I mention part size in header of those requests, like this :

( assume I use Curl command to do that ) :

```
curl --header "Range: bytes=0-19966" www.examople.com/file.jpg
```

in above command I tell to "www.examople.com/file.jpg" I need a specific part of file.jpg ( from byte 0 to 19966) not the complete size of file.jpg, now guess what ? in second requests I act like :

```
curl --header "Range: bytes=19967-39933" www.examople.com/file.jpg
```

After download manager grabs file.jpg in 8 parts, simply I can concrete those bytes in one file ( this file will be our final file ), and now we download file.jpg in 8 parts ( we can send those requests in concurrent to speed up our job ).

finally, this is an amazing time for me because now I learn :

- how download managers work

- how files being download

- how thread works

- how regex works 

- .......

Have fun :)