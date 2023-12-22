cpf = ""
password = ""

/*
  --------------------------------------------------------------------------------------
  UTILS: Função para criação dinamica de elementos no body
  --------------------------------------------------------------------------------------
  */

  const generateElement = (elementType,parent,attributesList) =>{
    var elementGenerated = document.createElement(elementType);
    parent.appendChild(elementGenerated);
    for(var key in attributesList) {
      elementGenerated.setAttribute(key,attributesList[key]);
    }
    return elementGenerated;
  }
/*
  --------------------------------------------------------------------------------------
  Função para adicionar um novo buscando o valores necessários para criação do form
  Parametrôs para um Schedule:
    - Doctor
    - Clinic
    - Clinic ID
    - CPF paciente
    - Nome paciente
    - Plano de saude
    - Contato
    - Dia da consulta
    - Horário da consulta
  --------------------------------------------------------------------------------------
*/
const newItem = () => {
  let inputAge = document.getElementById("newAge").value;
  let inputGender = getRadioBtnValue("newGender");
  let inputSleepDuration = document.getElementById("newSleepDuration").value;
  
  let inputRemPercentage = document.getElementById("newRemDuration").value;
  let inputDeepPercentage = document.getElementById("newDeepDuration").value;
  let inputLightPercentage = document.getElementById("newLightDuration").value;

  let inputAwakenings = document.getElementById("newAwakenings").value;
  let inputCaffeine = document.getElementById("newCaffeine").value;
  let inputAlcohol = document.getElementById("newAlcohol").value;
  let inputExercise = document.getElementById("newExercise").value;

  let inputBedtime = document.getElementById("newBedtime").value;
  let inputWaketime = document.getElementById("newWaketime").value;

  let inputSmoke = getRadioBtnValue("newSmoker");
  
  console.log([inputAge,inputGender,inputSleepDuration,inputAwakenings,inputCaffeine,inputAlcohol,inputExercise,inputSmoke])
  res = postItem(inputAge,inputGender,inputSleepDuration, inputRemPercentage, inputDeepPercentage, inputLightPercentage,inputAwakenings,inputAlcohol,inputCaffeine,inputExercise,inputSmoke,inputBedtime,inputWaketime)

}
/*
  --------------------------------------------------------------------------------------
  Função auxiliar para limpar items do formulário de agendamento
  --------------------------------------------------------------------------------------
*/

const limpaAgendamento = () => {
  document.getElementById("newCPF").value = "";
  document.getElementById("newPatient").value = "";
  document.getElementById("newHealthcare").value = "";
  document.getElementById("newContact").value = "";
  document.getElementById("newScheduleDate").value = "";
  document.getElementById("newScheduleTime").value = "";
}


const getRadioBtnValue = (name) => {
  var radios = document.getElementsByName(name);

  for (var i = 0, length = radios.length; i < length; i++) {
    if (radios[i].checked) {
      // do whatever you want with the checked radio
      return radios[i].value;

      // only one radio can be logically checked, don't check the rest
      break;
    }
  }
  return ""
}