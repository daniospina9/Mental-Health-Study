import utils
import read_csv
import charts

def run():
  
  data = read_csv.read_csv('data.csv')

  # filter for age
  while True:
    gender = input('What is the gender you want to search? (Male/Female/All) => ')
    if gender in ['Male', 'Female', 'All']:
      gender_data = utils.gender_definition(gender, data)
      break
    else:
      print('Invalid gender. Please enter Male, Female or All.')

  # elements for diagnosis and therapy sections
  diagnosis_list = list(set(utils.get_diagnosis(data)))
  diagnosis_list.append('All')
  therapy_list = list(set(utils.get_therapy(data)))
  therapy_list.append('All')
  order_list = [element for element in range(1, (len(diagnosis_list)) + 1)]
  
  # Select the diagnosis
  diagnosis_iterabe = {order_list: diagnosis_list for (order_list, diagnosis_list) in zip(order_list, diagnosis_list)}
  print('***Different Diagnoses***')
  print(diagnosis_iterabe)
  while True:
    diagnosis = input('What is the diagnosis you want to analyze? (1/2/3/4/5) => ')
    if int(diagnosis) in order_list:
      diagnosis_name = diagnosis_iterabe[int(diagnosis)]
      diagnosis_data = utils.diagnosis_data(diagnosis_name, gender_data)
      break
    else:
      print('Invalid diagnosis. Please enter a valid number from the list.')

  # Select the therapy
  therapy_iterable = {order_list: therapy_list for (order_list, therapy_list) in zip(order_list, therapy_list)}
  print('***Different Therapies***')
  print(therapy_iterable)
  while True:
    therapy = input('What is the therapy you want to analyze? (1/2/3/4/5) => ')
    if int(therapy) in order_list:
      therapy_name = therapy_iterable[int(therapy)]
      therapy_data = utils.therapy_data(therapy_name, diagnosis_data)
      break
    else:
      print('Invalid therapy. Please enter a valid number from the list.')
 
  # graphic section
  labels = therapy_name
  labels, values = utils.getting_graph_values(therapy_data)
  charts.generate_pie_chart(labels, values)
  
if __name__ == '__main__':
  run()