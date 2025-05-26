# -*-coding:Latin-1 -*
import pygeoip
gi = pygeoip.GeoIP('/opt/GeoIP/GeoLiteCity.dat')
IP = raw_input('Entrez l"addresse IP :')
def Localisation(IP):
recuperer = gi.record_by_name(IP)
city = recuperer['city']
country = recuperer['country_name']
longitude = recuperer['longitude']
latitude = recuperer['latitude']
print ' Localisation de : ' + IP + '........ \n',"="*60
print '\nCountry : '+str(country)+'\n','City : '+str(city)
print 'Latitude: '+str(latitude)+'\n','Longitude: '+ str(longitude)

LocalisationIP
