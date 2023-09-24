from lambdas.HelperFunctions.eventHandler import eventHandler

def lambda_handler(event, context):
    try:
        print("Came here inside lambda")
        print("Event is: " , event)
        print("This is to show that merge id happening and deployment is also happening")
        response = eventHandler(event)
        print("response is :", response)
        return response
    except Exception as e:
        print('Error Occurred in lambda Handler: ', str(e))