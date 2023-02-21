# byeBird

Deleting all your tweets, favorites, and follows using python...[while you still can](https://twitter.com/TwitterDev/status/1623467615539859456)! Read [more below](#why) about I wanted to.

### Set it up
The following steps create a virtual environment, and I deal with API credential handling using [dynaconf](https://www.dynaconf.com/). Alternatively, just copy [`birdBye.py`](https://github.com/tgj505/byeBird/blob/main/birdBye.py), install tweepy and tqdm, and insert your API variables directly in the file to run.
- Pull this repo.
- Set up your [virtual environment](https://docs.python.org/3/library/venv.html), e.g. using cmd:
    - `> py -m venv .venv`
    - `> .venv\Scripts\activate.bat`
    - `> py -m pip install --upgrade pip`
- install the needed packages and environment
    - `> py -m pip install -r requirements.txt		
	- `> dynaconf init -f toml`
	- You can update .gitignore, if you'd like.

### API access
- Get credentials to the twitter API [here](https://developer.twitter.com/). Or reach out to me if you want me to see if i can run this for you.
	- You have to have a twitter account.
	- Ensure your app is part of a project, set up user authentication, and apply for elevated access.
	
- Update your `.secrets.toml` file with your API credentials and your Twitter user ID. (Or just put these directly in the `byeBird.py` code).
  - api_key=""
  - api_key_secret=""
  - access_token=""
  - access_token_secret=""
  - bearer_token=""
  - user_id=""

### You might also want to ...
- Download your twitter data by going [here](https://twitter.com/settings/download_your_data). 
- Lock down your [posts](https://twitter.com/settings/audience_and_tagging).

### delete it
There's no going back, so make sure you're ready to delete all your twitter stuff.
- `> py -m birdBye`


---

### why

Why might you want to delete everything? Do you want [this guy](https://www.vanityfair.com/news/2022/04/elon-musk-twitter-terrible-things-hes-said-and-done) and his sycophantic lackeys to have access to your stuff, monetizing your attention and actions? Using your tweets to tune an AI? Selling your data to anyone they want?

Why not just delete the whole account? Paranoia of impersonatin

Some more specific bad things about twitter and the muskmelon, who (has said)[https://twitter.com/alx/status/1625734305447088128] that "at the end of the day, having some criticism is fine, ya know, it's really not that bad. I mean, I am constantly attacked on twitter, frankly, and I don't mind."

### API Access

Instead of providing accountability through public data, Twitter has decided to make their API access prohibitively expensive ($100/month). [So sorry](https://apnews.com/article/twitter-api-eca5709035a08d2ebed8fac673809ea8) activists, emergency workers, researchers, developers, and everyone else interested in keeping tabs on an influential media company roiled in scandal, criticism, and decline! Seems pretty [bad](https://www.nature.com/articles/d41586-023-00460-z)!


#### finance and labor
When the melonhusk acquisition deal went through, the new ceo went on a [firing spree](https://apnews.com/article/elon-musk-twitter-inc-technology-business-1f1a67299681beaf1fc9cbae4747287b), laying off [thousands](https://apnews.com/article/elon-musk-twitter-inc-business-layoffs-c0334da78b3af9faf2f43cf3f6e52ffa), including people in charge of safety and oversight. They're overworking their remaining staff, going "hardcore mode" and having workers [sleep at office](https://apnews.com/article/elon-musk-twitter-inc-technology-san-francisco-business-1c067f26852384d48a56f11fadda7142), with cascading fallout of [security issues](https://apnews.com/article/elon-musk-twitter-inc-technology-business-federal-trade-commission-329a984fe607d27ad7f8b37269ad8578), [leaks of pricate user information](https://apnews.com/article/twitter-inc-technology-social-media-business-ce4567176ed1824bb6e3e4376708c12d), and [disinformation](https://apnews.com/article/voting-rights-elon-musk-twitter-inc-technology-dd4273dbda5b15343753f56c1f43a659) on [multiple](https://apnews.com/article/voting-rights-elon-musk-twitter-inc-technology-dd4273dbda5b15343753f56c1f43a659) [fronts](https://apnews.com/article/elon-musk-twitter-inc-technology-science-social-media-a7e2e3214abb4470dcb6e2837aa39c2e).

And despite these kinds of cost cutting measures (in addition to making people pay to access [2-factor authentication](https://www.msn.com/en-gb/money/other/twitter-s-going-to-charge-people-for-sms-2fa-here-s-how-to-switch-to-a-free-option/ar-AA17Iq0k) and twitter blue), the company is still floundering. They are not paying the rent they owe on [multiple properties](https://apnews.com/article/elon-musk-twitter-inc-technology-business-san-francisco-173194eff0b8f70e6d2d3ff6f1f082f9). They could face hefty fines in the EU.


#### everyting else!
Don't forget the right wing propoganda, doxxing, potential fraud, international legal and [regulatory violations](https://apnews.com/article/elon-musk-twitter-inc-technology-politics-european-union-0f912b92a70742ba8ad280cde2f935d9), the climate [misinformation](https://apnews.com/a7e2e3214abb4470dcb6e2837aa39c2e), or the restriction of [free press](https://apnews.com/article/elon-musk-technology-business-social-media-647b3b9d5961da3cd8bd0c0041d05b49).
There's also all the bratty, adolescent absurdities. The 51 year old manchild CEO tweeted two vaguely pornographic memes (one showing the washington monument as a giant's dick). A couple days before, just after one of his tweets didn't get as much engagement as he wanted, the muskmelon [ordered engineers](https://www.theverge.com/2023/2/14/23600358/elon-musk-tweets-algorithm-changes-twitter) to increase propogation of his posts. 

All the aforementioned stuff is pretty recent. But lots of these issues run deep in both [twitter](https://apnews.com/article/technology-middle-east-saudi-arabia-money-laundering-dc9612bf2f80af6be192606bd1af7d71) and tech in general. [evil sentient Bing](https://erikhoel.substack.com/p/i-am-bing-and-i-am-evil) wasn't on my 2023 bingo board.

#### loneskum's business history
Tesla factories are unsafe and the CEO has illegally fired employees for attempting to [unionize](https://www.vanityfair.com/news/2023/02/elon-musks-tesla-fires-employees-unionize). PLus the cars themselves are extremely dangerous, with hundreds of thousands being [recalled all the time](https://time.com/6256478/tesla-recall-self-driving-safety-concerns/), and deaths resulting from Teslas crashing into [emergency vehicles](https://apnews.com/article/technology-business-injuries-fires-59d22dced75ec1ce6929c9dfb094524c). If his companies can only make expensive, buggy, unsafe cars, how can twitter take care of its security and misinformation problems?

### mastodon is chill. 
Check it out. [@tomasito@mas.to](https://mas.to/@tomasito). Or just get rid of it all.

Reach out if I can help!