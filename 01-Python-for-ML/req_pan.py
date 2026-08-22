# Web requests
import requests
import pandas as pd

response = requests.get("https://jsonplaceholder.typicode.com/posts")
data = response.json()
print(data)

# Data analysis

# Create a simple DataFrame
data = {
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'city': ['NYC', 'LA', 'Chicago']
}
df = pd.DataFrame(data)
print(df)