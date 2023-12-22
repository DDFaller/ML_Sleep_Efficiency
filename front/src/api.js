
var removeOptions = (selectElement) => {
  var i, L = selectElement.options.length - 1;
  for(i = L; i >= 0; i--) {
     selectElement.remove(i);
  }
};
/*
  --------------------------------------------------------------------------------------
  Função para obter a lista de agendamentos existente do servidor via requisição GET
  --------------------------------------------------------------------------------------
*/
var getList =  async function() {
  let url = 'http://127.0.0.1:5000/sleep';
  element = document.getElementById("myTable")
  if (element !== null){
    clearTable();
  }
  request = fetch(url, {
    method: 'get',
  })
    .then((response) => response.json())
    .then((data) => {
      data.agendamentos.forEach(item => insertList(
        item.Doutor, item.Dia, item.Horario,item.Consultorio_id,
        item.Consultorio,item.Status,item.CPF, item.Conttato, item.Paciente,item.Plano))

    })
    .catch((error) => {
      console.error('Error:', error);
    });
  return request.response;
};


/*
  --------------------------------------------------------------------------------------
  Função para colocar um item na lista do servidor via requisição POST
  --------------------------------------------------------------------------------------
   postItem(inputDoctor,inputPatient,inputHealthcare,inputClinic,inputContact,inputSchedule)
*/
var postItem = function(inputAge,inputGender,inputSleepDuration,inputRemPercentage, inputDeepPercentage, inputLightPercentage,inputAwakenings, inputAlcohol, inputCaffeine, inputExercise, inputSmoke, inputBedhour, inputWakehour) {
  const formData = new FormData();
  formData.append('Age', inputAge);
  formData.append('Sex', inputGender);
  formData.append('Sleep_duration', inputSleepDuration);

  formData.append('REM_sleep_percentage', inputRemPercentage);
  formData.append('Deep_sleep_percentage', inputDeepPercentage);
  formData.append('Light_sleep_percentage', inputLightPercentage);

  formData.append('Awakenings',inputAwakenings);
  formData.append('Alcohol_consumption', inputAlcohol);
  formData.append('Caffeine_consumption', inputCaffeine);
  formData.append('Exercise_frequency', inputExercise)
  formData.append('Smoking', inputSmoke);
  formData.append('Bedhour', inputBedhour);
  formData.append('Wakehour', inputWakehour);
  console.log(formData)
  let url = 'http://127.0.0.1:5000/sleep';
  request = fetch(url, {
    method: 'post',
    body: formData
  })
    .then((response) => response.json())
    .then(data=>{ result = document.getElementById("result")
    result.innerText = "A qualidade do seu sono é " + data['message'] })
    .catch((error) => {
      console.error('Error:', error);
      console.error(formData)
    });
  return request.response;
};

