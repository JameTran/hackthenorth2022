from fastapi import FastAPI
import summary

app = FastAPI()
paragraphs = summary.readFile()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/summary")
async def summaryasync():
    summaries = summary.generateSummary(paragraphs)
    

@app.get("/tone")
async def tone():
    return {"message": "placeholder, tones to be implemented"}

@app.get("/correction")
async def correction():
    return {"message": "placeholder, correction to be implemented"}
