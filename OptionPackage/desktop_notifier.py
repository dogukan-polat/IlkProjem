from plyer import notification

def notify():
    notification.notify(title= "Mail services", message="You've got a mail",
                        timeout=2)