# Reflection

Student Name:  josh elman
Sudent Email:  jdelman@syr.edu

## Instructions

Reflection is a key activity of learning. It helps you build a strong metacognition, or "understanding of your own learning." A good learner not only "knows what they know", but they "know what they don't know", too. Learning to reflect takes practice, but if your goal is to become a self-directed learner where you can teach yourself things, reflection is imperative.

- Now that you've completed the assignment, share your throughts. What did you learn? What confuses you? Where did you struggle? Where might you need more practice?
- A good reflection is: **specific as possible**,  **uses the terminology of the problem domain** (what was learned in class / through readings), and **is actionable** (you can pursue next steps, or be aided in the pursuit). That last part is what will make you a self-directed learner.
- Flex your recall muscles. You might have to review class notes / assigned readings to write your reflection and get the terminology correct.
- Your reflection is for **you**. Yes I make you write them and I read them, but you are merely practicing to become a better self-directed learner. If you read your reflection 1 week later, does what you wrote advance your learning?

Examples:

**Poor Reflection:**  "I don't understand loops."   
**Better Reflection:** "I don't undersand how the while loop exits."   
**Best Reflection:** "I struggle writing the proper exit conditions on a while loop." It's actionable: You can practice this, google it, ask Chat GPT to explain it, etc. 

**Poor Reflection** "I learned loops."   
**Better Reflection** "I learned how to write while loops and their difference from for loops."   
**Best Reflection** "I learned when to use while vs for loops. While loops are for sentiel-controlled values (waiting for a condition to occur), vs for loops are for iterating over collections of fixed values."

`--- Reflection Below This Line ---`


In this assignment, we built a complete ETL and data visualization pipeline for analyzing parking violations in Syracuse. In etl.py, we implemented three key functions to extract and transform the dataset final_cuse_parking_violations.csv. The function top_locations() filtered and aggregated violation amounts by location where total fines exceeded \$1,000. The function top_locations_mappable() added these locations with latitude and longitude coordinates for mapping, and function tickets_in_top_locations() selected all individual ticket records issued at these top locations. Each function saved the processed results to CSV files for downstream use. The map_dashboard.py script visualizes the top fine-heavy locations using a heatmap powered by Folium and GeoPandas, with each point scaled by the total amount of violations. The location_dashboard.py script provides an interactive dashboard where users can explore ticket data by selecting a location from a dropdown. The code difficulty is moderate in this assignment.