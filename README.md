###  Current Goals
- Need to review project requirements and decide on what to do.
- Do upvotes for live interactions

### To update your forked repo with main run:
1. `git pull upstream master`
2. `git push origin master`

# Foobar

Foobar is a Python library for dealing with word pluralization.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install foobar
```

## Usage

```python
import foobar

# returns 'words'
foobar.pluralize('word')

# returns 'geese'
foobar.pluralize('goose')

# returns 'phenomenon'
foobar.singularize('phenomena')
```

## Contributing
Only Steps 3 and 4 are needed to create a pull request, but it seems steps 1 and 2 are recommended for organizational purposes
1. Create a branch in your forked repository, with the name of whatever feature u are added
   1. `git checkout -b <new-feature>`
2. Once you have commited all wanted changes to your <new-feature> branch, run the command:
   `git push origin <new-feature>`
3. Go to the branch on github and click `contribute`
4. Confirm to send a pull request

## License
[MIT](https://choosealicense.com/licenses/mit/)