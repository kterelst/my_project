[![Test and Deploy](https://github.com/kterelst/my_project/actions/workflows/test-and-deploy.yml/badge.svg)](https://github.com/kterelst/my_project/actions/workflows/test-and-deploy.yml)

### My 3 elements

##### Element 1: Virtual Private Server **Digital Ocean**
This is the final destination. The place users can interact with.
Checkout the Webpage on ***http://134.209.198.158/***.

> Problem:
> 60-day free trail
> Payment method must be PayPal or Creditcard
> For PayPal a start-fee must be admitted, no refunds
> No creditcard owned
> Borrowed from my parents
> Hopefully no charge


##### Element 2: Using **SSH** with **SECRETS**
The ***safe*** way to communicate with your remote server and GitHub.
Putting these SSH-keys in GitHub Secrets ensures that these won't be prone to decription.

> Problem:
> No knowledge of SSH, Secrets of whatsoever
> Read all documentation provided and not-provided
> Watched all videos in live-lessons stored with slight reference
> Asked around at slack-channel #vraagbaak-python
> With the help of Donatas, Thomas and Dominique found a working solution

I advise to elaborate on the subject of SSH:
* Mainly the vision of when to use public and when private keys,
* But also how to implement them into het local, remote and GitHub.


##### Element 3: Web Server **NGINX**
As provided in earlier exercise I've used the Web Server ***NGINX***.
This Web Server is launching my project I called "cd",
running on my Digital Ocean Virtual Private Server.
Ofcourse this stands for Continuous Deployment!

> Problem:
> Restarting the webpage was difficult
> Or might I say: Impossible
> Until I had a epiphany!
> using my "server-name" instead of nginx did the trick