# TODO

* ~~We need a JSON parser capable of parsing a HAR file that can then recreate requests and responses from that file~~
* ~~Develop the above seperately and when done stitch that back into the BurpImporter.py~~
* ~~Once we can recreate a full request and response, add to sitemap using existing methods in BurpImporter.py, we MAY have to actually create a request from the data here ie an IHttpRequest and IHttpRequestResponse object to then add that item to the sitemap~~

* Create exception for .har files to not recreate the connection
* Instantiate IHttpRequest and IHttpResponse objects and use the setRequest and setResponse methods to set the request and response respectively 
* Populate site map with forged Request and Response objects 
* ???Profit?