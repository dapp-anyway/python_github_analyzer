from metrics import analyze_repository, concat_project_stats_to_results
from config import TEMP_DIR_PATH, RESULTS_DIR, SOURCE_METER_PATH, STATS_DIR, REPO_LINKS
from stats import add_stats_values_in_csv
from correlation import create_correlation_files
from utils import remove_empty_lines, create_folder
from git import Repo
import shutil
import stat
from os import path
import subprocess
import os


# Clone single repository and get metrics using SourceMeter
def clone_single_repository_and_get_metrics(url):
    remove_repository()
    project_name = parse_project_name(url)
    print(f"Start cloning: {project_name}")
    Repo.clone_from(url, TEMP_DIR_PATH, single_branch=True)
    print(f"Finish cloning: {project_name}")
    add_init_files(TEMP_DIR_PATH)

    try:
        subprocess.call(f"{SOURCE_METER_PATH} -projectBaseDir:{TEMP_DIR_PATH} -projectName:{project_name} -resultsDir:{RESULTS_DIR}\{project_name} -pythonVersion:3 -pythonBinary:C:\\Users\\dappa\\AppData\\Local\\Programs\\Python\\Python38\\python.exe", timeout=1500)
        remove_repository()
        return "Success"
    except subprocess.TimeoutExpired:
        remove_repository()
        return "Error"

    


# Add init files in every directory
def add_init_files(directory_path):
    for root, dirs, files in os.walk(directory_path):
        if "__init__.py" not in files:
            init_file_path = os.path.join(root, "__init__.py")
            with open(init_file_path, "w"):
                pass


# Remove local repository
def remove_repository(repository_path=TEMP_DIR_PATH):
    for root, dirs, files in os.walk(repository_path):
        for directory in dirs:
            os.chmod(path.join(root, directory), stat.S_IRWXU)
        for file in files:
            os.chmod(path.join(root, file), stat.S_IRWXU)
    try:
        shutil.rmtree(repository_path)
    except:
        print(f"Nothing to remove")

# Parse project name
def parse_project_name(url):
    if url[-1] == '/':
        url = url[0:-1]
    parts = url.split('/')[-2:]
    return "__".join(parts)

# Clone repositories and get metrics using SourceMeter
def clone_repositories_and_get_metrics():
    remove_repository()
    for url in REPO_LINKS:
        project_name = parse_project_name(url)
        print(f"Start cloning: {project_name}")
        Repo.clone_from(url, TEMP_DIR_PATH, single_branch=True)
        print(f"Finish cloning: {project_name}")
        add_init_files(TEMP_DIR_PATH)

        try:
            subprocess.call(f"{SOURCE_METER_PATH} -projectBaseDir:{TEMP_DIR_PATH} -projectName:{project_name} -resultsDir:{RESULTS_DIR}\{project_name} -pythonVersion:3 -pythonBinary:C:\\Users\\dappa\\AppData\\Local\\Programs\\Python\\Python38\\python.exe", timeout=1500)
        except subprocess.TimeoutExpired:
            print(f"TimeoutExpired: {project_name}")
        finally:
            remove_repository()

# Analyze all repositories
def analyze_all_repositories():
    create_folder(STATS_DIR)
    for project in next(os.walk(RESULTS_DIR))[1]:
        print(f"Analyzing repository: {project}")
        analyze_repository(f"{RESULTS_DIR}/{project}", project)
        concat_project_stats_to_results(f"{STATS_DIR}/{project}")


if __name__ == '__main__':
    # print("Clone repositories and get metrics")
    # clone_repositories_and_get_metrics()
    # print("Analyze all repositories")
    # analyze_all_repositories()
    # print("Add stats values in csv")
    # add_stats_values_in_csv()
    print("Create correlation files")
    create_correlation_files()
    remove_empty_lines()