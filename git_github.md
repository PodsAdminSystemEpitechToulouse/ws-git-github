---
module:			B-INN-000
title:			Git / Github
subtitle:	    Introduction a git et github

author:			Mathéo Martin & Xavier Mitaux
version:		1.0
---
#newpage
# Fork [Github]

- fork this repository

# Template [Github]

- clone the repository you have forked

- create a template that will be used when you will create an issue [docs](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/configuring-issue-templates-for-your-repository)

- create a template that will be used when you will create a pull requests [docs](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/creating-a-pull-request-template-for-your-repository)

# Template test [Github]

- create an issue on your repository

- create a branch named `github/test-pull-requests`

- create a pull request on your repository (branch `github/test-pull-requests` -> `main`)

# Branch [Git]

- create a branch named `dev`

- create a branch named `feat/new-feature-a` that starts from `dev`

- create a file named `CONTRIBUTING.md` and `git add`+`git commit` this file

- create a branch named `feat/new-feature-b` that starts from `dev`

- create a file named `CONTRIBUTING.md` and `git add`+`git commit` this file

- add some random characters to `CONTRIBUTING.md` and `git add`+`git commit` this file

- create a branch named `feat/new-feature-a-b` that starts from `feat/new-feature-a` and merge `feat/new-feature-b`

for now, if you run:

#terminal(git log --cherry --boundary --decorate --color --oneline --graph --all)

it will be something like this:

imageCenter(TODO.png, 350px, 30)

- push the branch `feat/new-feature-a-b` and create the pull requests (branch `feat/new-feature-a-b` -> `main`)

# Rebase vs Merge [Git]

- read more about Rebase vs Merge: [stackoverflow](https://stackoverflow.com/a/16666418) [stackoverflow](https://stackoverflow.com/a/25267150)

- create a branch named `feat/new-feature-a-b-rebase` that starts from `feat/new-feature-a` and rebase `feat/new-feature-b`

re run the following command

#terminal(git log --cherry --boundary --decorate --color --oneline --graph --all)

- enjoy the difference

# Hooks [Git]

- read more about hooks: [git-scm](https://githooks.com/)

- create a file named `hooks/pre-commit` and add the command to execute your norm check

- create a file named `hooks/pre-push` and add the command make to be sure that your code is ready to be pushed

# Github Actions [Github]

- read more about Github Actions: [github](https://docs.github.com/en/actions)

- create a workflow that will compile your code every time you push on a branch

- create a workflow that will check your norm every time you create a pull request

- create a workflow that open a issue when something goes wrong in your workflow
