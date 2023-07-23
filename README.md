# openai-hackday

Potential use cases:

Natural Language Summarization of Log Events: Use ChatGPT to provide a natural language summary of log events. For example, you might use Splunk to fetch the most recent log events, and then use ChatGPT to generate a human-readable summary of these events.

Automated Troubleshooting Guidance: Use ChatGPT to provide automated troubleshooting guidance based on log data. For example, if a specific error frequently appears in the logs, you could use ChatGPT to generate a step-by-step troubleshooting guide for that error.

Interactive Log Analysis: Create an interactive log analysis tool where users can ask questions about the log data in natural language, and use ChatGPT to generate responses. For example, a user might ask "What was the most common error yesterday?" and the tool would use Splunk to fetch the relevant data and ChatGPT to generate a response.

Anomaly Detection and Explanation: Use Splunk to detect anomalies in the log data (such as a sudden increase in errors), and then use ChatGPT to generate a possible explanation for the anomaly based on the context and details of the log events.

Training and Education: Use ChatGPT to create educational content based on the log data. For example, you might generate case studies or exercises based on real log data to help train staff in log analysis and troubleshooting.

Approach -
1) Take unique identifier or any error code warning or search string from the user via UI (streamlit app preferably)
2) Pass the search string to a script in the backend which is search by splunk queries and then written back to a text file
3) Perform basic preprocessing if needed and store the embeddings in FAISS/Redis
4) Generate a general summary of the results returned by FAISS/Redis by the openai API using summarisation model
5) Based on further probing questions return responses geenrated by the model
6) Discuss for a generic template of response you would want to look at or respond to end user
