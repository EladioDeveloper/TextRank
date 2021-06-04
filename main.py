from text_rank import TextRank4Keyword

text = '''
Cryptocurrency “cannot come at great cost to the environment,” the electric carmaker said in a statement tweeted by Musk. The statement was hedged, but only slightly, with praise for crypto’s “promising future” and a promise to investigate less energy-hungry networks than Bitcoin’s.

Bitcoin, a proof-of-work (PoW) blockchain reliant on energy-intensive mining units, has come under fire from environmental groups as its price has surged to all-time highs. The second-largest cryptocurrency by market cap, ether, also relies on PoW but is in the process of switching to proof-of-stake.

Tesla’s pledge turns up the heat on the race to move bitcoin away from fossil fuels. The company’s decision to accept bitcoin was a watershed moment for corporate bitcoin adoption. Tesla’s turnabout on environmental matters will likely give fuel to the social and even political moment clamoring for change to the world’s largest cryptocurrency by market cap.

The sudden freeze of Tesla’s bitcoin payments hands a decisive win to bitcoin’s energy critics. But it does not spell doom for Tesla’s remaining bitcoin investment nor its crypto experiment. “Tesla will not be selling any bitcoin,” the statement read. “We intend to use it for transactions as soon as mining transitions to more sustainable energy.”

Tesla did test the liquidity of the bitcoin market with a $272 million sell announced during its most recent earnings call.
'''
tr4w = TextRank4Keyword()
tr4w.analyze(text, candidate_pos = ['NOUN', 'PROPN'], window_size=4, lower=False)
tr4w.get_keywords(20)