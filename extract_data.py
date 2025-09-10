
from datasets import load_dataset, Dataset, load_from_disk

dataset = load_dataset("VietAI/vi_pubmed", split="pubmed22[:2000000]")

print(dataset)

df =  dataset.to_pandas()

df = df.drop(['vi'], axis=1)

df = df.drop_duplicates()

data = Dataset.from_pandas(df, preserve_index=False)
print(data)

data.save_to_disk("data_pubmed")

# dataset = load_from_disk("data_pubmed")
# print(dataset)

# dataset[0]

