# abbr
Abbreviation checker

## User Requirements

Refer to [docs](docs/task.rst) for project requirements.


## Technical Requirements

The following was established to be required from a technical perspective:

- The project needs to be written in Python.
- The project needs to be written using the Django framework.
- The project needs to use an REST API.
- The project needs to return appropriate headers.
- The project needs to have unit tests for accuracy.
- The project needs to be performant for viability. 


### ETA
-------

It is hard to estimate the time as the work will be done intermittently 
part-time. Best estimate is about 2 business days (2 days * 8 hours)
Log:
- spent about 5 hours on Thursday, much thereof just reading REST docs.
- spent about 6 hours on Friday, mostly just doing the serializer (sigh) and complex algorithm.
- spent about 1 hour on Saturday just doing the profiling and finishing up.


## Installation

Just clone this repo.
I work only in 2.7 as it is a constraint by the Google SDK. There is no viable reason
why this project should not be on the latest version, thus I used environments to 
set the versions and libraries appropriately. Considering the ease of virtualenv
the need for a docker/vagrant image was not considered necessary.

This is what got it working for me, not sure if it is the best way (e.g. the 
env does not seem to auto-activate).

> cd abbr
> pyenv local 3.5.1 && pip install --upgrade pip
> pyenv virtualenv abbr
> pip install -r requirements.txt

Do not think migrations are necessary, maybe.
 

### Python libraries
--------------------

The following libraries were used:
- django                # django requirement
- djangorestframework   # REST API requirement
- markdown              # Markdown support for the browsable API.
- django-filter         # Filtering support
- profilehooks          # seems like a nice profile decorator


## Algorithm

Created `abbr` app for the requirement. Refer classifier.py.
Test revealed additional complexity on complex algorithm.
Todo: handle complex situation of TCP/IP vs Comma-Separated Values (is non-alpha incl or not?)
Luckily complex requirement did not specify "zero or more" (imagine that...)
When I considered splitting up the complex abbr to build a tree(s) to check the long
 form, [this answer](http://stackoverflow.com/questions/35361369/create-possible-combinations-of-specific-size?noredirect=1#answer-35362634) was really good
 In the end I just used the simple loop I wrote myself. 
 
## REST API

Did not bother prefixing it with `/api`: not enough scope to build proper url structure.
Which also means proper routing were not set up. Please ignore.

It seems the serializer plays a big role in the controllers, needs more investigation.
REST library seems more exhaustive than initially thought - requires more reading.

Did not set up OPTIONS response.

Oh my, I'm so [opinionated](https://github.com/tomchristie/django-rest-framework/issues/1755). There
does not seem to be an easy way to represent the data with the serializer, not too impressed. I
might prefer [marshalling it](http://stackoverflow.com/questions/22035974/flask-restful-marshal-complex-object-to-json/34310639#34310639).

#### Countering request method

As data is supplied, it should be a post or patch.
As data is not uuid, it should be in the body.
E.g. `curl --data "abbreviation=a&long_form=abba" http://127.0.0.1:8000/abbr/classify`

#### Countering 204 No Content

1) That is normally the response for a DELETE request. Providing the feedback that
the *resource* location successfully has no content.
2) If I pass empty data to a mail server and returns a 2xx response, I can assume
the email was sent - clearly it should return 4xx. The wiki state 4xx as:
> "The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing)."

Thus it should be handled as invalid.


### Testing
-----------

Test were written to test the classifier.


### Profiling
-------------

Did you know: timeit also disables garbage collection for the duration of the test.
Decided to try out profilehooks. I just added it onto the test (longest running func) :p
It seems the recursion is not that bad, and the timings are 0. I guess that is good
enough for now.


### Tools used
--------------

- Pycharm used for IDE
- Github repository used for vcs


#### Notes
----------

- Small project, not bothering with dev branch, or PRs
- Apparently there is a difference between creating apps with manage.py and django-admin.py... (learned something new) but it screwed up my importing in abbr app; need to fix.
- The serializers seems good enough. (not sure why extracting the model is not available? @todo investigate) Also updating the model isn't available (mmm, I like the validation it offers but the immutability is a bit over the top).
- Set locale to en-au
- I know why you hate Turkish, I'm not even going near that.
