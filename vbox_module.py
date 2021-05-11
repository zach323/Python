import io
import os
import json
import requests
import datetime as dt
import time
import logging
logging.basicConfig(filename='vbox_log.log', level=logging.INFO, filemode='a')
logger = logging.getLogger()
class VirtualBox:
    def __init__(self):
        self.__config = Config("C:\\_source\\virtual_powerbox\\vbox.json") 
        self.__config_data = self.__config.read_configs()
        self.__url = self.__config_data["url"]
        self.__wellId = self.__config_data["wellId"]
        self.__interval = self.__config_data["timeInterval"]
        self.__Post = PostData(self.__url, self.__wellId, self.__interval)
        
    def start(self):
        self.__Post.post_data()
        



class Config:
    def __init__(self, filePath):
        self.__filePath = filePath
    
    def read_configs(self):
        config = None
        default_configs = {'url':"https://pbportal-default.dev.avenirre.com:60010/api/well/rawdata4MT", 'wellId': '10528', 'timeInterval': 60 }
        if not os.path.exists(self.__filePath):
            with open(self.__filePath,"w") as file:
                json.dump(default_configs, file)
        else:
            with open(self.__filePath, 'r') as f:
                config = json.load(f)
        return config

class PostData:
    def __init__(self, url, wellid, interval):
        self.url = url
        self.wellId = wellid
        self.interval = interval
        self.rawdata = RawData()
       
        
    def post_data(self):
        while(True):
            try:
                data = None
                utctime = dt.datetime.utcnow().isoformat() + "Z"
                self.rawdata.data["dateTime"] = utctime
                if not os.path.exists("rawdata.json"):
                    with open("rawdata.json","w") as file:
                        json.dump(self.rawdata.data, file)
                else:
                    with open("rawdata.json", 'r') as f:
                        data = json.load(f)

                with open("rawdata.json", "w") as f:
                    json.dump(self.rawdata.data, f)
            except FileNotFoundError as fnf:
                logging.error(fnf, dt.datetime.utcnow)
            except Exception as e:
                logging.error(e)
                print(e)
                    
        
        
            headers = {'Content-Type': 'application/json'}
            try:
                r = requests.post(self.url, json=[data], headers = headers)
                print (r.status_code)
                logger.info("StatusCode: " + str(r.status_code) + " | " + str(utctime))
            except ConnectionError as ce:
                print(ce)
                logging.error(ce)
            except Exception as e:
                logging.error(e)
            else:
                time.sleep(self.interval)

class RawData:
    data = \
         {
        "wellId": 10528,
        "dateTime": "2021-01-01T12:00:00.000Z",
        "tubingPressure": 555,
        "casingPressure": 0.0,
        "linePressure": 0.0,
        "bottomHolePressure": -1.010383,
        "efmGasRate": 0,
        "prodValvePosition": 0,
        "injValvePosition": 0,
        "plungerArrived": 0,
        "oilTankGaugeHeight": 0.0,
        "waterTankGaugeHeight": 0.0,
        "soapPmpSwitch": 0,
        "soapPmpDuration": 0,
        "solarPanelVoltage": 12.517863,
        "tubingTemp": 0.0,
        "efmDateTime": "",
        "efmBatteryVoltage": None,
        "powerBoxStatus": 2,
        "reStart": 0,
        "firmwareVersion": 11,
        "transducerLinePressure": 0.0,
        "efmLinePressure": 0.0,
        "efmGasVolume": 0.0,
        "injGasTemp": 99.9,
        "injGasFlowRate": 342.33,
        "injGasDailyVol": 2000.99,
        "injGasAccumulatedVol": 12500.807,
        "injGasPressure": 120.807
        }
vbox = VirtualBox()
vbox.start()
print(vbox)
        
        