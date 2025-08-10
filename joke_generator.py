from google.ai import generativelanguage

def generate_silly_joke():
    client = generativelanguage.GenerativeServiceClient()
    model = "models/gemini-1"

    # Compose TextPrompt first
    prompt = generativelanguage.TextPrompt(text="Tell me a silly joke.")

    # Pass the prompt directly to GenerateContentRequest
    request = generativelanguage.GenerateContentRequest(
        model=model,
        prompt=prompt,
        temperature=0.7,
        candidate_count=1,
        max_output_tokens=60,
    )

    response = client.generate_content(request=request)
    return response.candidates[0].output

if __name__ == "__main__":
    joke = generate_silly_joke()
    print("Here's a silly joke for you:\n")
    print(joke)
