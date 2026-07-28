# Tennis Data Extraction, Cleaning, and Analysis


## Overview

This project focuses on extracting, cleaning, processing, and analyzing large-scale tennis match data using Python and Jupyter Notebook.

The raw dataset consisted of more than 200,000 parquet files distributed across multiple folders. The project involved building a complete workflow for reading parquet files, organizing the extracted data into structured DataFrames, cleaning inconsistent and missing values, and preparing the data for analysis.

After preprocessing and cleaning the data, the project answered 17 analytical questions related to tennis players, match statistics, rankings, tournament performance, and gameplay trends.

The workflow included:

- Extracting data from parquet files
- Organizing and exploring tables
- Cleaning and preprocessing datasets
- Joining DataFrames when needed
- Performing analytical queries using Python
- Generating insights from tennis match data

## Project Objectives

The main objective of this project was to gain hands-on experience working with large-scale raw datasets and applying data analysis techniques to answer real analytical questions.

During the project, the team worked with a massive collection of raw `.parquet` files containing tennis match data. One of the primary learning goals was understanding how to efficiently extract, read, organize, and process parquet datasets using Python.

The project also focused on:

- Learning how to work with raw and unstructured data
- Managing and processing large volumes of files efficiently
- Cleaning missing and inconsistent data
- Structuring datasets into usable DataFrames
- Combining multiple tables for analysis
- Performing analytical queries to answer 17 business-style questions
- Improving practical data analysis and problem-solving skills

Since the project was completed as part of a Data Science Bootcamp, special attention was given to both correctness and efficient handling of large datasets.

## Dataset Description

The dataset used in this project contained large-scale raw tennis data stored in `.parquet` format.

