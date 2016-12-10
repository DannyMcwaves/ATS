#ATS

**Applicant tracking system**

NB: this is not a full readme just yet

myAPP/Django_project is where the django project will be based.
Your task is to choose one of the configurations and do away with
the other. ROB...

the webscraper will use scrapy and parsel for web data mining.

The database_driver directory contains modules that will help in writing to databases
more easily as well as reading from them. For now, it has one for sqlite. our cross-transfer datahandling
database.

the process_pdf directory exposes api's that we will use to process the pdf.
I have written two functions for concurrency. One usees thread and the other uses
multiprocessing. let me get some feedback on the two.

the tests directory will use py.test for testing

sample_pdf directory contains sample pdf for test purpose incase you need one hands on.

sqlLite directory holds the sqllite database files that we will use for cross-datahandling.

### the basic structure.

scrapy.cfg -- basic scrapy configurations

setup.cfg -- basic setup configuration

requirements.txt --- project dependencies.

In case of any database base needs. We will either sql or mongoDB
I am good with both.

**Can we use get the blueprint done by the end of this week.**


##### Just a starter.

