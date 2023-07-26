import streamlit as st
import openai
import os
import re
from collections import Counter

# Set the API key
openai.api_key = 'your-openai-api-key'

# Preprocessing function
def preprocess(log_entry):
    # Remove non-alphanumeric characters
    log_entry = re.sub(r'\W+', ' ', log_entry)
    # Additional preprocessing steps can be added here
    return log_entry

# This function makes an API call to GPT-3.5 and returns the response
def analyze_log_batch(log_batch, previous_analysis):
    # Create the prompt with context
    prompt = "Given the previous analysis:\n" + previous_analysis
    prompt += "\nPlease identify any errors in the following log data:\n" + log_batch

    # Make the API call
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.5,
        max_tokens=100
    )

    return response.choices[0].text.strip()

# Streamlit application
def main():
    st.title("Log Analysis with OpenAI GPT-3.5")

    # Specify the directory where the log files are located
    log_directory = "/path/to/your/log/files"

    # Get a list of all log files in the directory
    log_files = [f for f in os.listdir(log_directory) if os.path.isfile(os.path.join(log_directory, f))]

    # Button to start analysis
    if st.button("Analyze"):
        if log_files:
            # Initialize a list to store all the errors
            all_errors = []

            # Analyze each file and store the results
            for log_file in log_files:
                st.write(f"Analyzing file: {log_file}")
                with open(os.path.join(log_directory, log_file), 'r') as file:
                    file_text = file.read()

                    # Preprocess the log lines
                    log_lines = file_text.split('\n')
                    log_lines = [preprocess(line) for line in log_lines[:2000]]  # Limit to 2000 lines

                    # Create batches of lines
                    batch_size = 5
                    log_batches = [log_lines[i:i+batch_size] for i in range(0, len(log_lines), batch_size)]

                    # Analyze each batch and store the results
                    previous_analysis = ""
                    for batch in log_batches:
                        # Join the lines in the batch into a single string
                        batch_text = '\n'.join(batch)
                        result = analyze_log_batch(batch_text, previous_analysis)
                        previous_analysis = result  # Update the previous analysis for the next batch

                        # Parse the result into individual errors and add them to the list
                        errors = result.split('\n')
                        for error in errors:
                            all_errors.append(error)

            # Count the occurrence of each error
            error_counts = Counter(all_errors)

            # Display the count of each error
            st.write("Error counts:")
            for error, count in error_counts.items():
                st.write(f"{error}: {count}")
        else:
            st.write("No log files found in the specified directory.")

if __name__ == "__main__":
    main()
  
