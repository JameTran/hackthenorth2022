from fastapi import FastAPI
import summary
import grammar
import tones

app = FastAPI()
paragraphs = summary.readFile("sample.txt")
p2 = summary.readFile("sample2.txt")
p3 = summary.readFile("sample3.txt")
#print(paragraphs)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/summary")
async def summaryasync():
    summaries = summary.generateSummary(paragraphs)
    return summaries
    
@app.get("/informal_tone")
async def tone():
    informal_paragraphs = []
    for i in p3:
        informal_paragraphs.append(tones.informal_to_formal(i))
    return informal_paragraphs
'''
@app.get("/formal_tone")
async def tone():
    formal_paragraphs = []
    for i in paragraphs:
        formal_paragraphs.append(tones.tones.formal_to_informal(i))
    return formal_paragraphs
'''
@app.get("/correction")
async def correction():
    corrected_paragraphs = []
    for i in p2:
        corrected_paragraphs.append(grammar.correct_grammar(i))
    return corrected_paragraphs
