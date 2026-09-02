import urllib.request
import os

topics = [
    "python", "java", "cpp", "c", "javascript", "typescript",
    "react", "html", "css", "tailwind",
    "nodejs", "express", "flask",
    "opencv",
    "mongodb", "mysql", "postgresql",
    "docker", "kubernetes", "gitlab", "argocd",
    "git", "github", "postman"
]

os.makedirs("assets/tech", exist_ok=True)

success = []
for topic in topics:
    url = f"https://raw.githubusercontent.com/github/explore/master/topics/{topic}/{topic}.png"
    filepath = f"assets/tech/{topic}.png"
    try:
        urllib.request.urlretrieve(url, filepath)
        success.append(topic)
        print(f"Downloaded {topic}")
    except Exception as e:
        print(f"Failed {topic}: {e}")

print("Successful:", success)
