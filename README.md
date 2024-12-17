# Mental Health Study
With this proyect you can graph the effectiveness of different therapies in the mental health of 500 people that have suffered different disorders. To get it, you need filter the gender, the diagnosis, and finally the therapy type. However, you can analize all data in every category.

## Code description
The code defines a function called **`run`**. Inside the **`run`** function, it reads data from a CSV file using the **`read_csv`** module and then prompts the user to enter a gender, diagnosis, and therapy. It filters the data based on the user's input and then generates a pie chart using the **`charts`** module.

The **`if __name__ == '__main__':`** block ensures that the run function is executed only when the file is run as a script.

## Source
The data using for this proyect includes the analisys of 500 people representing real-world mental health diagnoses, treatment plans, and outcomes. It includes patient demographics, symptom severity, medication, therapy types, and progress tracking, but in this proyect only it is analiced the first datas. However, this dataset is synthetic and created for research and analysis purposes. Then, this proyect representing only a model. The source was download from [mental-health-diagnosis-tretament](https://www.kaggle.com/datasets/uom190346a/mental-health-diagnosis-and-treatment-monitoring/data "mental-health-diagnosis-tretament")