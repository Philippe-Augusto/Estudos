from clearml import Dataset

dataset = Dataset.create(
    dataset_name="meu_dataset",
    dataset_project="meu_projeto",
    description="Dataset com arquivos do MinIO local",
    output_uri="s3://localhost:9000/clearml"
)

dataset.add_external_files(
    source_url="s3://localhost:9000/clearml/",
    wildcard="*.png",
    recursive=True,
    verbose=True
)

dataset.upload()
dataset.finalize(verbose=True, auto_upload=True)
print(f"Dataset criado com ID: {dataset.id}")
