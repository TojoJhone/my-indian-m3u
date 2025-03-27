import requests

# URL of the source M3U playlist
source_url = "https://raw.githubusercontent.com/Esmaeli/m3u/refs/heads/main/mvp.m3u"

# Fetch the M3U file
response = requests.get(source_url)
content = response.text

# Define keywords to filter Indian channels
keywords = ["India", "Hindi", "star gold", "zee cinema", "bollywood", "zee", "star plus", "and pictures"]

# Split channels
channels = content.split("#EXTINF")

# Filter only Indian channels
filtered_channels = [f"#EXTINF{channel}" for channel in channels if any(keyword in channel for keyword in keywords)]

# Create the new M3U content
filtered_m3u = "#EXTM3U\n" + "\n".join(filtered_channels)

# Save the filtered file
with open("indian_channels.m3u", "w", encoding="utf-8") as file:
    file.write(filtered_m3u)

print("Filtered M3U file created: indian_channels.m3u")
