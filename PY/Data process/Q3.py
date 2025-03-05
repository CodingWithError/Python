import urllib
import json
import urllib.request
import math

def retrieve_data(course_name: str):
  url=f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats"
  with urllib.request.urlopen(url) as resp:
    data=json.loads(resp.read().decode())

  dir={}
  weeks=len(data)
  students=max(week["students"] for week in data.values())
  hours=max(week["hour_total"] for week in data.values())
  exercises=sum(week["exercise_total"] for week in data.values())

  hours_average = math.floor(hours / students) if students > 0 else 0
  exercises_average = math.floor(exercises / students) if students > 0 else 0
  
  dir["weeks"]=weeks
  dir["students"]=students
  dir["hours"]=hours
  dir["hours_average"]=hours_average
  dir["exercises"]=exercises
  dir["exercises_average"]=exercises_average

  return dir

print(retrieve_data("docker2019"))