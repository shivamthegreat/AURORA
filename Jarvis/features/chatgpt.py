import openai

# Set your OpenAI API key here
openai.api_key = 'your-open-ai-key'


def get_response(prompt):
    """
    Sends a prompt to the OpenAI API and returns the response.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",  # Use the latest available model
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        return f"Error: {str(e)}"

def answer_question(question):
    """
    Answers a basic question using the OpenAI API.
    """
    prompt = f"Answer the following question: {question}"
    response = get_response(prompt)
    return response

# Example usage
if __name__ == "__main__":
    question = "hello?"
    answer = answer_question(question)
    print(answer)
