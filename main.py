from fastapi import FastAPI
import summary

paragraphs = summary.readFile()
print(paragraphs)
print("\n")
a = summary.generateSummary(paragraphs)
print(a)