Due to size constraints, the dataset is hosted externally. Download it here: [Link](https://s5.uupload.ir/files/daneshkaracademy/Data%20analysis/%D9%81%D8%A7%DB%8C%D9%84%20%D9%87%D8%A7%DB%8C%20%D8%AF%D9%88%D8%B1%D9%87/Tennis%20Project.rar)

### Data Source Structure

The project data was organized as follows:

Tennis Project  
└── Tennis Schema  
  └── tennis_data.zip  

After extracting `tennis_data.zip`, the dataset contained around **60 compressed `.zip` files**. These files were extracted using a Python-based extraction script.

After the extraction process, the following folders were created:

- raw_match_parquet
- raw_odds_parquet
- raw_votes_parquet
- raw_statistics_parquet
- raw_point_by_point_parquet
- raw_tennis_power_parquet

Each folder contained a large number of `.parquet` files representing different types of tennis match data.

### Dataset Content

The dataset includes information related to:

- tennis matches
- match statistics
- betting odds
- player votes
- point-by-point match data
- tennis performance metrics

### Dataset Size

The total dataset size was approximately **2 GB**, containing hundreds of thousands of parquet files distributed across multiple folders.

## Data Extraction and Processing

Due to the nested structure of the dataset, a custom extraction process was implemented to handle multiple layers of compressed files.

The main dataset file (`tennis_data.zip`) contained approximately 60 additional `.zip` files. A Python script was written to automatically iterate through these compressed files and extract their contents into a target directory.

Python's `zipfile` module was used to programmatically extract the inner zip files. The script opened the main archive, detected all nested `.zip` files, and extracted them to the desired output folder.

After extraction, the dataset folders contained large numbers of `.parquet` files. These files were then loaded into pandas DataFrames using `pandas.read_parquet()`.

To efficiently locate and iterate through the parquet files, the following libraries were used:

- `os` for directory and path management  
- `glob` for locating parquet files across folders  
- `pandas` and `numpy` for data handling and analysis  

This workflow allowed the team to systematically read, organize, and prepare large volumes of parquet data for further cleaning and analysis.

## Data Cleaning

After extracting and loading the parquet files into pandas DataFrames, several preprocessing and cleaning steps were applied to prepare the data for analysis.

A helper function called `load.to_clean()` was used during the preprocessing stage to inspect DataFrames and prepare them before saving the cleaned datasets. This step helped review the data and ensure it was ready for further analysis.

Basic data cleaning operations included:

- Handling missing values using methods such as `notna()`
- Removing duplicate records using `drop_duplicates()`
- Inspecting DataFrames before saving cleaned versions
- Exporting cleaned tables into new `.parquet` files for easier reuse

For example, cleaned tables were saved after inspection using commands similar to:

`load.to_clean(home_team_df, 10)`

first input: table to clean

second input: minimum not-null columns

`home_team_df.to_parquet(clean + 'home_team.parquet')`

In some situations, specific columns were prioritized depending on their relevance to the analysis, especially when building structured tables related to players or match entities.

Additionally, many transformations were performed dynamically while answering the analytical questions. Depending on the question, different tables were filtered, merged, or combined inside the notebook cells. Some questions required data from a single table, while others required merging multiple datasets before performing calculations.

## Project Structure

The project is organized into the following files and folders:
```text
Tennis Project/
├── Tennis project.pdf
├── Tennis Schema.pdf
├── Presentation.pdf
├── Requirements.txt
├── Notebooks/
│   ├── 1_extracting_all_files.ipynb
│   ├── 2_inspecting_tables.ipynb
│   ├── 3_cleaning_data.ipynb
│   └── 4_analysing_data.ipynb
├── src/
│   ├── __init__.py
│   ├── paths.py
│   ├── utils.py
│   └── load.py
└── fugures/
    ├── corr1.png
    ├── corr2.png
    ├── countries1.png
    ├── countries2.png
    ├── duration.png
    ├── gender.png
    ├── handedness.png
    ├── height.png
    ├── surfaces.png
    └── top3.png

```
## File Descriptions

### Project Files

- **Tennis project.pdf**: The project documentation containing the analytical questions.
- **Tennis Schema.pdf**: The dataset schema and structure reference.
- **Requirements.txt**: A full list of installed Python packages exported from the project environment using `pip freeze`, used to reproduce the same environment.


### Notebooks

- **1_extracting_all_files.ipynb**: Extracting nested zip files and preparing the raw data.
- **2_inspecting_tables.ipynb**: Exploring and inspecting the extracted parquet tables.
- **3_cleaning_data.ipynb**: Cleaning, preprocessing, and saving cleaned datasets.
- **4_analysing_data.ipynb**: Answering the analytical questions and performing the main analysis.

### Source Code (`src/`)

- paths.py: Path definitions used across the project.
- utils.py: Utility functions used during the workflow.
- load.py: Data loading and cleaning helper functions.

## Technologies Used

The project was developed using the following technologies and libraries:

### Programming Language

- Python 3

### Main Libraries

- `pandas` — Data manipulation and analysis
- `pyarrow` — Reading and processing parquet files
- `glob` — Searching and handling file paths
- `os` — Directory and file management
- `zipfile` — Extracting nested zip files
- `numpy` — Numerical operations and array processing

### Development Environment

- Jupyter Notebook

### Data Format

- Parquet (`.parquet`)
- ZIP archives (`.zip`)
`


## Installation

To run this project locally, follow these steps:

### 1. Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
```
Activate the environment:

**Windows**
```bash
venv\Scripts\activate
```
**Mac / Linux**
```bash
source venv/bin/activate
```
### 2. Install Required Dependencies
```bash
pip install -r Requirements.txt
```

## How to Run the Project

The project workflow is divided into four main notebooks.  
Run the notebooks in the following order.

### 1. Extract the Dataset Files

Open and run:

`Notebooks/1_extracting_all_files.ipynb`

This notebook:
- Extracts nested `.zip` files
- Traverses large directory structures
- Collects and organizes raw parquet datasets
- Prepares the files for inspection and processing

### 2. Inspect the Extracted Tables

Open and run:

`Notebooks/2_inspecting_tables.ipynb`

This notebook is used for:
- Exploring dataset tables
- Inspecting schemas and column names
- Understanding relationships between tables
- Checking data quality and structure

### 3. Clean and Prepare the Data

Open and run:

`Notebooks/3_cleaning_data.ipynb`

This notebook includes:
- Handling missing values
- Removing duplicates
- Filtering invalid records
- Applying custom cleaning functions
- Preparing cleaned datasets for analysis

### 4. Run the Analysis

Open and run:

`Notebooks/4_analysing_data.ipynb`

This notebook:
- Answers the analytical questions of the project
- Performs tennis match data analysis
- Generates insights from the cleaned datasets

### Running the Notebooks

Start Jupyter Notebook or JupyterLab:

`jupyter notebook`

or

`jupyter lab`

Then open the notebooks and run them sequentially from top to bottom.
