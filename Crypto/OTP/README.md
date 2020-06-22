# CsecIITB CTF 2020
## Category: Misc
## Challenge: Fibonacci

![](Capture.png)

### Idea: 

The question requires you to find some string (flag) in a bunch of cipher text. Clearly the cipher texts do not make much sense at first glance. Its actually
encrypted using OTP in which the message is XOR'ed with some key of the same length, except in this challenge all the messages have been XOR'ed with the
same key (also known as Two Time Pad). There are ways to get back the message in these cases. One way, the one I'll be using, is called crib dragging. Lets get some terms straight. Call two messages as m1 and m2, the key as k (same length as message), and c1 and c2 as their corresponding ciphertexts. 
So c1= m1 xor k and c2= m2 xor k. Now if you XOR the two cipher texts, you'll get m3= c1 xor c2= m1 xor k xor m2 xor k = m1 xor m2. This is where crib dragging comes to use. In order to make guesses of what m1 and m2 might contain, we actually used a [project](https://github.com/MrBhendel/2Time) that deals with this 
problem using some Natural Language Processing appraoch. For it to work, you'll have to provide it with a large enough corpus. I used [this](http://www.cs.cmu.edu/~enron/) as the corpus. When you give this program the xor of two strings, it outputs what the two strings could have been. Although I didn't get exact results from it, I got many words that were actually present, so much so that I got the entire key (using crib dragging) using just two of the 9 messages. Used [this](https://lzutao.github.io/cribdrag/) tool for crib dragging.

*Flag*
> 7h3_OTP_h45_b33n_br34ch3d_I_repeat_MTP_is_br34ch3d

