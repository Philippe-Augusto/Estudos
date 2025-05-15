from clearml import Dataset
import os

# Carregar o dataset original
parent_dataset = Dataset.get(dataset_project="meu_projeto", dataset_name="meu_dataset")
print(f"Dataset original carregado: {parent_dataset.id}")

# Criar um novo dataset como filho do dataset original
new_dataset = Dataset.create(
    dataset_name="meu_dataset_subconjunto",
    dataset_project="meu_projeto",
    parent_datasets=[parent_dataset.id],  # Vincula ao dataset original
    description="Subconjunto do dataset original com arquivos PNG selecionados",
    output_uri="s3://localhost:9000/clearml"  # Mesmo bucket, apenas referências
)

# Obter o caminho local do dataset original
local_path = parent_dataset.get_local_copy()
print(f"Dataset original baixado para: {local_path}")

# Selecionar um subconjunto de arquivos (exemplo: até 2 arquivos PNG)
selected_files = []
file_count = 0
max_files = 2  # Limite de arquivos para o subconjunto
for root, _, files in os.walk(local_path):
    for file in files:
        if file.endswith(".png"):
            file_path = os.path.join(root, file)
            # Converter o caminho local para o caminho relativo no dataset
            relative_path = os.path.relpath(file_path, local_path)
            selected_files.append(relative_path)
            file_count += 1
            if file_count >= max_files:
                break
    if file_count >= max_files:
        break

# Adicionar os arquivos selecionados ao novo dataset
for relative_path in selected_files:
    # O arquivo já está no bucket original, então apenas referenciamos
    new_dataset.add_files(
        path=os.path.join(local_path, relative_path),
        dataset_path=relative_path,  # Manter o mesmo caminho relativo
        verbose=True
    )

# Finalizar o dataset
new_dataset.upload()
new_dataset.finalize(verbose=True, auto_upload=True)
print(f"Novo dataset criado com ID: {new_dataset.id}")
print(f"Arquivos adicionados: {selected_files}")
