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
Pull requests are welcome.

1. Create a branch in your forked repository, with the name of whatever feature u are added
   1. `git checkout -b <new-feature>`
2. Once you have commited all wanted changes to your <new-feature> branch, run the command:
   `git push origin <new-feature>`
   1. This will create a pull request on the main branch
3. Once the pull request is on the pull requests tab in the main hahshtrit, someone has to merge the pull request

## License
[MIT](https://choosealicense.com/licenses/mit/)