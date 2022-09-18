import cohere
co = cohere.Client('kVZ1RsPpqi2y7lX5tVZJX8fcD7mtFKIDlteoo0GB')
response = co.generate(
  model='large',
  prompt='No, unlike Vicky Pollard, I also go to the gym. As you can tell by the tonality of my thighs, it does not convey that I\'m in great shape, but also reveals that I\'m a strong woman and who does not want a strong woman by their side. Now don\'t tell me Maria looks don\'t matter because reality looks do matter. OK, think about it. Site is the first contributor that makes someone attract, that will make you attracted to someone. The I noticed something that likes in the body will walk towards it when it doesn\'t see something it likes. It usually will go away, so when the body goes towards something it likes, the other senses begin to investigate. Touch this brings me to my next point. I have incredibly smooth skin. These are photos of my arm and my leg. How about is it? Laughing great notice. Notice how there was no hair in it whatsoever? And practically and naked cat. Now, how does this benefit you, in a sense? Well, imagine I\'m canoodling. What? We\'re doing something else, and you have the ability to fill in my silky smooth caramelized skin. A rare feel in today\'s society. Enough about the physical attributes that make me a Greek goddess, and let\'s talk about the deeper things. Me, but my personality first and foremost. OK, that\'s wrong. First and foremost, I am funny. Look, you\'re all laughing at my speech right now. Exactly. If you don\'t believe it, here\'s a video of me being funny. ',
  max_tokens=0,
  temperature=0.9,
  k=0,
  p=0.75,
  frequency_penalty=0,
  presence_penalty=0,
  stop_sequences=[],
  return_likelihoods='ALL')
print('Prediction: {}'.format(response.generations[0].token_likelihoods))


