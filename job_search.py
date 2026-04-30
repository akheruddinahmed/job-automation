from google import genai
import datetime
import os

# 🔐 API key from GitHub Secrets
client = genai.Client(api_key=os.getenv("API_KEY"))

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

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=prompt
)

print(f"\n📅 Report for {datetime.date.today()}:\n")
print(response.text)
