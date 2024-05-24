---
title: Solving Bugcrowd's Spooky Challenge- The Nerd's Way
date: 2023-11-04 19:30:00 +500
categories: [BugBounty]
tags: [bugbounty,cybersecurity]    
---

Hello Everyone! I hope you're all doing well. Over the past couple of days, my inbox has been flooded with DMs, all revolving around the same intriguing topic: Bugcrowd's recent Spooky Challenge.

What's got everyone buzzing, you ask? Recently BugCrowd announced the winners of the challenge and I was one of the very first to solve the challenge, the challenge was quite easy and straight forward in itself.
The Challenge was announced on Oct 30 at 09:53 PM, I was lucky enough to spot the tweet within 25 seconds of it going live and was able to solve and submit a solution(atleast this is what I thought) within the very first 2 minutes at 09:55 PM

[![blog4a.png](https://i.postimg.cc/59vZdbY4/blog4a.png)](https://postimg.cc/23kHnp7M)

The Challenge is created by ZWink and revolves around basic Authentication Bypass to retrive a hidden secert flag/code. The challenge can be found [here](http://spooky.bugcrowd.zw.ink/klown.cfm)

---
## Walkthrough

On first visting the challenge page we are served with a bold ```ACCESS  DENIED``` message and a clown laughing on our face.
Below that we see a form with a inpout field containing the message ```Kreepy Klown denies you access!```, our goal is to get to the other side of the webapp and get the hidden flag.

[![blog4a3home.png](https://i.postimg.cc/9fsSMfK8/blog4a3home.png)](https://postimg.cc/yJXnp7Vc)

There seems nothing intresting in first glance and fuzzing/automated testing is strictly prohibited as it is not going to help us in anyway :)
Looking at the source code of the application, we see a form making a POST request to ```/klown.cfm``` with various input fields but the one which caught the attention is the hidden field named ```captcha``` with a random value.

[![blog4a2.png](https://i.postimg.cc/BQL6Wfmp/blog4a2.png)](https://postimg.cc/LnSRfwKg)

My immediate thought was to play around with this value but big question is what we can even do with a random 30 character long string? Maybe pass it in the input field provided? Another thing we see is the ```Submit``` button is intentionally disbaled with a hard coded disabled HTML attribute.

We are going to solve the challenge using the browser console like a Nerd :) It's time for some Console Magic!! 

![](https://media.giphy.com/media/iBjylURwS9N9FCl8Dl/giphy.gif)

First thing first, we need to copy the hidden captcha value and paste it into the password input field 
>```document.getElementById('password').value=document.getElementById('captcha').value```

[![blog4b.png](https://i.postimg.cc/YC5S3Dk9/blog4b.png)](https://postimg.cc/BjCsZgj9)

>Note: The server is expecting any random value in the password input field and passing the captcha in the password input is not at all necessary, this is just what I did.

Now, we need to submit the form but we see the Submit button doesn't work, let's fix that
>```document.getElementById('smile').disabled=false```

[![blog4c.png](https://i.postimg.cc/g2XJ3FCQ/blog4c.png)](https://postimg.cc/Js8MWg45)

Great, now let's submit the form and see what happens
>```document.getElementById('smile').click()```

[![blog4d.png](https://i.postimg.cc/MZ5vSY0P/blog4d.png)](https://postimg.cc/23qzdhKh)

Voilla!! We have some progress and the secret password is ```KR33PIE-KL0WN``` BUT is that the final code we are after or is it just a key to another door? Whatever it is atleast we have impressed the Klown 

Okay, let's go on another console spree but this time with the ```secret-password``` given by the Klown ;)

Enter the secret password into the password input field
>```document.getElementById('password').value="KR33PIE-KL0WN"```

[![blog4e.png](https://i.postimg.cc/BQwb8QV2/blog4e.png)](https://postimg.cc/SJCk3qqK)

Submit the form once again
>```document.getElementById('smile').disabled=false;document.getElementById('smile').click()```

[![blog4f.png](https://i.postimg.cc/3JwWJDnK/blog4f.png)](https://postimg.cc/SjwmgRB5)

There we have it!!!! The Secret Code is ```BUGCROWD-KLOWN-2023```, we have made it to the other side of the circus and guess who is laughing now ;)

The challenge conclueded on Oct 31st and the results were declared on Nov 2. 80+ hackers were able to solve this challenge and 12 hackers completed the challenge in under 14 minutes.

[![blog4g.png](https://i.postimg.cc/VvfvtSwW/blog4g.png)](https://postimg.cc/LYWmK8nJ)


It was a fun challenge,I had great fun solving and writing about it. I hope you enjoyed reading the walkthrough :)