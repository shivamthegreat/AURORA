import wikipedia

def tell_me_about(topic):
    try:
        # Get a summary of the topic
        summary = wikipedia.summary(topic, sentences=3)
        
        # Return the summary
        return summary
    except wikipedia.exceptions.PageError:
        print(f"Sorry, the page for '{topic}' does not exist.")
        return False
    except wikipedia.exceptions.DisambiguationError as e:
        print(f"Multiple results found for '{topic}'. Please be more specific. Options include: {e.options}")
        return False
    except wikipedia.exceptions.HTTPTimeoutError:
        print("The request to Wikipedia timed out. Please try again later.")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
