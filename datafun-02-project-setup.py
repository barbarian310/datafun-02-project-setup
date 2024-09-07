'''
This module allows for the creation of chronological folders for 
data analytics
'''

from pathlib import Path

created_folders = []

def create_quarterly_data_directories(directory_name:str) -> None:
    base_path = Path(directory_name)
    base_path.mkdir(parents=True, exist_ok=True)  # Create the base directory if it doesn't exist

    for i in range(1, 5):
        quarter_dir = base_path / f'Q{i}'
        quarter_dir.mkdir(exist_ok=True)  # Create quarterly folder (e.g., Q1, Q2, etc.)
        print(f"Created directory: {quarter_dir}")
        created_folders.append(quarter_dir)

    # Provide a summary of the created folders
    print("Summary of created folders:")
    for folder in created_folders:
        print(f"Folder '{folder.name}' created at: {folder.resolve()}")




if __name__ == '__main__':
    create_quarterly_data_directories('Data')