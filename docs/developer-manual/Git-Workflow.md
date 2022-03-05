## Force Push Flow

Here is the git workflow I mostly use when you see me (@hairmare) force pushing.

Buyers beware, if something goes wrong I'm ready to `git reflog` my way out of issues.

```bash
cd libretime-working-copy
```

Get master up to date before I start features.

```bash
git checkout master
git pull origin master
```

If the pull fails and my master is dirty due to local edits I usually use stash.

```bash
# 1. stash local changes
git stash
# 2. rerun pull
git pull origin master
# 3. apply (pop) stash onto updated working copy
git stash pop stash@{0}
```

Once my master is up to date I start a feature branch for everything I work on. I usually use a folder structure like branch naming convention.

```bash
git checkout -b feature/<featurename>
```

Once I'm on a branch I hack away and commit my results. The `-p` flag makes it easy to only stash the changes I actually want to commit.

```bash
git add -p
```

When I commit I mostly use [commitizen](http://commitizen.github.io/cz-cli/) with [gitmojis](https://github.com/Landish/cz-gitmoji) 😜

```bash
git cz
```

Sometimes I also use plain old commit.

```bash
git commit
```

After having committed and tested something it's time for a push.

```bash
git push <forkname>
```

Now I wait for travis and maybe do more local testing. If something is still wrong with the code I often amend/force-push.

```bash
# 1. I fix the code and then stage the fix
git add -p
# 2. I add the fix to the previous commit by rewriting the commit
git commit --amend
# 3. I force push to the fork
git push <forkame> --force-with-lease
```

I repeat this until I am ready to open a PR. I try to keep force-pushing on open
PRs at a minimum.

If a PR is open and needs rebasing I do the following steps.

```bash
# 1. temporarily switch to master
git checkout master
# 2. update master
git pull origin master
# 3. switch back to branch
git checkout <branchname>
# 4. rebase branch onto master
git rebase master
# 5. if all went well, force push back up
git push <forkame> --force-with-lease
```

All of this only works when I'm the only one committing on a branch, if the branch
has commits by others I use the _traditional_ merge model (unless I'm last in the
chain, then I rebase my stuff, git is complicated in a good way like that).

One last thing.

If anything goes wrong and you realize you want a commit you _lost_ due to the rebase,
you can usually still find it in the reflog.
Learning the reflog is a good idea, it gets you to really know the underbelly of all
this staging business concerning the git DAG.

```bash
git reflog --help
```

If you still know the sha sum of the old branch (ie. from github in an open PR or from travis)
you might get away with this (on a clean working copy).

```bash
git reset --hard <shasum>
git checkout -b <newbranch>
```
