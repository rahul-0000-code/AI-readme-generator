from transformers import RobertaTokenizer, RobertaForSequenceClassification, Trainer, TrainingArguments
from datasets import load_dataset

# Load the CodeBERT tokenizer and model
tokenizer = RobertaTokenizer.from_pretrained("microsoft/codebert-base")
model = RobertaForSequenceClassification.from_pretrained("microsoft/codebert-base")

# Load your custom dataset
# You can use the load_dataset function from the datasets library
dataset = load_dataset('json', data_files={'train': 'dataset.jsonl', 'test': 'dataset.jsonl'})

# Preprocessing the dataset (tokenizing)
def tokenize_function(examples):
    return tokenizer(examples["input"], max_length=512, padding="max_length", truncation=True)

tokenized_datasets = dataset.map(tokenize_function, batched=True)

# Set the format to PyTorch tensors
tokenized_datasets.set_format("torch", columns=["input_ids", "attention_mask", "label"])

# Define training arguments
training_args = TrainingArguments(
    output_dir="./results",
    evaluation_strategy="epoch",
    learning_rate=2e-5,
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    num_train_epochs=3,
    weight_decay=0.01,
)

# Create a Trainer instance
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_datasets["train"],
    eval_dataset=tokenized_datasets["test"],
)

# Start the training
trainer.train()



# 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