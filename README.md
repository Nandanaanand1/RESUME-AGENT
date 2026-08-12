# AI Resume Screening Agent

An AI-powered agent that automates the first round of resume screening using Groq's Llama-3.1 model.

# What it Does
Instead of manually reading 100s of resumes, this agent:
1. Takes a Job Description as input
2. Takes multiple Resumes as input  
3. Uses Groq AI to compare and give each candidate a Score out of 100 + 3 reasons
4. Helps HR shortlist candidates 10x faster

# Tech Stack
- **Language**: Python 3
- **AI Model**: Llama-3.1-8b-instant via Groq API
- **Libraries**: groq

# Setup & Installation

1.  **Clone the repo**
    ```bash
    git clone <your-repo-link>
    cd ai-resume-screener