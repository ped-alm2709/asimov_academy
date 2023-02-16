import hikari
import lightbulb


bot = lightbulb.BotApp(
    token=open('token.txt', 'r').read(), 
    default_enabled_guilds=(int(open('ds_channel_id.txt', 'r').read())))

@bot.listen(hikari.StartedEvent)
async def on_started(event):
    print('Asimotron ta online!')

#Mensagem de saudação
@bot.command
@lightbulb.command('msg_asmv', 'Saudação Asimov Academy')
@lightbulb.implements(lightbulb.SlashCommand)
async def hello(ctx):
    await ctx.respond('*Olá, comunidade Asimov Academy!*')

#Calculadora
@bot.command
@lightbulb.command('calculadora', 'Calculadora')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def my_calculator(ctx):
    pass

@my_calculator.child
@lightbulb.option('n2', 'Segundo número', type=float)
@lightbulb.option('n1', 'Primeiro número', type=float)
@lightbulb.command('soma', 'Operação de Adição')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def soma(ctx):
    r = ctx.options.n1 + ctx.options.n2
    await ctx.respond(f"*O resultado é  **{r}***")

@my_calculator.child
@lightbulb.option('n2', 'Segundo número', type=float)
@lightbulb.option('n1', 'Primeiro número', type=float)
@lightbulb.command('subtracao', 'Operação de Subtração')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def subtracao(ctx):
    r = ctx.options.n1 - ctx.options.n2
    await ctx.respond(f"*O resultado é  **{r}***")

@my_calculator.child
@lightbulb.option('n2', 'Segundo número', type=float)
@lightbulb.option('n1', 'Primeiro número', type=float)
@lightbulb.command('multiplicacao', 'Operação de Multiplicação')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def multiplicacao(ctx):
    r = ctx.options.n1 * ctx.options.n2
    await ctx.respond(f"*O resultado é  **{round(r, 1)}***")

@my_calculator.child
@lightbulb.option('n2', 'Segundo número', type=float)
@lightbulb.option('n1', 'Primeiro número', type=float)
@lightbulb.command('divisao', 'Operação de Divisão')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def divisao(ctx):
    r = ctx.options.n1 / ctx.options.n2
    await ctx.respond(f"*O resultado é  **{round(r, 1)}***")
