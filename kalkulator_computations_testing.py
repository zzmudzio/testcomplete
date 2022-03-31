"""
this testcomplete script works on windows calculator, 
it takes 2 numbers from values_to_compute dict, then performs 
some random computations (such as multiplication, division etc.)
the result of computation shown on calc board is then compared with 
result calculated by the script(aqObject.CheckProperty..)
"""
import random 

def start_app():
  return TestedApps.WindowsCalculator.Run()

def make_computations():
  values_to_compute = {3: "Trzy", 4: "Cztery"}
  dict_keys = [x for x in values_to_compute.keys()]
  operations_dict = {"Podziel_przez": dict_keys[0]/dict_keys[1], 
                "Pomnóż_przez": dict_keys[0]*dict_keys[1], 
                "Minus": dict_keys[0]-dict_keys[1],
                "Plus": dict_keys[0]+dict_keys[1]
                }
  app_handler = start_app()
  for y in range(1, 6):
    app_handler.UIAObject("Kalkulator").UIAObject("LandmarkTarget")\
    .UIAObject("Klawiatura_numeryczna").UIAObject(values_to_compute[3]).Click()
    random_operation = random.choice([y for y in operations_dict.keys()])
    app_handler.UIAObject("Kalkulator").UIAObject("LandmarkTarget")\
    .UIAObject("Operatory_standardowe").UIAObject(random_operation).Click()
    app_handler.UIAObject("Kalkulator").UIAObject("LandmarkTarget")\
    .UIAObject("Klawiatura_numeryczna").UIAObject(values_to_compute[4]).Click()
    app_handler.UIAObject("Kalkulator").UIAObject("LandmarkTarget")\
        .UIAObject("Operatory_standardowe").UIAObject("Równa_się").Click()
    aqObject.CheckProperty(app_handler.UIAObject("Kalkulator").UIAObject("LandmarkTarget")\
    .UIAObject("Wyświetlana_wartość_to_0").UIAObject("TextContainer").UIAObject("NormalOutput"),"Text",cmpEqual, 
    operations_dict[random_operation])
    aqUtils.Delay(3000)
    