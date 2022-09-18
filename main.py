from fastapi import FastAPI
import summary
import grammar

app = FastAPI()
paragraphs = summary.readFile("sample.txt")
#print(paragraphs)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/summary")
async def summaryasync():
    summaries = summary.generateSummary(paragraphs)
    return {summaries}
    
@app.get("/tone")
async def tone():
    return {"message": "placeholder, tones to be implemented"}

@app.get("/correction")
async def correction():
    corrected_paragraphs = []
    for i in paragraphs:
        corrected_paragraphs.append(grammar.correct_grammar(i))
    return corrected_paragraphs
