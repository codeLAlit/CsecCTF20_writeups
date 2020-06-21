# CsecIITB CTF 2020
## Category: Misc
## Challenge: John Cena Again

![](Capture.png)

Is the flag really `CsecIITB{Yоu_still_cаn't_sеe_me}`?

Submitted the flag around 20 times in different ways `Csec`,`CSec` etc etc. Until I realised someday that is that flag really the real flag?

Noooooooooooooo it ain't :)
Spawn up python3 terminal!

```python
>>> s = "CsecIITB{Yоu_still_cаn't_sеe_me}"
>>> s.encode()
b"CsecIITB{Y\xd0\xbeu_still_c\xd0\xb0n't_s\xd0\xb5e_me}"
```

Damnn! So our flag is `CsecIITB{You_still_can't_see_me}` (Yeah, you can copy this one now :wink:)