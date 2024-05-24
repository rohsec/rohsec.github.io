---
title: "A Developer’s Nightmare: Story of a simple IDOR and some poor fixes worth $1125"
date: 2022-07-24 20:30:00 +500
categories: [BugBounty]
tags: [bugbounty,cybersecurity]   
pin: true 
---

Hello Everyone, I hope you all are doing good. This is my second blog and in this will be covering a finding of a Simple IDOR followed by a series of some poor fixes by the developer.

---

So lately I have been getting a lot of questions on twitter, some of them are

> How often do you go back to your previously reported bugs?\
\
Is it worth to reproduce fixed reports?\
\
Should I try to bypass the fix applied or is it just waste of time?

Well, the answer is a big YES. You should always have throwback to your reports and have a look at the fix applied by the program. Try to spend 10–15 minutes on reproducing the issue and learn more about the fix, try to reverse engineer the fix .

![](https://camo.githubusercontent.com/85810bf477c6078a2f3ac443e177c9979570bce401e3eee47ed24eda2e70f16e/68747470733a2f2f6d65646961342e67697068792e636f6d2f6d656469612f4a333336564373314a4334327a4752686a482f67697068792e6769663f6369643d373930623736313136306662396161393861653430313838616131623539643066303337626232323165316663393166267269643d67697068792e6769662663743d67)

In this write up we will be covering how I was able to bypass a series of poor fixes applied to one of my report. Not once, not twice but three times.

The target Redacted.com, a big a media company allows it’s partners to create different video/advertisement campaigns over the subdomain partner.redacted.com.

I started testing for Access Control Issues on the partner portal when I saw a POST request being made to https://partner.redacted.com/index.cfm?fuseaction=partner.linkcode with JSON body containing the following data:
```json
{

“affiliateid”:12345,

“campaign_name”:”Tester”

}
```

As expected the request was vulnerable to IDOR and the affiliateid being sequential in nature I was able to change the affiliateid and add/edit Campaign’s to anyone’s account. The bigger threatening impact of this was that once a campaign has been added then the user can’t remove the campaigns. I was able to populate anyone’s available campaign list and exhaust their paid quota.

### Timeline:
>Reported: 21-Dec-2021\
\
Fixed: 09-Dec-2021\
\
 Bounty awarded: $325

I have a habit of going back to my reports, later in March I revisited and tried to reproduce the bug. Hard luck but the fix was applied and the affiliateid was completely removed from the json body and instead cookie based authorization check was implemented.

I didn’t gave up and started looking into the JavaScript files, where I found another domain embed.redacted.com which was used to create and preview embedded advertisement campaigns. I started exploring it and to my surprise there was an option to add new campaigns to the Campaign List.

![](https://camo.githubusercontent.com/af11ef9a79d7461ce041a8590818e1eab3d3fd1c16ebe79d486cf6414e2b9ec7/68747470733a2f2f6d65646961332e67697068792e636f6d2f6d656469612f336f73785961446c784c6365787351694b6b2f67697068792e6769663f6369643d373930623736313162326537376639333734333332656162663062353439336532626631356366663834326337613633267269643d67697068792e6769662663743d67)

## Fix Bypass x1 :

This time a GET request was being made to https://embed.redacted.com/builder?affiliateid=[VICTIM_AFFID]&affId=[VICTIM_AFFID_LAST_DIGITS]

Replaced the affiliateid with Victim’s Id and bang we are back in business. I was able to bypass the previous fix via this embed advertisement builder endpoint.

![$300 Bounty awarded for First Bypass](https://miro.medium.com/max/720/1*INNEjxgkObSFBjXvfLTkrw.webp)

### Timeline:
>Reported: 21-March-2022\
\
Fixed: 28- march-2022\
\
Bounty awarded: $300

## Fix Bypass x2:

After the first fix, the page was made inaccessible publicly and was throwing a 403 Forbidden error. One thing I noticed here was the Error page was not the server default instead a custom 403 page with just a single word “Denied”. Connecting the dots, I was able to bypass the fix within 10 minutes.

**OLD Exploit URL:**

```http://embed.redacted.com/builder?affiliateid=[]&affId=[]```

Sometimes things as small as a slash can have a huge impact on overall security of the Organization.This vulnerable path was fixed by the developer earlier and visiting the above stated Path will result in 403 Denied page.I was able to bypass the fix by appending a / at the end of the path, i.e; /builder/?affiliateId=[VICTIM_AFFID]&affId=[VICTIM_AFFID_LAST_DIGITS]

![](https://miro.medium.com/max/720/1*yLxL0TzcbpD0cfmc_AmF4A.webp)

**Bypassed Exploit URL:**

```http://embed.redacted.com/builder/?affiliateid=[]&affId=[]```

>Note the / at the end of the request.

![$250 bounty awarded for the Second Bypass](https://miro.medium.com/max/720/1*_crdY3vkJwdItWXK-ohTFg.webp)

### Timeline:
>Reported: 07-June-2022\
\
Fixed: 13-June-2022\
\
Bounty: $250

## Fix Bypass x3:

After 2 months of all these i decided to revisit the report once again and started reproducing the issue. I started with the previous bypass, i.e; adding a / but this time it will still lead to 403 Forbidden Page but again something was still phishy here. The page was still a custom 403 page with just a Denied message on it.

After seeing this one thing was sure that the builder was not taken down and instead some kind of regex is being used to filter the response. After 20 mins of hit and trial I was able to bypass the fix by capitalizing the directory name. i.e; I bypassed the second fix by capitalizing the endpoint from /builder to /BUILDER/ and bang we are back into business once again.

![](https://miro.medium.com/max/720/1*dmDqWXUM_NsuBJRFv6Mthg.webp)

**Bypassed Exploit URL:**

```http://embed.redacted.com/BUILDER/?affiliateid=[]&affId=[]```

![$250 bounty awarded for Third Bypass](https://miro.medium.com/max/720/1*v6WF51aaEf5gzf3snqu3-Q.webp)

### Timeline:
>Reported: 02-July-2022\
\
Fixed:08-July-2022\
\
Bounty awarded: $250

Now, they have completely taken down the controller responsible for the embed builder so no more bypasses possible.

---
\
This is my story of turning a simple IDOR vulnerability into a Developer’s Nightmare. This is how I turned a $300 worth IDOR into $1125.

![](https://camo.githubusercontent.com/fddf594173c3b0bfc0534442c41ed9b093785fdf9237e3a9e11c06a57fb876ab/68747470733a2f2f6d65646961302e67697068792e636f6d2f6d656469612f36375468525a6c5942766962746446394a482f67697068792e6769663f6369643d373930623736313139653461633632396636303432623436653033306434376362386133383561316535613634623566267269643d67697068792e6769662663743d67)

So this was it, I enjoyed bypassing these fixes and I hope you enjoyed reading it and learned something new today. Thanks for holding with me :)