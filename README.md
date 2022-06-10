# Web Crawler
This program is a crawler that allows you to browse a link and extract information. <br />
The program can be used on the command line and offers the following features: <br /> <br />
Return a report in the terminal <br />
$python3 cli.py [--url|u] https://example.net
 <br /> <br />
Return a report in a file passed as a parameter <br />
$ python3 cli.py [--url|u] https://example.net [--export] filename
 <br /> <br />
The generated report is in text format and contains the following information: <br />
The number of unique URLs <br />
URLs pointing to the same domain <br />
Addresses pointing to an external domain <br />
Addresses containing forms (all forms combined) <br />
Addresses containing password-protected pages<br <br />
The number of addresses pointing to the same domain name returning a 404 page <br /> <br />

The mode of use is as follows: <br /> <br />

Return only pages returning a 404 error code <br />
$python3 cli.py [--url|u] https://example.net --404 <br /> <br />

Return only addresses pointing to an external domain name <br />
$python3 cli.py [--url|u] https://example.net --external-url <br /> <br />

Return only pages requiring authentication <br />
$ python3 cli.py [--url|u] https://example.net --protected_url <br />

