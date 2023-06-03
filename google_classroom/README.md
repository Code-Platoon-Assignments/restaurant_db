# App Scripts for Google Classroom

## Requirements

You will need to follow & do [this Google Guide on setting up local App Scripts Development using Typescript](https://developers.google.com/apps-script/guides/typescript).

Be sure to [install and configure clasp](https://github.com/google/clasp) so you can interact with Google App Scripts from the command line.

## Recommended before first use

In a separate directory follow this [Google tutorial on writing a "hello world" app script in Typescript.](https://github.com/google/clasp/blob/master/docs/typescript.md) This will familiarize you with clasp and with Google App Scripts. Also read that doc in full **as there are several gotchas.**

## Installation

1. `npm install`
2. `clasp login`
3. Run `clasp pull` and then `clasp open` to confirm clasp is set up. This will pull down the app script project from Google cloud, and then, open the project code in google's in-browser editor. This is just to confirm you have correct accesses.
4. Ask someone for the OAuth credentials for this project. Once they give them to you (they will be text in JSON format) put them in a file named `creds.json` in the project root.
    a. Then run `clasp login --creds creds.json`. **NEVER CHECK creds.json into version control.**
    b. This will have generated a file named `.clasprc.json` which is your access toekn. **Never check this file into version control.**
5. `clasp push`
6. `clasp run` -- this should prompt you on the command line to select a function you wish to run. Run a "helloworld" function first as a test.

## Use -- Important

You will probably have to run `clasp login` and also `clasp login --creds creds.json` **every time** you open a new shell. The second login step is to get OAuth permissions to do stuff w/various Google API's - like interact with Google Classroom, and, to be able to run app script functions with clasp. So it is very important.