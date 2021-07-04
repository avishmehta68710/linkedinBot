# LinkedinBot - Make the process of applying and getting referrals easier


### Overview

It consists of three stages

#### Stage 1

- in the first Stage the bot fetches the list of all people working in your dream companies and stores them in a csv file
- ![stage1](https://user-images.githubusercontent.com/69706506/124388286-5ec40380-dcf3-11eb-9c2d-8f8ef83ae1e5.gif)


#### Stage2

- In the second stage the bot goes into all the profiles of the persons from the first stage and scraps all their previous experiences including the company Name, Duration and their work details and store them in a csv file
- ![stage2](https://user-images.githubusercontent.com/69706506/124387436-c11b0500-dcef-11eb-81b4-7f550f362197.gif)


#### Stage3

- In the third stage we retrieve the data of the companies from the second stage and we basically clean the data from the second stage to remove stop words such as Full-time, part-time, contract etc. after cleaning the data we go into each company people section on linkedin and send a customized connection request to all the people working there with a note and your resume.
- ![stage3](https://user-images.githubusercontent.com/69706506/124387850-28858480-dcf1-11eb-8f22-16af9f9473eb.gif)


### Requirements

- Python3
- Selenium
- Beatiful Soup

### Installation

- Clone the respository using the command `git clone https://gitlab.com/<your_username>/linkedinBot.git`  
- Download all the requirements using `pip3 install -r requirements.txt`

### Run it on Local Machine

- In the config.py file add you Linkedin Username, Linkedin Password ,the customized message you want to send and the your dream companies
- For the stage 1 - run the command `python3 stage1.py`
- For the stage 2 - run the command `python3 stage2.py`
- For the stage 3 - run the command `python3 stage3.py`

### Contributing

When contributing to this repository, please first discuss the change you wish to make via issue,
email, or any other method with the owners of this repository before making a change.

Please note we have a code of conduct, please follow it in all your interactions with the project.

## Pull Request Process

1. Ensure any install or build dependencies are removed before the end of the layer when doing a
   build.
2. Update the README.md with details of changes to the interface, this includes new environment
   variables, exposed ports, useful file locations and container parameters.
3. You may merge the Pull Request in once you have the sign-off of two other developers, or if you
   do not have permission to do that, you may request the second reviewer to merge it for you.

## Code of Conduct

### Our Pledge

In the interest of fostering an open and welcoming environment, we as
contributors and maintainers pledge to making participation in our project and
our community a harassment-free experience for everyone, regardless of age, body
size, disability, ethnicity, gender identity and expression, level of experience,
nationality, personal appearance, race, religion, or sexual identity and
orientation.

### Our Standards

Examples of behavior that contributes to creating a positive environment
include:

* Using welcoming and inclusive language
* Being respectful of differing viewpoints and experiences
* Gracefully accepting constructive criticism
* Focusing on what is best for the community
* Showing empathy towards other community members

Examples of unacceptable behavior by participants include:

* The use of sexualized language or imagery and unwelcome sexual attention or
  advances
* Trolling, insulting/derogatory comments, and personal or political attacks
* Public or private harassment
* Publishing others' private information, such as a physical or electronic
  address, without explicit permission
* Other conduct which could reasonably be considered inappropriate in a
  professional setting

### Scope

This Code of Conduct applies both within project spaces and in public spaces
when an individual is representing the project or its community. Examples of
representing a project or community include using an official project e-mail
address, posting via an official social media account, or acting as an appointed
representative at an online or offline event. Representation of a project may be
further defined and clarified by project maintainers.

### Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be
reported by contacting the project team at [INSERT EMAIL ADDRESS]. All
complaints will be reviewed and investigated and will result in a response that
is deemed necessary and appropriate to the circumstances. The project team is
obligated to maintain confidentiality with regard to the reporter of an incident.
Further details of specific enforcement policies may be posted separately.

Project maintainers who do not follow or enforce the Code of Conduct in good
faith may face temporary or permanent repercussions as determined by other
members of the project's leadership.

### Attribution

This Code of Conduct is adapted from the [Contributor Covenant][homepage], version 1.4,
available at [http://contributor-covenant.org/version/1/4][version]

[homepage]: http://contributor-covenant.org

[version]: http://contributor-covenant.org/version/1/4/

### Caution

- Linkedin monitors the number of profiles you view and the amount of connection request you send.
- I strongly recommend you not to visit more than 1000 profiles and not send more than 100 connection request per week
- To prevent this i have have added a checker which will break the loop if you exceed the above limits
- In case of not obeying the caution, linkedin will send you a warning

### I hope you lend to your dream company soon, keep patience and best of luck for the further process
