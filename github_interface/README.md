# Github Interface - CLI Tool

A CLI tool for doing stuff like copying github repos from one org to another while preserving git commit history. Depending on your preference and comfort level the bash script may be easier for copying over a single repo. The python script may be better if you need to copy a whole bunch of stuff or do add a bunch of users, etc.

## Installation & usage: bash script

This is for the bash shell script.

### Requirements & installation

- The github cli tool `gh`.
- git, obviously.

First, you must have git installed & configured.

Then install `gh` - see https://cli.github.com/ for github's cli docs & install instructions. First, install it. Then you must then run `gh authenticate login` to authenticate the gh cli tool with your github account so it has the necessary permission to do stuff. It should now work.

### Example

```bash
# Copy the guessing-game repo from romeoplatoon org to sierraplatoon org:
./copyrepos.sh romeoplatoon sierraplatoon oop-guessing-game
```

## Installation & usage: python script

`github_interface.py` uses & is a wrapper for the bash script, so, first get the bash script set up and test that it works. Then you will also need a github personal access token named GITHUB_TOKEN in an `.env` file in project root. The token will need the following permissions:

- repo
- admin:org
- user

See the "batch" python files and the python code itself for usage examples.