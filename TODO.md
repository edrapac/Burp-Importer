# TODO

* ~~We need a JSON parser capable of parsing a HAR file that can then recreate requests and responses from that file~~
* ~~Develop the above seperately and when done stitch that back into the BurpImporter.py~~
* ~~Once we can recreate a full request and response, add to sitemap using existing methods in BurpImporter.py, we MAY have to actually create a request from the data here ie an IHttpRequest and IHttpRequestResponse object to then add that item to the sitemap~~

* add cookies to GET request in get method
* add cookies to POST request in post method