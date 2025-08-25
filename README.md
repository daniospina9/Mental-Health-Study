# 🧠 Mental Health Study
A data analysis and visualization project focused on the impact of different therapies on the mental health of 500 synthetic patients.
The tool enables filtering by gender, diagnosis, and therapy type, generating insightful visualizations to better understand treatment outcomes.

This project demonstrates skills in data processing, Python scripting, and data visualization for healthcare research.

## Features
- 📊 Data filtering by gender, diagnosis, and therapy.

- 🥧 Pie chart visualization of therapy effectiveness.

- ⚡ Interactive workflow to explore synthetic patient data.

- 📂 Clear project structure for reproducibility.

## 📦 Installation & Setup
Clone the repository and set up the environment:
```sh
# Clone the repository
git clone https://github.com/daniospina9/Mental-Health-Study.git
cd Mental-Health-Study/app

# Create and activate a virtual environment
python3 -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

# Install dependencies
pip3 install -r requirements.txt

# (Linux only) Install imview to visualize generated charts
sudo apt install imview
```

## ▶️ Usage
Run the program:
```sh
python3 main.py
```
After completing the prompts, a pie chart will be generated in the imgs/ folder.
To open the chart:
```sh
cd imgs
imview pie.png
```

## 🛠️ How It Works
1. Reads data from a CSV file.

2. Requests user input (gender, diagnosis, therapy).

3. Filters the dataset accordingly.

4. Generates a pie chart summarizing the results.

The entry point is handled in if __name__ == "__main__":, ensuring a clean and modular script design.

## 📊 Dataset
- Represents 500 synthetic patients with diverse mental health conditions.
- Includes:
  - Demographics
  - Diagnoses
  - Therapy types
  - Treatment outcomes
⚠️ This dataset is synthetic and created for research purposes only.
Source: [Mental Health Diagnosis & Treatment – Kaggle.](https://www.kaggle.com/datasets/uom190346a/mental-health-diagnosis-and-treatment-monitoring/data "mental-health-diagnosis-tretament")

## 🖥️ Technologies Used
- Python 3 → Core programming language
- Pandas → Data manipulation and filtering
- Matplotlib → Data visualization (pie charts)
- Virtualenv → Environment management
- CSV → Data source format
- imview (Linux) → Image viewer for generated graphs

## 🎯 Project Value
This project highlights:
- ✅ Data preprocessing and filtering with Python.
- ✅ Visualization with Matplotlib.
- ✅ Application of data analysis in healthcare research contexts.
- ✅ Reproducible workflow for future extensions (e.g., more visualizations or predictive models).

# Instructions
To run the program you need follow the next instructions in the terminal:
```sh
git clone
cd app
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
sudo apt install imview
python3 main.py
```
After you complete all parameters of the program, you need follow the nex intruction to see the graph
```sh
cd imgs
imview pie.png
```

## Mental Health Study
With this project you can graph the effectiveness of different therapies in the mental health of 500 people that have suffered different disorders. To get it, you need filter the gender, the diagnosis, and finally the therapy type. However, you can analize all data in every category.

## Code description
The code defines a function called **`run`**. Inside the **`run`** function, it reads data from a CSV file using the **`read_csv`** module and then prompts the user to enter a gender, diagnosis, and therapy. It filters the data based on the user's input and then generates a pie chart using the **`charts`** module.

The **`if __name__ == '__main__':`** block ensures that the run function is executed only when the file is run as a script.

## Source
The data using for this project includes the analisys of 500 people representing real-world mental health diagnoses, treatment plans, and outcomes. It includes patient demographics, symptom severity, medication, therapy types, and progress tracking, but in this project only it is analiced the first datas. However, this dataset is synthetic and created for research and analysis purposes. Then, this project representing only a model. The source was download from [mental-health-diagnosis-tretament](https://www.kaggle.com/datasets/uom190346a/mental-health-diagnosis-and-treatment-monitoring/data "mental-health-diagnosis-tretament")
