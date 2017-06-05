# Objective
Develop a model combining data from Yelp and Groupon to predict the longterm success of a business. The project will focus on business failure first by obtaining and analyzing the Yelp pages of thousands of closed business, then augmenting the training set with random samples of successful businesses from each category. 

This project will a lighter side. We will develop a website called Grelp Me! That uses this combined model to predict whether a current Groupon deal is a good deal, and whether the company stands of chance of staying in business in the next few months.   

Underneath, however, this project is really about the asymmetric web and walled gardens. Yelp hides failed businesses from their search, but search engines still scrape them. Groupon also does not make past deals available to the public. While google claims it has over 2 million results for closed businesses in its index, it doesn’t allow scraping or even human access to more than 500 results. 

# The Data
Yelp's Business API returns an  "is\_closed" boolean flag indicating a business has permanently or temporarily closed. However, this variable is not exposed in the Search API. It is also impossible to search for a closed businesses through the consumer facing channels (web, mobile, etc).  Yelp even removes closed business from the general search within a year or two (source: yelp forums). Fortunately, Yelp leaves the business information exposed if you know the URL or the Yelp business_id (which, it turns out are actually the same, there goes a half day of work). It has not been easy (more on this later), but I’ve accumulative a list of 10,000 failed businesses and their Yelp ids from search engine results, mostly google. Businesses also using Groupon is obviously a smaller subset. However, the nature of the discount and the profitability of the deal can be estimated and tied to the prediction.

# Groupon as unsustainable model

"Sucking value out of the small business market will ultimately damage the local merchants that are the bread and butter of Groupon’s base. Groupon’s model is not sustainable. In a race to the bottom everyone drowns."--[CEO, SpaBoom and CoverBoom, Bill Bice (Sep 20, 2012)](http://www.cnbc.com/id/49092709)


# Groupon as a Hail Mary pass
"...if you’re going out of business (in which case the Groupon is a Hail Mary pass) then Groupon might be for you."--[Ding Dong, Daily Deals Are Dead](http://www.slate.com/articles/technology/technology/2012/08/groupon_earnings_report_the_daily_deals_site_s_crummy_business_model_is_finally_dead_hooray_.html)

# References
There are hundreds of papers written on Groupon and Yelp, and even the influence of Groupon on Yelp reviews:
- [Slight Changes in Yelp Ratings Can Mean Huge Losses for Small Businesses](https://www.theatlantic.com/technology/archive/2012/09/slight-changes-in-yelp-ratings-can-mean-huge-losses-for-small-businesses/261943/)
- [Groupon's Hidden Influence on Reputation (MIT Technology Review)](https://www.technologyreview.com/s/425395/groupons-hidden-influence-on-reputation/)
- [To Groupon or Not to Groupon: The Profitability of Deep Discounts (Harvard Business School research)](http://www.hbs.edu/research/pdf/11-063.pdf)
- [Is Yelp hurting chain restaurant sales?](http://www.restaurant-hospitality.com/consumer-trends/yelp-hurting-chain-restaurant-sales)
- [Businesses accusing Yelp of extortion lose another round in court](http://www.latimes.com/business/la-fi-yelp-ratings-20140905-story.html)

