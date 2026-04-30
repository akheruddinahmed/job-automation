import google.generativeai as genai
import datetime
import os

# 🔐 Use API key from environment (GitHub Secrets or local env)
genai.configure(api_key=os.getenv("API_KEY"))

# ✅ Use stable model (works with your current setup)
model = genai.GenerativeModel('gemini-pro')

# 🔍 Your job search prompt
prompt = """
Find job listings posted in the last 24 hours for a Java Full Stack Developer.

Profile:
- Skills: Java, Spring Boot, Hibernate, REST APIs, JWT, OAuth2, React.js, MySQL
- Experience: Fresher / Entry Level
- Location: Bangalore or Remote

Requirements:
1. Search LinkedIn, Indeed, and company career pages
2. Provide Job Title, Company Name, Location
3. Include direct application links
4. Prefer fresher / junior roles
"""

# 🚀 Generate response
response = model.generate_content(prompt)

# 📅 Print result
print(f"\n📅 Report for {datetime.date.today()}:\n")
print(response.text)
