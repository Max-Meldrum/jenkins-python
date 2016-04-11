Jekins python setup
===================

Test configuration with jenkins and python

Includes coverage report and violations.


==================
Setting up jenkins
==================

git clone https://github.com/jenkinsci/docker.git

Add this to the Dockerfile::
    
    FROM jenkins
    USER root
    RUN apt-get update && apt-get install -y python python-dev python-distribute python-pip
    RUN pip install nose
    RUN pip install pylint
    RUN pip install coverage
    USER jenkins # drop back to the regular jenkins user - good practice


Build image::

    docker build -t jenkins .


Run container::
    
    # Create a directory called jenkins where the data will be mapped from
    docker run -d -p 49001:8080 -v $PWD/jenkins:/var/jenkins_home -t jenkins



====================
Building jenkins job
====================

While i was doing this i followed http://bhfsteve.blogspot.se/2012/04/automated-python-unit-testing-code.html

Things to notice is that i ran jenkins in a docker container and built the job manually.

I don't use mock and my tests are different.

