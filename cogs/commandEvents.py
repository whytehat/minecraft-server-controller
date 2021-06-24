from discord.ext import commands
import discord, screens, time


class CommandHandler(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.LogChannel = "replace with logchannel id as just numbers not as a string"
        self.control = screens.controller('place screen id in here')
        
    @commands.command()
    @commands.has_role("smp_controller")
    async def whitelist(self,ctx,username):
        self.Player_name = username
        self.log_channel = self.client.get_channel(self.LogChannel)
        self.nerds = self.control.whitelist_Add(player_name=self.Player_name)
        embed = discord.Embed(
                title = "Whitelist",
                description = "these are logs are to be saved",
                color = 0xe74c3c        
            )
        embed.add_field(name=f"Player Whitelisted:",value=f"{self.Player_name}",inline=True)
        if self.nerds == True:
            await ctx.send("the user has been added to the whitelist")
            await self.log_channel.send(embed=embed)
        else:
            await ctx.send("sorry that user doesn't exist")

    @commands.command()
    @commands.has_role("smp_controller")
    async def whitelistRemove(self,ctx,username): 
        self.Player_name = username
        self.log_channel = self.client.get_channel(self.LogChannel)
        self.nerds = self.control.whitelist_remove(player_name=self.Player_name)
        embed = discord.Embed(
                title = "Whitelist log",
                description = "these are logs are to be saved",
                color = 0xe74c3c        
            )
        embed.add_field(name=f"Player Removed from Whitelisted:",value=f"{self.Player_name}",inline=True)
        if self.nerds == True:
            await ctx.send("the user has been removed whitelist")
            await self.log_channel.send(embed=embed)
        else:
            await ctx.send("sorry that user doesn't exist")

    @commands.command()
    @commands.has_role("smp_controller")
    async def Command(self,ctx,command):
        self.Command = command
        self.StartTime = time.time()
        self.sending_command = self.control.commands(command=self.Command)
        self.log_channel = self.client.get_channel(self.LogChannel)
        embed = discord.Embed(
                title = "Server log",
                description = "these are logs are to be saved",
                color = 0xe74c3c        
            )
        embed.add_field(name=f"command sent to server:",value=f" {self.Command} was sent at:{self.startTime}",inline=False)  
        if self.sending_command == True:
            await ctx.send("sending the command to the server please standby")
            await self.log_channel.send(embed=embed) 
        else:
            await ctx.send("Error contact admistrator")

    @commands.command()
    @commands.has_role("smp_controller")
    async def start(self,ctx):       
        self.start = self.control.Start()
        self.startTime = time.time()
        self.log_channel = self.client.get_channel(self.LogChannel)
        embed = discord.Embed(
                title = "Server log",
                description = "these are logs are to be saved",
                color = 0xe74c3c        
        )
        embed.add_field(name=f"the server was started at:",value=f"{self.startTime}",inline=True) 
        if self.start == True:
            await ctx.send("i am starting up the server please wait")
            await self.log_channel.send(embed=embed)
        else:
            await ctx.send("Error contact admistrator")

    @commands.command()
    @commands.has_role("smp_controller")
    async def stop(self,ctx):   
        self.Stop = self.control.Stop()
        self.startTime = time.time()
        self.log_channel = self.client.get_channel(self.LogChannel)
        embed = discord.Embed(
                title = "Server log",
                description = "these are logs are to be saved",
                color = 0xe74c3c        
            )
        embed.add_field(name=f"the server was stopped at:",value=f"{self.startTime}",inline=True) 
        if self.Stop == True:
            await ctx.send("the server was stopped")
            await self.log_channel.send(embed=embed)
        else:
            await ctx.send("Error contact admistrator")

    @commands.command()
    @commands.has_role("admin")
    async def ban(self, ctx, member :discord.Member, *, reason=None):
        self.channel = discord.utils.get(self.client.get_all_channels(), name='ban-kick-logs')
        await member.ban(reason=reason)
        await ctx.send(f"the ban hammer has stuck {member.mention}")
        await self.channel.send(f"{member.mention} was banned for {reason}")

    @commands.command()
    @commands.has_role("admin")  
    async def nuke(self,ctx):
        self.nukelimt = 999999999999999
        await ctx.channel.purge(limit=self.nukelimt)
        await ctx.send(f"this channel has been nuked by your friends in the USA!!!")

    @commands.command()
    @commands.has_role("admin")  
    async def clear(self,ctx,amount):
        self.clearAmount = int(amount)
        await ctx.channel.purge(limit=self.clearAmount)
        await ctx.send(f"this channel has been nuked by your friends in the USA!!!")

    @commands.command()
    @commands.has_role("admin")
    async def unban(self, ctx, *, member):
        self.banneduser = await ctx.guild.bans()
        self.member_name, member_discriminator = member.split('#')

        for ban_entry in self.banneduser:
            user = ban_entry.user
            
            if (user.name, user.discriminator) == (self.member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send('user has been unbanned')

def setup(client):
    client.add_cog(CommandHandler(client))
