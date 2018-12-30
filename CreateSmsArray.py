def create_sms_array(phone_number):
    with open('textlists/SMS_Gateways.txt') as f:
        array=f.readlines()
    array=[x.strip() for x in array]
    sms_list = []
    for x in range(len(array)):
        sms_list.append(phone_number+'@'+array[x])
    return sms_list

print(create_sms_array('7247093936'))
