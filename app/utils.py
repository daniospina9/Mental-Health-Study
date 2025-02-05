def gender_definition(gender, data):
  mental_list = []
  if gender == 'Male':
    mental_list = list(filter(lambda item: item['Gender'] == 'Male', data))
  elif gender == 'Female':
    mental_list = list(filter(lambda item: item['Gender'] == 'Female', data))
  elif gender == 'All':
    mental_list = data
  else:
    print('Invalid gender')
  return mental_list
  
def get_diagnosis(diagnosis_list):
  diagnosis_list = list(map(lambda item: item['Diagnosis'], diagnosis_list))
  return diagnosis_list

def get_therapy(therapy_list):
  therapy_list = list(map(lambda item: item['Therapy Type'], therapy_list))
  return therapy_list

def diagnosis_data(diagnosis_name, new_list):
  if diagnosis_name == 'All':
    return new_list
  else:
    diagnosis_data = list(filter(lambda item: item['Diagnosis'] == diagnosis_name, new_list))
    return diagnosis_data

def therapy_data(therapy_name, filter_list):
  if therapy_name == 'All':
    return filter_list
  else:
    therapy_data = list(filter(lambda item: item['Therapy Type'] == therapy_name, filter_list))
    return therapy_data

def getting_graph_values(final_list):

  Outcome_list = list(map(lambda item: item['Outcome'], final_list))

  def counter_values(Outcome_list, item):
    counter = 0
    for i in Outcome_list:
      if i == item:
        counter+=1
    return counter

  Improved_numbers = counter_values(Outcome_list, 'Improved')
  Nochange_numbers = counter_values(Outcome_list, 'No Change')
  Deteriorated_numbers = counter_values(Outcome_list, 'Deteriorated')
     
  labels = ['Improved', 'No change', 'Deteriorated']
  values = [Improved_numbers, Nochange_numbers, Deteriorated_numbers]
     
  return labels, values
