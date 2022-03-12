###  Current Goals
- Need to review project requirements and decide on what to do.
- Do upvotes for live interactions

## Collaboration
#### Creating Branch 
Instead of using forked repos, we can use branches to keep everyone's work flow separate.
1. Clone the main repo
2. Create a branch for a new feature using 
   ```
   git checkout -b <new-feature>
   ```
   or `git checkout branch` into an existing branch
3. Work on the code

#### Pushing changes
Once you think a feature is ready to be implemented, you can push those changes onto the main branch
1. 



### To update your forked repo with main run:
1. `git remote add upstream <url>`
2. `git pull upstream master`
3. `git push origin master`

#### Note:
`git push upstream` pushes to the branch matching the one on `hahshtrit/solid-server`

## Contributing
Only Steps 3 and 4 are needed to create a pull request, but it seems steps 1 and 2 are recommended for organizational purposes
1. Create a branch in your forked repository, with the name of whatever feature u are added 
2. Once you have commited all wanted changes to your <new-feature> branch, run the command:
   ```
   git push origin <new-feature>
   ```
3. Go to the branch on github and click `contribute`
4. Confirm to send a pull request

## License
[MIT](https://choosealicense.com/licenses/mit/)
