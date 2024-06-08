""" Discord için bir bot yazmak istiyorsak discord kütüphanesini bilgisayarımza indirmemiz gerekiyor.
 Terminal --> Kodlarımızın çıktısını gördüğümüz yer. Terminal açmak için  ctrl + shift + "" --> terminal açıyorum.
 Python Paket Yönetim Sistemi Kullanılır. --> Python Install Package --> pip install 
 Terminalde bu pakey yönetim sistemini güncellemek. --> pip install --upgrade pip
 Bilgisayarımıza herhangi bir kütüphaneyi indirmek istiyorsak, pip install (indireceğiniz kütüphanein adı)
 discord kütüphanesi kurulacaksa --> pip install discord komutu terminale yazılmalı."""
 
# Discord botu oluşturmak istiyorsak discord kütüphanesini içeri aktaralım.
import discord
#discord modülü bir eklenti ile gelir. ve  siz eğer bot komutlarını kullancaksınız o zbu şekilde tanıtmalısınız.
from discord.ext import commands
import os, random

 
# Botun ayrıcalıklarını depolayacak bir değişken oluşturmamız gerekir.
# intents = ayrıcalık
intents = discord.Intents.default()
# Mesajları okuma ayrıcalığını vermemiz gerekir.
intents.message_content = True
# bot olarak(CBot) değişkeni ile bot oluşturalım.
# prefix --> botun mesajı algılayabilmesi için anahtar sembol
bot = commands.Bot(command_prefix='!', intents=intents)
 
# def --> definiton (tanımlama)
# on_ready() fonksiyonu bizim discord'a giriş yaptığımız anda botun hazır olduğunu belirten bir mesajı yayınlamak için kullanılan fonksiyondur.
# dekaratör: bazı fonksiyonların belirli eylemler gerçekeştikten sonra çalışmasını sağlar.
# Bir dekaratör oluşturmak istiyorsak @ işaretiyle başlarız.
# @client.event dekaratörü on_ready() fonksiyonun bot tarafından işleneceğni ve bu şekilde çalıştırılacağını belirtir.
# fonksiyonların senkronize bir şekilde çalışmasını sağlamak için async anahtar kelimesi kullanılır. 
 
@bot.event
async def on_ready():
    print(f'{bot.user} olarak discorda uçtuk!')
     
@bot.command()
async def merhaba(ctx):
    await ctx.send('MerHaba!')


@bot.command()
async def çevrekirlilinedir(ctx):
    await ctx.send('Çevrenin canlı ve cansız öğelerini olumsuz yönde etkileyen, üzerinde yapısal zararlar meydana getiren ve niteliklerini bozan yabancı maddelerin hava, su ve toprağa yoğun bir şekilde karışması olayına “çevre kirliliği” adı verilmektedir.')

@bot.command()
async def türler(ctx):
    await ctx.send('Çevre kirliliği çeşitleri genel olarak; hava kirliliği, su kirliliği, toprak kirliliği, gürültü kirliliği ve görüntü kirliliği olarak sınıflandırılır.!')

@bot.command()
async def önlemek(ctx):
    await ctx.send('Çevre konusunda bilgi edinin enerji tasarufu yapın!')

@bot.command()
async def havakirliginiönlemek(ctx):
    await ctx.send('Enerji tüketimini azaltın. ...Yenilenebilir enerji kaynaklarını kullanın.Araç emisyonlarını azaltın. !')


@bot.command()
async def sukirliliginiönlem(ctx):
    await ctx.send('denizlere çöp atmayanız. !')


@bot.command()
async def önerinnedir(ctx):
    await ctx.send("çevre kirliğini önnemek için Çevre konusunda bilgi edinin Kirliliğe engel olun Atıklarınızı ayrıştırın, geri dönüşüme katkı sağlayın. !")


@bot.command()
async def örnekresim(ctx):
    img_list = os.listdir("images")
    img_name = random.choice(img_list)
    
    with open(f'images/{img_name}', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)



     
# Botu çalıştırmak --> .run() fonksiyonu botu çalştırmamızı sağlar.
# API --> Token
# Yazarken bunun veri türünü string olarak kullanmanız gerekir.
bot.run('TOKEN')
