# Workshop git/github

1. Fork [Github]

  - fork this repository

2. Template [Github]

  - clone the repository you have forked

  - create a template that will be used when you will create an issue [docs](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/configuring-issue-templates-for-your-repository)

  - create a template that will be used when you will create a pull requests [docs](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/creating-a-pull-request-template-for-your-repository)

3. Template test [Github]

  - create an issue on your repository

  - create a branch named `github/test-pull-requests`
  - create a pull request on your repository (branch `github/test-pull-requests` -> `main`)

4. Branch [Git]

  - create a branch named `dev`

  - create a branch named `feat/new-feature-a` that starts from `dev`
  - create a file named `CONTRIBUTING.md` and `git add`+`git commit` this file
 
  - create a branch named `feat/new-feature-b` that starts from `dev`
  - create a file named `CONTRIBUTING.md` and `git add`+`git commit` this file
  - add some random characters to `CONTRIBUTING.md` and `git add`+`git commit` this file
 
  - create a branch named `feat/new-feature-a-b` that starts from `feat/new-feature-a` and merge `feat/new-feature-b`

for now, if you run:

```bash
git log --cherry --boundary --decorate --color --oneline --graph --all
```

it will be something like this:

![TODO](./assets/todo.png)

  - push the branch `feat/new-feature-a-b` and create the pull requests (branch `feat/new-feature-a-b` -> `main`)

5. Rebase vs Merge [Git]

  - read more about Rebase vs Merge: [stackoverflow](https://stackoverflow.com/a/16666418) [stackoverflow](https://stackoverflow.com/a/25267150)
  
  - create a branch named `feat/new-feature-a-b-rebase` that starts from `feat/new-feature-a` and rebase `feat/new-feature-b`

re run the following command

```bash
git log --cherry --boundary --decorate --color --oneline --graph --all
```

  - enjoy the difference

5. 
