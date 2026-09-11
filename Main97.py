# E54.Regular Expressions in Python.
# https://regexr.com/.
import re;
pattern = r"[A-Z]+yclodne"
text = '''Cyclone Nargis was one of the deadliest tropical cyclones of the 21st century. It struck Myanmar in May 2008, especially the densely populated Ayeyarwady Delta. The cyclone brought extremely strong winds, heavy rainfall, and a massive storm surge that flooded large coastal areas. More than 138,000 people were reported dead or missing, and millions of people were affected. Thousands of homes, farms, roads, bridges, and boats were destroyed. The disaster caused a major humanitarian crisis and highlighted the importance of early warning systems, evacuation plans, cyclone shelters, and disaster preparedness in vulnerable coastal regions.'''
match = re.search(pattern, text)
print(match)
# matches = re.finditer(pattern, text).
# for match in matches:
#     print(match.span()).
#     print(text[match.span()[0]]:match.span()[1]).