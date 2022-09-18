import cohere
co = cohere.Client('kVZ1RsPpqi2y7lX5tVZJX8fcD7mtFKIDlteoo0GB')

def correct_grammar(str):
    response = co.generate(
    model='large',
    prompt='This is voice-to-text transcription corrector. Given a transcribed excerpt with errors, the model responds with the correct version of the excerpt.\n\nIncorrect transcription: I am balling into hay to read port missing credit card. I lost by card when I what\'s at the grocery store and I need to see sent a new one.\n\nCorrect transcription: I am calling in today to report a missing credit card. I lost my card when I was at the grocery store and I need to be sent a new one.\n--\nIncorrect transcription: Can you repeat the dates for the three and five dear fixed mortgages? I want to compare them a gain the dates I was quoted by a other broker.\n\nCorrect transcription: Can you repeat the rates for the three and five year fixed mortgages? I want to compare them against the rates I was quoted by another broker.\n--\nIncorrect transcription: I got got charged interest on ly credit card but I paid my pull balance one day due date. I not missed a pavement year yet. Man you reverse the interest charge?\n\nCorrect transcription: I got charged interest on my credit card but I paid my balance on the due date. I haven\'t missed a payment yet. Can you reverse the interest charge?\n--\nIncorrect transcription: I walk to the store and I bought milk.\n\nCorrect transcription: I walked to the store and I bought milk\n--\nIncorrect transcription: I is calling on to report a missing credit bard. I lost I card when I was at the grocery store and I need to be sent a new one.\n\nCorrect transcription: I am calling to report a missing credit card. I lost my card when I was at the grocery store and I need to be sent a new one.\n--\nIncorrect transcription: I sold a house and I get a check for the deposit.\n\nCorrect transcription: I sold a house and I get a check for the deposit.\n--\nIncorrect transcription: It is raining when I got home last night.\n\nCorrect transcription: It was raining when I got home last night.\n--\nIncorrect transcription: My sister is annoying today, but usually she is nice.\n\nCorrect transcription: My sister is being annoying today, but usually she is nice.\n--\nIncorrect transcription: I have not ate anything today.\n\nCorrect transcription: I have not eaten anything today.\n--\nIncorrect transcription: If I am a child, I would play outside.\n\nCorrect transcription: If I were a child, I would play outside.\n--\nIncorrect transcription: Everyone have seen that movie.\n\nCorrect transcription: Everyone has seen that movie.\n--\nIncorrect transcription:' + str + '\n' + '\nCorrect transcription:',
    max_tokens=200,
    temperature=0.5,
    k=0,
    p=1,
    frequency_penalty=0,
    presence_penalty=0,
    stop_sequences=["--"],
    return_likelihoods='NONE')
    return ('Prediction: {}'.format(response.generations[0].text))

#print(correct_grammar("At the start of school Dora was afrad of  her new Teacher. Mrs. Davis  seamed nice, but she had so manny rules for the class to folow. Scare  someone to pieces. As the school year cotinued, Dora begun to understan  how the Teacher come up with the rules The rules were their so students  would be respecful of  theyselves and each other. By the end of  the year,  Dora though Mrs. Davis was the best Teacher she evere had!"))

