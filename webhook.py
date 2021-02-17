from discord_webhook import DiscordWebhook, DiscordEmbed

webhook = DiscordWebhook(url='webhook-url-here', username="test")

embed = DiscordEmbed(title="Welcome to a test webhook sender!", description='I hope you enjoy', color=242424)
embed.set_author(name='Ntdi', url='https://github.com/professional-tdi?tab=repositories', icon_url='https://avatars.githubusercontent.com/u/79174456?s=400&u=ebbf784303d23f57c1f5cb553e92ee278477c3c3&v=4')
embed.set_footer(text='by ntdi')
embed.set_timestamp()
embed.add_embed_field(name='Woah a new field', value='Woah a subfield')
embed.add_embed_field(name='ANOTHER ONE??', value='THIS IS CRAYCRAY')


webhook.add_embed(embed)

response = webhook.execute()