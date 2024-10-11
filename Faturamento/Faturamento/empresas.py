from botcity.core import DesktopBot
from botcity.maestro import *

class Bot(DesktopBot):
        def action(self, execution=None):

            #######################-----LOGIN-----############################
        
            #self.execute(r"C:\Users\Rafael\Desktop\2207\faturamento.exe")
            self.execute(r"C:\teorema\bin\faturamento.exe")
            
            if not self.find( "btn_codigo_usuario", matching=0.97, waiting_time=10000):
                self.not_found("btn_codigo_usuario")
            self.click_relative(47, 12)
                    
            self.type_keys_with_interval(1,"999")
            self.enter()
            self.wait(500)
            self.type_keys_with_interval(1,"tsfmx24")
            self.enter()

            if not self.find( "btn_login", matching=0.97, waiting_time=10000):
                self.not_found("btn_login")
            self.click()
            self.enter()    
            self.enter()

            ###################################################################


            #################-----CADASTRO DE EMPRESAS-----####################

            #################-----TESTE INCLUIR/EDITAR-----####################
            self.wait(1500)
            if not self.find( "cadastro_aba_abrir", matching=0.97, waiting_time=10000):
                 self.not_found("cadastro_aba_abrir")
            self.click()
            self.wait(1000)
            #self.type_down()
            #self.type_down()
            self.wait(1500)
            """
            self.enter()
            self.enter()
            self.enter()
            """
            if not self.find( "abrir_empresas_cadast", matching=0.97, waiting_time=10000):
                self.not_found("abrir_empresas_cadast")
            self.click()
            if not self.find( "escolher_empresa", matching=0.97, waiting_time=10000):
                self.not_found("escolher_empresa")
            self.click()
            '''
            if not self.find( "abrir_menu_cadastro_empresa2", matching=0.97, waiting_time=10000):
                self.not_found("abrir_menu_cadastro_empresa2")
            self.click()
            '''
            self.wait(500)
            if not self.find( "faturament0_localizar_empresas", matching=0.97, waiting_time=10000):
                self.not_found("faturament0_localizar_empresas")
            self.click()
            if not self.find( "fatument0_editar_empresas", matching=0.97, waiting_time=10000):
                self.not_found("fatument0_editar_empresas")
            self.click()
            if not self.find( "faturamento_incluir_empresas", matching=0.97, waiting_time=10000):
                self.not_found("faturamento_incluir_empresas")
            self.click()
            self.type_right()
            self.enter()

            ####################-----CADASTRO ABA 1-----#######################
            
            self.wait(1500)
            if not self.find( "cadastro_empresa_nome2", matching=0.97, waiting_time=10000):
                self.not_found("cadastro_empresa_nome2")
            self.click_relative(232, 89)
            self.type_keys_with_interval(1,'te12!@')
            x=0
            while x<3:
                if not self.find( "empresa_ident1", matching=0.97, waiting_time=10000):
                    self.not_found("empresa_ident1")
                self.click_relative(37, 27)
                self.type_down()
                self.enter()
                x=x+1
            """if not self.find( "empresa_ident2", matching=0.97, waiting_time=10000):
                self.not_found("empresa_ident2")
            self.click()
            if not self.find( "empresa_ident1", matching=0.97, waiting_time=10000):
                self.not_found("empresa_ident1")
            self.click_relative(37, 27)
            if not self.find( "empresa_ident3", matching=0.97, waiting_time=10000):
                self.not_found("empresa_ident3")
            self.click()
            if not self.find( "empresa_ident1", matching=0.97, waiting_time=10000):
                self.not_found("empresa_ident1")
            self.click_relative(37, 27)
            if not self.find( "empresa_identf4", matching=0.97, waiting_time=10000):
                self.not_found("empresa_identf4")
            self.click()
            """
            if not self.find( "empresa_cpf1", matching=0.97, waiting_time=10000):
                self.not_found("empresa_cpf1")
            self.click_relative(41, 25)
            self.type_keys_with_interval(1,'08658033902')
            if not self.find( "empresa_rg1", matching=0.97, waiting_time=10000):
                self.not_found("empresa_rg1")
            self.click_relative(-5, 26)
            self.type_keys_with_interval(1,'147345348')
            if not self.find( "ativo", matching=0.97, waiting_time=10000):
                self.not_found("ativo")
            self.click()
            if not self.find( "inativo", matching=0.97, waiting_time=10000):
                self.not_found("inativo")
            self.click()
            """if not self.find( "inativo2", matching=0.97, waiting_time=10000):
                self.not_found("inativo2")
            self.click()
            if not self.find( "ativo2", matching=0.97, waiting_time=10000):
                self.not_found("ativo2")
            self.click()"""
            self.type_up()
            
                            ###---ABA 1 PRINCIPAL---###
                            ####---DADOS DA EMPRESA---####
            
            if not self.find( "nome_fantasia", matching=0.97, waiting_time=10000):
                self.not_found("nome_fantasia")
            self.click_relative(73, 25)
            self.type_keys_with_interval(1,'te12!@')
            self.tab()
        
            x = 0
            while x < 5:           
                if not self.find( "ramo_atividade", matching=0.97, waiting_time=10000):
                    self.not_found("ramo_atividade")
                self.click_relative(609, 191)
                self.type_down()
                self.enter()
                x = x+1 
            
            
            y = 0
            while y < 7:
                if not self.find( "tipora2", matching=0.97, waiting_time=10000):
                    self.not_found("tipora2")
                self.click_relative(57, 24)
                self.type_down()
                self.enter()
                y = y+1
                
            
            
    
            if not self.find( "im1", matching=0.97, waiting_time=10000):
                self.not_found("im1")
            self.click_relative(39, 25)
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "iest", matching=0.97, waiting_time=10000):
                self.not_found("iest")
            self.click_relative(61, 24)
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "rantt", matching=0.97, waiting_time=10000):
                self.not_found("rantt")
            self.click_relative(33, 28)
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "especiempresa", matching=0.97, waiting_time=10000):
                self.not_found("especiempresa")
            self.click_relative(53, 26)
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "cdgagente", matching=0.97, waiting_time=10000):
                self.not_found("cdgagente")
            self.click_relative(43, 26)
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "cinstanp", matching=0.97, waiting_time=10000):
                self.not_found("cinstanp")
            self.click_relative(33, 26)
            self.type_keys_with_interval(1,'te12!@')
            
                            ####---ENDEREÇO---###
            
            if not self.find( "rua", matching=0.97, waiting_time=10000):
                self.not_found("rua")
            self.click_relative(50, 28)
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "numerorua", matching=0.97, waiting_time=10000):
                self.not_found("numerorua")
            self.click_relative(17, 29)
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "municipio", matching=0.97, waiting_time=10000):
                self.not_found("municipio")
            self.click_relative(377, 24)
            self.type_down()
            self.enter()
            if not self.find( "municipioloop1", matching=0.97, waiting_time=10000):
                self.not_found("municipioloop1")
            self.double_click_relative(17, 25)
            self.backspace()
            self.wait(100)
            self.backspace()
            self.wait(500)
            self.enter()
            if not self.find( "municipioloop2", matching=0.97, waiting_time=10000):
                self.not_found("municipioloop2")
            self.click_relative(51, 29)       
            self.backspace(wait=100)
            if not self.find( "selecionar_municipio", matching=0.97, waiting_time=10000):
                self.not_found("selecionar_municipio")
            self.click()
            self.type_keys_with_interval(1,'0003')
            #if not self.find( "gorpacity", matching=0.97, waiting_time=10000):
                #self.not_found("gorpacity")
            #self.click()  
            #if not self.find( "faturament0_selecionar_municipio", matching=0.97, waiting_time=10000):
                #self.not_found("faturament0_selecionar_municipio")
            #self.click()
            #self.wait(1000)         
            if not self.find( "faturament0_cep_localizar", matching=0.97, waiting_time=10000):
                self.not_found("faturament0_cep_localizar")
            self.click_relative(1115, 294)
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "complemento", matching=0.97, waiting_time=10000):
                self.not_found("complemento")
            self.click_relative(80, 31)
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "bairro", matching=0.97, waiting_time=10000):
                self.not_found("bairro")
            self.click_relative(53, 27)
            self.type_keys_with_interval(1,'te12!@')
            self.tab()
            self.type_keys_with_interval(1,'(42)98411-9244')
            if not self.find( "fax", matching=0.97, waiting_time=10000):
                self.not_found("fax")
            self.click_relative(62, 28)
            self.type_keys_with_interval(1,'123123123123')
            
                            ####---DADOS DE CONTATO---####
            
            self.tab()
            self.type_keys_with_interval(1,'emaildetesteteorema@gmail.com')
            if not self.find( "botaoemailce1", matching=0.97, waiting_time=10000):
                self.not_found("botaoemailce1")
            self.click_relative(435, 43) 
            
            """           
            if not self.find( "fechar_email", matching=0.97, waiting_time=10000):
                self.not_found("fechar_email")
            self.click_relative(429, 8)
            if not self.find( "fecharemail2", matching=0.97, waiting_time=10000):
                self.not_found("fecharemail2")
            self.click()
            """
            self.alt_f4()
            self.alt_f4()
            self.tab()
            self.type_keys_with_interval(1,'www.google.com')

            self.tab()  
            if not self.find( "responsavel", matching=0.97, waiting_time=10000):
                self.not_found("responsavel")
            self.click_relative(55, 25)
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "funcaoresp", matching=0.97, waiting_time=10000):
                self.not_found("funcaoresp")
            self.click_relative(400, 27)
            self.type_down(wait=10)
            self.enter()
            #if not self.find( "codigo_funcresp", matching=0.97, waiting_time=10000):
            #    self.not_found("codigo_funcresp")
            #self.click()
            if not self.find( "funcaoresp", matching=0.97, waiting_time=10000):
                self.not_found("funcaoresp")
            self.click_relative(400, 27)
            self.backspace()
            self.wait(100)
            self.backspace()
            self.wait(500)
            if not self.find( "loopfresp1", matching=0.97, waiting_time=10000):
                self.not_found("loopfresp1")
            self.double_click_relative(55, 28)
            #if not self.find( "selecionar_funcao", matching=0.97, waiting_time=10000):
                #self.not_found("selecionar_funcao")
            #self.click()
            if not self.find( "faturament0_selecionar", matching=0.97, waiting_time=10000):
                self.not_found("faturament0_selecionar")
            self.click()
            if not self.find( "titular", matching=0.97, waiting_time=10000):
                self.not_found("titular")
            self.click_relative(55, 29)
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "funcaotitular", matching=0.97, waiting_time=10000):
                self.not_found("funcaotitular")
            self.click_relative(36, 26)
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "cpftitular", matching=0.97, waiting_time=10000):
                self.not_found("cpftitular")
            self.click_relative(53, 24)
            self.type_keys_with_interval(1,'086.580.339-02')
            
                            ####---DADOS DE CONTADOR---####
            
            if not self.find( "dados_nome_outro3", matching=0.97, waiting_time=10000):
                self.not_found("dados_nome_outro3")
            self.click_relative(66, 25)
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "dados_cpf_outro", matching=0.97, waiting_time=10000):
                self.not_found("dados_cpf_outro")
            self.click_relative(52, 27)
            self.type_keys_with_interval(1,'086.580.339-02')
            if not self.find( "dados_crc", matching=0.97, waiting_time=10000):
                self.not_found("dados_crc")
            self.click_relative(30, 27)
            self.type_keys_with_interval(1,'te12!@')
            #if not self.find( "dados_funcao_outro2", matching=0.97, waiting_time=10000):
            #    self.not_found("dados_funcao_outro2")
            #self.click_relative(58, 25)
            self.tab()
            self.type_keys_with_interval(1,'te12!@')
            
                            ####---ABAIXANDO TELA---####

            if not self.find( "faturament0_rolar_pra_baixo", matching=0.97, waiting_time=10000):
                self.not_found("faturament0_rolar_pra_baixo")
            self.click()
             
              
            x= 0
            while  x< 22:                        
                if not self.find( "seta_baixo", matching=0.97, waiting_time=10000):
                    self.not_found("seta_baixo")
                self.doubleclick()         
                x=x+1
            
                            ####---CONTINUACAO DADOS DE CONTADOR---####                         
            
            if not self.find( "email_outro_dados_2", matching=0.97, waiting_time=10000):
                self.not_found("email_outro_dados_2")
            self.click_relative(77, 29)
            self.type_keys_with_interval(1,'testeemailteorema@teste.com.br')
            if not self.find( "botaoemailce2", matching=0.97, waiting_time=10000):
                self.not_found("botaoemailce2")
            self.click_relative(432, 26)            
            self.wait(500)
            #if not self.find( "fecharemailagorafoi", matching=0.97, waiting_time=10000):
                #self.not_found("fecharemailagorafoi")
            #self.click_relative(424, 9)
            self.alt_f4()
            self.alt_f4()
            if not self.find( "telefone", matching=0.97, waiting_time=10000):
                self.not_found("telefone")
            self.click_relative(40, 27)
            self.type_keys_with_interval(1,'(42)98411-9244')
            if not self.find( "numerocontrato", matching=0.97, waiting_time=10000):
                self.not_found("numerocontrato")
            self.click_relative(21, 28)
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "postoselagem", matching=0.97, waiting_time=10000):
                self.not_found("postoselagem")
            self.click_relative(-98, 29)
            self.type_keys_with_interval(1,'te12!@')
            
                            ####---DATAS---####
            
            self.tab()
            self.tab()
            self.tab()
            self.tab()
            if not self.find( "faturament0_data_e_hora", matching=0.97, waiting_time=10000):
                self.not_found("faturament0_data_e_hora")
            self.click_relative(87, 26)
            if not self.find( "limpadata", matching=0.97, waiting_time=10000):
                self.not_found("limpadata")
            self.click()
            self.type_keys_with_interval(1,'123')
            self.enter(wait=100)
            self.enter(wait=100)
            if not self.find( "vencimentoalvara", matching=0.97, waiting_time=10000):
                self.not_found("vencimentoalvara")
            self.click_relative(91, 28)
            if not self.find( "limpar2", matching=0.97, waiting_time=10000):
                self.not_found("limpar2")
            self.click()
            self.type_keys_with_interval(1,'123')
            self.enter(wait=100)
            
                            ####---LogoTipo---####
            """        
            if not self.find( "inserirlogo", matching=0.97, waiting_time=10000):
                self.not_found("inserirlogo")
            self.click()
            #if not self.find( "arq_logo", matching=0.97, waiting_time=10000):
            #    self.not_found("arq_logo")
            #self.double_click_relative(155, 118)
            self.key_esc()
            if not self.find( "excluir_logo", matching=0.97, waiting_time=10000):
                self.not_found("excluir_logo")
            self.click()
            """    
            ##################-----CADASTRO ABA 2-----#######################
                ####---PERCENTUAIS, DIAS, ARREDONDAMENTO---####

            if not self.find( "a2_cad_empresas", matching=0.97, waiting_time=10000):
                self.not_found("a2_cad_empresas")
            self.click()
            
            self.type_keys_with_interval(1,'123')
            if not self.find( "arredondamento", matching=0.97, waiting_time=10000):
                self.not_found("arredondamento")
            self.click_relative(89, 28)
            self.type_keys_with_interval(1,'123')
            self.enter(wait=100)
            self.enter(wait=100)
            self.type_keys_with_interval(1,'123')
            if not self.find( "arredferias", matching=0.97, waiting_time=10000):
                self.not_found("arredferias")
            self.click_relative(88, 28)
            self.type_keys_with_interval(1,'123')
            self.enter()
            self.enter()
            self.type_keys_with_interval(1,'123')
            if not self.find( "adiantamento", matching=0.97, waiting_time=10000):
                self.not_found("adiantamento")
            self.click_relative(91, 31)
            self.type_keys_with_interval(1,'123')
            self.enter()
            self.enter()
            self.type_keys_with_interval(1,'123')
            if not self.find( "anuenio", matching=0.97, waiting_time=10000):
                self.not_found("anuenio")
            self.click_relative(90, 29)
            self.type_keys_with_interval(1,'123')
            self.enter()
            self.enter()
            self.type_keys_with_interval(1,'123')
            if not self.find( "trienio", matching=0.97, waiting_time=10000):
                self.not_found("trienio")
            self.click_relative(89, 31)
            self.type_keys_with_interval(1,'123')
            self.enter()
            self.enter()
            self.type_keys_with_interval(1,'123')
            if not self.find( "quinquenio", matching=0.97, waiting_time=10000):
                self.not_found("quinquenio")
            self.click_relative(88, 28)
            self.type_keys_with_interval(1,'123')
            self.enter()
            self.enter()
            self.type_keys_with_interval(1,'123')
            if not self.find( "issporcentagem", matching=0.97, waiting_time=10000):
                self.not_found("issporcentagem")
            self.click_relative(91, 29)
            self.type_keys_with_interval(1,'123')
            self.enter()
            self.enter()
            self.type_keys_with_interval(1,'123')
            if not self.find( "pisfolha", matching=0.97, waiting_time=10000):
                self.not_found("pisfolha")
            self.click_relative(88, 26)
            self.type_keys_with_interval(1,'123')
            self.enter()
            self.enter()
            self.type_keys_with_interval(1,'123')
            if not self.find( "contribsocial", matching=0.97, waiting_time=10000):
                self.not_found("contribsocial")
            self.click_relative(87, 26)
            self.type_keys_with_interval(1,'123')
            self.enter()
            self.enter()
            self.type_keys_with_interval(1,'123')
            if not self.find( "desoneracao", matching=0.97, waiting_time=10000):
                self.not_found("desoneracao")
            self.click_relative(87, 26)
            self.type_keys_with_interval(1,'123')
            self.enter()
            self.enter()
            if not self.find( "examemedico", matching=0.97, waiting_time=10000):
                self.not_found("examemedico")
            self.double_click_relative(64, 19)
            if not self.find( "examemedico2", matching=0.97, waiting_time=10000):
                self.not_found("examemedico2")
            self.double_click_relative(62, 30)
            if not self.find( "diaexpvamo2", matching=0.97, waiting_time=10000):
                self.not_found("diaexpvamo2")
            self.click_relative(63, 23)
            self.click()                        
            if not self.find( "diaexpvamo2", matching=0.97, waiting_time=10000):
                self.not_found("diaexpvamo2")            
            self.click_relative(64, 32)
            self.type_up()
            self.enter()
            self.type_keys_with_interval(1,'123')
            if not self.find( "contribconf", matching=0.97, waiting_time=10000):
                self.not_found("contribconf")
            self.click_relative(64, 28)
            self.type_keys_with_interval(1,'123')
            self.enter()
            self.enter()
            
            z = 0
            while z < 5:
                if not self.find( "aliquotaebase", matching=0.97, waiting_time=10000):
                    self.not_found("aliquotaebase")
                self.click_relative(85, 26)
                self.type_down()
                self.enter()
                z = z+1
        
            x = 0
            while x < 4:
                if not self.find( "contrataaprendiz", matching=0.97, waiting_time=10000):
                    self.not_found("contrataaprendiz")
                self.click_relative(54, 28)
                self.type_down()
                self.enter()
                x = x+1
            
            y = 0
            while y < 4:
                if not self.find( "PCD", matching=0.97, waiting_time=10000):
                    self.not_found("PCD")
                self.click_relative(-32, 29)
                self.type_down()
                self.enter()
                y = y+1
            
            if not self.find( "cnpjentidade", matching=0.97, waiting_time=10000):
                    self.not_found("cnpjentidade")
            self.click_relative(16, 30)
            self.type_keys_with_interval(1,'te12!@')
        
                        ####---CÓDIGOS---####
                            
            if not self.find( "fpas", matching=0.97, waiting_time=10000):
                self.not_found("fpas")
            self.click_relative(28, 26)
            self.type_keys_with_interval(1,'t1!')
            if not self.find( "cnae", matching=0.97, waiting_time=10000):
                self.not_found("cnae")
            self.click_relative(30, 32)
            self.type_keys_with_interval(1,'t1!')
            if not self.find( "contafgts", matching=0.97, waiting_time=10000):
                self.not_found("contafgts")
            self.click_relative(39, 26)
            self.type_keys_with_interval(1,'t1!')
            self.enter()
            #if not self.find( "codcaixa", matching=0.97, waiting_time=10000):
            #    self.not_found("codcaixa")
            #self.click_relative(43, 29)
            self.type_keys_with_interval(1,'t1!')
        
            z = 0
            while z < 6:
                if not self.find( "categoria", matching=0.97, waiting_time=10000):
                    self.not_found("categoria")
                self.click_relative(69, 24)
                self.type_up()
                self.enter()
                z = z+1
            
                            ####---EMPRESAS ISENTAS---####
            #if not self.find( "siglaenome", matching=0.97, waiting_time=10000):
            #    self.not_found("siglaenome")
            #self.click_relative(71, 25)
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "entbene", matching=0.97, waiting_time=10000):
                self.not_found("entbene")
            self.click_relative(-21, 25)
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(1,'123')
            self.enter()
            if not self.find( "emicertf", matching=0.97, waiting_time=10000):
                self.not_found("emicertf")
            self.click_relative(88, 27)
            if not self.find( "clearempisen", matching=0.97, waiting_time=10000):
                self.not_found("clearempisen")
            self.click_relative(26, 11)
            if not self.find( "emicertf2", matching=0.97, waiting_time=10000):
                self.not_found("emicertf2")
            self.click_relative(3, 26)
            self.type_keys_with_interval(1,'123')
            self.enter()
            self.type_keys_with_interval(1,'123')
            self.enter()
            if not self.find( "venccert", matching=0.97, waiting_time=10000):
                self.not_found("venccert")
            self.click_relative(89, 28)
            if not self.find( "clearvenccert", matching=0.97, waiting_time=10000):
                self.not_found("clearvenccert")
            self.click()
            self.enter()
            if not self.find( "venccert2", matching=0.97, waiting_time=10000):
                self.not_found("venccert2")
            self.click_relative(7, 29)
            self.type_keys_with_interval(1,'123')
            self.enter
            
            
            if not self.find( "protoped", matching=0.97, waiting_time=10000):
                self.not_found("protoped")
            self.click_relative(39, 28)
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(1,'123')
            self.enter()
            if not self.find( "renodata", matching=0.97, waiting_time=10000):
                self.not_found("renodata")
            self.click_relative(168, 26)
            if not self.find( "clearempisen4", matching=0.97, waiting_time=10000):
                self.not_found("clearempisen4")
            self.click()
            if not self.find( "renodata2", matching=0.97, waiting_time=10000):
                self.not_found("renodata2")
            self.click_relative(83, 26)
            self.type_keys_with_interval(1,'123')
            self.enter()
            self.type_keys_with_interval(1,'123')
            self.enter()
            if not self.find( "pubdou", matching=0.97, waiting_time=10000):
                self.not_found("pubdou")
            self.click_relative(88, 26)
            if not self.find( "clearempisen5", matching=0.97, waiting_time=10000):
                self.not_found("clearempisen5")
            self.click()
            if not self.find( "pubdou2", matching=0.97, waiting_time=10000):
                self.not_found("pubdou2")
            self.click_relative(3, 27)
            self.type_keys_with_interval(1,'123')
            self.enter()
            if not self.find( "numeropagina", matching=0.97, waiting_time=10000):
                self.not_found("numeropagina")
            self.click_relative(86, 19)
            if not self.find( "numeropagina2", matching=0.97, waiting_time=10000):
                self.not_found("numeropagina2")
            self.click_relative(87, 31)
            
                            ####---ABA 2 P.2---####
                            
            if not self.find( "a2p2_cad_empresas", matching=0.97, waiting_time=10000):
                self.not_found("a2p2_cad_empresas")
            self.click()
            if not self.find( "subirtela", matching=0.97, waiting_time=10000):
                self.not_found("subirtela")
            self.click()
            
            if not self.find( "gerarrais", matching=0.97, waiting_time=10000):
                self.not_found("gerarrais")
            self.click_relative(67, 8)        
            self.wait(100)
            self.click()
            if not self.find( "participapat", matching=0.97, waiting_time=10000):
                self.not_found("participapat")
            self.click_relative(75, 7)
            self.wait(100)
            if not self.find( "participapatmarcado", matching=0.97, waiting_time=10000):
                self.not_found("participapatmarcado")
            self.click_relative(73, 5)
            self.click()
            
            
                    
            if not self.find( "raisnegativa", matching=0.97, waiting_time=10000):
                self.not_found("raisnegativa")
            self.click_relative(55, 5)
            self.wait(100)
            if not self.find( "raisnegativamarcado", matching=0.97, waiting_time=10000):
                self.not_found("raisnegativamarcado")
            self.click_relative(80, 7)
            self.click()
            
            
                
            
            if not self.find( "codmuni", matching=0.97, waiting_time=10000):
                self.not_found("codmuni")
            self.click_relative(24, 28)
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            
            
            if not self.find( "enquadramento2", matching=0.97, waiting_time=10000):
                self.not_found("enquadramento2")
            self.click_relative(105, 25)
            self.type_down()
            self.type_down()
            self.enter()
            if not self.find( "enquadramento2", matching=0.97, waiting_time=10000):
                self.not_found("enquadramento2")
            self.click_relative(105, 25)
            self.type_up()
            self.enter()
            if not self.find( "enquadramento2", matching=0.97, waiting_time=10000):
                self.not_found("enquadramento2")
            self.click_relative(105, 25)
            self.type_down()
            self.type_down()
            self.enter()
                        
                
                
                
            if not self.find( "enceatv", matching=0.97, waiting_time=10000):
                self.not_found("enceatv")
            self.click_relative(-25, 28)
            self.type_keys_with_interval(1,'123')
            self.enter()
            if not self.find( "enc_atv2", matching=0.97, waiting_time=10000):
                self.not_found("enc_atv2")
            self.click_relative(61, 27)
            if not self.find( "clearp2", matching=0.97, waiting_time=10000):
                self.not_found("clearp2")
            self.click()
            if not self.find( "enc_atv2", matching=0.97, waiting_time=10000):
                self.not_found("enc_atv2")
            self.click_relative(61, 27)
            if not self.find( "data1", matching=0.97, waiting_time=10000):
                self.not_found("data1")
            self.click_relative(97, 73)
            self.enter()
            if not self.find( "nproprietarios", matching=0.97, waiting_time=10000):
                self.not_found("nproprietarios")
            self.click_relative(65, 23)
            if not self.find( "nproprietarios2", matching=0.97, waiting_time=10000):
                self.not_found("nproprietarios2")
            self.click_relative(65, 34)
            if not self.find( "mesdatabase", matching=0.97, waiting_time=10000):
                self.not_found("mesdatabase")
            self.click_relative(25, 29)
            self.type_keys_with_interval(1,'01')
            self.enter()
            if not self.find( "mesdatabase2", matching=0.97, waiting_time=10000):
                self.not_found("mesdatabase2")
            self.click_relative(29, 32)
            self.backspace()
            self.type_keys_with_interval(1,'1')
            self.enter()
            if not self.find( "nat_esta", matching=0.97, waiting_time=10000):
                self.not_found("nat_esta")
            self.click_relative(24, 28)
            self.type_keys_with_interval(1,'t1!@')
            
                            ####---CONTRIBUICOES PATRONAIS---####
                            
            if not self.find( "sindical", matching=0.97, waiting_time=10000):
                self.not_found("sindical")
            self.click_relative(37, 26)
            self.type_keys_with_interval(1,'123')
            self.enter()
            self.type_keys_with_interval(1,'123')
            if not self.find( "assistencial", matching=0.97, waiting_time=10000):
                self.not_found("assistencial")
            self.click_relative(49, 29)
            self.type_keys_with_interval(1,'123')
            self.enter()
            self.type_keys_with_interval(1,'123')
            if not self.find( "confederativa", matching=0.97, waiting_time=10000):
                self.not_found("confederativa")
            self.click_relative(35, 20)
            self.type_keys_with_interval(1,'123')
            self.enter()
            self.type_keys_with_interval(1,'123')
            if not self.find( "associativa", matching=0.97, waiting_time=10000):
                self.not_found("associativa")
            self.click_relative(36, 28)
            self.type_keys_with_interval(1,'123')
            self.enter()
            self.type_keys_with_interval(1,'123')
            
                            ####---INF. EXCL. FGTS---####
                            
            if not self.find( "utilizafgts", matching=0.97, waiting_time=10000):
                self.not_found("utilizafgts")
            self.click()
            self.wait(200)
            if not self.find( "utilizarecurso2", matching=0.97, waiting_time=10000):
                self.not_found("utilizarecurso2")
            self.click()
            self.wait(200)
            if not self.find( "utilizarecurso2", matching=0.97, waiting_time=10000):
                self.not_found("utilizarecurso2")
            self.click()
        
            if not self.find( "debauto2", matching=0.97, waiting_time=10000):
                self.not_found("debauto2")
            self.click()        
            self.wait(200)
            if not self.find( "debautomarcado", matching=0.97, waiting_time=10000):
                self.not_found("debautomarcado")
            self.click()
            self.wait(200)
            if not self.find( "debautomarcado2", matching=0.97, waiting_time=10000):
                self.not_found("debautomarcado2")
            self.click_relative(-9, 7)
            self.click()
            
            
        
            if not self.find( "adesaoservi3", matching=0.97, waiting_time=10000):
                self.not_found("adesaoservi3")
            self.click()      
            self.wait(200)
            if not self.find( "adesaoservi", matching=0.97, waiting_time=10000):
                self.not_found("adesaoservi")
            self.click()
            self.wait(200)
            if not self.find( "adesaoservi", matching=0.97, waiting_time=10000):
                self.not_found("adesaoservi")
            self.click()
        
            if not self.find( "agenreco", matching=0.97, waiting_time=10000):
                self.not_found("agenreco")
            self.click()
            self.wait(200)
            if not self.find( "agendarecolhemarcado", matching=0.97, waiting_time=10000):
                self.not_found("agendarecolhemarcado")
            self.click()
            self.wait(200)
            if not self.find( "recolhefgtsmarcado2", matching=0.97, waiting_time=10000):
                self.not_found("recolhefgtsmarcado2")
            self.click_relative(-9, 7)
            self.click()
            
            
        
        
            
                            ####---OUTRAS INF.---####
                            
            if not self.find( "calcrefldsr49", matching=0.97, waiting_time=10000):
                self.not_found("calcrefldsr49")
            self.click_relative(-10, 5)                
            self.wait(200)
            if not self.find( "reflexodsr0049", matching=0.97, waiting_time=10000):
                self.not_found("reflexodsr0049")
            self.click()
            self.click()        
            if not self.find( "dsr18", matching=0.97, waiting_time=10000):
                self.not_found("dsr18")
            self.click()                       
            self.wait(200)
            if not self.find( "dsr18", matching=0.97, waiting_time=10000):
                self.not_found("dsr18")
            self.click()
            self.click()
            
            if not self.find( "refhoraextra", matching=0.97, waiting_time=10000):
                self.not_found("refhoraextra")
            self.click()
            self.wait(200)
            if not self.find( "reflexohoraextramarcado", matching=0.97, waiting_time=10000):
                self.not_found("reflexohoraextramarcado")
            self.click()
            self.click()
                    
            if not self.find( "addnot", matching=0.97, waiting_time=10000):
                self.not_found("addnot")
            self.click_relative(-67, 8)
            self.wait(200)
            if not self.find( "gerainteaddnotmarcado", matching=0.97, waiting_time=10000):
                self.not_found("gerainteaddnotmarcado")
            self.click()
            self.click()        
            
            
                            ####---OUTRAS INF. PT.2---####
                            
            z = 0                 
            while z < 7:                 
                if not self.find( "controleponto", matching=0.97, waiting_time=10000):
                    self.not_found("controleponto")
                self.click_relative(43, 27)
                self.type_down()
                self.enter()
                z = z+1
                
            y = 0
            while y < 2:
                if not self.find( "regeletroemp", matching=0.97, waiting_time=10000):
                    self.not_found("regeletroemp")
                self.click_relative(66, 30)
                self.type_down()
                self.enter()
                y = y+1
                
                            ####---SEFIP---####
                            
            self.enter()                 
            if not self.find( "sefipsemmarca", matching=0.97, waiting_time=10000):
                self.not_found("sefipsemmarca")
            self.click()        
            self.wait(200)
            if not self.find( "gerarsefip", matching=0.97, waiting_time=10000):
                self.not_found("gerarsefip")
            self.click_relative(69, 8)
            
            if not self.find( "dadosadd", matching=0.97, waiting_time=10000):
                self.not_found("dadosadd")
            self.click_relative(102, 7)
            self.wait(200)
            if not self.find( "geradadosmarcado", matching=0.97, waiting_time=10000):
                self.not_found("geradadosmarcado")
            self.click()
            self.click()        
            if not self.find( "altend", matching=0.97, waiting_time=10000):
                self.not_found("altend")
            self.click_relative(92, 7)
            self.wait(200)
            if not self.find( "alteraenderecomarcado", matching=0.97, waiting_time=10000):
                self.not_found("alteraenderecomarcado")
            self.click()
            self.click()
            
            
            
            x = 0
            while x < 2:
                if not self.find( "alteracnae", matching=0.97, waiting_time=10000):
                    self.not_found("alteracnae")
                self.click_relative(80, 28)
                self.type_down()
                self.enter()
                x=x+1
                
            if not self.find( "alteracnae", matching=0.97, waiting_time=10000):
                    self.not_found("alteracnae")
            self.click_relative(80, 28)
            self.type_up()
            self.type_up()
            self.enter()    
                
            self.enter()    
            self.type_keys_with_interval(1,'123')
            self.enter()
            if not self.find( "isenfilan", matching=0.97, waiting_time=10000):
                self.not_found("isenfilan")
            self.click_relative(65, 26)
            self.type_keys_with_interval(1,'123')
            self.enter()
            self.enter()
            
            z = 0
            while z < 3:
                if not self.find( "tipocentr", matching=0.97, waiting_time=10000):
                    self.not_found("tipocentr")
                self.click_relative(105, 26)
                self.type_down()
                self.enter()
                z=z+1
                
                            ####---ABAIXANDO TELA---####
                            
            if not self.find( "abaixatela2", matching=0.97, waiting_time=10000):
                self.not_found("abaixatela2")
            self.click()
            
            t = 0
            while t < 15:
                if not self.find( "abaixatela3", matching=0.97, waiting_time=10000):
                    self.not_found("abaixatela3")
                self.double_click()
                t=t+1
                
                            ####---CAGED---####
                            
            if not self.find( "geracagedmarcado", matching=0.97, waiting_time=10000):
                self.not_found("geracagedmarcado")
            self.click()        
            self.wait(200)
            if not self.find( "geracagedmarcado", matching=0.97, waiting_time=10000):
                self.not_found("geracagedmarcado")
            self.click()
            if not self.find( "declara", matching=0.97, waiting_time=10000):
                self.not_found("declara")
            self.click_relative(82, 9)
            self.wait(200)
            if not self.find( "primeiradecmarcado", matching=0.97, waiting_time=10000):
                self.not_found("primeiradecmarcado")
            self.click()
            self.click()
            if not self.find( "nconv", matching=0.97, waiting_time=10000):
                self.not_found("nconv")
            self.click_relative(41, 28)
            self.type_keys_with_interval(1,'te12!@')
            
            
            x = 0
            while x < 3:
                if not self.find( "info", matching=0.97, waiting_time=10000):
                    self.not_found("info")
                self.click_relative(43, 26)
                self.type_down()
                self.enter()
                x=x+1
                
                            ####---GPS---####
            
            if not self.find( "codgps", matching=0.97, waiting_time=10000):
                self.not_found("codgps")
            self.click_relative(49, 26)
            self.type_keys_with_interval(1,'t1@')
            self.enter()
            self.type_keys_with_interval(1,'123')
            self.enter()
            self.type_keys_with_interval(1,'123')
            self.enter()
            self.enter()
            self.type_keys_with_interval(1,'t1@')
            self.enter()
            self.type_keys_with_interval(1,'123')
            self.enter()
            if not self.find( "terce", matching=0.97, waiting_time=10000):
                self.not_found("terce")
            self.click_relative(91, 27)
            self.type_keys_with_interval(1,'123')
            self.enter()
            self.type_keys_with_interval(1,'123')
            self.enter()
            self.type_keys_with_interval(1,'t1@')
            self.enter()
            if not self.find( "rat", matching=0.97, waiting_time=10000):
                self.not_found("rat")
            self.click_relative(89, 24)
            self.type_keys_with_interval(1,'123')
            self.enter()
            self.enter()
            self.type_keys_with_interval(1,'123')
            self.enter()
            if not self.find( "fap", matching=0.97, waiting_time=10000):
                self.not_found("fap")
            self.click_relative(87, 27)
            self.type_keys_with_interval(1,'123')
            self.enter()
            self.enter()
            self.type_keys_with_interval(1,'123')
            self.enter()
            if not self.find( "incra", matching=0.97, waiting_time=10000):
                self.not_found("incra")
            self.click_relative(89, 26)
            self.type_keys_with_interval(1,'123')
            self.enter()
            self.enter()
            self.type_keys_with_interval(1,'123')
            self.enter()
            if not self.find( "sebrae", matching=0.97, waiting_time=10000):
                self.not_found("sebrae")
            self.click_relative(89, 27)
            self.type_keys_with_interval(1,'123')
            self.enter()
            self.enter()
            self.type_keys_with_interval(1,'123')
            self.enter()
            if not self.find( "saledu", matching=0.97, waiting_time=10000):
                self.not_found("saledu")
            self.click_relative(85, 26)
            self.type_keys_with_interval(1,'123')
            self.enter()
            self.enter()
            self.type_keys_with_interval(1,'123')
            self.enter()
            if not self.find( "sesi", matching=0.97, waiting_time=10000):
                self.not_found("sesi")
            self.click_relative(90, 25)
            self.type_keys_with_interval(1,'123')
            self.enter()
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            if not self.find( "senai", matching=0.97, waiting_time=10000):
                self.not_found("senai")
            self.click_relative(88, 27)
            self.type_keys_with_interval(1,'123')
            self.enter()
            self.enter()
            if not self.find( "emprural", matching=0.97, waiting_time=10000):
                self.not_found("emprural")
            self.click_relative(78, 6)
            self.wait(200)
            if not self.find( "emprural", matching=0.97, waiting_time=10000):
                self.not_found("emprural")
            self.click()
            
            
                            ####---E SOCIAL---####
                            
            self.tab()
            if not self.find( "certificado", matching=0.97, waiting_time=10000):
                self.not_found("certificado")
            self.click_relative(33, 25)
            self.type_keys_with_interval(1,'te12!@')
            
                            ####---ABA 2 P.3---####
                            
            if not self.find( "aba2p3", matching=0.97, waiting_time=10000):
                self.not_found("aba2p3")
            self.click()
            self.type_keys_with_interval(1,'te12!@')
            self.tab()
            self.type_keys_with_interval(1,'te12!@')
            self.tab()
            self.type_keys_with_interval(1,'te12!@')
            
                            ####---ABA 3---####
                        ####---INF.FISCAIS---####
                            
            if not self.find( "aba3", matching=0.97, waiting_time=10000):
                self.not_found("aba3")
            self.click()
            if not self.find( "nojunta", matching=0.97, waiting_time=10000):
                self.not_found("nojunta")
            self.click_relative(21, 24)
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            """if not self.find( "data_registro_cadastroEmpresa", matching=0.97, waiting_time=10000):
                self.not_found("data_registro_cadastroEmpresa")
            self.click_relative(180, 178)
            if not self.find( "clearaba3", matching=0.97, waiting_time=10000):
                self.not_found("clearaba3")
            self.click()
            if not self.find( "data_registro_cadastroEmpresa", matching=0.97, waiting_time=10000):
                self.not_found("data_registro_cadastroEmpresa")
            self.click_relative(180, 178)
            if not self.find( "hoje", matching=0.97, waiting_time=10000):
                self.not_found("hoje")
            self.click()"""
            self.tab()
            self.type_keys_with_interval(1,'te12!@')
            
                            ####---INF.SIMPLES---####
            
            x = 0
            while x < 6:
                if not self.find( "simples", matching=0.97, waiting_time=10000):
                    self.not_found("simples")
                self.click_relative(464, 45)
                self.type_down()
                self.enter()
                x=x+1
                
            if not self.find( "simples", matching=0.97, waiting_time=10000):
                    self.not_found("simples")
            self.click_relative(464, 45)
            self.type_up()
            self.enter()
            self.type_keys_with_interval(1,'123')
            self.enter()
            if not self.find( "icmssimples", matching=0.97, waiting_time=10000):
                self.not_found("icmssimples")
            self.click_relative(71, 27)
            self.type_keys_with_interval(1,'123')
            self.enter()
            self.enter()
            self.type_keys_with_interval(1,'123')
            if not self.find( "diferenciado", matching=0.97, waiting_time=10000):
                self.not_found("diferenciado")
            self.click_relative(-2, 26)
            self.type_keys_with_interval(1,'123')
            self.enter()
            
            y = 0
            while y < 4:
                if not self.find( "estadual", matching=0.97, waiting_time=10000):
                    self.not_found("estadual")
                self.click_relative(145, 27)
                self.type_down()
                self.enter()
                y=y+1
                
            z = 0
            while z < 12:
                if not self.find( "federal", matching=0.97, waiting_time=10000):
                    self.not_found("federal")
                self.click_relative(145, 27)
                self.type_down()
                self.enter()
                z=z+1
                
                            ####---INF.EFD---####
                                                    
            x=0
            while x < 3:                
                if not self.find( "juridica", matching=0.97, waiting_time=10000):
                    self.not_found("juridica")
                self.click_relative(182, 26)
                self.type_down()
                self.enter()
                x=x+1
                
            y=0
            while y < 6:
                if not self.find( "atvprepon", matching=0.97, waiting_time=10000):
                    self.not_found("atvprepon")
                self.click_relative(244, 27)
                self.type_down()
                self.enter()
                y=y+1
                
                            ####---INF.ISS---####
                            
            if not self.find( "incfiscal", matching=0.97, waiting_time=10000):
                self.not_found("incfiscal")
            self.click()
            self.wait(100)
            if not self.find( "incfiscal", matching=0.97, waiting_time=10000):
                self.not_found("incfiscal")
            self.click()
            self.click()
            if not self.find( "inccultural", matching=0.97, waiting_time=10000):
                self.not_found("inccultural")
            self.click()        
            if not self.find( "incculturalmarcado", matching=0.97, waiting_time=10000):
                self.not_found("incculturalmarcado")
            self.click()               
            self.enter()
            self.type_keys_with_interval(1,'t1')
            self.enter()
            if not self.find( "regimetrib", matching=0.97, waiting_time=10000):
                self.not_found("regimetrib")
            self.click_relative(36, 28)
            self.backspace()
            self.type_keys_with_interval(1,'!')
            
                            ####---INF.DMED---####
                            
            if not self.find( "cnes", matching=0.97, waiting_time=10000):
                self.not_found("cnes")
            self.click_relative(36, 27)
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            
            x=0
            while x < 3:
                if not self.find( "tipodeclarante", matching=0.97, waiting_time=10000):
                    self.not_found("tipodeclarante")
                self.click_relative(186, 23)
                self.type_down()
                self.enter()
                x=x+1
                
                            ####---E SOCIAL---####
                            
            z=0
            while z < 19:
                if not self.find( "tributaria", matching=0.97, waiting_time=10000):
                    self.not_found("tributaria")
                self.click_relative(394, 25)
                self.type_down()
                self.enter()
                z=z+1
            
            y=0
            while y < 14:
                if not self.find( "lotacao", matching=0.97, waiting_time=10000):
                    self.not_found("lotacao")
                self.click_relative(464, 25)
                self.type_down()
                self.enter()
                y=y+1
                
                            ####---OUTRAS INF.---####
                            
            if not self.find( "escolarmarcado", matching=0.97, waiting_time=10000):
                self.not_found("escolarmarcado")
            self.click()
            if not self.find( "escolarmarcado", matching=0.97, waiting_time=10000):
                self.not_found("escolarmarcado")
            self.click()
            if not self.find( "ipi", matching=0.97, waiting_time=10000):
                self.not_found("ipi")
            self.click()
            if not self.find( "temipimarcado", matching=0.97, waiting_time=10000):
                self.not_found("temipimarcado")
            self.click() 
            self.click()       
            if not self.find( "issno", matching=0.97, waiting_time=10000):
                self.not_found("issno")
            self.click()
            if not self.find( "issicmsmarcado", matching=0.97, waiting_time=10000):
                self.not_found("issicmsmarcado")
            self.click()
            self.click()        
            if not self.find( "darfserv", matching=0.97, waiting_time=10000):
                self.not_found("darfserv")
            self.click()
            if not self.find( "darfservmarcado", matching=0.97, waiting_time=10000):
                self.not_found("darfservmarcado")
            self.click()
            if not self.find( "icmsno", matching=0.97, waiting_time=10000):
                self.not_found("icmsno")
            self.click()
            if not self.find( "icmsnomarcado", matching=0.97, waiting_time=10000):
                self.not_found("icmsnomarcado")
            self.click()
            self.click()
            if not self.find( "construtora", matching=0.97, waiting_time=10000):
                self.not_found("construtora")
            self.click()
            if not self.find( "construtoramarcado", matching=0.97, waiting_time=10000):
                self.not_found("construtoramarcado")
            self.click()
            if not self.find( "construtoramarcado", matching=0.97, waiting_time=10000):
                self.not_found("construtoramarcado")
            self.click()
            self.space()
            
            z=0
            while z < 3:
                if not self.find( "coop", matching=0.97, waiting_time=10000):
                    self.not_found("coop")
                self.click_relative(143, 27)
                self.type_down()
                self.enter()
                z=z+1
                
            if not self.find( "coop", matching=0.97, waiting_time=10000):
                    self.not_found("coop")
            self.click_relative(143, 27)
            self.type_up()
            self.type_up()
            self.type_up()
            self.enter()
            
                            ####---ABA 4---####
                            
            if not self.find( "aba4", matching=0.97, waiting_time=10000):
                self.not_found("aba4")
            self.click()
            if not self.find( "grupoempresaaba4", matching=0.97, waiting_time=10000):
                self.not_found("grupoempresaaba4")
            self.click_relative(66, 27)        
            #if not self.find( "faturament0_aba4_localizar", matching=0.97, waiting_time=10000):
                #self.not_found("faturament0_aba4_localizar")
            #self.click()
            if not self.find( "faturament0_aba4_localizar1", matching=0.97, waiting_time=10000):
                self.not_found("faturament0_aba4_localizar1")
            self.click()
            #self.type_keys_with_interval(1,"005")
            #if not self.find( "faturamento_grupo_de_empresa01", matching=0.97, waiting_time=10000):
                #self.not_found("faturamento_grupo_de_empresa01")
            #self.click()
            if not self.find( "faturamento_usa_clientes", matching=0.97, waiting_time=10000):
                self.not_found("faturamento_usa_clientes")
            self.click_relative(66, 29)
            self.type_keys_with_interval(1,"0111")
            if not self.find( "faturament0_selecionar", matching=0.97, waiting_time=10000):
                self.not_found("faturament0_selecionar")
            self.click()
            if not self.find( "transporte_clientes_fornecedores", matching=0.97, waiting_time=10000):
                self.not_found("transporte_clientes_fornecedores")
            self.click_relative(42, 32)
            self.type_keys_with_interval(1,"0111")
            if not self.find( "faturament0_Selecionar_empresas_consulta_de_empresa", matching=0.97, waiting_time=10000):
                self.not_found("faturament0_Selecionar_empresas_consulta_de_empresa")
            self.click()
            #if not self.find( "faturamento_consulta_de_empresas", matching=0.97, waiting_time=10000):
                #self.not_found("faturamento_consulta_de_empresas")
            #self.click()
            if not self.find( "pcpfaba4", matching=0.97, waiting_time=10000):
                self.not_found("pcpfaba4")
            self.click_relative(45, 28)
            self.type_keys_with_interval(1,"0001")
            if not self.find( "faturamento_selecionar_ictus_empresa", matching=0.97, waiting_time=10000):
                self.not_found("faturamento_selecionar_ictus_empresa")
            self.click()
            if not self.find( "faturament0_itens", matching=0.97, waiting_time=10000):
                self.not_found("faturament0_itens")
            self.click_relative(-27, 24)
            #if not self.find( "faturament0_selecionar_0itens", matching=0.97, waiting_time=10000):
                #self.not_found("faturament0_selecionar_0itens")
            #self.click()
            #if not self.find( "seleci0nar_itens", matching=0.97, waiting_time=10000):
                #self.not_found("seleci0nar_itens")
            #self.click()
            if not self.find( "faturamento_contrato_da_empresa", matching=0.97, waiting_time=10000):
                self.not_found("faturamento_contrato_da_empresa")
            self.click_relative(41, 29)
            if not self.find( "retornar_consultas_precos", matching=0.97, waiting_time=10000):
                self.not_found("retornar_consultas_precos")
            self.click()

            #self.type_keys_with_interval(1,"0001")
           
            #if not self.find( "codigozeradotabelapreco", matching=0.97, waiting_time=10000):
                #self.not_found("codigozeradotabelapreco")
            #self.double_click()
            #self.backspace()
            
            #if not self.find( "contratos", matching=0.97, waiting_time=10000):
                #self.not_found("contratos")
            #self.click_relative(40, 23)
            #if not self.find( "aba4codcontratos", matching=0.97, waiting_time=10000):
                #self.not_found("aba4codcontratos")
            #self.click()
            #if not self.find( "selecionartpitens", matching=0.97, waiting_time=10000):
                #self.not_found("selecionartpitens")
            #self.click()
            if not self.find( "pcempresa", matching=0.97, waiting_time=10000):
                self.not_found("pcempresa")
            self.click_relative(42, 25)
            if not self.find( "faturament0_contas_da_empresa", matching=0.97, waiting_time=10000):
                self.not_found("faturament0_contas_da_empresa")
            self.click()
            if not self.find( "consulta_empresas_", matching=0.97, waiting_time=10000):
                self.not_found("consulta_empresas_")
            self.click_relative(68, 30)
            if not self.find( "cod0015_consul_empres_contratos", matching=0.97, waiting_time=10000):
                self.not_found("cod0015_consul_empres_contratos")
            self.click()
            if not self.find( "faturament0_contas_da_empresa", matching=0.97, waiting_time=10000):
                self.not_found("faturament0_contas_da_empresa")
            self.click()
            if not self.find( "usait", matching=0.97, waiting_time=10000):
                self.not_found("usait")
            self.click_relative(68, 25)
            if not self.find( "cod_0015_consulta_empresa", matching=0.97, waiting_time=10000):
                self.not_found("cod_0015_consulta_empresa")
            self.click()
            if not self.find( "faturament0_selecionar_aaaaaaaaaaaaaa", matching=0.97, waiting_time=10000):
                self.not_found("faturament0_selecionar_aaaaaaaaaaaaaa")
            self.click()
            if not self.find( "vendedores", matching=0.97, waiting_time=10000):
                self.not_found("vendedores")
            self.click_relative(41, 24)
            if not self.find( "faturament0_concretize", matching=0.97, waiting_time=10000):
                self.not_found("faturament0_concretize")
            self.click()
            if not self.find( "faturament0_selecionar", matching=0.97, waiting_time=10000):
                self.not_found("faturament0_selecionar")
            self.click()
            if not self.find( "precosservico", matching=0.97, waiting_time=10000):
                self.not_found("precosservico")
            self.click_relative(-21, 25)
            if not self.find( "localizar_tabela_zerada", matching=0.97, waiting_time=10000):
                self.not_found("localizar_tabela_zerada")
            self.click()
            if not self.find( "tabelaprecoszerado01", matching=0.97, waiting_time=10000):
                self.not_found("tabelaprecoszerado01")
            self.click() 
            if not self.find( "faturament0_selecionar", matching=0.97, waiting_time=10000):
                self.not_found("faturament0_selecionar")
            self.click()
            if not self.find( "codigozeradotabelapreco", matching=0.97, waiting_time=10000):
                self.not_found("codigozeradotabelapreco")
            self.double_click()
            self.backspace()
            
            if not self.find( "contabilista_selecionar", matching=0.97, waiting_time=10000):
                self.not_found("contabilista_selecionar")
            self.click_relative(62, 26)
            if not self.find( "localizar_consulta_clientes", matching=0.97, waiting_time=10000):
                self.not_found("localizar_consulta_clientes")
            self.click()
            if not self.find( "cod001_consultas_clientes_faturament0", matching=0.97, waiting_time=10000):
                self.not_found("cod001_consultas_clientes_faturament0")
            self.click()
            if not self.find( "localizar_empresa_contabeis", matching=0.97, waiting_time=10000):
                self.not_found("localizar_empresa_contabeis")
            self.click()
            x=0
            while x<18:
                self.type_down()
                x=x+1
            if not self.find( "selecionar_empresa_contabeis", matching=0.97, waiting_time=10000):
                self.not_found("selecionar_empresa_contabeis")
            self.click()
            if not self.find( "historicos", matching=0.97, waiting_time=10000):
                self.not_found("historicos")
            self.click_relative(47, 28)
            if not self.find( "faturament0_concretize", matching=0.97, waiting_time=10000):
                self.not_found("faturament0_concretize")
            self.click()
            if not self.find( "Selecionar_historico", matching=0.97, waiting_time=10000):
                self.not_found("Selecionar_historico")
            self.click()
            #if not self.find( "usapreços", matching=0.97, waiting_time=10000):
            #    self.not_found("usapreços")
            #self.click_relative(44, 25)
            #if not self.find( "selecionartpitens", matching=0.97, waiting_time=10000):
            #    self.not_found("selecionartpitens")
            #self.click()
            #if not self.find( "aba4codcontratos", matching=0.97, waiting_time=10000):
            #    self.not_found("aba4codcontratos")
            #self.click()
            #if not self.find( "selecionartpitens", matching=0.97, waiting_time=10000):
            #    self.not_found("selecionartpitens")
            #self.click()
            if not self.find( "situaçoesempresa", matching=0.97, waiting_time=10000):
                self.not_found("situaçoesempresa")
            self.click_relative(44, 26)
            if not self.find( "faturament0_concretize", matching=0.97, waiting_time=10000):
                self.not_found("faturament0_concretize")
            self.click()
            if not self.find( "selecionar_situacao_empresa", matching=0.97, waiting_time=10000):
                self.not_found("selecionar_situacao_empresa")
            self.click()
            if not self.find( "veículos", matching=0.97, waiting_time=10000):
                self.not_found("veículos")
            self.click_relative(46, 25)
            if not self.find( "faturament0_concretize", matching=0.97, waiting_time=10000):
                self.not_found("faturament0_concretize")
            self.click()
            if not self.find( "selecionar_veiculos", matching=0.97, waiting_time=10000):
                self.not_found("selecionar_veiculos")
            self.click()
                            ####---GRUPOS CONTABEIS---####         
           
            if not self.find( "salvar_faturamento", matching=0.97, waiting_time=10000):
                self.not_found("salvar_faturamento")
            self.click()
            #if not self.find( "contacliente", matching=0.97, waiting_time=10000):
                #self.not_found("contacliente")
            #self.click_relative(122, 22)           
            if not self.find( "faturament0_contas_clientes", matching=0.97, waiting_time=10000):
                self.not_found("faturament0_contas_clientes")
            self.click_relative(122, 28)
            if not self.find( "localizagrupos", matching=0.97, waiting_time=10000):
                self.not_found("localizagrupos")
            self.click()
            if not self.find( "localizar_plano_De_Contas", matching=0.97, waiting_time=10000):
                self.not_found("localizar_plano_De_Contas")
            self.click()
            if not self.find( "codigobensnumerarios", matching=0.97, waiting_time=10000):
                self.not_found("codigobensnumerarios")
            self.click()
            if not self.find( "selecionar_plano_de_contas", matching=0.97, waiting_time=10000):
                self.not_found("selecionar_plano_de_contas")
            self.click()
            if not self.find( "contafornecedores", matching=0.97, waiting_time=10000):
                self.not_found("contafornecedores")
            self.click_relative(102, 26)
            if not self.find( "localizagrupos", matching=0.97, waiting_time=10000):
                self.not_found("localizagrupos")
            self.click()
            if not self.find( "localizar_PLANOS_DE_CUSTOS__00001", matching=0.97, waiting_time=10000):
                self.not_found("localizar_PLANOS_DE_CUSTOS__00001")
            self.click()
            if not self.find( "codigobensnumerarios", matching=0.97, waiting_time=10000):
                self.not_found("codigobensnumerarios")
            self.click()
            if not self.find( "selecionar_plano_de_contas", matching=0.97, waiting_time=10000):
                self.not_found("selecionar_plano_de_contas")
            self.click()
            #if not self.find( "codclientes", matching=0.97, waiting_time=10000):
                #self.not_found("codclientes")
            #self.click_relative(42, 26)
            if not self.find( "conta_contabil_99996", matching=0.97, waiting_time=10000):
                self.not_found("conta_contabil_99996")
            self.click_relative(120, 26)
            if not self.find( "localizagrupos", matching=0.97, waiting_time=10000):
                self.not_found("localizagrupos")
            self.click()
            if not self.find( "localizar_PLANOS_DE_CUSTOS__00001", matching=0.97, waiting_time=10000):
                self.not_found("localizar_PLANOS_DE_CUSTOS__00001")
            self.click()
            if not self.find( "codigobensnumerarios", matching=0.97, waiting_time=10000):
                self.not_found("codigobensnumerarios")
            self.click()
            #if not self.find( "contabil_9996", matching=0.97, waiting_time=10000):
                #self.not_found("contabil_9996")
            #self.click_relative(124, 29)
            #if not self.find( "localizar_plano_contas", matching=0.97, waiting_time=10000):
                #self.not_found("localizar_plano_contas") 
            if not self.find( "planos_de_continhas", matching=0.97, waiting_time=10000):
                 self.not_found("planos_de_continhas")
            self.click_relative(201, 193)
            if not self.find( "consulta_de_planos_Contas", matching=0.97, waiting_time=10000):
                 self.not_found("consulta_de_planos_Contas")
            self.click_relative(154, 39)
            #if not self.find( "faturament0_selecionar_planos_custos", matching=0.97, waiting_time=10000):
                #self.not_found("faturament0_selecionar_planos_custos")
            #self.click()
            if not self.find( "conta_Contabil999995", matching=0.97, waiting_time=10000):
                self.not_found("conta_Contabil999995")
            self.click_relative(123, 28)
            #if not self.find( "localizar_PLANOS_DE_CUSTOS__00001", matching=0.97, waiting_time=10000):
                #self.not_found("localizar_PLANOS_DE_CUSTOS__00001")
            #self.click()
            if not self.find( "localizar_grupos_no_plano_contas", matching=0.97, waiting_time=10000):
                self.not_found("localizar_grupos_no_plano_contas")
            self.click()
            self.type_keys_with_interval(1,"1.1.01.01. ")
            if not self.find( "localizar_plano_de_contas", matching=0.97, waiting_time=10000):
                self.not_found("localizar_plano_de_contas")
            self.click()
            if not self.find( "selecionar_plano_de_contas", matching=0.97, waiting_time=10000):
                self.not_found("selecionar_plano_de_contas")
            self.click()
            if not self.find( "conta_contabil99994", matching=0.97, waiting_time=10000):
                    self.not_found("conta_contabil99994")
            self.click_relative(123, 32)
            if not self.find( "localiza_grupos", matching=0.97, waiting_time=10000):
                self.not_found("localiza_grupos")
            self.click()
            self.enter()
            self.type_keys_with_interval(1,"1.1.01.01.")
            if not self.find( "selecionar_planos_de_Custgos", matching=0.97, waiting_time=10000):
                self.not_found("selecionar_planos_de_Custgos")
            self.click()
            if not self.find( "conta_contabil9992", matching=0.97, waiting_time=10000):
                self.not_found("conta_contabil9992")
            self.click_relative(124, 28)
            if not self.find( "localiza_99923", matching=0.97, waiting_time=10000):
                self.not_found("localiza_99923")
            self.click()
            if not self.find( "faturamento_seleecionarr_0003", matching=0.97, waiting_time=10000):
               self.not_found("faturamento_seleecionarr_0003")
            self.click()
            if not self.find( "retornarr_faturamentos", matching=0.97, waiting_time=10000):
                    self.not_found("retornarr_faturamentos")
            self.click()
            #if not self.find( "localizar_PLANOS_DE_CUSTOS__00001", matching=0.97, waiting_time=10000):
                #self.not_found("localizar_PLANOS_DE_CUSTOS__00001")
            #self.click()
            #self.tab()
            #if not self.find( "conta_contabil_99992", matching=0.97, waiting_time=10000):
                #self.not_found("conta_contabil_99992")
            #self.click_relative(130, 28)
            self.enter()
            self.type_keys_with_interval(1,"1.1.01.01.")
            if not self.find( "localizar_contabils_99992", matching=0.97, waiting_time=10000):
                self.not_found("localizar_contabils_99992")
            self.click()
            #if not self.find( "codigobensnumerarios", matching=0.97, waiting_time=10000):
                #self.not_found("codigobensnumerarios")
            #self.click()
            if not self.find( "selecionar_plano_de_contas", matching=0.97, waiting_time=10000):
                self.not_found("selecionar_plano_de_contas")
            self.click()

            if not self.find( "99992", matching=0.97, waiting_time=10000):
                self.not_found("99992")
            self.click_relative(49, 24)
            if not self.find( "localizagrupos", matching=0.97, waiting_time=10000):
                self.not_found("localizagrupos")
            self.click()
            self.type_keys_with_interval(1,"1.1.01.01.")
            self.enter()
            if not self.find( "selecionar_contabis_999991", matching=0.97, waiting_time=10000):
                self.not_found("selecionar_contabis_999991")
            self.click()
            if not self.find( "99991", matching=0.97, waiting_time=10000):
                self.not_found("99991")
            self.click_relative(47, 22)
            if not self.find( "localizagrupos", matching=0.97, waiting_time=10000):
                self.not_found("localizagrupos")
            self.click()
            self.type_keys_with_interval(1,"1.1.01.01.")
            if not self.find( "localizar_planos_de_contas", matching=0.97, waiting_time=10000):
                self.not_found("localizar_planos_de_contas")
            self.click()
            if not self.find( "selecionar_planos_de_contas", matching=0.97, waiting_time=10000):
                self.not_found("selecionar_planos_de_contas")
            self.click()
            if not self.find( "conta_contabil_99990", matching=0.97, waiting_time=10000):
                self.not_found("conta_contabil_99990")
            self.click_relative(219, 53)
            
            ''''
            if not self.find( "99998", matching=0.97, waiting_time=10000):
                self.not_found("99998")
            self.click_relative(119, 26)
            if not self.find( "localiza_grupo_de_planos", matching=0.97, waiting_time=10000):
                self.not_found("localiza_grupo_de_planos")
            self.click()
            if not self.find( "localizagrupos", matching=0.97, waiting_time=10000):
                self.not_found("localizagrupos")
            self.click()
            if not self.find( "localizarplanodecontas", matching=0.97, waiting_time=10000):
                self.not_found("localizarplanodecontas")
            self.click()
            if not self.find( "codigobensnumerarios", matching=0.97, waiting_time=10000):
                self.not_found("codigobensnumerarios")
            self.click()
            if not self.find( "selecionarplanodecontas", matching=0.97, waiting_time=10000):
                self.not_found("selecionarplanodecontas")
            self.click()
            if not self.find( "99988", matching=0.97, waiting_time=10000):
                self.not_found("99988")
            self.click_relative(47, 25)
            if not self.find( "localizagrupos", matching=0.97, waiting_time=10000):
                self.not_found("localizagrupos")
            self.click()
            if not self.find( "localizarplanodecontas", matching=0.97, waiting_time=10000):
                self.not_found("localizarplanodecontas")
            self.click()
            if not self.find( "codigobensnumerarios", matching=0.97, waiting_time=10000):
                self.not_found("codigobensnumerarios")
            self.click()
            if not self.find( "selecionarplanodecontas", matching=0.97, waiting_time=10000):
                self.not_found("selecionarplanodecontas")
            self.click()
            
            if not self.find( "99987", matching=0.97, waiting_time=10000):
                self.not_found("99987")
            self.click_relative(48, 26)
            if not self.find( "localizagrupos", matching=0.97, waiting_time=10000):
                self.not_found("localizagrupos")
            self.click()
            if not self.find( "localizarplanodecontas", matching=0.97, waiting_time=10000):
                self.not_found("localizarplanodecontas")
            self.click()
            if not self.find( "codigobensnumerarios", matching=0.97, waiting_time=10000):
                self.not_found("codigobensnumerarios")
            self.click()
            if not self.find( "selecionarplanodecontas", matching=0.97, waiting_time=10000):
                self.not_found("selecionarplanodecontas")
            self.click()
            
            if not self.find( "99986", matching=0.97, waiting_time=10000):
                self.not_found("99986")
            self.click_relative(47, 26)
            if not self.find( "localizagrupos", matching=0.97, waiting_time=10000):
                self.not_found("localizagrupos")
            self.click()
            if not self.find( "localizarplanodecontas", matching=0.97, waiting_time=10000):
                self.not_found("localizarplanodecontas")
            self.click()
            if not self.find( "codigobensnumerarios", matching=0.97, waiting_time=10000):
                self.not_found("codigobensnumerarios")
            self.click()
            if not self.find( "selecionarplanodecontas", matching=0.97, waiting_time=10000):
                self.not_found("selecionarplanodecontas")
            self.click()
            if not self.find( "99985", matching=0.97, waiting_time=10000):
                self.not_found("99985")
            self.click_relative(47, 25)
            if not self.find( "localizagrupos", matching=0.97, waiting_time=10000):
                self.not_found("localizagrupos")
            self.click()
            if not self.find( "localizarplanodecontas", matching=0.97, waiting_time=10000):
                self.not_found("localizarplanodecontas")
            self.click()
            if not self.find( "codigobensnumerarios", matching=0.97, waiting_time=10000):
                self.not_found("codigobensnumerarios")
            self.click()
            if not self.find( "selecionarplanodecontas", matching=0.97, waiting_time=10000):
                self.not_found("selecionarplanodecontas")
            self.click()
            if not self.find( "99984", matching=0.97, waiting_time=10000):
                self.not_found("99984")
            self.click_relative(48, 26)
            if not self.find( "localizagrupos", matching=0.97, waiting_time=10000):
                self.not_found("localizagrupos")
            self.click()
            if not self.find( "localizarplanodecontas", matching=0.97, waiting_time=10000):
                self.not_found("localizarplanodecontas")
            self.click()
            if not self.find( "codigobensnumerarios", matching=0.97, waiting_time=10000):
                self.not_found("codigobensnumerarios")
            self.click()
            if not self.find( "selecionarplanodecontas", matching=0.97, waiting_time=10000):
                self.not_found("selecionarplanodecontas")
            self.click()
            if not self.find( "99983", matching=0.97, waiting_time=10000):
                self.not_found("99983")
            self.click_relative(47, 27)
            if not self.find( "localizagrupos", matching=0.97, waiting_time=10000):
                self.not_found("localizagrupos")
            self.click()
            if not self.find( "localizarplanodecontas", matching=0.97, waiting_time=10000):
                self.not_found("localizarplanodecontas")
            self.click()
            if not self.find( "codigobensnumerarios", matching=0.97, waiting_time=10000):
                self.not_found("codigobensnumerarios")
            self.click()
            if not self.find( "selecionarplanodecontas", matching=0.97, waiting_time=10000):
                self.not_found("selecionarplanodecontas")
            self.click()
            if not self.find( "99982", matching=0.97, waiting_time=10000):
                self.not_found("99982")
            self.click_relative(49, 27)
            if not self.find( "localizagrupos", matching=0.97, waiting_time=10000):
                self.not_found("localizagrupos")
            self.click()
            if not self.find( "localizarplanodecontas", matching=0.97, waiting_time=10000):
                self.not_found("localizarplanodecontas")
            self.click()
            if not self.find( "codigobensnumerarios", matching=0.97, waiting_time=10000):
                self.not_found("codigobensnumerarios")
            self.click()
            if not self.find( "selecionarplanodecontas", matching=0.97, waiting_time=10000):
                self.not_found("selecionarplanodecontas")
            self.click()
            if not self.find( "99981", matching=0.97, waiting_time=10000):
                self.not_found("99981")
            self.click_relative(47, 25)
            if not self.find( "localizagrupos", matching=0.97, waiting_time=10000):
                self.not_found("localizagrupos")
            self.click()
            if not self.find( "localizarplanodecontas", matching=0.97, waiting_time=10000):
                self.not_found("localizarplanodecontas")
            self.click()
            if not self.find( "codigobensnumerarios", matching=0.97, waiting_time=10000):
                self.not_found("codigobensnumerarios")
            self.click()
            if not self.find( "selecionarplanodecontas", matching=0.97, waiting_time=10000):
                self.not_found("selecionarplanodecontas")
            self.click()
            
            if not self.find( "contpatri", matching=0.97, waiting_time=10000):
                self.not_found("contpatri")
            self.click_relative(-2, 19)
            self.type_keys_with_interval(1,'t1!')
            self.enter()
            '''
                            ####---ABA 5---####
                        ####---ABA5 P1---####
                            
            if not self.find( "aba5", matching=0.97, waiting_time=10000):
                self.not_found("aba5")
            self.click()
            if not self.find( "salvar_relacionamento", matching=0.97, waiting_time=10000):
                self.not_found("salvar_relacionamento")
            self.click()
            self.enter()
            if not self.find( "incluirnovoregistro", matching=0.97, waiting_time=10000):
                self.not_found("incluirnovoregistro")
            self.click()
            if not self.find( "estadoaba5", matching=0.97, waiting_time=10000):
                self.not_found("estadoaba5")
            self.click_relative(43, 27)
            self.type_keys_with_interval(1,"001")
            if not self.find( "selecionar_consulta_estados", matching=0.97, waiting_time=10000):
                    self.not_found("selecionar_consulta_estados")
            self.click()
            if not self.find( "inscricaoestad", matching=0.97, waiting_time=10000):
                self.not_found("inscricaoestad")
            self.click_relative(40, 30)
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            if not self.find( "gravar", matching=0.97, waiting_time=10000):
                self.not_found("gravar")
            self.click()
            if not self.find( "cancelarcertoa5p1", matching=0.97, waiting_time=10000):
                self.not_found("cancelarcertoa5p1")
            self.click_relative(11, 8)                
            if not self.find( "abandonarop", matching=0.97, waiting_time=10000):
                self.not_found("abandonarop")
            self.click_relative(16, 63) 
            if not self.find( "aba5p2", matching=0.97, waiting_time=10000):
                self.not_found("aba5p2")
            self.click()
            if not self.find( "aba5p1_inscricao", matching=0.97, waiting_time=10000):
                self.not_found("aba5p1_inscricao")
            self.click()
            if not self.find( "a5p1inscri", matching=0.97, waiting_time=10000):
                self.not_found("a5p1inscri")
            self.click()
            if not self.find( "deletara5p2", matching=0.97, waiting_time=10000):
                self.not_found("deletara5p2")
            self.click()
            self.enter()
                            ####---ABA5 P2---####
                            
            if not self.find( "aba5p2", matching=0.97, waiting_time=10000):
                self.not_found("aba5p2")
            self.click()
            if not self.find( "incluirnovoregistro", matching=0.97, waiting_time=10000):
                self.not_found("incluirnovoregistro")
            self.click()
            #if not self.find( "cadnomeaba5", matching=0.97, waiting_time=10000):
            #    self.not_found("cadnomeaba5")
            #self.click_relative(107, 56)        
            self.type_keys_with_interval(1,'te12!@')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.enter()
            if not self.find( "nascimentoaba5p2", matching=0.97, waiting_time=10000):
                self.not_found("nascimentoaba5p2")
            self.click_relative(76, 27)
            if not self.find( "clearaba5p2normal", matching=0.97, waiting_time=10000):
                self.not_found("clearaba5p2normal")
            self.click()
            self.type_keys_with_interval(1,'123')
            self.enter()
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            
                            ####---ENDERECO ABA 5---####
            
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "ufaba5", matching=0.97, waiting_time=10000):
                self.not_found("ufaba5")
            self.click_relative(209, 28)
            x=0
            while x < 27:
                self.type_down()
                self.enter()
                if not self.find( "ufaba5", matching=0.97, waiting_time=10000):
                    self.not_found("ufaba5")
                self.click_relative(209, 28)
                x=x+1
                
            self.enter()
            self.type_keys_with_interval(1,'85055-370')
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(1,'(42)98411-9244')
            self.enter()
            self.type_keys_with_interval(1,'testeteorema@teste.com.br')
            self.enter()
            
                            ####---CARACTERISTICAS---####
                            
            if not self.find( "ocorrenciaaba5", matching=0.97, waiting_time=10000):
                self.not_found("ocorrenciaaba5")
            self.click_relative(316, 26)
            self.type_down()
            self.type_down()
            self.enter()
            
            y=0
            while y < 8:
                if not self.find( "ocorrenciaaba5", matching=0.97, waiting_time=10000):
                    self.not_found("ocorrenciaaba5")
                self.click_relative(316, 26)
                self.type_down()
                self.enter()
                y=y+1
                
            if not self.find( "classeaba5p2", matching=0.97, waiting_time=10000):
                self.not_found("classeaba5p2")
            self.click_relative(10, 25)
            self.type_keys_with_interval(1,'t1')
            self.enter()
            if not self.find( "classeaba5p2", matching=0.97, waiting_time=10000):
                self.not_found("classeaba5p2")
            self.click_relative(10, 25)
            self.backspace()
            self.type_keys_with_interval(1,'!')
            self.enter()
            if not self.find( "ndepende", matching=0.97, waiting_time=10000):
                self.not_found("ndepende")
            self.click_relative(73, 21)
            if not self.find( "ndependes3", matching=0.97, waiting_time=10000):
                self.not_found("ndependes3")
            self.click_relative(73, 31)
            self.enter()
            
            x=0
            while x<22:
                if not self.find( "categ", matching=0.97, waiting_time=10000):
                    self.not_found("categ")
                self.click_relative(320, 21)
                self.type_down()
                self.enter()
                x=x+1
                
            self.type_keys_with_interval(1,'123')
            self.enter()
            if not self.find( "admissaodataaba5", matching=0.97, waiting_time=10000):
                self.not_found("admissaodataaba5")
            self.click_relative(55, 23)
            if not self.find( "clearadmissao", matching=0.97, waiting_time=10000):
                self.not_found("clearadmissao")
            self.click()
            if not self.find( "admissaodataaba5", matching=0.97, waiting_time=10000):
                self.not_found("admissaodataaba5")
            self.click_relative(55, 23)
            if not self.find( "dataadmis", matching=0.97, waiting_time=10000):
                self.not_found("dataadmis")
            self.click_relative(93, 65)
            self.enter()
            self.type_keys_with_interval(1,'123')
            self.enter()
            if not self.find( "saidaaba5", matching=0.97, waiting_time=10000):
                self.not_found("saidaaba5")
            self.click_relative(47, 21)
            if not self.find( "clearsaida", matching=0.97, waiting_time=10000):
                self.not_found("clearsaida")
            self.click()
            if not self.find( "saidaaba5", matching=0.97, waiting_time=10000):
                self.not_found("saidaaba5")
            self.click_relative(47, 21)
            if not self.find( "datasaida", matching=0.97, waiting_time=10000):
                self.not_found("datasaida")
            self.click_relative(9, 64)
            self.enter()
            self.type_keys_with_interval(1,'123')
            self.enter()
            if not self.find( "prolabore", matching=0.97, waiting_time=10000):
                self.not_found("prolabore")
            self.click_relative(105, 25)
            self.type_keys_with_interval(1,'123')
            self.enter()
            self.enter()
            self.type_keys_with_interval(1,'123')
            if not self.find( "vinculos", matching=0.97, waiting_time=10000):
                self.not_found("vinculos")
            self.click_relative(51, 25)
            self.type_keys_with_interval(1,'123')
            self.enter()
            self.enter()
            self.type_keys_with_interval(1,'123')
            if not self.find( "inssdatabela", matching=0.97, waiting_time=10000):
                self.not_found("inssdatabela")
            self.click_relative(32, 27)
            self.type_keys_with_interval(1,'123')
            self.enter()
            self.enter()
            self.type_keys_with_interval(1,'123')
            if not self.find( "inssempresa", matching=0.97, waiting_time=10000):
                self.not_found("inssempresa")
            self.click_relative(58, 25)
            self.type_keys_with_interval(1,'123')
            self.enter()
            self.enter()
            if not self.find( "recolhefgtsmarcado", matching=0.97, waiting_time=10000):
                self.not_found("recolhefgtsmarcado")
            self.click()
            self.wait(100)
            if not self.find( "recolhefgtsmarcado", matching=0.97, waiting_time=10000):
                self.not_found("recolhefgtsmarcado")
            self.click()
            if not self.find( "recolhefgtsmarcado", matching=0.97, waiting_time=10000):
                self.not_found("recolhefgtsmarcado")
            self.click()
            self.enter()
            if not self.find( "isentoinssaba5", matching=0.97, waiting_time=10000):
                self.not_found("isentoinssaba5")
            self.click()
            self.wait(100)
            if not self.find( "isentoinssaba5", matching=0.97, waiting_time=10000):
                self.not_found("isentoinssaba5")
            self.click()
            self.enter()
            if not self.find( "isentoirmarcado", matching=0.97, waiting_time=10000):
                self.not_found("isentoirmarcado")
            self.click()
            self.wait(100)
            if not self.find( "isentoirmarcado", matching=0.97, waiting_time=10000):
                self.not_found("isentoirmarcado")
            self.click()
            self.enter()
            if not self.find( "spedcontabilaba5", matching=0.97, waiting_time=10000):
                self.not_found("spedcontabilaba5")
            self.click()
            self.wait(100)
            if not self.find( "spedcontabilaba5", matching=0.97, waiting_time=10000):
                self.not_found("spedcontabilaba5")
            self.click()
            if not self.find( "spedcontabilaba5", matching=0.97, waiting_time=10000):
                self.not_found("spedcontabilaba5")
            self.click()

                            ####---AGRUPAMENTO---####

            if not self.find( "funcaoagrupa", matching=0.97, waiting_time=10000):
                self.not_found("funcaoagrupa")
            self.click_relative(331, 26)
            self.type_up()
            self.enter()
            if not self.find( "departagrupa", matching=0.97, waiting_time=10000):
                self.not_found("departagrupa")
            self.click_relative(328, 23)
            self.type_up()
            self.enter()
            if not self.find( "setoragrupa", matching=0.97, waiting_time=10000):
                self.not_found("setoragrupa")
            self.click_relative(327, 27)
            self.type_up()
            self.enter()
            if not self.find( "secaoagrupa", matching=0.97, waiting_time=10000):
                self.not_found("secaoagrupa")
            self.click_relative(325, 24)
            self.type_up()
            self.enter()
            if not self.find( "bancoagrupa", matching=0.97, waiting_time=10000):
                self.not_found("bancoagrupa")
            self.click_relative(327, 25)
            self.type_up()
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(1,'t1!')
            self.tab()
            
                            ####---ABAIXAR TELA---####

            if not self.find( "abaixatelaa5p2", matching=0.97, waiting_time=10000):
                self.not_found("abaixatelaa5p2")
            self.click()
            
            z=0
            while z < 12:
                if not self.find( "abaixatelaa5b2m", matching=0.97, waiting_time=10000):
                    self.not_found("abaixatelaa5b2m")
                self.double_click()
                z=z+1

                            ####---OBSERVACOES---####
            """
            if not self.find( "obsinfa5p2", matching=0.97, waiting_time=10000):
                self.not_found("obsinfa5p2")
            self.click_relative(34, 52)
            self.type_keys_with_interval(1,'te12!@')
            """
            
                            ####---SALVAR E CONSULTAR---####

            if not self.find( "salvara5p2", matching=0.97, waiting_time=10000):
                self.not_found("salvara5p2")
            self.click()        
            if not self.find( "consultara5p2", matching=0.97, waiting_time=10000):
                self.not_found("consultara5p2")
            self.click()            
            if not self.find( "cancelara5p2", matching=0.97, waiting_time=10000):
                self.not_found("cancelara5p2")
            self.click()
            self.enter()
            #if not self.find( "sima5p2", matching=0.97, waiting_time=10000):
            #    self.not_found("sima5p2")
            #self.click()
            if not self.find( "aba5p3", matching=0.97, waiting_time=10000):
                self.not_found("aba5p3")
            self.click()
            if not self.find( "aba5p2", matching=0.97, waiting_time=10000):
                self.not_found("aba5p2")
            self.click()
            if not self.find( "testea5p2", matching=0.97, waiting_time=10000):
                self.not_found("testea5p2")
            self.click()
            if not self.find( "deletara5p2", matching=0.97, waiting_time=10000):
                self.not_found("deletara5p2")
            self.click()
            self.enter()

                        ####---ABA5 P3---####

            if not self.find( "aba5p3", matching=0.97, waiting_time=10000):
                self.not_found("aba5p3")
            self.click()
            if not self.find( "incluirnovoregistro", matching=0.97, waiting_time=10000):
                self.not_found("incluirnovoregistro")
            self.click()
            if not self.find( "tipodoca5p3", matching=0.97, waiting_time=10000):
                self.not_found("tipodoca5p3")
            self.click_relative(348, 26)
            self.type_up()
            self.enter()
            self.type_keys_with_interval(1,'123')
            self.enter()
            if not self.find( "vencimentoa5p3", matching=0.97, waiting_time=10000):
                self.not_found("vencimentoa5p3")
            self.click_relative(74, 27)
            if not self.find( "cleara5p3", matching=0.97, waiting_time=10000):
                self.not_found("cleara5p3")
            self.click()
            if not self.find( "vencimentoa5p3", matching=0.97, waiting_time=10000):
                self.not_found("vencimentoa5p3")
            self.click_relative(74, 27)
            if not self.find( "datasa5p3", matching=0.97, waiting_time=10000):
                self.not_found("datasa5p3")
            self.click_relative(92, 67)
            self.tab()
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "abrirdoca5p3", matching=0.97, waiting_time=10000):
                self.not_found("abrirdoca5p3")
            self.click()
            #if not self.find( "abrirarq", matching=0.97, waiting_time=10000):
            #    self.not_found("abrirarq")
            #self.click_relative(621, 10)
            self.key_esc()
            if not self.find( "obsa5p3", matching=0.97, waiting_time=10000):
                self.not_found("obsa5p3")
            self.click_relative(36, 34)
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "salvara5p2", matching=0.97, waiting_time=10000):
                self.not_found("salvara5p2")
            self.click()
            if not self.find( "cancelara5p2", matching=0.97, waiting_time=10000):
                self.not_found("cancelara5p2")
            self.click()
            self.enter()
            #if not self.find( "sima5p2", matching=0.97, waiting_time=10000):
            #    self.not_found("sima5p2")
            #self.click()
            #if not self.find( "arqte12!@", matching=0.97, waiting_time=10000):
            #    self.not_found("arqte12!@")
            #self.click()
            if not self.find( "deletara5p2", matching=0.97, waiting_time=10000):
                self.not_found("deletara5p2")
            self.click()
            self.enter()
            #if not self.find( "sima5p2", matching=0.97, waiting_time=10000):
            #    self.not_found("sima5p2")
            #self.click()

                            ####---ABA5 P4---####

            if not self.find( "a5p4_cad_empresa", matching=0.97, waiting_time=10000):
                self.not_found("a5p4_cad_empresa")
            self.click()  
            if not self.find( "incluirnovoregistro", matching=0.97, waiting_time=10000):
                self.not_found("incluirnovoregistro")
            self.click()
            if not self.find( "aba5p4cliente", matching=0.97, waiting_time=10000):
                self.not_found("aba5p4cliente")
            self.click_relative(67, 25)
            if not self.find( "localizar_cliente", matching=0.97, waiting_time=10000):
                self.not_found("localizar_cliente")
            self.click()
            #if not self.find( "codclientea5p4", matching=0.97, waiting_time=10000):
            #    self.not_found("codclientea5p4")
            #self.click()
            if not self.find( "selecionar_cliente_consulta", matching=0.97, waiting_time=10000):
                self.not_found("selecionar_cliente_consulta")
            self.click()
            if not self.find( "obsaba5p4", matching=0.97, waiting_time=10000):
                self.not_found("obsaba5p4")
            self.click_relative(28, 39)
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "salvara5p2", matching=0.97, waiting_time=10000):
                self.not_found("salvara5p2")
            self.click()
            if not self.find( "consultara5p2", matching=0.97, waiting_time=10000):
                self.not_found("consultara5p2")
            self.click()
            if not self.find( "cancelara5p2", matching=0.97, waiting_time=10000):
                self.not_found("cancelara5p2")
            self.click()
            self.enter()
            #if not self.find( "sima5p2", matching=0.97, waiting_time=10000):
            #    self.not_found("sima5p2")
            #self.click()
            if not self.find( "acharparaexcluiraba5p4", matching=0.97, waiting_time=10000):
                self.not_found("acharparaexcluiraba5p4")
            self.click()        
            if not self.find( "deletara5p2", matching=0.97, waiting_time=10000):
                self.not_found("deletara5p2")
            self.click()
            self.enter()
            #if not self.find( "sima5p2", matching=0.97, waiting_time=10000):
            #    self.not_found("sima5p2")
            #self.click()
            
                            ####---GNRE---####

            if not self.find( "GNRE", matching=0.97, waiting_time=10000):
                self.not_found("GNRE")
            self.click()
            if not self.find( "a6tipo", matching=0.97, waiting_time=10000):
                self.not_found("a6tipo")
            self.click_relative(98, 25)
            self.type_down()
            self.enter()
            if not self.find( "a6tipo", matching=0.97, waiting_time=10000):
                self.not_found("a6tipo")
            self.click_relative(98, 25)
            self.type_up()
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "arquivoaba6", matching=0.97, waiting_time=10000):
                self.not_found("arquivoaba6")
            self.click_relative(437, 25)
            if not self.find( "abrirarq", matching=0.97, waiting_time=10000):
                self.not_found("abrirarq")
            self.click_relative(621, 10)
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "pastaschema", matching=0.97, waiting_time=10000):
                self.not_found("pastaschema")
            self.click_relative(384, 25)
            if not self.find( "cancelar", matching=0.97, waiting_time=10000):
                self.not_found("cancelar")
            self.click()
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "gerados", matching=0.97, waiting_time=10000):
                self.not_found("gerados")
            self.click_relative(340, 26)
            if not self.find( "cancelar", matching=0.97, waiting_time=10000):
                self.not_found("cancelar")
            self.click()
            if not self.find( "ambiente", matching=0.97, waiting_time=10000):
                self.not_found("ambiente")
            self.click_relative(97, 27)
            self.type_up()
            self.enter()
            if not self.find( "ambiente", matching=0.97, waiting_time=10000):
                self.not_found("ambiente")
            self.click_relative(97, 27)
            self.type_down()
            self.enter()
            if not self.find( "imprimir", matching=0.97, waiting_time=10000):
                self.not_found("imprimir")
            self.click_relative(45, 27)
            self.type_down()
            self.enter()
            if not self.find( "imprimir", matching=0.97, waiting_time=10000):
                self.not_found("imprimir")
            self.click_relative(45, 27)
            self.type_down()
            self.enter()
            if not self.find( "imprimir", matching=0.97, waiting_time=10000):
                self.not_found("imprimir")
            self.click_relative(45, 27)
            self.type_up()
            self.type_up()
            self.type_keys_with_interval(1,'086.580.339-02')
            self.enter()    
            self.enter()
            self.type_keys_with_interval(1,'14.734.534-8')
         
            
                        ####---FINALIZAÇÃO (SALVAMENTO E EXCLUSÃO)---####

            if not self.find( "faturament0_salvar_cadastro_empresa", matching=0.97, waiting_time=10000):
               self.not_found("faturament0_salvar_cadastro_empresa")
            self.click()
            self.wait(1000)
            self.enter()
            if not self.find( "retornar_fim", matching=0.97, waiting_time=10000):
                self.not_found("retornar_fim")
            self.click()
            if not self.find( "localizar_fim", matching=0.97, waiting_time=10000):
                self.not_found("localizar_fim")
            self.click()
            if not self.find( "selecionarempresafim", matching=0.97, waiting_time=10000):
                self.not_found("selecionarempresafim")
            self.click()
            if not self.find( "cadastro_empresa_editar", matching=0.97, waiting_time=10000):
                self.not_found("cadastro_empresa_editar")
            self.click()
            self.wait(500)
            if not self.find( "ativo", matching=0.97, waiting_time=10000):
                self.not_found("ativo")
            self.click()
            if not self.find( "inativo", matching=0.97, waiting_time=10000):
                self.not_found("inativo")
            self.click()
            if not self.find( "salvar_fim", matching=0.97, waiting_time=10000):
                self.not_found("salvar_fim")
            self.click()
            self.wait(1000)
            self.enter()
            if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                self.not_found("retornarfim")
            self.click()
            if not self.find( "a2_cadastro_empresa", matching=0.97, waiting_time=10000):
                self.not_found("a2_cadastro_empresa")
            self.click()            
            if not self.find( "todosfiltro", matching=0.97, waiting_time=10000):
                self.not_found("todosfiltro")
            self.click()
            if not self.find( "1consulta", matching=0.97, waiting_time=10000):
                self.not_found("1consulta")
            self.click()
            if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                self.not_found("localizarfim")
            self.click()
            if not self.find( "empresainativa", matching=0.97, waiting_time=10000):
                self.not_found("empresainativa")
            self.click()
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            self.wait(500)
            if not self.find( "excluirfim", matching=0.97, waiting_time=10000):
                self.not_found("excluirfim")
            self.click()
            #if not self.find( "simexcluirfim", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirfim")
            #self.click()
            self.enter()
            if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                self.not_found("retornarfim")
            self.click()
            if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                self.not_found("localizarfim")
            self.click()
            if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                self.not_found("retornarfim")
            self.click()
    
                ####---GRUPO DE EMPRESAS---####

            if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro2")
            self.click()
            self.wait(1500)
            if not self.find( "abrir_menu_cadastro_empresa2", matching=0.97, waiting_time=10000):
                self.not_found("abrir_menu_cadastro_empresa2")
            self.click()
            self.wait(1500)
            #if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
            #    self.not_found("abrircadastros_abacadastro2")
            #self.click()
            #self.enter()
            #self.type_down()
            #self.enter()
            #self.enter()
            #self.enter()
            #if not self.find( "mnu_cadastros_empresas", matching=0.97, waiting_time=10000):
            #    self.not_found("mnu_cadastros_empresas")
            #self.click()
            self.wait(1500)
            if not self.find( "grupodeempresas", matching=0.97, waiting_time=10000):
                self.not_found("grupodeempresas")
            self.click()
            if not self.find( "empresas_localizar", matching=0.97, waiting_time=10000):
                self.not_found("empresas_localizar")
            self.click()
            if not self.find( "empresas_incluir", matching=0.97, waiting_time=10000):
                self.not_found("empresas_incluir")
            self.click()
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            if not self.find( "fimsalvar", matching=0.97, waiting_time=10000):
                self.not_found("fimsalvar")
            self.click()
            if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                self.not_found("retornarfim")
            self.click()
            if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                self.not_found("localizarfim")
            self.click()
            if not self.find( "selecionarempresafim", matching=0.97, waiting_time=10000):
                self.not_found("selecionarempresafim")
            self.click()
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            self.wait(500)
            #if not self.find( "excluirfim", matching=0.97, waiting_time=10000):
                #self.not_found("excluirfim")
            #self.click()
            #if not self.find( "simexcluirfim", matching=0.97, waiting_time=10000):
            #        self.not_found("simexcluirfim")
            #self.click()
            self.enter()
            if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                self.not_found("retornarfim")
            self.click()
            if not self.find( "localizarfim", matching=0.97, waiting_time=10000):
                self.not_found("localizarfim")
            self.click()
            if not self.find( "retornarfim", matching=0.97, waiting_time=10000):
                self.not_found("retornarfim")
            self.click()
            if not self.find( "fechargestaoadm", matching=0.97, waiting_time=10000):
                self.not_found("fechargestaoadm")
            self.click()
            if not self.find( "simfecharfim", matching=0.97, waiting_time=10000):
                self.not_found("simfecharfim")
            self.click()
            #self.enter()0021811

        def not_found(self, label):
            print(f"Element not found: {label}")  
        
if __name__ == '__main__':

    Bot.main()
