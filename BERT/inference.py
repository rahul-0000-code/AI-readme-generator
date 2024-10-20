from transformers import RobertaTokenizer, RobertaForSequenceClassification

# Load fine-tuned model and tokenizer
tokenizer = RobertaTokenizer.from_pretrained("path_to_finetuned_model")
model = RobertaForSequenceClassification.from_pretrained("path_to_finetuned_model")

def generate_readme(repo_data):
    # Tokenize the input (folder structure + snippets)
    inputs = tokenizer(repo_data, return_tensors="pt", truncation=True, max_length=512)

    # Generate predictions
    outputs = model.generate(inputs["input_ids"], max_length=512, num_return_sequences=1)

    # Decode and return the README content
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# Example usage
repo_data = "src/app.py, README.md, requirements.txt"
readme_md = generate_readme(repo_data)
print(readme_md)
