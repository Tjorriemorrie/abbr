Recognizing abbreviations and acronyms
======================================

For today’s absurdly convoluted programming exercise to verify your basic
ability by producing something of roughly no value, we have a task related to
recognising abbreviations and acryonyms: a string processing exercise. Python
can work really well for this, and Python is the language we work with the most
at roi.com.au, so Python it is.

Part one: the algorithm
-----------------------

Our goal is to classify some user input, checking if the user is giving us an
abbreviation of another term. I dunno why, I think the business plan was
something like this:

1. Synergistically leverage a PaaS vendor to make a value-adding RESTful API.
2. ???
3. Profit!

Anyway, we ended up with this thing for abbreviation and acronym detection.

Here are some examples of classifications:

1. “RADIUS” is an abbreviation of “Remote Authentication Dial In User Service”.
2. “TCP/IP” is an abbreviation of “Transmission Control Protocol / Internet
   Protocol”.
3. “FedEx” is an abbreviation of “Federal Express”.
4. “Auspost” is an abbreviation of “Australia Post”.
5. “frisco” is an abbreviation of “San Francisco”.
6. “staple” is an abbreviation of “Preposterous Examples” (prepo\ **st**\
   erous ex\ **a**\ m\ **ple**\ s).

In the above list:

- Examples 1 and 2 are simple abbreviations (a.k.a. acronyms); the abbreviation
  if formed by taking the first letter of each word in the list.
- Examples 3 and 4 are complex abbreviations; they consist of one or more
  letters from the beginning of each word in the list.
- Examples 5 and 6 are substring abbreviations; they may take any part of any
  word as long as the letters appear in the original presented order.

Your task is to write a function to detect if one string is an abbreviation of
another and, if it is, classify the abbreviation as either simple, complex or
substring.

All of this is case-insensitive, but don’t worry about Unicode case
normalisation. Bonus marks if you know why I hate Turkish.

Your function should take this form:

.. code:: python

    def classify_abbreviation(abbreviation, long_form):
        # Returns one of: None, 'simple', 'complex', 'substring'.

Perform the task as you might normally expect to perform it, with whatever
commentary, documentation, testing, &c. you would do.

Part two: the RESTful API
-------------------------

We missed a part of the requirements! How are our customers going to access
this?

For this MVP (another buzzword! yay!), we just want a trivial little thing with
a single endpoint that takes query string parameters and produces a plain text
response.

So then: requests like ``GET /classify?abbreviation=…&long_form=…`` will
produce a ``text/plain`` response with an empty body or the word “simple”,
“complex” or “substring”.

You get to decide what the most appropriate response code is for the ``None``
case (where the response body will be an empty string); a certain case could be
made for 404 Not Found, but it seems a bit pedestrian, yeah? Also rather
semantically incorrect. 200 OK (or rather, 204 No Content) is probably going to
be the most appropriate.

Please use Django for the server.

Submission
----------

Send a tarball with the code to chris.morgan+hiring@roi.com.au; ideally .tar.xz
(`tar caf foo.tar.xz project/`); Gmail seems to block most .tar.gz files, pesky
thing. Or else make a secret gist.