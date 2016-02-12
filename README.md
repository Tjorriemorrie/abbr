# abbr
Abbreviation checker

## User Requirements
--------------------

Refer to [docs](docs/task.rst) for project requirements.

## Technical Requirements
-------------------------

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
- spent about 5 hours on Thursday, many reading REST docs
- spent about x on Friday


## Installation
---------------

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
 

### Python libraries
--------------------

The following libraries were used:
- django                # django requirement
- djangorestframework   # REST API requirement
- markdown              # Markdown support for the browsable API.
- django-filter         # Filtering support


## Algorithm
------------

Created `abbr` app for the requirement. Refer classifier.py.
Test revealed additional complexity on complex algorithm.
 
 
## REST API
-----------

Did not bother prefixing it with `/api`: not enough scope to build proper url structure.
Which also means proper routing were not set up. Please ignore.
It seems the serializer plays a big role in the controllers, needs more investigation.
REST library seems more exhaustive than initially thought - requires more reading.


### Tools used
--------------

- Pycharm used for IDE
- Github repository used for vcs


#### Notes
----------

- Small project, not bothering with dev branch, or PRs
- Apparently there is a difference between creating apps with manage.py and django-admin.py... (learned something new)
- The serializers seems good enough. (not sure why extracting the model is not available? @todo investigate)
- Set locale to en-au
