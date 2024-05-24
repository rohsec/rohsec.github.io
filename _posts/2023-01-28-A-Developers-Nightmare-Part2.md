---
title: "A Developer’s Nightmare (Part - II): Story of an innocent looking parameter and some poor fixes worth $1650"
date: 2023-01-28 13:50:00 +530
categories: [BugBounty]
tags: [bugbounty,cybersecurity]   
pin: true 
---

Hello Everyone, I hope you all are doing good. This is my third blog and in this I will be covering a different class of vulnerablities followed by a series of some poor fixes by the developer.\
This is in continutaion to my preivous writeup [A Developer's Nightmare](/posts/A-Developers-Nightmare/)

![](https://i.postimg.cc/qMYHhvhJ/intgirittweet.png)

This writeup reiterates the importance of revisting your old reports. In this write up we will be covering how I was able to bypass a series of poor fixes applied to one of my report. Not once, not twice, not three but four times, so without wasting any time let's get straight into the findings.

> The target is a big production company which operates a low key bounty program so we will be referring to it as ```redacted.com``` throughout this article.

---

So, the first finding dates back to Oct, 2021 where in while doing simple overview of the target I came across an innocent looking parameter ```?f=```\
The parameter was containing a relative path to one of the endpoints of the application and the value was used to redirect the user to that particular endpoint after a POST request.\
Like everyone my very first thought was to check for arbitrary domain injection causing an Open Redierct Attack.

I simply tried  ```?f=//evil.com``` and too my surpirse it worked 😮. There were no checks, nothing.\
I was successfully able to pollute the anchor tags via the parameter but it's not enough as the user needs to click on the links to get redirected to evil.com

After few minutes of digging into javascripts, I was able to find an endpoint ```/theme/dark``` . It was a GET request and thus perfect for my Open Redirection purposes. I quickly appended the ```?f=//evil.com``` to the request and I was successfully able to achive an Open Redirect via ```https://redacted.com/theme/dark?f=//evil.com``` .

I quickly created a POC and reported this to the program. The program was quick to acknowledge the issue and deployed a fix within a day.

![](https://i.postimg.cc/sgzK0P7M/rep1.png)
![](https://i.postimg.cc/G3ZXvnpJ/rew1.png)

>Note: In the year 2021 I was just getting started in BugBounties and I was too excited to report the issues hence I highly suspect I surely missed a XSS on this report. You will come to know why later

### Timeline:
>Reported: 04-Oct-2021\
\
Fixed: 05-Oct-2021\
\
Bounty awarded: $250

As you know from my previous articles I have a habit of going back to my old reports, later in Jan,2022 I revisited and tried to reproduce the bug. Hard luck but the fix was applied and upon detecting double slashes ```(//)``` in the parameter the server started dropping any keywords directly followed by the // until it encounters next single / . i.e;
the server was converting ```f=//evil.com/index.html```  to ```f=/index.html```
>Note: Notice how it dropeed the term evil.com which was immediately followed by // and retained /index.html only.

## Fix Bypass x1 :
I noticed the above behaviour and immediately figured what the developer did there and started bypassing it.
After few tries, I was successfully able to bypass the poor fix by injecting double slasess (//) twice in the parameter. i.e;

### Payload:
```
https://redacted.com/theme/dark?f=//example//evil.com
```

As expected, it encountered  the // and dropped of the keyword ```example``` which is directly followed by the first // until it encountered the first single / of the second part ```//evil.com``` thus,\
```//example//evil.com``` becomes ```//evil.com```

![](https://i.postimg.cc/qBtmtvpv/rep2.png)\
![](https://i.postimg.cc/k4GbpGT6/rew2.png)

### Timeline:
>Reported: 01-Jan-2022\
\
Fixed: 06-Jan-2022\
\
Bounty awarded: $250

After this, I stopped hunting on this prorgram for a while and switched to another one. But all this time I had this report in my mind and I was blamming myself for missing an opprtunity to escalte these to XSS.
Fast forward to Oct,2022 I revisted the old reports and started looking for bypasses again.

## Fix Bypass x2 :
I took previous bypass as an inspiration and started playing with double slashes (//) but to no success, the developer has learned his lesson and is now dropping everything after // and replacing it with ```/home``` :(\
BUT But But it's really interesting how the browsers interpret the http protocol :) After few hours of hit and trial I found a working payload for the Open Redirect. HOW?

![](https://camo.githubusercontent.com/af11ef9a79d7461ce041a8590818e1eab3d3fd1c16ebe79d486cf6414e2b9ec7/68747470733a2f2f6d65646961332e67697068792e636f6d2f6d656469612f336f73785961446c784c6365787351694b6b2f67697068792e6769663f6369643d373930623736313162326537376639333734333332656162663062353439336532626631356366663834326337613633267269643d67697068792e6769662663743d67)

As the server was replacing everything after the // with /home I thought of playing with the preceding of // and started adding payloads in the form ```http://evil.com``` and it returned a response ```Location: http:/home``` in the headers. 

Now I only need to tackle the replacment due to those //. As I said earlier the browsers behaviour is really interesting and removing a /, i.e; http:/evil.com resulted into ```Location: http:/evil.com``` and the browser perfectly got redirected to evil.com ;)\
We have a third bypass for the Open Redirect now but 
it was late in 2022 and by this time I have gained some good knowledge about Bug Bounties and knew exactly what I am doing.
Instead of reporting it I started looking for options to escalate this to XSS. I moved back to the very first endpoint where I was able to pollute the anchor tags on the page and started testing injections there.\
The webapp was behind Cloudflare and gave me a really hard time. The Big challenge was to bypass the Firewall and obtain a full fledged XSS. Even though the challenge was big for me I was determined this time. After spending hours on this, I was able to bypass the Cloudflare and obtain a working XSS.

### Payload: 
```
?f=http:/evil.com
?f=javascript:throw%20onerror=alert,Bug_Bounty_POC_by_ROHIT
```
![rep3.png](https://i.postimg.cc/QCWWjPGj/rep3.png)\
![](https://i.postimg.cc/4d09kG08/rew3.png)

### Timeline:
>Reported: 01-Oct-2022\
\
Fixed: 05-Oct-2022\
\
Bounty awarded: $500

Aftre this I got busy in some other program but after 2 months ,i.e; in Dec,2022 I again revisted the old report to check the fixes.
The developer has put in some efforts and the old bypass was not working anymore.

## Fix Bypass x3 :
After few minutes of playing around and understanding what's going on I figured out what the developer did here. 
The developer is now looking for the characters ```/ followed by a :``` , i.e; ```/:``` in the parameter value and it will be redirected to /home.
As I said earlier, browsers are really interesting and within few minutes of looking I already had the bypass. I simply removed the / completely from the parameter so that it becomes ```?f=http:evil.com``` (Notice there's no / and it will still go to evil.com).

Wow, I now have a bypass for the same issue for the third time but what about the XSS ? \
We need a bypass for XSS as well, I noticed what the developer did there was blocked the term ```javascript``` completely and simly capiatlizing the very first alphabet worked LOL, i.e; ```Javascript``` (Notice the capital J in javascript).

### Payload:
```
## Old Payload Used:
?f=http:/evil.com
?f=javascript:throw%20onerror=alert,Bug_Bounty_POC

## Payload Used (Fix Bypass):
?f=http:evil.com     (Notice no use of /)
?f=Javascript:throw%20onerror=alert,Bug_Bounty_POC  (Notice capitalization of J )
```

![](https://i.postimg.cc/HsXB2vcG/rep4.png)\
![](https://i.postimg.cc/K4S3jNxB/rew4.png)

### Timeline:
>Reported: 11-Dec-2022\
\
Fixed: 14-Dec-2022\
\
Bounty awarded: $300

That was one hell of a journey for the developers, we have moved to a New Year, it's Jan,2023 and I was really hopping the devs must have taken care of everything by now.\
And yes everything seems to be good now and no bypass works anymore. Seems like the devs did a good job BUT they forgot they got more than on subdomain :(

## Fix Bypass x4 :
It was 11 Jan 2023, I was getting bored and thought of revisiting the old reports, as I mentioned earlier everything seems to be fixed by now and no bypasses worked anymore until I noticed a weird subdomain lying silently in one of my separate report(related to Business Logic Issue). 
The subdomain was of the form ```cinemabox-12fthsxpoq.redacted.com``` . I tried pasing the parameter ```?f=```` with the very same attack vectors and to my surprise it worked and I was redirectd to evil.com.

### Payload:
```
## Payload Used:
?f=http:evil.com (No //)
```
This was not vulnerable to XSS forunately and only limited to Open Redirect attacks.

![](https://i.postimg.cc/ZqVNHpxz/rep5.png)
![](https://i.postimg.cc/fbwXYBXv/rew5.png)

### Timeline:
>Reported: 11-Jan-2023\
\
Fixed: 17-Jan-2023\
\
Bounty awarded: $350

As of today, everything seems in good shape but I am sure there will be something more hiding here and there which yet needs to be unearthed.

So that was it, I enjoyed bypassing these fixes and I hope you enjoyed reading it and learned something new today. Thanks for holding with me :)

---

> If you liked the wrietup and learned something consider liking and sharing it with others on infosec twitter ;)