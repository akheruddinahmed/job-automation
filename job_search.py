import google.generativeai as genai
import datetime
import os

# ✅ Correct way: read from environment variable
genai.configure(api_key=os.getenv("API_KEY"))

model = genai.GenerativeModel('gemini-1.5-flash-latest')

prompt = """
Find job listings posted in the last 24 hours for a Java Full Stack Developer.

Profile:
- Skills: Java, Spring Boot, Hibernate, REST APIs, JWT, OAuth2, React.js, MySQL
- Experience: Fresher / Entry Level
- Location: Bangalore or Remote

Requirements:
1. Search LinkedIn, Indeed, company career pages
2. Provide Job Title, Company, Location
3. Include direct apply links
4. Prefer fresher / junior roles
"""

response = model.generate_content(prompt)

print(f"\n📅 Report for {datetime.date.today()}:\n")
print(response.text)
