# test-github-actions

![Coverage](./docs/img/Coverage.svg)

This repository exists to give me a playground with Github Actions, allowing me to test workflows before implementing them.

## What workflows exists?
I currently have one workflows (with one job) running, doing three things (post-checkout and pip install):
 1) Run all tests using unittest
 2) Generate coverage - create and save Coverage.svg with updated coverage percentage
 3) Commit and push Coverage.svg to the project, if it has changed
 
## Why?
This project came to be because I am working on automating testing for a different project, where the resulting website will hopefully live for a long time. I want to implement a Coverage-badge for that project as well, and the hopefully long lifetime of the projects means I want to generate this locally. This is, therefore, a test to see if it can be done, and how.
It is also a nice playground for Github Actions!

## What can I take from this?
Well, I hope it can - if nothing else - be used as an inspiration for similar projects. There are IMO a couple interesting things being done here, which can be reused later:
 * The workflow itself can probably be reused for similar purposes later. It is a pretty standard python-test workflow, but with the added commit-and-push of Coverage.svg
 * generate_coverage.py can be used as inspiration for how to generate Coverage-badges for other projects. While it is pretty rough around the edges and probably can benefit from some optimalization or general refactor, it works for how I want to use it.
 
## Is there anything wrong with this way of doing things?
Well, yes. The major thing here is that all triggers of the workflow (in this case pushes to main) triggers it, and all changes that affect the Coverage percentage updates the badge (adding another commit to the repository). While this might seem like a small thing, it can be annoying, both because the commit history fills up over time and because it means the developer who just pushed code needs to pull again before making other changes (which is remarkably hard to remember). While this might be annoying for me in this project, it will probably work fine for projects demanding pull requests be used.
