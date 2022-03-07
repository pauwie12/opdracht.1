

from asyncio import new_event_loop


gegevens = '.'

hostname = input ("geef uw naam ") 
while True:
    ip = input("Geef een ip address: ")
    ip_address_check = ip.split('.')

    if (len(ip_address_check) == 4) and (1 <= int(ip_address_check[0]) <= 223) and (int(ip_address_check[0]) != 127) and (int(ip_address_check[0]) != 169 or int(ip_address_check[1]) != 254) and (0 <= int(ip_address_check[1]) <= 255 and 0 <= int(ip_address_check[2]) <= 255 and 0 <= int(ip_address_check[3]) <= 255):
        break

    else:
     print (ip)
     print ("geen geldig ip address")
    
OS  = input ("kies uw operating system: Windows, linux, macOS ")
while OS not in {"Linux", "Windows", "macOS" }: #kijkt of een operating system geldig is
 print ("dit is geen geldig operating system ") 
 OS =input ("kies een bestaand operating system ")
print ("uw naam is " + hostname)

print ("uw ip address is  " + ip)

print ("uw operating system is "+ OS )

systeem = (hostname,ip,OS )
print (systeem)

savesystem = input ("wilt u deze gegevens opslaan ja/nee ")
while savesystem not in {"ja","nee"}:
    print ("antwoord ja of nee ")
    savesystem = input ("will u opslaan")
if savesystem  in ("ja") :
  (gegevens,systeem)
if savesystem in ("nee") :
    print ("niet opgeslagen")



 
    
 
 
