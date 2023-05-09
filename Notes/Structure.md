# Project Structure

## Objective:
- [ ] Create a service to get all the data from the fastf1 cache
- [ ] Create a service to apply different analysis technique on the session data
- [ ] Store all the session data in a database
- [ ] Make a dashboard for people to play around with this data
- [ ] Write a document to explain how to use this data
- [ ] Write a document for this project


### Task 1. Create a Service to get all the data from FastF1
We can create a session using the following

```python
"""
To get the qualifying session from the 2019, Monza Race Weekend
"""
session = fastf1.get_session(2019, 'Monza', 'Q')
```
