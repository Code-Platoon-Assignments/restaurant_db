# teacherbot
Scripts and utilities for helping with classroom administration

Related repos which we maybe should fold into this one. Listing them here now just to get everything in one place.

- https://github.com/codeplatoon-fullstack/copy-git-repo
  - Utility for copying github repos from one organization to another. Useful for moving assignment repos between orgs for each cohort.

 
- https://github.com/codeplatoon-fullstack/student-status
  - A larger project which maybe should remain it's own repo.

- https://github.com/codeplatoon-fullstack/pairs-gui
  - A desktop Python GUI app for generating pair-programming pairs, removing students who don't want to pair, and sending it all to slack.

- https://github.com/CodePlatoon/invite_automator
  - A django web app hosted somewhere that self-paced students use. It is an automation hook that was written by Mike Lee several years ago on a small Django server. When people sign up for the self paced course and you provide a github handle it automates the invitation process to the repo.
  - This form on the CP website goes to the invite automator: https://www.codeplatoon.org/self-paced/
     - This sends an e-mail to Rod which he has a forwarding rule to Zapier, not sure if you've checked that out yet or not, that then pings this server on heroku which then pings the Github AP
