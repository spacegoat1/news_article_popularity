## Data

The data was collected during a two year period, from January 7 2013 to January 7 2015. We discarded a small portion of special occasion articles that did not follow the
general HTML structure, since processing each occasion type would require a speciﬁc parser. We also discarded very recent articles (less than 3 weeks), since the number of Mashable shares did not reach convergence for some of these articles (e.g., with less than 4 days) and we also wanted to keep a constant number of articles per test set in our rolling windows assessment strategy (see Section 2.3).

We selected a large list of characteristics that describe diﬀerent aspects of the article and that were considered possibly relevant to inﬂuence the number of shares. Some of the features are dependent of particularities of the Mashable service: articles often reference other articles published in the same service; and articles have meta-data, such as keywords, data channel type and total number of shares (when considering Facebook, Twitter, Google+, LinkedIn, StumbleUpon and Pinterest).

Thus, we extracted the minimum, average and maximum number of shares (known before publication) of all Mashable links cited in the article. Similarly, we rank all article keyword average shares (known before publication), in order to get the worst, average and best keywords. For each of these keywords, we extract the minimum, average and maximum number of shares. The data channel categories are: “lifestyle”,“bus”,“entertainment”,“socmed”, “tech”,“viral” and “world”.

We also extracted several natural language processing features. The Latent Dirichlet Allocation (LDA) [12] algorithm was applied to all Mashable texts (known before publication) in order to ﬁrst identify the ﬁve top relevant topics and then measure the closeness of current article to such topics. To compute the subjectivity and polarity sentiment analysis, we adopted the Pattern web mining module (http://www.clips.ua.ac.be/pattern) [13], allowing the computation of sentiment polarity and subjectivity scores.


