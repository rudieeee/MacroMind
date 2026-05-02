def process_text(text):
    # Simple parsing logic (replace with Gemini later)

    # Convert to lowercase
    text = text.lower()

    # Replace commas with space
    text = text.replace(",", " ")

    # Split words
    words = text.split()

    # Filter basic food-like words (very simple logic)
    items = [word for word in words if len(word) > 2]

    return items