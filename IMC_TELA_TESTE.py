import customtkinter as ctk
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("green")

def validar_genero_iac():
    if genero.get() == "Selecione seu gênero":
        resultado_iac.configure(text="Por favor, preencha todos os campos!")   
    else:
        validar_campos_iac()

def validar_campos_iac():
    if not altura_caixa_iac.get() or not quadril_caixa.get():
        resultado_iac.configure(text="Por favor, preencha todos os campos!")
        if not altura_caixa_iac.get():
            altura_caixa_iac.configure(border_color="red")
        if not quadril_caixa.get():
            quadril_caixa.configure(border_color="red")
    else:
        iac_calculo()

def iac_calculo():
    altura = float(altura_caixa_iac.get())
    quadril = float(quadril_caixa.get())
    IAC = (quadril / (altura * (altura ** (1/2)))) - 18
    resultado_iac.configure(text= f"Seu IAC é {IAC:.2f}")
    if genero.get() == "Homem" and IAC < 8:
        status_iac.configure(text="Você está magro!")
    elif genero.get() == "Homem" and IAC >= 8:
        status_iac.configure(text="Você está no peso ideal!")
    elif genero.get() == "Homem" and IAC >= 21:
        status_iac.configure(text="Você está em sobrepeso!")
    elif genero.get() == "Homem" and IAC > 25:
        status_iac.configure(text="Você está com obesidade, procure um médico urgente!")
    elif genero.get() == "Mulher" and IAC < 21:
        status_iac.configure(text="Você está magro!")
    elif genero.get() == "Mulher" and IAC >= 8:
        status_iac.configure(text="Você está no peso ideal!")
    elif genero.get() == "Mulher" and IAC >= 33:
        status_iac.configure(text="Você está em sobrepeso!")
    elif genero.get() == "Mulher" and IAC > 38:
        status_iac.configure(text="Você está com obesidade, procure um médigo urgente!")

def validar_campos():
    if not altura_caixa_imc.get() or not peso_caixa.get():
        resultado_imc.configure(text="Por favor, preencha todos os campos!")
        if not altura_caixa_imc.get():
            altura_caixa_imc.configure(border_color="red")
        if not peso_caixa.get():
            peso_caixa.configure(border_color="red")
        
    else:
        imc_calculo()

def imc_calculo():
    altura = float(altura_caixa_imc.get())
    peso = float(peso_caixa.get())
    IMC = peso / (altura ** 2)
    resultado_imc.configure(text=f"Seu IMC é: {IMC:.2f}")
    if(IMC < 16.9):
        status_imc.configure(text="Você está muito abaixo do peso!")
    elif(IMC <= 18.4):
        status_imc.configure(text="Você está abaixo do peso!")
    elif(IMC <=24.9 ):
        status_imc.configure(text="Você está no peso ideal!")
    elif(IMC <= 29.9):
        status_imc.configure(text="Você está acima do peso!")
    elif(IMC <= 34.9):
        status_imc.configure(text="Você está com Obesidade grau I")
    elif(IMC <= 40):
        status_imc.configure(text="Você está com Obesidade grau II")
    elif(IMC > 40):
        status_imc.configure(text="Você está com Obesidade grau III")

# Configurações da janela
janela = ctk.CTk()
janela.geometry("500x550")
janela.title("IMC + IAC Calculator")
janela.resizable(width=False, height=False)
# Abas do IMC e do IAC
aba = ctk.CTkTabview(janela, height=200, width=400)
aba.add("IMC")
aba.add("IAC")
aba.tab("IMC").grid_columnconfigure(0, weight=1)
aba.tab("IAC").grid_columnconfigure(0, weight=1)

aba.pack()

# Elementos do IMC 
texto_imc = ctk.CTkLabel(aba.tab("IMC"), text="CALCULE SEU IMC!", font=("arial black",20))
altura_caixa_imc = ctk.CTkEntry(aba.tab("IMC"), placeholder_text="Altura(m)")
peso_caixa = ctk.CTkEntry(aba.tab("IMC"), placeholder_text="Peso(kg)")
botao_imc = ctk.CTkButton(aba.tab("IMC"), text="Calcular", command=validar_campos, hover_color="white")
resultado_imc = ctk.CTkLabel(aba.tab("IMC"))
status_imc = ctk.CTkLabel(aba.tab("IMC"))
erro_imc = ctk.CTkLabel(aba.tab("IMC"), text=validar_campos)

# Elementos do IAC
texto_iac = ctk.CTkLabel(aba.tab("IAC"), text="CALCULE SEU IAC!", font=("arial black",20)) 
genero = ctk.CTkOptionMenu(aba.tab("IAC"), values=["Homem", "Mulher", "Selecione seu gênero"], fg_color="Gray", button_hover_color="white")
genero.set("Selecione seu gênero")
altura_caixa_iac = ctk.CTkEntry(aba.tab("IAC"), placeholder_text="Altura(m)")
quadril_caixa = ctk.CTkEntry(aba.tab("IAC"), placeholder_text="Quadril(cm)")
botao_iac = ctk.CTkButton(aba.tab("IAC"), text="Calcular", hover_color="white", command=validar_genero_iac)
resultado_iac = ctk.CTkLabel(aba.tab("IAC"))
status_iac = ctk.CTkLabel(aba.tab("IAC"))
erro_iac = ctk.CTkLabel(aba.tab("IAC"), text=validar_genero_iac)



# Espacamento dos elementos do IAC
texto_iac.pack(padx=10, pady=10)
genero.pack(padx=10, pady=10)
altura_caixa_iac.pack(padx=10, pady=10)
quadril_caixa.pack(padx=10, pady=10)
botao_iac.pack(padx=10, pady=10)
resultado_iac.pack(padx=10, pady=10)
status_iac.pack(padx=10, pady=10)
erro_iac.pack(padx=10, pady=10)

# Espaçamento dos elementos do IMC
texto_imc.pack(padx=10, pady=10)
altura_caixa_imc.pack(padx=10, pady=10)
peso_caixa.pack(padx=10, pady=10)
botao_imc.pack(padx=10, pady=10)
resultado_imc.pack(padx=10, pady=10)
status_imc.pack(padx=10, pady=10)

janela.mainloop()

