import requests
import sys
import getopt

#Enviamos a slack el mesaje y esperamos un ok
def send_slack_message(message):
    payload = '{"text": %s}' % message
    response = requests.post('Aqui url del bot',data=payload)

    print(response.text)

# Comprobamos el mensaje
def main(argv):
    message = ''

    try:
        otps, args = getopt.getopt(argv,"hm:",["message="])

    except getopt.GetoptError as e:
        print(e)
        sys.exit(1)

    if len(otps) == 0:
        message = "Buenos días a todos"

        for otp, arg in otps:
            if otp == '-h':
                print("main.py -h")
                sys.exit(0)
            elif otp in ("-m","--message"):
                message = arg

        send_slack_message(message)


if __name__ == " main ":
    main(sys.argv[1:])
