
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))
print("=== RESUME SCREENING AI AGENT ===")

jd = input("\nPaste Job Description: ")
r1 = input("Priya Singh. Skills: Java, Spring, MySQL, 2 years exp. Projects: Banking app. Education: BTech CSE ")
r2 = input("Rahul Verma. Skills: Python, Pandas, SQL, 1 year exp. Projects: Data analysis dashboard. Education: BCom ")
r3 = input("Aryan Sharma. Skills: Python, Django, SQL, 3 years exp. Projects: E-commerce website, Blog app. Education: BCA ")

resumes = [r1, r2, r3]


print("\n=== RANKING CANDIDATES ===")
for i, resume in enumerate(resumes, 1):
    prompt = f"""
    You are an HR AI Agent.
    Job Description: {jd}
    Resume: {resume}
    
    Task: Give a Score out of 100 and 3 bullet points explaining why.
    Format:
    Score: X/100
    Reasons: 
    1. 
    2. 
    3.
    """
    
    res = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role":"user","content":prompt}]
    )
    print(f"\n--- Resume {i} ---")
    print(res.choices[0].message.content)

print("\n=== DONE ===")