# Manifold Markets Arbitrage

Simultaneously with the [firing of Sam Altman](https://openai.com/blog/openai-announces-leadership-transition) I got pulled into [prediction markets](https://en.wikipedia.org/wiki/Prediction_market), specifically [Manifold](https://manifold.markets/). It was great for both following news as it came out (answering questions like "why did that market just pop up?") and making some minor profits off of weirder, most likely false predictions. Overall, I was surprised with the ease with which a novice predictor (like myself) could take profits off of these questions.

There are also pretty impressive arbitrage[^1] opportunities. For example, I found the following two questions:

- ["Sam Altman will return to OpenAI by the end of 2024"](https://manifold.markets/NealShrestha58d3/sam-altman-will-return-to-openai-by) at ~75% probability, 439 traders and 110K Mana in volume
- ["Will Sam Altman start a new company before 2025?"](https://manifold.markets/Soli/will-sam-altman-start-a-new-company?r=U29saQ) at ~62% probability, 119 traders and 9.8K Mana in volume

These two are likely mutually exclusive - I would guess that the probability of Sam both returning to OpenAI _and_ opening a new company would be pretty much 0. I would also guess that Sam won't go work for, say, Anthropic, Grok, e.t.c., and that most likely he'd use his opportunity right now to start something new. These are the assumptions that we use for this trade.

So, let's do some calculations on what positions we can take, and what the likely profit would be! Let

- `YY` be the outcome of Sam rejoining OpenAI and starting a new company
- `NY` be the outcome of Sam not rejoining OpenAI and starting a new company
- `YN` be the outcome of Sam rejoining OpenAI and not starting a new company
- `NN` be the outcome of Sam going to pick flowers or to live in a cabin in the woods or something.

So, by betting either `YY` or `NN`, it is very likely (based on our assumtions) that we will be correct on at least *one* of the markets! If that profit is greater than the cost of betting in both markets, we have a tidy guarunteed profit. Since both market probabilities were above 0.5, by betting `NN` we have a higher potential return, so let's do that.

For ease of calculation, let's buy 100 mana worth of `N` contracts in both markets, so total cost so far is 200 Mana[^2] Here's the payout table:

| Outcome | Gross Profit | ROI |
| ------- | ------------ | ---------- |
| `YY`    | 0      | 0 :( |
| `YN`    | 246    | 1.23 |
| `NY`    | 380    | 1.9 |
| `NN`    | 246 + 380 = 626 | 3.13 |

By our assumptions, we'll make 23% to 90% profit by this strategy! All that was left to do was make the trades and wait. Doing so dropped the probability of Sam returning to OAI from 75% to 72%, and the probability of Sam creating a new company from 62% to 57%. Time will tell how I do.

Finally: I feel that this was fairly straight-forward - of course, I would not be super surprised if I got something wrong and will take a loss, just because I am new to this. But! If I am right, why has this not been taken advantage of already? Maybe I am under estimating the `YY` case? Maybe other traders don't care so much (and, if they were betting real money, they'd take advantage of these trades)? I think that that is the most likely explanation, and would be very interested in knowing the answer. Beyond the intrinsic benefits of trading on Manifold (which are many! I've had a blast so far), the extrinsic benefits are clout and the ability to [donate their won Mana to charity](https://manifold.markets/charity). Those are both valuable! But, maybe not as much as USD.

Finally-finally: Maybe it would be possible to get an LLM to find correlated markets using Manifold's API? Algo would be something like "stream in market titles, use `gpt-3-turbo` to evaluate correlated markets, and automatically make these hedged trades to make a tidy profit. Since I wouldn't be using real money, I'd feel comfortable offloading most of the evaluation of markets to LLMs. The potential downside would be cost, especially if you are trying to do pairwise-comparisons! But, if you decided that you want to donate some amount to charity, and if this strategy can successfully get more than 100 Mana per $1 of API costs, you would donate more than you put in!

[^1]: Is this actually called arbitrage? I think it would be in the case where `YY` and `NN` are impossible. In the real world case, I guess this would be called hedging your bets? Dunno.
[^2]: I think that the optimal strategy would be to invest more in the less probable market and less in the more probable market so the net profit would be the same for both. That way, expected return would be higher. But, for ease of explanation and just getting the trade in, we'll bet 100 on each market.
