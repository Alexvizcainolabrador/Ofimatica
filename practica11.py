# Paso 1) Obtener la URL del webhook del canal de Discord:
# https://discord.com/api/webhooks/781926076112830534/DaLMt5qzYNHtXBr6D8SXtoNbUUBvbkpW0nJxXRJnBP-SPjLqUL4tnnRI-6KUTl7-bFQ7

# Paso 2) Instalar la libreria de discord-webhook
# pip3 install discord-webhook

from discord_webhook import DiscordWebhook, DiscordEmbed

url_webhook = "https://discord.com/api/webhooks/781926076112830534/DaLMt5qzYNHtXBr6D8SXtoNbUUBvbkpW0nJxXRJnBP-SPjLqUL4tnnRI-6KUTl7-bFQ7"

def print_image():
    webhook = DiscordWebhook(url=url_webhook)
    embed = DiscordEmbed(title="Plat", description="El plat està al forn")
    

def print_discord(missatge):
    webhook = DiscordWebhook(url=url_webhook), content=missatge)
    webhook.execute()

def calcula_precio_total(menjar):

    IVA = round((float(comida) * 0.1),2)
    Propina = round((float(comida) * 0.1),2)
    Total = round((float(comida) + (float(IVA)) + (float(Propina))),2)

    print_discord("Preu del comida = " + str(float(comida)))
    print_discord("IVA = " + str(float(IVA)))
    print_discord("Propina = " + str(float(Propina)))
    print_discord("Total = " + str(float(Total)) + "€")

    return calcula_precio_total


print_discord("1.Pizza     6€")
print_discord("2.Ensalada  4€")
print_discord("3.Kebab     3€")
print_discord("4.Salmon     8€")

num_ordre = int(input("Escribe el numero del plato"))

if num_ordre == 1:
    calcula_precio_total(6)
elif num_ordre == 2:
    calcula_precio_total(4)
elif num_ordre == 3:
    calcula_precio_total(3)
elif num_ordre == 4:
    calcula_precio_total(8)
else:
    print("no tenemos ese plato.")