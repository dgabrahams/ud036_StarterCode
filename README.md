# ud036_StarterCode
Source code for a Movie Trailer website.

## Overview

The instructions in this readme will get a copy of the project up and running on a local machine for development and testing purposes.

### Prerequisites

It is assumed that an active connection to the internet will be available at all times. To run this program Python and GIT are required, plus access to Terminal (MAC Linux) or Command Prompt (Windows). Also required is that a web browser be installed. It was designed and tested using Python 2.7.10.

Check if you have python installed:

MAC
Most Macs come with Python 2.7 already installed, but it’s good to double-check the version. To determine whether you have Python 2.7, open the Terminal application, type the following, and press Return:
```
python -V
```

This command will report the version of Python:
```
Python 2.7.3
```


WINDOWS 7
To get to the command line, open the Windows menu and type “command” in the search bar. Select Command Prompt from the search results.

In the Command Prompt window, type the following and press Enter.
```
python
```

If Python is installed and in your path, then this command will run python.exe and show you the version number.
```
Python 2.7.4 (r264:75708, Oct 10 2009, 07:36:50) [MSC v.1500 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for further information.
```

Otherwise, you will see:
```
'python' is not recognized as an internal or external command, operable program or batch file.
```

In this case, you need to download and install Python 2.7.10 and then add it to your path. These instructions were taken from Google documentation and more examples on setting up testing for Python can be found here:
https://edu.google.com/openonline/course-builder/docs/1.10/set-up-course-builder/check-for-python.html

Python is available for download here:
https://www.python.org/downloads/


To test if you have GIT on Terminal (Linux, macOS) or Command prompt (Windows) use:
```
git --version 
```

Which if installed should produce an output similar to:
```
git version 2.3.2
```

If an supported version is seen or the command itself isn't recognised, then GIT will need to be installed. Please see the link below for furthe rinstructions on installing GIT:
https://git-scm.com/book/en/v2/Getting-Started-Installing-Git


### Installing

To install the application, assuming that the required prerequistite software is installed, use GIT to either clone the repo, or download it.

Download:
https://github.com/dgabrahams/ud036_StarterCode

//LIST WHAT TO DO WITH A DOWNLOAD


Clone: https://github.com/dgabrahams/ud036_StarterCode.git

To clone run:
```
git clone https://github.com/dgabrahams/ud036_StarterCode.git
```

It should build into your current working folder, and produce an output similar to that found below:
```
Cloning into 'ud036_StarterCode'...
remote: Counting objects: 29, done.
remote: Total 29 (delta 0), reused 0 (delta 0), pack-reused 29
Unpacking objects: 100% (29/29), done.
Checking connectivity... done.
```

To run simply type the following:
```
python entertainment_center.py
```

This should open a browser and it should contain the 3 movies listed in entertainment_center.py plus be interactive as setout in the project specification. The project specification can be found in the link below:
https://classroom.udacity.com/nanodegrees/nd004/parts/fe2ad0cf-06b0-4541-87ab-0b6d59e21ef1/modules/3a35570a-8e9d-4088-96d0-3dbe22d1fcb6/lessons/3561209451239847/concepts/36057486950923

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Some components such as 'fresh_tomatoes.py' has taken from xxx

