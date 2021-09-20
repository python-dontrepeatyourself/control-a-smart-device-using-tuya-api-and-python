from tuya_iot import TuyaOpenAPI	

# Cloud project authorization info	
ACCESS_ID ='your-access-id'	
ACCESS_KEY ='your-access-key'	
	
# Select an endpoint base on your project availability zone	
# For more info: https://developer.tuya.com/en/docs/iot/api-request?id=Ka4a8uuo1j4t4	
ENDPOINT = "https://openapi.tuyaeu.com"	
	
# Project configuration	
USERNAME = 'your-username' # email address or phone number	
PASSWORD = 'your-password'	
	
DEVICE_ID = 'vdevo163137171462882'	

# Initialization of tuya openapi	
openapi = TuyaOpenAPI(ENDPOINT, ACCESS_ID, ACCESS_KEY)	
openapi.login(USERNAME, PASSWORD)	
    
#### Control the Device with Python ####

# commands = {'commands': [{'code':'switch_1','value': True}]}	
# request = openapi.post(f'/v1.0/iot-03/devices/{DEVICE_ID}/commands', commands)	
# print(request)


#### Turn the Device on/off Depending on the Temperature ####

location = openapi.get('/v1.0/iot-03/locations/ip?ip=your-ip-address')
print(location)
location = location['result']
latitude, longitude = location['latitude'], location['longitude']

weather_url = f'/v2.0/iot-03/weather/current?lat={latitude}&lon={longitude}'
weather = openapi.get(weather_url)
print(weather)
temperature = weather['result']['current_weather']['temp']
print(temperature)

if float(temperature) >= 30:
    commands = {'commands': [{'code':'switch_1','value': True}]}	
    request = openapi.post(f'/v1.0/iot-03/devices/{DEVICE_ID}/commands', commands)
    print(request)
