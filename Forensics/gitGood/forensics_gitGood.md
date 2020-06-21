# CsecIITB CTF 2020
## Category: Forensics
## Challenge: EXampleIF
## Points: 500
### Description:

> git is good, only if you could open it somehow
[gitGood.zip](https://ctf.cseciitb.in/files/6742d071836b4792aed48d65cf2b2c39/gitGood.zip?token=eyJ1c2VyX2lkIjo2NywidGVhbV9pZCI6NDMsImZpbGVfaWQiOjY5fQ.Xu-zdQ.cdlWWJ2sastbogAjxQsT0RIlnEg)

### Idea:
The zip is password protected. There is a file `flag.txt` and `.git` folder in it. One first glance it appears that the flag will be in any of the version of the `flag.txt`.

We used `John the Ripper` to crack the password. The password was `sweetpotato`. On extracting the file, just do `git log` to see the
versions of the file. You will found only two commits. `git checkout` to last commit. Check the file your flag is there.

*Flag :*
> CsecIITB{git_Good_GeT_Be77er}