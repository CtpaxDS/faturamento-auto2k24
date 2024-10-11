from botcity.core import DesktopBot
# from botcity.maestro import *



class Bot(DesktopBot):
        def action(self, execution=None):

            #######################-----LOGIN-----############################
        
            self.execute(r"C:\Users\Rafael\Desktop\2207\faturamento.exe")
            
            if not self.find( "btn_codigo_usuario", matching=0.97, waiting_time=10000):
                self.not_found("btn_codigo_usuario")
            self.click_relative(47, 12)
                    
            self.paste("999")
            self.paste("teofire21")
            self.enter()

            if not self.find( "btn_login", matching=0.97, waiting_time=10000):
                self.not_found("btn_login")
            self.click()
            self.enter()    
            

            ###################################################################


            #################-----CADASTRO DE EMPRESAS-----####################

            #################-----TESTE INCLUIR/EDITAR-----####################

            if not self.find( "abrircadastros_abacadastro", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro")
            self.click()
            if not self.find( "mnu_cadastros_empresas", matching=0.97, waiting_time=10000):
                self.not_found("mnu_cadastros_empresas")
            self.click()
            if not self.find( "mnu_cadastros_empresas2", matching=0.97, waiting_time=10000):
                self.not_found("mnu_cadastros_empresas2")
            self.click()
            #if not self.find( "abrir_empresas", matching=0.97, waiting_time=10000):
            #    self.not_found("abrir_empresas")
            #self.click()
            if not self.find( "localizar", matching=0.97, waiting_time=10000):
                self.not_found("localizar")
            self.click()
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            self.wait(2000)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()
            self.type_right()
            self.enter()

            ####################-----CADASTRO ABA 1-----#######################
            

            if not self.find( "cadastro_empresa_nome2", matching=0.97, waiting_time=10000):
                self.not_found("cadastro_empresa_nome2")
            self.click_relative(155, 27)
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "empresa_ident1", matching=0.97, waiting_time=10000):
                self.not_found("empresa_ident1")
            self.click_relative(37, 27)
            if not self.find( "empresa_ident2", matching=0.97, waiting_time=10000):
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
            if not self.find( "inativo2", matching=0.97, waiting_time=10000):
                self.not_found("inativo2")
            self.click()
            if not self.find( "ativo2", matching=0.97, waiting_time=10000):
                self.not_found("ativo2")
            self.click()
            
                            ###---ABA 1 PRINCIPAL---###
                            ####---DADOS DA EMPRESA---####
            
            if not self.find( "nome_fantasia", matching=0.97, waiting_time=10000):
                self.not_found("nome_fantasia")
            self.click_relative(73, 25)
            self.type_keys_with_interval(1,'te12!@')
            
        
            x = 0
            while x < 5:           
                if not self.find( "ramo_atividade", matching=0.97, waiting_time=10000):
                    self.not_found("ramo_atividade")
                self.click_relative(57, 25)
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
            if not self.find( "localizarbuscar", matching=0.97, waiting_time=10000):
                self.not_found("localizarbuscar")
            self.click()
            if not self.find( "gorpacity", matching=0.97, waiting_time=10000):
                self.not_found("gorpacity")
            self.click()
            if not self.find( "selecionar", matching=0.97, waiting_time=10000):
                self.not_found("selecionar")
            self.click()
            self.wait(1000)
            if not self.find( "cep", matching=0.97, waiting_time=10000):
                self.not_found("cep")
            self.click_relative(28, 28)
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "complemento", matching=0.97, waiting_time=10000):
                self.not_found("complemento")
            self.click_relative(80, 31)
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "bairro", matching=0.97, waiting_time=10000):
                self.not_found("bairro")
            self.click_relative(53, 27)
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "telefone", matching=0.97, waiting_time=10000):
                self.not_found("telefone")
            self.click_relative(40, 26)
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
            if not self.find( "fecharemail1", matching=0.97, waiting_time=10000):
                self.not_found("fecharemail1")
            self.click_relative(425, 10)
            
            if not self.find( "fecharemail2", matching=0.97, waiting_time=10000):
                self.not_found("fecharemail2")
            self.click()
            if not self.find( "site", matching=0.97, waiting_time=10000):
                self.not_found("site")
            self.click_relative(106, 30)
            self.type_keys_with_interval(1,'www.google.com')
            if not self.find( "abresite", matching=0.97, waiting_time=10000):
                self.not_found("abresite")
            self.click()
            if not self.find( "fechargoogle", matching=0.97, waiting_time=10000):
                self.not_found("fechargoogle")
            self.click_relative(213, 9)       
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
            if not self.find( "selecaofuncao", matching=0.97, waiting_time=10000):
                self.not_found("selecaofuncao")
            self.click()
            if not self.find( "selecionarfuncao", matching=0.97, waiting_time=10000):
                self.not_found("selecionarfuncao")
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
            if not self.find( "dados_funcao_outro2", matching=0.97, waiting_time=10000):
                self.not_found("dados_funcao_outro2")
            self.click_relative(58, 25)
            self.type_keys_with_interval(1,'te12!@')
            
                            ####---ABAIXANDO TELA---####
                            
            if not self.find( "abaixar_tela", matching=0.97, waiting_time=10000):
                self.not_found("abaixar_tela")
            self.click() 
                            
            t = 0
            while t < 22:                        
                if not self.find( "seta_baixo", matching=0.97, waiting_time=10000):
                    self.not_found("seta_baixo")
                self.doubleclick()         
                t = t+1
            
                            ####---CONTINUACAO DADOS DE CONTADOR---####                         
            
            if not self.find( "email_outro_dados_2", matching=0.97, waiting_time=10000):
                self.not_found("email_outro_dados_2")
            self.click_relative(77, 29)
            self.type_keys_with_interval(1,'testeemailteorema@teste.com.br')
            if not self.find( "botaoemailce2", matching=0.97, waiting_time=10000):
                self.not_found("botaoemailce2")
            self.click_relative(432, 26)            
            self.wait(500)
            if not self.find( "fecharemailagorafoi", matching=0.97, waiting_time=10000):
                self.not_found("fecharemailagorafoi")
            self.click_relative(424, 9)
            if not self.find( "fecharemail2", matching=0.97, waiting_time=10000):
                self.not_found("fecharemail2")
            self.click()
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
            
            if not self.find( "datacadastro", matching=0.97, waiting_time=10000):
                self.not_found("datacadastro")
            self.click_relative(89, 27)
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
                
            ##################-----CADASTRO ABA 2-----#######################
                ####---PERCENTUAIS, DIAS, ARREDONDAMENTO---####

            if not self.find( "ABA2", matching=0.97, waiting_time=10000):
                self.not_found("ABA2")
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
            if not self.find( "siglaenome", matching=0.97, waiting_time=10000):
                self.not_found("siglaenome")
            self.click_relative(71, 25)
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
                            
            if not self.find( "p2", matching=0.97, waiting_time=10000):
                self.not_found("p2")
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
            if not self.find( "inss", matching=0.97, waiting_time=10000):
                self.not_found("inss")
            self.click_relative(91, 29)
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
            self.enter()
            self.type_keys_with_interval(1,'123')
            self.enter()
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
            self.enter()
            self.type_keys_with_interval(1,'123')
            self.enter()
            if not self.find( "registro", matching=0.97, waiting_time=10000):
                self.not_found("registro")
            self.click_relative(47, 28)
            if not self.find( "clearaba3", matching=0.97, waiting_time=10000):
                self.not_found("clearaba3")
            self.click()
            if not self.find( "registro", matching=0.97, waiting_time=10000):
                self.not_found("registro")
            self.click_relative(47, 28)
            if not self.find( "hoje", matching=0.97, waiting_time=10000):
                self.not_found("hoje")
            self.click()
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            
                            ####---INF.SIMPLES---####
            
            x = 0
            while x < 6:
                if not self.find( "simples", matching=0.97, waiting_time=10000):
                    self.not_found("simples")
                self.click_relative(463, 27)
                self.type_down()
                self.enter()
                x=x+1
                
            if not self.find( "simples", matching=0.97, waiting_time=10000):
                    self.not_found("simples")
            self.click_relative(463, 27)
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
            if not self.find( "aba4localizar1", matching=0.97, waiting_time=10000):
                self.not_found("aba4localizar1")
            self.click()
            if not self.find( "aba4selecionar1", matching=0.97, waiting_time=10000):
                self.not_found("aba4selecionar1")
            self.click()
            if not self.find( "cfempresa", matching=0.97, waiting_time=10000):
                self.not_found("cfempresa")
            self.click_relative(41, 24)
            if not self.find( "aba4cod1", matching=0.97, waiting_time=10000):
                self.not_found("aba4cod1")
            self.click()
            if not self.find( "aba4selecionar2", matching=0.97, waiting_time=10000):
                self.not_found("aba4selecionar2")
            self.click()
            if not self.find( "pcpfaba4", matching=0.97, waiting_time=10000):
                self.not_found("pcpfaba4")
            self.click_relative(45, 28)
            if not self.find( "aba4cod2", matching=0.97, waiting_time=10000):
                self.not_found("aba4cod2")
            self.click()
            if not self.find( "aba4selecionar3", matching=0.97, waiting_time=10000):
                self.not_found("aba4selecionar3")
            self.click()
            if not self.find( "tpitens", matching=0.97, waiting_time=10000):
                self.not_found("tpitens")
            self.click_relative(-22, 26)
            if not self.find( "localizartpitens", matching=0.97, waiting_time=10000):
                self.not_found("localizartpitens")
            self.click()
            if not self.find( "tabelaprecoszerado01", matching=0.97, waiting_time=10000):
                self.not_found("tabelaprecoszerado01")
            self.click()            
            if not self.find( "selecionartpitens", matching=0.97, waiting_time=10000):
                self.not_found("selecionartpitens")
            self.click()
            if not self.find( "codigozeradotabelapreco", matching=0.97, waiting_time=10000):
                self.not_found("codigozeradotabelapreco")
            self.double_click()
            self.backspace()
            
            if not self.find( "contratos", matching=0.97, waiting_time=10000):
                self.not_found("contratos")
            self.click_relative(40, 23)
            if not self.find( "aba4codcontratos", matching=0.97, waiting_time=10000):
                self.not_found("aba4codcontratos")
            self.click()
            if not self.find( "selecionartpitens", matching=0.97, waiting_time=10000):
                self.not_found("selecionartpitens")
            self.click()
            if not self.find( "pcempresa", matching=0.97, waiting_time=10000):
                self.not_found("pcempresa")
            self.click_relative(42, 25)
            if not self.find( "aba4codcontratos", matching=0.97, waiting_time=10000):
                self.not_found("aba4codcontratos")
            self.click()
            if not self.find( "selecionartpitens", matching=0.97, waiting_time=10000):
                self.not_found("selecionartpitens")
            self.click()
            if not self.find( "usait", matching=0.97, waiting_time=10000):
                self.not_found("usait")
            self.click_relative(68, 25)
            if not self.find( "aba4codcontratos", matching=0.97, waiting_time=10000):
                self.not_found("aba4codcontratos")
            self.click()
            if not self.find( "selecionartpitens", matching=0.97, waiting_time=10000):
                self.not_found("selecionartpitens")
            self.click()
            if not self.find( "vendedores", matching=0.97, waiting_time=10000):
                self.not_found("vendedores")
            self.click_relative(41, 24)
            if not self.find( "aba4codcontratos", matching=0.97, waiting_time=10000):
                self.not_found("aba4codcontratos")
            self.click()
            if not self.find( "selecionartpitens", matching=0.97, waiting_time=10000):
                self.not_found("selecionartpitens")
            self.click()
            if not self.find( "precosservico", matching=0.97, waiting_time=10000):
                self.not_found("precosservico")
            self.click_relative(-21, 25)
            if not self.find( "localizartpitens", matching=0.97, waiting_time=10000):
                self.not_found("localizartpitens")
            self.click()
            if not self.find( "tabelaprecoszerado01", matching=0.97, waiting_time=10000):
                self.not_found("tabelaprecoszerado01")
            self.click() 
            if not self.find( "selecionartpitens", matching=0.97, waiting_time=10000):
                self.not_found("selecionartpitens")
            self.click()
            if not self.find( "codigozeradotabelapreco", matching=0.97, waiting_time=10000):
                self.not_found("codigozeradotabelapreco")
            self.double_click()
            self.backspace()
            if not self.find( "contabilista", matching=0.97, waiting_time=10000):
                self.not_found("contabilista")
            self.click_relative(67, 26)
            if not self.find( "localizartpitens", matching=0.97, waiting_time=10000):
                self.not_found("localizartpitens")
            self.click()
            if not self.find( "codcinco0", matching=0.97, waiting_time=10000):
                self.not_found("codcinco0")
            self.click()
            if not self.find( "selecionartpitens", matching=0.97, waiting_time=10000):
                self.not_found("selecionartpitens")
            self.click()
            if not self.find( "historicos", matching=0.97, waiting_time=10000):
                self.not_found("historicos")
            self.click_relative(47, 28)
            if not self.find( "aba4codcontratos", matching=0.97, waiting_time=10000):
                self.not_found("aba4codcontratos")
            self.click()
            if not self.find( "selecionartpitens", matching=0.97, waiting_time=10000):
                self.not_found("selecionartpitens")
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
            if not self.find( "aba4codcontratos", matching=0.97, waiting_time=10000):
                self.not_found("aba4codcontratos")
            self.click()
            if not self.find( "selecionartpitens", matching=0.97, waiting_time=10000):
                self.not_found("selecionartpitens")
            self.click()
            if not self.find( "veículos", matching=0.97, waiting_time=10000):
                self.not_found("veículos")
            self.click_relative(46, 25)
            if not self.find( "aba4codcontratos", matching=0.97, waiting_time=10000):
                self.not_found("aba4codcontratos")
            self.click()
            if not self.find( "selecionartpitens", matching=0.97, waiting_time=10000):
                self.not_found("selecionartpitens")
            self.click()
            
            
                            ####---GRUPOS CONTABEIS---####
                             
            if not self.find( "salvaraba4paragrupocontabil", matching=0.97, waiting_time=10000):
                self.not_found("salvaraba4paragrupocontabil")
            self.click()
            
                            
            if not self.find( "contacliente", matching=0.97, waiting_time=10000):
                self.not_found("contacliente")
            self.click_relative(122, 22)        
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
            
            
            if not self.find( "contafornecedores", matching=0.97, waiting_time=10000):
                self.not_found("contafornecedores")
            self.click_relative(102, 26)
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
            
            if not self.find( "codclientes", matching=0.97, waiting_time=10000):
                self.not_found("codclientes")
            self.click_relative(42, 26)
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

            if not self.find( "codforne", matching=0.97, waiting_time=10000):
                self.not_found("codforne")
            self.click_relative(42, 24)
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


            if not self.find( "99994", matching=0.97, waiting_time=10000):
                self.not_found("99994")
            self.click_relative(46, 24)
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


            if not self.find( "99993", matching=0.97, waiting_time=10000):
                self.not_found("99993")
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


            if not self.find( "99992", matching=0.97, waiting_time=10000):
                self.not_found("99992")
            self.click_relative(49, 24)
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


            if not self.find( "99991", matching=0.97, waiting_time=10000):
                self.not_found("99991")
            self.click_relative(47, 22)
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


            if not self.find( "99990", matching=0.97, waiting_time=10000):
                self.not_found("99990")
            self.click_relative(48, 24)
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


            if not self.find( "99989", matching=0.97, waiting_time=10000):
                self.not_found("99989")
            self.click_relative(47, 24)
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

                            ####---ABA 5---####
                        ####---ABA5 P1---####
                            
            if not self.find( "aba5", matching=0.97, waiting_time=10000):
                self.not_found("aba5")
            self.click()
            if not self.find( "salvar", matching=0.97, waiting_time=10000):
                self.not_found("salvar")
            self.click()
            if not self.find( "incluirnovoregistro", matching=0.97, waiting_time=10000):
                self.not_found("incluirnovoregistro")
            self.click()
            if not self.find( "estadoaba5", matching=0.97, waiting_time=10000):
                self.not_found("estadoaba5")
            self.click_relative(43, 27)
            if not self.find( "cod01aba5", matching=0.97, waiting_time=10000):
                self.not_found("cod01aba5")
            self.click()
            if not self.find( "selecionaraba5", matching=0.97, waiting_time=10000):
                self.not_found("selecionaraba5")
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
            if not self.find( "aba5p1inscricao", matching=0.97, waiting_time=10000):
                self.not_found("aba5p1inscricao")
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
            if not self.find( "cadnomeaba5", matching=0.97, waiting_time=10000):
                self.not_found("cadnomeaba5")
            self.click_relative(107, 56)        
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
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
            self.type_keys_with_interval(1,'086.580.339-02')
            self.enter()
            self.type_keys_with_interval(1,'14.734.534-8')
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

            if not self.find( "obsinfa5p2", matching=0.97, waiting_time=10000):
                self.not_found("obsinfa5p2")
            self.click_relative(34, 52)
            self.type_keys_with_interval(1,'te12!@')
            
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
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "abrirdoca5p3", matching=0.97, waiting_time=10000):
                self.not_found("abrirdoca5p3")
            self.click()
            if not self.find( "abrirarq", matching=0.97, waiting_time=10000):
                self.not_found("abrirarq")
            self.click_relative(621, 10)
            #self.key_esc()
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

            if not self.find( "aba5p4", matching=0.97, waiting_time=10000):
                self.not_found("aba5p4")
            self.click()
            if not self.find( "incluirnovoregistro", matching=0.97, waiting_time=10000):
                self.not_found("incluirnovoregistro")
            self.click()
            if not self.find( "aba5p4cliente", matching=0.97, waiting_time=10000):
                self.not_found("aba5p4cliente")
            self.click_relative(67, 25)
            if not self.find( "localizarcliente", matching=0.97, waiting_time=10000):
                self.not_found("localizarcliente")
            self.click()
            if not self.find( "codclientea5p4", matching=0.97, waiting_time=10000):
                self.not_found("codclientea5p4")
            self.click()
            if not self.find( "selecionaraba5p4", matching=0.97, waiting_time=10000):
                self.not_found("selecionaraba5p4")
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
            self.enter()
            
                        ####---FINALIZAÇÃO (SALVAMENTO E EXCLUSÃO)---####

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
            if not self.find( "ativo", matching=0.97, waiting_time=10000):
                self.not_found("ativo")
            self.click()
            if not self.find( "inativo", matching=0.97, waiting_time=10000):
                self.not_found("inativo")
            self.click()
            if not self.find( "fimsalvar", matching=0.97, waiting_time=10000):
                self.not_found("fimsalvar")
            self.click()
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

            if not self.find( "abrircadastros_abacadastro", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro")
            self.click()
            if not self.find( "mnu_cadastros_empresas", matching=0.97, waiting_time=10000):
                    self.not_found("mnu_cadastros_empresas")
            self.click()
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
            if not self.find( "excluirfim", matching=0.97, waiting_time=10000):
                    self.not_found("excluirfim")
            self.click()
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
            
	         
                        ####---ABRINDO PARAMETROS---####
            
            if not self.find( "abrircadastros_abacadastro", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro")
            self.click()
            if not self.find( "parametros", matching=0.97, waiting_time=10000):
                self.not_found("parametros")
            self.click()
            if not self.find( "parametrosempresa", matching=0.97, waiting_time=10000):
                self.not_found("parametrosempresa")
            self.click()
            if not self.find( "localizape", matching=0.97, waiting_time=10000):
                self.not_found("localizape")
            self.click()
            if not self.find( "editarpe", matching=0.97, waiting_time=10000):
                self.not_found("editarpe")
            self.click()
            self.wait(3500)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()
            if not self.find( "naope", matching=0.97, waiting_time=10000):
                self.not_found("naope")
            self.click()
            if not self.find( "buscaempresape", matching=0.97, waiting_time=10000):
                self.not_found("buscaempresape")
            self.click()
            self.backspace()
            if not self.find( "localizape", matching=0.97, waiting_time=10000):
                self.not_found("localizape")
            self.click()
            if not self.find( "cod0101ictusteste", matching=0.97, waiting_time=10000):
                self.not_found("cod0101ictusteste")
            self.click()
            
                                    
            if not self.find( "selecionarpe", matching=0.97, waiting_time=10000):
                self.not_found("selecionarpe")
            self.click()
            
                            ####---TITULOS COM ATRASOS---####
            
            if not self.find( "tituloatrasopagamentoapartir1", matching=0.97, waiting_time=10000):
                self.not_found("tituloatrasopagamentoapartir1")
            self.click_relative(25, 19)
            if not self.find( "titulopagamentoapartir2", matching=0.97, waiting_time=10000):
                self.not_found("titulopagamentoapartir2")            
            self.click_relative(27, 29)            
            self.backspace()
            self.backspace()
            self.type_keys_with_interval(1,'874')
             
            
            
                               ####---INTEGRACOES ERP---####
            
            if not self.find( "administrativo_com_livros_fiscais", matching=0.97, waiting_time=10000):
                self.not_found("administrativo_com_livros_fiscais")
            self.click_relative(163, 27)
            self.type_down()
            self.enter()
            if not self.find( "administrativo_com_livros_fiscais", matching=0.97, waiting_time=10000):
                self.not_found("administrativo_com_livros_fiscais")
            self.click_relative(163, 27)
            self.type_up()
            self.enter()
            if not self.find( "financeirocomcontabilidade", matching=0.97, waiting_time=10000):
                self.not_found("financeirocomcontabilidade")
            self.click_relative(160, 22)
            self.type_down()
            self.enter()
            if not self.find( "financeirocomcontabilidade", matching=0.97, waiting_time=10000):
                self.not_found("financeirocomcontabilidade")
            self.click_relative(160, 22)
            self.type_down()
            self.enter()
            if not self.find( "livrosfiscaiscomcontabilidade", matching=0.97, waiting_time=10000):
                self.not_found("livrosfiscaiscomcontabilidade")
            self.click_relative(162, 27)
            self.click()
            self.type_down()
            self.enter()
            if not self.find( "livrosfiscaiscomcontabilidade", matching=0.97, waiting_time=10000):
                self.not_found("livrosfiscaiscomcontabilidade")
            self.click_relative(162, 27)
            self.type_up()
            self.enter()
            if not self.find( "estoquecomcontabilidade", matching=0.97, waiting_time=10000):
                self.not_found("estoquecomcontabilidade")
            self.click_relative(164, 24)
            self.type_down()
            self.enter()
            if not self.find( "estoquecomcontabilidade", matching=0.97, waiting_time=10000):
                self.not_found("estoquecomcontabilidade")
            self.click_relative(164, 24)
            self.type_up()
            self.enter()
            if not self.find( "gestaopessoalcomcontabilidade", matching=0.97, waiting_time=10000):
                self.not_found("gestaopessoalcomcontabilidade")
            self.click_relative(162, 27)
            self.type_down()
            self.enter()
            if not self.find( "gestaopessoalcomcontabilidade", matching=0.97, waiting_time=10000):
                self.not_found("gestaopessoalcomcontabilidade")
            self.click_relative(162, 27)
            self.type_up()
            self.enter()
            if not self.find( "alterarlancamentoscontabeis", matching=0.97, waiting_time=10000):
                self.not_found("alterarlancamentoscontabeis")
            self.click_relative(164, 25)
            self.type_down()
            self.enter()
            if not self.find( "alterarlancamentoscontabeis", matching=0.97, waiting_time=10000):
                self.not_found("alterarlancamentoscontabeis")
            self.click_relative(164, 25)
            self.type_up()
            self.enter()
            if not self.find( "conhecimentoscomlivrosfiscais", matching=0.97, waiting_time=10000):
                self.not_found("conhecimentoscomlivrosfiscais")
            self.click_relative(165, 25)
            self.type_up()
            self.enter()
            if not self.find( "conhecimentoscomlivrosfiscais", matching=0.97, waiting_time=10000):
                self.not_found("conhecimentoscomlivrosfiscais")
            self.click_relative(165, 25)
            self.type_down()
            self.enter()
            
                            ####---DOC E---####
                             
            if not self.find( "utilizanfe", matching=0.97, waiting_time=10000):
                self.not_found("utilizanfe")
            self.click_relative(161, 23)
            self.type_down()
            self.enter()
            if not self.find( "utilizanfe", matching=0.97, waiting_time=10000):
                self.not_found("utilizanfe")
            self.click_relative(161, 23)
            self.type_up()
            self.enter()
            if not self.find( "mododeenvionfe", matching=0.97, waiting_time=10000):
                self.not_found("mododeenvionfe")
            self.click_relative(162, 24)
            self.type_down()
            self.enter()
            if not self.find( "mododeenvionfe", matching=0.97, waiting_time=10000):
                self.not_found("mododeenvionfe")
            self.click_relative(162, 24)
            self.type_up()
            self.enter()
            if not self.find( "mododeenvionfce", matching=0.97, waiting_time=10000):
                self.not_found("mododeenvionfce")
            self.click_relative(164, 24)
            self.type_down()
            self.enter()
            if not self.find( "mododeenvionfce", matching=0.97, waiting_time=10000):
                self.not_found("mododeenvionfce")
            self.click_relative(164, 24)
            self.type_up()
            self.enter()
            if not self.find( "mododefinalizacaonfse", matching=0.97, waiting_time=10000):
                self.not_found("mododefinalizacaonfse")
            self.click_relative(164, 27)
            self.type_down()
            self.enter()
            if not self.find( "mododefinalizacaonfse", matching=0.97, waiting_time=10000):
                self.not_found("mododefinalizacaonfse")
            self.click_relative(164, 27)
            self.type_up()
            self.enter()
            if not self.find( "utilizanfsenfem", matching=0.97, waiting_time=10000):
                self.not_found("utilizanfsenfem")
            self.click_relative(165, 25)
            self.type_up()
            self.enter()
            if not self.find( "utilizanfsenfem", matching=0.97, waiting_time=10000):
                self.not_found("utilizanfsenfem")
            self.click_relative(165, 25)
            self.type_down()
            self.enter()
            
                            ####---VERIFICACOES E EXIGENCIAS---####
                             
            x=0
            while x < 4:
                if not self.find( "verificarlimitedecredito", matching=0.97, waiting_time=10000):
                    self.not_found("verificarlimitedecredito")
                self.click_relative(161, 25)
                self.type_down()
                self.enter()
                x=x+1
                
            x=0
            while x < 4:
                if not self.find( "verificarlimitedecredito", matching=0.97, waiting_time=10000):
                    self.not_found("verificarlimitedecredito")
                self.click_relative(161, 25)
                self.type_up()
                self.enter()
                x=x+1
                
            x=0
            while x < 4:
                if not self.find( "verificasituacaocadastro", matching=0.97, waiting_time=10000):
                    self.not_found("verificasituacaocadastro")
                self.click_relative(162, 25)
                self.type_down()
                self.enter()
                x=x+1
                
            x=0
            while x < 4:
                if not self.find( "verificasituacaocadastro", matching=0.97, waiting_time=10000):
                    self.not_found("verificasituacaocadastro")
                self.click_relative(162, 25)
                self.type_up()
                self.enter()
                x=x+1
                
                
            x=0
            while x<2:
                if not self.find( "verificacnpjcpfduplicado", matching=0.97, waiting_time=10000):
                    self.not_found("verificacnpjcpfduplicado")
                self.click_relative(164, 24)
                self.type_down()
                self.enter()
                x=x+1
                
            x=0
            while x<2:
                if not self.find( "verificacnpjcpfduplicado", matching=0.97, waiting_time=10000):
                    self.not_found("verificacnpjcpfduplicado")
                self.click_relative(164, 24)
                self.type_up()
                self.enter()
                x=x+1


            x=0
            while x<4:
                if not self.find( "nivelexigenciacadastro", matching=0.97, waiting_time=10000):
                    self.not_found("nivelexigenciacadastro")
                self.click_relative(161, 24)
                self.type_down()
                self.enter()
                x=x+1
                
            x=0
            while x<4:
                if not self.find( "nivelexigenciacadastro", matching=0.97, waiting_time=10000):
                    self.not_found("nivelexigenciacadastro")
                self.click_relative(161, 24)
                self.type_up()
                self.enter()
                x=x+1
            
            if not self.find( "cadastramentosemmacros", matching=0.97, waiting_time=10000):
                self.not_found("cadastramentosemmacros")
            self.click_relative(165, 26)
            self.type_down()
            self.enter()
            if not self.find( "cadastramentosemmacros", matching=0.97, waiting_time=10000):
                self.not_found("cadastramentosemmacros")
            self.click_relative(165, 26)
            self.type_up()
            self.enter()
            
            x=0
            while x<4:
                if not self.find( "atrasospagamentos", matching=0.97, waiting_time=10000):
                    self.not_found("atrasospagamentos")
                self.click_relative(164, 27)
                self.type_down()
                self.enter()
                x=x+1
            
            x=0
            while x<4:
                if not self.find( "atrasospagamentos", matching=0.97, waiting_time=10000):
                    self.not_found("atrasospagamentos")
                self.click_relative(164, 27)
                self.type_up()
                self.enter()
                x=x+1
            
            
            x=0
            while x<3:
                if not self.find( "verificarchequesnolimite", matching=0.97, waiting_time=10000):
                    self.not_found("verificarchequesnolimite")
                self.click_relative(162, 23)
                self.type_down()
                self.enter()
                x=x+1
                
            x=0
            while x<3:
                if not self.find( "verificarchequesnolimite", matching=0.97, waiting_time=10000):
                    self.not_found("verificarchequesnolimite")
                self.click_relative(162, 23)
                self.type_up()
                self.enter()
                x=x+1
                
            
            if not self.find( "modochecagemfinanceira", matching=0.97, waiting_time=10000):
                self.not_found("modochecagemfinanceira")
            self.click_relative(165, 26)
            self.type_down()
            self.enter()
            if not self.find( "modochecagemfinanceira", matching=0.97, waiting_time=10000):
                self.not_found("modochecagemfinanceira")
            self.click_relative(165, 26)
            self.type_down()
            self.enter()
        
                        ####---ABA2 FINANCEIRO---####

            if not self.find( "aba2parametros", matching=0.97, waiting_time=10000):
                self.not_found("aba2parametros")
            self.click()
            
            if not self.find( "baixaarecebermultiempresas", matching=0.97, waiting_time=10000):
                self.not_found("baixaarecebermultiempresas")
            self.click_relative(160, 24)
            self.type_down()
            self.enter()
            if not self.find( "baixaarecebermultiempresas", matching=0.97, waiting_time=10000):
                self.not_found("baixaarecebermultiempresas")
            self.click_relative(160, 24)
            self.type_up()
            self.enter()
            
            x=0
            while x<3:
                if not self.find( "exportarobservacaonabaixa", matching=0.97, waiting_time=10000):
                    self.not_found("exportarobservacaonabaixa")
                self.click_relative(162, 27)
                self.type_up()
                self.enter()
                x=x+1
                
            y=0
            while y<3:
                if not self.find( "exportarobservacaonabaixa", matching=0.97, waiting_time=10000):
                    self.not_found("exportarobservacaonabaixa")
                self.click_relative(162, 27)
                self.type_down()
                self.enter()
                y=y+1    
            
            
            x=0
            while x<2:
                if not self.find( "exigenciaplanofinanceiro", matching=0.97, waiting_time=10000):
                    self.not_found("exigenciaplanofinanceiro")
                self.click_relative(163, 25)
                self.type_up()
                self.enter()
                x=x+1
                
            y=0
            while y<3:
                if not self.find( "exigenciaplanofinanceiro", matching=0.97, waiting_time=10000):
                    self.not_found("exigenciaplanofinanceiro")
                self.click_relative(163, 25)            
                self.type_down()
                y=y+1
            self.enter()
            
            
            x=0
            while x<2:
                if not self.find( "exigenciarateiocentrodecusto", matching=0.97, waiting_time=10000):
                    self.not_found("exigenciarateiocentrodecusto")
                self.click_relative(222, 21)
                self.type_up()
                self.enter()
                x=x+1
                
            x=0
            while x<5:
                if not self.find( "exigenciarateiocentrodecusto", matching=0.97, waiting_time=10000):
                    self.not_found("exigenciarateiocentrodecusto")
                self.click_relative(222, 21)
                self.type_down()
                self.enter()
                x=x+1
                
            x=0
            while x<3:
                 if not self.find( "exigenciarateiocentrodecusto", matching=0.97, waiting_time=10000):
                    self.not_found("exigenciarateiocentrodecusto")
                 self.click_relative(222, 21)
                 self.type_up()
                 self.enter()
                 x=x+1
                
            x=0
            while x<2:
                 if not self.find( "exigenciaclassificacao", matching=0.97, waiting_time=10000):
                     self.not_found("exigenciaclassificacao")
                 self.click_relative(163, 25)
                 self.type_up()
                 self.enter()
                 x=x+1
                 
            x=0
            while x<2:
                if not self.find( "exigenciaclassificacao", matching=0.97, waiting_time=10000):
                     self.not_found("exigenciaclassificacao")
                self.click_relative(163, 25)
                self.type_down()
                self.enter()
                x=x+1
            

            x=0
            while x<2:
                if not self.find( "exigencialocaldecobranca", matching=0.97, waiting_time=10000):
                    self.not_found("exigencialocaldecobranca")
                self.click_relative(162, 24)
                self.type_up()
                self.enter()
                x=x+1
                
            if not self.find( "exigencialocaldecobranca", matching=0.97, waiting_time=10000):
                    self.not_found("exigencialocaldecobranca")
            self.click_relative(162, 24)
            self.type_down()
            self.type_down()
            self.enter()
            
            x=0
            while x<2:
                if not self.find( "quandodiavencefds", matching=0.97, waiting_time=10000):
                    self.not_found("quandodiavencefds")
                self.click_relative(163, 25)
                self.type_down()
                self.enter()
                x=x+1
            
            if not self.find( "quandodiavencefds", matching=0.97, waiting_time=10000):
                self.not_found("quandodiavencefds")
            self.click_relative(163, 25)
            self.type_up()
            self.type_up()
            self.enter()
            
            x=0
            while x<4:
                if not self.find( "valordaparcelamenorqueminimo", matching=0.97, waiting_time=10000):
                     self.not_found("valordaparcelamenorqueminimo")
                self.click_relative(163, 26)
                self.type_down()
                self.enter()
                x=x+1
                 
            x=0
            while x<4:
                if not self.find( "valordaparcelamenorqueminimo", matching=0.97, waiting_time=10000):
                     self.not_found("valordaparcelamenorqueminimo")
                self.click_relative(163, 26)
                self.type_up() 
                self.enter()               
                x=x+1                   
    
            
            if not self.find( "somarcobrancabancariaavalor", matching=0.97, waiting_time=10000):
                self.not_found("somarcobrancabancariaavalor")
            self.click_relative(162, 23)
            self.type_up()
            self.enter()
            if not self.find( "somarcobrancabancariaavalor", matching=0.97, waiting_time=10000):
                self.not_found("somarcobrancabancariaavalor")
            self.click_relative(162, 23)
            self.type_down()
            self.enter()
            
            if not self.find( "operacaonabaixacheques", matching=0.97, waiting_time=10000):
                self.not_found("operacaonabaixacheques")
            self.click_relative(163, 26)
            self.type_down()
            self.enter()
            if not self.find( "operacaonabaixacheques", matching=0.97, waiting_time=10000):
                self.not_found("operacaonabaixacheques")
            self.click_relative(163, 26)
            self.type_up()
            self.enter()
            
            if not self.find( "tipocontabilizacaobaixa", matching=0.97, waiting_time=10000):
                self.not_found("tipocontabilizacaobaixa")
            self.click_relative(161, 24)
            self.type_down()
            self.enter()
            if not self.find( "tipocontabilizacaobaixa", matching=0.97, waiting_time=10000):
                self.not_found("tipocontabilizacaobaixa")
            self.click_relative(161, 24)
            self.type_up()
            self.enter()
            
            x=0
            while x < 2:
                if not self.find( "permitirdescontodurantebaixa", matching=0.97, waiting_time=10000):
                    self.not_found("permitirdescontodurantebaixa")
                self.click_relative(161, 24)
                self.type_down()
                self.enter()
                x=x+1
                
            x=0
            while x<3:
                if not self.find( "permitirdescontodurantebaixa", matching=0.97, waiting_time=10000):
                    self.not_found("permitirdescontodurantebaixa")
                self.click_relative(161, 24)
                self.type_up()
                x=x+1
            self.enter()
            
            if not self.find( "chequeemitidocamponominal", matching=0.97, waiting_time=10000):
                self.not_found("chequeemitidocamponominal")
            self.click_relative(159, 24)
            self.type_down()
            self.enter()
            if not self.find( "chequeemitidocamponominal", matching=0.97, waiting_time=10000):
                self.not_found("chequeemitidocamponominal")
            self.click_relative(159, 24)
            self.type_up()
            self.enter()
            
            if not self.find( "encontrodecontas", matching=0.97, waiting_time=10000):
                self.not_found("encontrodecontas")
            self.click_relative(164, 27)
            self.type_up()
            self.enter()
            if not self.find( "encontrodecontas", matching=0.97, waiting_time=10000):
                self.not_found("encontrodecontas")
            self.click_relative(164, 27)
            self.type_down()
            self.enter()
            
            
            
            x=0
            while x<2:
                if not self.find( "agrupartitulosfornecedores", matching=0.97, waiting_time=10000):
                    self.not_found("agrupartitulosfornecedores")
                self.click_relative(167, 24)
                self.type_down()
                self.enter()
                x=x+1
                
            x=0
            while x<3:
                if not self.find( "agrupartitulosfornecedores", matching=0.97, waiting_time=10000):
                    self.not_found("agrupartitulosfornecedores")
                self.click_relative(167, 24)
                self.type_up()
                x=x+1
            
            self.enter()
            
            if not self.find( "prazominimoconvenio", matching=0.97, waiting_time=10000):
                self.not_found("prazominimoconvenio")
            self.click_relative(99, 26)
            self.type_keys_with_interval(1,'123')
            self.enter()
            if not self.find( "prazominimoconvenio", matching=0.97, waiting_time=10000):
                self.not_found("prazominimoconvenio")
            self.click_relative(163, 23)
            self.type_keys_with_interval(1,'123')
            self.enter()
            
                            ####---REAJUSTES JUROS MORA E MULTA---####
                             
            self.enter()
            self.type_keys_with_interval(1,'123')
            if not self.find( "jurosdemora", matching=0.97, waiting_time=10000):
                self.not_found("jurosdemora")
            self.click_relative(167, 26)
            self.type_keys_with_interval(1,'123')
            self.enter()
            if not self.find( "tipodoreajustejurosdemora", matching=0.97, waiting_time=10000):
                self.not_found("tipodoreajustejurosdemora")
            self.click_relative(165, 27)
            self.type_down()
            self.enter()
            if not self.find( "tipodoreajustejurosdemora", matching=0.97, waiting_time=10000):
                self.not_found("tipodoreajustejurosdemora")
            self.click_relative(165, 27)
            self.type_up()
            self.enter()
            if not self.find( "tipocalculojuros1", matching=0.97, waiting_time=10000):
                self.not_found("tipocalculojuros1")
            self.click_relative(164, 25)           
            self.type_down()
            self.enter()
            if not self.find( "tipocalculojuros1", matching=0.97, waiting_time=10000):
                self.not_found("tipocalculojuros1")
            self.click_relative(164, 25)
            self.type_up()
            self.enter()
            self.type_keys_with_interval(1,'123')
            if not self.find( "multa", matching=0.97, waiting_time=10000):
                self.not_found("multa")
            self.click_relative(161, 24)
            self.type_keys_with_interval(1,'123')
            self.enter()
            if not self.find( "tipodoreajustemulta", matching=0.97, waiting_time=10000):
                self.not_found("tipodoreajustemulta")
            self.click_relative(163, 23)
            self.type_down()
            self.enter()
            if not self.find( "tipodoreajustemulta", matching=0.97, waiting_time=10000):
                self.not_found("tipodoreajustemulta")
            self.click_relative(163, 23)
            self.type_up()
            self.enter()
            self.type_keys_with_interval(1,'123')
            if not self.find( "diascarenciareajuste1", matching=0.97, waiting_time=10000):
                self.not_found("diascarenciareajuste1")
            self.click_relative(163, 23)                        
            self.type_keys_with_interval(1,'123')
            self.enter()
            self.enter()
            self.type_keys_with_interval(1,'123')
            if not self.find( "diastoleranciavencimentoparcial", matching=0.97, waiting_time=10000):
                self.not_found("diastoleranciavencimentoparcial")
            self.click_relative(165, 25)
            self.type_keys_with_interval(1,'123')
            self.enter()
            self.enter()
            self.type_keys_with_interval(1,'123')
            if not self.find( "diastoleranciaatrasobalcao", matching=0.97, waiting_time=10000):
                self.not_found("diastoleranciaatrasobalcao")
            self.click_relative(165, 25)
            self.type_keys_with_interval(1,'123')
            self.enter()
            
                        ####---DESCONTO DE RECEBIMENTOS---####
    
            self.enter()
            self.type_keys_with_interval(1,'123')
            if not self.find( "desconto", matching=0.97, waiting_time=10000):
                self.not_found("desconto")
            self.click_relative(162, 23)
            self.type_keys_with_interval(1,'123')
            self.enter()
            
            x=0
            while x<3:
                if not self.find( "tipododesconto", matching=0.97, waiting_time=10000):
                    self.not_found("tipododesconto")
                self.click_relative(162, 25)
                self.type_down()
                self.enter()
                x=x+1
                
            x=0
            while x<5:
                if not self.find( "tipododesconto", matching=0.97, waiting_time=10000):
                    self.not_found("tipododesconto")
                self.click_relative(162, 25)
                self.type_up()
                x=x+1
            
            self.enter()
            
            if not self.find( "tipocalculoquevaidarcerto", matching=0.97, waiting_time=10000):
                self.not_found("tipocalculoquevaidarcerto")
            self.click_relative(654, 43)           
            self.type_down()
            self.enter()
            if not self.find( "tipocalculoquevaidarcerto", matching=0.97, waiting_time=10000):
                self.not_found("tipocalculoquevaidarcerto")
            self.click_relative(654, 43) 
            self.type_up()
            self.enter()            
            self.type_keys_with_interval(1,'123')
            if not self.find( "diascarenciareajuste", matching=0.97, waiting_time=10000):
                self.not_found("diascarenciareajuste")
            self.click_relative(163, 25)
            self.type_keys_with_interval(1,'123')
            self.enter()
            
            if not self.find( "valorbordero", matching=0.97, waiting_time=10000):
                self.not_found("valorbordero")
            self.click_relative(164, 24)
            self.type_down()
            self.enter()
            if not self.find( "valorbordero", matching=0.97, waiting_time=10000):
                self.not_found("valorbordero")
            self.click_relative(164, 24)
            self.type_up()
            self.enter()
            
                            ####---ABA 3 GESTAO ADM/VAREJO---####
                             
            if not self.find( "aba3paemp", matching=0.97, waiting_time=10000):
                self.not_found("aba3paemp")
            self.click()
            
            x=0
            while x<8:
                if not self.find( "tipodametadosvendedores", matching=0.97, waiting_time=10000):
                    self.not_found("tipodametadosvendedores")
                self.click_relative(211, 24)
                self.type_down()
                self.enter()
                x=x+1
                
            x=0
            while x<8:
                if not self.find( "tipodametadosvendedores", matching=0.97, waiting_time=10000):
                    self.not_found("tipodametadosvendedores")
                self.click_relative(211, 24)
                self.type_up()
                self.enter()
                x=x+1

            
            if not self.find( "calculocomissaoitens", matching=0.97, waiting_time=10000):
                self.not_found("calculocomissaoitens")
            self.click_relative(216, 25)
            self.type_down()
            self.enter()
            if not self.find( "calculocomissaoitens", matching=0.97, waiting_time=10000):
                self.not_found("calculocomissaoitens")
            self.click_relative(216, 25)
            self.type_up()
            self.enter()
            
            
            x=0
            while x<6:
                if not self.find( "tipolimiteparacompradores", matching=0.97, waiting_time=10000):
                    self.not_found("tipolimiteparacompradores")               
                self.click_relative(215, 27)
                self.type_down()
                self.enter()
                x=x+1
                
                
            x=0
            while x<5:
                if not self.find( "tipolimiteparacompradores", matching=0.97, waiting_time=10000):
                    self.not_found("tipolimiteparacompradores")
                self.click_relative(215, 27)
                self.type_up()
                self.enter()
                x=x+1    
                
             
            x=0
            while x<4:
                 if not self.find( "empresametaselimite", matching=0.97, waiting_time=10000):
                     self.not_found("empresametaselimite")
                 self.click_relative(214, 27)
                 self.type_down()
                 self.enter()
                 x=x+1
                 
            x=0
            while x<4:
                if not self.find( "empresametaselimite", matching=0.97, waiting_time=10000):
                    self.not_found("empresametaselimite")
                self.click_relative(214, 27)
                self.type_up()
                self.enter()
                x=x+1
             
            self.enter()
                 
                             ####---GERAIS---####
                              
            if not self.find( "recalculocustomediotravaperiodo", matching=0.97, waiting_time=10000):
                self.not_found("recalculocustomediotravaperiodo")
            self.click_relative(210, 24)
            self.type_up()
            self.enter()
            if not self.find( "recalculocustomediotravaperiodo", matching=0.97, waiting_time=10000):
                self.not_found("recalculocustomediotravaperiodo")
            self.click_relative(210, 24)
            self.type_down()
            self.enter()
            
            if not self.find( "calcularprecosnoprelancamento", matching=0.97, waiting_time=10000):
                self.not_found("calcularprecosnoprelancamento")
            self.click_relative(210, 25)
            self.type_up()
            self.enter()
            if not self.find( "calcularprecosnoprelancamento", matching=0.97, waiting_time=10000):
                self.not_found("calcularprecosnoprelancamento")
            self.click_relative(210, 25)
            self.type_down()
            self.enter()
            
            if not self.find( "abrirteladecalculodepreco", matching=0.97, waiting_time=10000):
                self.not_found("abrirteladecalculodepreco")
            self.click_relative(212, 22)
            self.type_up()
            self.enter()
            if not self.find( "abrirteladecalculodepreco", matching=0.97, waiting_time=10000):
                self.not_found("abrirteladecalculodepreco")
            self.click_relative(212, 22)
            self.type_down()
            self.enter()
            
            if not self.find( "adicionarfornecedorepreconositens", matching=0.97, waiting_time=10000):
                self.not_found("adicionarfornecedorepreconositens")
            self.click_relative(210, 23)
            self.type_up()
            self.enter()
            if not self.find( "adicionarfornecedorepreconositens", matching=0.97, waiting_time=10000):
                self.not_found("adicionarfornecedorepreconositens")
            self.click_relative(210, 23)
            self.type_down()
            self.enter()
            
            x=0
            while x<9:
                if not self.find( "situacaofiscalnaoencontrada", matching=0.97, waiting_time=10000):
                    self.not_found("situacaofiscalnaoencontrada")
                self.click_relative(212, 27)
                self.type_down()
                self.enter()
                x=x+1
                
            x=0
            while x<9:
                if not self.find( "situacaofiscalnaoencontrada", matching=0.97, waiting_time=10000):
                    self.not_found("situacaofiscalnaoencontrada")
                self.click_relative(212, 27)
                self.type_up()
                self.enter()
                x=x+1
                
            if not self.find( "codificarocusto", matching=0.97, waiting_time=10000):
                self.not_found("codificarocusto")
            self.click_relative(211, 26)
            self.type_up()
            self.enter()
            if not self.find( "codificarocusto", matching=0.97, waiting_time=10000):
                self.not_found("codificarocusto")
            self.click_relative(211, 26)
            self.type_down()
            self.enter()
            
            if not self.find( "codificacaodocusto", matching=0.97, waiting_time=10000):
                self.not_found("codificacaodocusto")
            self.click_relative(29, 26)
            self.type_keys_with_interval(1,'te12!@')
            
            if not self.find( "letraduplicidade", matching=0.97, waiting_time=10000):
                self.not_found("letraduplicidade")
            self.click_relative(41, 27)
            self.type_keys_with_interval(1,'t')
            self.enter()
            if not self.find( "letraduplicidade", matching=0.97, waiting_time=10000):
                self.not_found("letraduplicidade")
            self.click_relative(41, 27)
            self.backspace()
            self.type_keys_with_interval(1,'1')
            self.enter()
            if not self.find( "letraduplicidade", matching=0.97, waiting_time=10000):
                self.not_found("letraduplicidade")
            self.click_relative(41, 27)
            self.backspace()
            self.type_keys_with_interval(1,'!')
            self.enter()
            
            x=0
            while x<6:
                if not self.find( "duplicidadeesmovtoitens", matching=0.97, waiting_time=10000):
                    self.not_found("duplicidadeesmovtoitens")
                self.click_relative(212, 23)
                self.type_down()
                self.enter()
                x=x+1
            x=0
            while x<6:
                if not self.find( "duplicidadeesmovtoitens", matching=0.97, waiting_time=10000):
                    self.not_found("duplicidadeesmovtoitens")
                self.click_relative(212, 23)
                self.type_up()
                self.enter()
                x=x+1
             
                             ####---ITENS---####
                              
            x=0
            while x<6:
                if not self.find( "custodoitemaexibirnaconsulta", matching=0.97, waiting_time=10000):
                    self.not_found("custodoitemaexibirnaconsulta")
                self.click_relative(210, 25)
                self.type_down()
                self.enter()
                x=x+1
                
            x=0
            while x<6:
                if not self.find( "custodoitemaexibirnaconsulta", matching=0.97, waiting_time=10000):
                    self.not_found("custodoitemaexibirnaconsulta")
                self.click_relative(210, 25)
                self.type_up()
                self.enter()
                x=x+1
             
            if not self.find( "permitecadastraritens", matching=0.97, waiting_time=10000):
                self.not_found("permitecadastraritens")
            self.click_relative(210, 24)
            self.type_up()
            self.enter()
            if not self.find( "permitecadastraritens", matching=0.97, waiting_time=10000):
                self.not_found("permitecadastraritens")
            self.click_relative(210, 24)
            self.type_down()
            self.enter()
             
            x=0
            while x<2:
                if not self.find( "exigenciadocentrodecusto", matching=0.97, waiting_time=10000):
                    self.not_found("exigenciadocentrodecusto")
                self.click_relative(212, 25)
                self.type_down()
                self.enter()
                x=x+1
                
            x=0
            while x<2:
                if not self.find( "exigenciadocentrodecusto", matching=0.97, waiting_time=10000):
                    self.not_found("exigenciadocentrodecusto")
                self.click_relative(212, 25)
                self.type_up()
                self.enter()
                x=x+1
                
            x=0
            while x<4:
                if not self.find( "tipodocodigodebarrasdoitem", matching=0.97, waiting_time=10000):
                    self.not_found("tipodocodigodebarrasdoitem")
                self.click_relative(213, 27)
                self.type_down()
                self.enter()
                x=x+1
                
            x=0
            while x<4:
                if not self.find( "tipodocodigodebarrasdoitem", matching=0.97, waiting_time=10000):
                    self.not_found("tipodocodigodebarrasdoitem")
                self.click_relative(213, 27)
                self.type_up()
                self.enter()
                x=x+1
             
                            ####---MOVIMENTOS---####

            if not self.find( "entradadeitenscontabilizacao", matching=0.97, waiting_time=10000):
                self.not_found("entradadeitenscontabilizacao")
            self.click_relative(211, 23)
            self.type_up()
            self.enter()
            if not self.find( "entradadeitenscontabilizacao", matching=0.97, waiting_time=10000):
                 self.not_found("entradadeitenscontabilizacao")
            self.click_relative(211, 23)
            self.type_down()
            self.enter()
             
            if not self.find( "permiteinclusaodeitensnaimportacao", matching=0.97, waiting_time=10000):
                 self.not_found("permiteinclusaodeitensnaimportacao")
            self.click_relative(210, 23)
            self.type_up()
            self.enter()
            if not self.find( "permiteinclusaodeitensnaimportacao", matching=0.97, waiting_time=10000):
                 self.not_found("permiteinclusaodeitensnaimportacao")
            self.click_relative(210, 23)
            self.type_down()
            self.enter()
             
            x=0
            while x<4:
                if not self.find( "manutencaodeprecosabaixo", matching=0.97, waiting_time=10000):
                    self.not_found("manutencaodeprecosabaixo")
                self.click_relative(211, 27)
                self.type_down()
                self.enter()
                x=x+1
                 
            x=0
            while x<3:
                if not self.find( "manutencaodeprecosabaixo", matching=0.97, waiting_time=10000):
                    self.not_found("manutencaodeprecosabaixo")
                self.click_relative(211, 27)
                self.type_up()
                self.enter()
                x=x+1
             
            self.type_keys_with_interval(1,'123')
            self.enter()
            if not self.find( "percentualdetolerancia", matching=0.97, waiting_time=10000):
                self.not_found("percentualdetolerancia")
            self.click_relative(212, 25)
            self.type_keys_with_interval(1,'123')
            self.enter()
             
            if not self.find( "valoresdemovimentacao", matching=0.97, waiting_time=10000):
                self.not_found("valoresdemovimentacao")
            self.click_relative(212, 26)
            self.type_down()
            self.enter()
            if not self.find( "valoresdemovimentacao", matching=0.97, waiting_time=10000):
                self.not_found("valoresdemovimentacao")
            self.click_relative(212, 26)
            self.type_up()
            self.enter()
             
            if not self.find( "trensferenciadeitensentreempresa", matching=0.97, waiting_time=10000):
                self.not_found("trensferenciadeitensentreempresa")
            self.click_relative(208, 26)
            self.type_down()
            self.enter()
            if not self.find( "trensferenciadeitensentreempresa", matching=0.97, waiting_time=10000):
                self.not_found("trensferenciadeitensentreempresa")
            self.click_relative(208, 26)
            self.type_up()
            self.enter()
             
            if not self.find( "geratransferencialiberada", matching=0.97, waiting_time=10000):
                self.not_found("geratransferencialiberada")
            self.click_relative(210, 26)
            self.type_down()
            self.enter()
            if not self.find( "geratransferencialiberada", matching=0.97, waiting_time=10000):
                self.not_found("geratransferencialiberada")
            self.click_relative(210, 26)
            self.type_up()
            self.enter()
             
            if not self.find( "exigirlancamentocentrocustos", matching=0.97, waiting_time=10000):
                self.not_found("exigirlancamentocentrocustos")
            self.click_relative(208, 25)
            self.type_up()
            self.enter()
            if not self.find( "exigirlancamentocentrocustos", matching=0.97, waiting_time=10000):
                self.not_found("exigirlancamentocentrocustos")
            self.click_relative(208, 25)
            self.type_down()
            self.enter()
             
            if not self.find( "bloquearliberacaomovitens", matching=0.97, waiting_time=10000):
                self.not_found("bloquearliberacaomovitens")
            self.click_relative(258, 25)
            self.type_down()
            self.enter()
            if not self.find( "bloquearliberacaomovitens", matching=0.97, waiting_time=10000):
                self.not_found("bloquearliberacaomovitens")
            self.click_relative(258, 25)
            self.type_down()
            self.enter()
            if not self.find( "bloquearliberacaomovitens", matching=0.97, waiting_time=10000):
                self.not_found("bloquearliberacaomovitens")
            self.click_relative(258, 25)
            self.type_up()
            self.enter()
            
                             ####---PERCENTUAIS E ARREDONDAMENTOS---####     

            
            if not self.find( "numerocasasdecimaiscustos", matching=0.97, waiting_time=10000):
                self.not_found("numerocasasdecimaiscustos")
            self.double_click_relative(122, 22)            
            if not self.find( "numerocasasdecimaiscustos", matching=0.97, waiting_time=10000):
                self.not_found("numerocasasdecimaiscustos")
            self.click_relative(121, 31)    
            self.backspace()
            self.type_keys_with_interval(1,'1')
            
            if not self.find( "ncasasdecimaisprecovenda1", matching=0.97, waiting_time=10000):
                self.not_found("ncasasdecimaisprecovenda1")
            self.double_click_relative(122, 19)
            if not self.find( "ncasasdecimaisprecovenda1", matching=0.97, waiting_time=10000):
                self.not_found("ncasasdecimaisprecovenda1")
            self.click_relative(123, 29)            
            self.backspace()
            self.backspace()
            self.type_keys_with_interval(1,'1') 
            if not self.find( "numerocasasdecimaisquantidade", matching=0.97, waiting_time=10000):
                self.not_found("numerocasasdecimaisquantidade")
            self.double_click_relative(125, 23)
            if not self.find( "numerocasasdecimaisquantidade", matching=0.97, waiting_time=10000):
                self.not_found("numerocasasdecimaisquantidade")
            self.click_relative(123, 30)             
            self.backspace()
            self.backspace()
            self.type_keys_with_interval(1,'1')            
            self.enter()
            self.type_keys_with_interval(1,'123')
            if not self.find( "calculocustooperacional", matching=0.97, waiting_time=10000):
                self.not_found("calculocustooperacional")
            self.click_relative(15, 25)             
            self.type_keys_with_interval(1,'123')
            self.enter()
            self.enter()
            self.type_keys_with_interval(1,'123')
            if not self.find( "calculopis", matching=0.97, waiting_time=10000):
                self.not_found("calculopis")
            self.click_relative(-1, 27)
            self.type_keys_with_interval(1,'123')
            self.enter()
            self.enter()
            self.type_keys_with_interval(1,'123')
            if not self.find( "calculocofins", matching=0.97, waiting_time=10000):
                self.not_found("calculocofins")
            self.click_relative(2, 25)
            self.type_keys_with_interval(1,'123')
            self.enter()
            self.enter()
            self.type_keys_with_interval(1,'123')
            if not self.find( "calculodebitoicms", matching=0.97, waiting_time=10000):
                self.not_found("calculodebitoicms")
            self.click_relative(-1, 25)
            self.type_keys_with_interval(1,'123')
            self.enter()
            self.enter()
            self.type_keys_with_interval(1,'123')
            if not self.find( "calculoprecoscomissao", matching=0.97, waiting_time=10000):
                self.not_found("calculoprecoscomissao")
            self.click_relative(125, 26)           
            self.type_keys_with_interval(1,'123')
            self.enter()
            if not self.find( "origempiscofins", matching=0.97, waiting_time=10000):
                self.not_found("origempiscofins")
            self.click_relative(125, 25)
            self.type_down()
            self.enter()
            if not self.find( "origempiscofins", matching=0.97, waiting_time=10000):
                self.not_found("origempiscofins")
            self.click_relative(125, 25)
            self.type_up()
            self.enter()
            self.type_keys_with_interval(1,'123')
            if not self.find( "curvaA", matching=0.97, waiting_time=10000):
                self.not_found("curvaA")
            self.click_relative(122, 22)
            self.type_keys_with_interval(1,'20')
            self.enter()
            self.enter()
            self.type_keys_with_interval(1,'123')
            if not self.find( "curvaB", matching=0.97, waiting_time=10000):
                self.not_found("curvaB")
            self.click_relative(125, 25)
            self.type_keys_with_interval(1,'20')
            self.enter()
            self.enter()
            if not self.find( "curvaC", matching=0.97, waiting_time=10000):
                self.not_found("curvaC")
            self.click_relative(124, 27)
            self.type_keys_with_interval(1,'60')
            self.enter()
            
                            ####---ABAIXANDO TELA---####
                             
            if not self.find( "abaixatelaparametrosempresa", matching=0.97, waiting_time=10000):
                self.not_found("abaixatelaparametrosempresa")
            self.click()
            
            x=0
            while x<7:
                if not self.find( "abaixartelamarcadaparametrosempresa", matching=0.97, waiting_time=10000):
                    self.not_found("abaixartelamarcadaparametrosempresa")
                self.double_click()
                x=x+1
                
                            ####---VENDAS---####
                             
            if not self.find( "infopadraofrete", matching=0.97, waiting_time=10000):
                self.not_found("infopadraofrete")
            self.click_relative(213, 25)
            self.type_up()
            self.enter()
            
            x=0
            while x<5:
                if not self.find( "infopadraofrete", matching=0.97, waiting_time=10000):
                    self.not_found("infopadraofrete")
                self.click_relative(213, 25)
                self.type_down()
                self.enter()
                x=x+1
                 
            x=0
            while x<4:
                if not self.find( "infopadraofrete", matching=0.97, waiting_time=10000):
                        self.not_found("infopadraofrete")
                self.click_relative(213, 25)
                self.type_up()
                self.enter()
                x=x+1
             
            if not self.find( "validarsituacaoclientegerarpedido", matching=0.97, waiting_time=10000):
                self.not_found("validarsituacaoclientegerarpedido")
            self.click_relative(213, 25)
            self.type_down()
            self.enter()
            if not self.find( "validarsituacaoclientegerarpedido", matching=0.97, waiting_time=10000):
                self.not_found("validarsituacaoclientegerarpedido")
            self.click_relative(213, 25)
            self.type_down()
            self.enter()
            if not self.find( "validarsituacaoclientegerarpedido", matching=0.97, waiting_time=10000):
                self.not_found("validarsituacaoclientegerarpedido")
            self.click_relative(213, 25)
            self.type_up()
            self.enter() 
             
            if not self.find( "reservarestoqueorcamento", matching=0.97, waiting_time=10000):
                self.not_found("reservarestoqueorcamento")
            self.click_relative(212, 24)
            self.type_down()
            self.enter() 
            if not self.find( "reservarestoqueorcamento", matching=0.97, waiting_time=10000):
                self.not_found("reservarestoqueorcamento")
            self.click_relative(212, 24)
            self.type_down()
            self.enter()
            if not self.find( "reservarestoqueorcamento", matching=0.97, waiting_time=10000):
                self.not_found("reservarestoqueorcamento")
            self.click_relative(212, 24)
            self.type_up()
            self.enter()
            
            x=0
            while x<5:
                if not self.find( "custoparacalculodasmargens", matching=0.97, waiting_time=10000):
                    self.not_found("custoparacalculodasmargens")
                self.click_relative(215, 24)
                self.type_down()
                self.enter()
                x=x+1
            x=0
            while x<5:
                if not self.find( "custoparacalculodasmargens", matching=0.97, waiting_time=10000):
                    self.not_found("custoparacalculodasmargens")
                self.click_relative(215, 24)
                self.type_up()
                self.enter()
                x=x+1 
            
            x=0
            while x<2:
                if not self.find( "utilizadataentregavendas", matching=0.97, waiting_time=10000):
                    self.not_found("utilizadataentregavendas")
                self.click_relative(214, 27)
                self.type_down()
                self.enter()
                x=x+1
            x=0
            while x<2:
                if not self.find( "utilizadataentregavendas", matching=0.97, waiting_time=10000):
                    self.not_found("utilizadataentregavendas")
                self.click_relative(214, 27)
                self.type_up()
                self.enter()
                x=x+1    
            x=0
            while x<2:
                if not self.find( "lancaritenssemdataentrega", matching=0.97, waiting_time=10000):
                    self.not_found("lancaritenssemdataentrega")
                self.click_relative(210, 25)
                self.type_down()
                self.enter()
                x=x+1
            x=0
            while x<2:
                if not self.find( "lancaritenssemdataentrega", matching=0.97, waiting_time=10000):
                    self.not_found("lancaritenssemdataentrega")
                self.click_relative(210, 25)
                self.type_up()
                self.enter()
                x=x+1     
            x=0
            while x<2:
                if not self.find( "calcularquantidadeparaconfirmacao", matching=0.97, waiting_time=10000):
                    self.not_found("calcularquantidadeparaconfirmacao")
                self.click_relative(215, 24)
                self.type_down()
                self.enter()
                x=x+1 
            x=0
            while x<2:
                if not self.find( "calcularquantidadeparaconfirmacao", matching=0.97, waiting_time=10000):
                    self.not_found("calcularquantidadeparaconfirmacao")
                self.click_relative(215, 24)
                self.type_up
                ()
                self.enter()
                x=x+1
             
                            ####---ABA 4 VENDAS---####

            if not self.find( "aba4vendasparametrosempresa", matching=0.97, waiting_time=10000):
                self.not_found("aba4vendasparametrosempresa")
            self.click()
            
                            ####---SUBIR TELA---####
            
            if not self.find( "subirtelaparametrosempresa", matching=0.97, waiting_time=10000):
                self.not_found("subirtelaparametrosempresa")
            self.click()
            
            x=0
            while x<5:
                if not self.find( "subirtelaparametrosempresa2", matching=0.97, waiting_time=10000):
                    self.not_found("subirtelaparametrosempresa2")
                self.click()
                x=x+1
            
                            ####---CONFIGURACOES---####
            
            if not self.find( "informarcomissao", matching=0.97, waiting_time=10000):
                self.not_found("informarcomissao")
            self.click_relative(162, 27)
            self.type_up()
            self.enter()
                
            x=0
            while x<3:
                if not self.find( "informarcomissao", matching=0.97, waiting_time=10000):
                    self.not_found("informarcomissao")
                self.click_relative(162, 27)
                self.type_down()
                self.enter()
                x=x+1
                
            x=0
            while x<2:
                if not self.find( "informarcomissao", matching=0.97, waiting_time=10000):
                    self.not_found("informarcomissao")
                self.click_relative(162, 27)
                self.type_up()
                self.enter()
                x=x+1
                
            if not self.find( "lotedeitensnospedidosdevenda", matching=0.97, waiting_time=10000):
               self.not_found("lotedeitensnospedidosdevenda")
            self.click_relative(162, 27)
            self.type_up()
            self.enter()
            if not self.find( "lotedeitensnospedidosdevenda", matching=0.97, waiting_time=10000):
               self.not_found("lotedeitensnospedidosdevenda")
            self.click_relative(162, 27)
            self.type_down()
            self.enter()
           
            if not self.find( "saldodopedidonanfdesaida", matching=0.97, waiting_time=10000):
               self.not_found("saldodopedidonanfdesaida")
            self.click_relative(163, 27)
            self.type_up()
            self.enter()
            if not self.find( "saldodopedidonanfdesaida", matching=0.97, waiting_time=10000):
               self.not_found("saldodopedidonanfdesaida")
            self.click_relative(163, 27)
            self.type_down()
            self.enter()
           
            x=0
            while x<6:
               if not self.find( "senhamargemminimavendas", matching=0.97, waiting_time=10000):
                   self.not_found("senhamargemminimavendas")
               self.click_relative(162, 28)
               self.type_down()
               self.enter()
               x=x+1
            x=0
            while x<6:
               if not self.find( "senhamargemminimavendas", matching=0.97, waiting_time=10000):
                   self.not_found("senhamargemminimavendas")
               self.click_relative(162, 28)
               self.type_up()
               self.enter()
               x=x+1
               
            self.type_keys_with_interval(1,'123')
            self.enter()
            
            if not self.find( "margemminimavendas", matching=0.97, waiting_time=10000):
                self.not_found("margemminimavendas")
            self.click_relative(162, 26)
            self.type_keys_with_interval(1,'123')
            self.enter()
            
            x=0
            while x<2:
                if not self.find( "custoparachecagemdamargemminima", matching=0.97, waiting_time=10000):
                    self.not_found("custoparachecagemdamargemminima")
                self.click_relative(159, 27)
                self.type_up()
                self.enter()
                x=x+1
                
            x=0
            while x<5:
                if not self.find( "custoparachecagemdamargemminima", matching=0.97, waiting_time=10000):
                    self.not_found("custoparachecagemdamargemminima")
                self.click_relative(159, 27)
                self.type_down()
                self.enter()
                x=x+1
                
            if not self.find( "aoimprimirvendasexibir", matching=0.97, waiting_time=10000):
                self.not_found("aoimprimirvendasexibir")
            self.click_relative(161, 25)
            self.type_up()
            self.enter()
            
            x=0
            while x<23:
                if not self.find( "aoimprimirvendasexibir", matching=0.97, waiting_time=10000):
                    self.not_found("aoimprimirvendasexibir")
                self.click_relative(161, 25)
                self.type_down()
                self.enter()
                x=x+1
                
            x=0
            while x<4:
                if not self.find( "itemsemestoquepedidopara", matching=0.97, waiting_time=10000):
                    self.not_found("itemsemestoquepedidopara")
                self.click_relative(163, 29)
                self.type_down()    
                self.enter()
                x=x+1
                
            x=0
            while x<5:
                if not self.find( "ordemdeimpressaopedidosenf", matching=0.97, waiting_time=10000):
                    self.not_found("ordemdeimpressaopedidosenf")
                self.click_relative(159, 26)
                self.type_down()
                self.enter()
                x=x+1
                
            x=0
            while x<3:
                if not self.find( "cdgimprimirpedidos", matching=0.97, waiting_time=10000):
                    self.not_found("cdgimprimirpedidos")
                self.click_relative(163, 26)
                self.type_down()
                self.enter()
                x=x+1
                
            x=0
            while x<3:
                if not self.find( "cdgimprimirvendasbalcaoedev", matching=0.97, waiting_time=10000):
                    self.not_found("cdgimprimirvendasbalcaoedev")
                self.click_relative(123, 23)
                self.type_down()
                self.enter()
                x=x+1
                
            x=0
            while x<3:
                if not self.find( "cdgimprimircondicionais", matching=0.97, waiting_time=10000):
                    self.not_found("cdgimprimircondicionais")
                self.click_relative(120, 26)
                self.type_down()
                self.enter()
                x=x+1
                
            if not self.find( "linhasimpressaoformulariovendas", matching=0.97, waiting_time=10000):
                self.not_found("linhasimpressaoformulariovendas")
            self.double_click_relative(159, 20)
            if not self.find( "linhasimpressaoformulariovendas2", matching=0.97, waiting_time=10000):
                self.not_found("linhasimpressaoformulariovendas2")
            self.click_relative(160, 30)
            self.backspace()
            self.backspace()
            self.type_keys_with_interval(1,'1')
            self.enter()
            
            if not self.find( "ondeimprimironomedovendedor", matching=0.97, waiting_time=10000):
                self.not_found("ondeimprimironomedovendedor")
            self.click_relative(161, 27)
            self.type_up()
            self.enter()
            
            x=0
            while x<11:
                if not self.find( "ondeimprimironomedovendedor", matching=0.97, waiting_time=10000):
                    self.not_found("ondeimprimironomedovendedor")
                self.click_relative(161, 27)
                self.type_down()
                self.enter()
                x=x+1
                
            if not self.find( "mascaranrocontrole", matching=0.97, waiting_time=10000):
                self.not_found("mascaranrocontrole")
            self.click_relative(162, 27)
            self.type_down()
            self.enter()
            
            if not self.find( "vendaitemsemestoque", matching=0.97, waiting_time=10000):
                self.not_found("vendaitemsemestoque")
            self.click_relative(161, 24)
            self.type_up()
            self.enter()
            if not self.find( "vendaitemsemestoque", matching=0.97, waiting_time=10000):
                self.not_found("vendaitemsemestoque")
            self.click_relative(161, 24)
            self.type_down()
            self.enter()        
             
            x=0
            while x<4:
                if not self.find( "lancamentoitememduplicidade", matching=0.97, waiting_time=10000):
                    self.not_found("lancamentoitememduplicidade")
                self.click_relative(162, 28)
                self.type_down()
                self.enter()
                x=x+1
                
            if not self.find( "itenscomtabeladopcalc", matching=0.97, waiting_time=10000):
                self.not_found("itenscomtabeladopcalc")
            self.click_relative(165, 28)
            self.type_down()
            self.enter()
            if not self.find( "itenscomtabeladopcalc", matching=0.97, waiting_time=10000):
                self.not_found("itenscomtabeladopcalc")
            self.click_relative(165, 28)
            self.type_up()
            self.enter()
            
            x=0
            while x<3:
                if not self.find( "exigenciadotransportadornavenda", matching=0.97, waiting_time=10000):
                    self.not_found("exigenciadotransportadornavenda")
                self.click_relative(165, 27)
                self.type_down()
                self.enter()
                x=x+1
                
            x=0
            while x<2:
                if not self.find( "exigenciadeclassificacao", matching=0.97, waiting_time=10000):
                    self.not_found("exigenciadeclassificacao")
                self.click_relative(162, 25)
                self.type_up()
                self.enter()
                x=x+1
                
            if not self.find( "exigenciadovendedor", matching=0.97, waiting_time=10000):
                self.not_found("exigenciadovendedor")
            self.click_relative(162, 27)
            self.type_up()
            self.enter()
            if not self.find( "exigenciadovendedor", matching=0.97, waiting_time=10000):
                self.not_found("exigenciadovendedor")
            self.click_relative(162, 27)
            self.type_down()
            self.enter()
            
            x=0
            while x<4:
                if not self.find( "margemminimavendasbalcao", matching=0.97, waiting_time=10000):
                    self.not_found("margemminimavendasbalcao")
                self.click_relative(163, 25)
                self.type_up()
                self.enter()
                x=x+1
                
            if not self.find( "validarestoquedescontospedido", matching=0.97, waiting_time=10000):
               self.not_found("validarestoquedescontospedido")
            self.click_relative(162, 29)
            self.type_down()
            self.enter()  
            if not self.find( "validarestoquedescontospedido", matching=0.97, waiting_time=10000):
               self.not_found("validarestoquedescontospedido")
            self.click_relative(162, 29)
            self.type_up()
            self.enter()
            
            if not self.find( "capturapeso", matching=0.97, waiting_time=10000):
               self.not_found("capturapeso")
            self.click_relative(163, 27)
            self.type_up()
            self.enter()
            if not self.find( "capturapeso", matching=0.97, waiting_time=10000):
               self.not_found("capturapeso")
            self.click_relative(163, 27)
            self.type_down()
            self.enter() 
                 
            if not self.find( "planoprecoaotrocarcliente", matching=0.97, waiting_time=10000):
                self.not_found("planoprecoaotrocarcliente")
            self.click_relative(163, 26)
            self.type_up()
            self.enter()
            if not self.find( "planoprecoaotrocarcliente", matching=0.97, waiting_time=10000):
                self.not_found("planoprecoaotrocarcliente")
            self.click_relative(163, 26)
            self.type_down()
            self.enter() 
             
            if not self.find( "ordemdeservicoopcoes", matching=0.97, waiting_time=10000):
                self.not_found("ordemdeservicoopcoes")
            self.click_relative(161, 25)
            self.type_down()
            self.enter()
            if not self.find( "ordemdeservicoopcoes", matching=0.97, waiting_time=10000):
                self.not_found("ordemdeservicoopcoes")
            self.click_relative(161, 25)
            self.type_down()
            self.enter()
            if not self.find( "ordemdeservicoopcoes", matching=0.97, waiting_time=10000):
                self.not_found("ordemdeservicoopcoes")
            self.click_relative(161, 25)
            self.type_down()
            self.enter()
            
            if not self.find( "alteracaodovendedor", matching=0.97, waiting_time=10000):
                self.not_found("alteracaodovendedor")
            self.click_relative(164, 25)
            self.type_down()
            self.enter() 
            if not self.find( "alteracaodovendedor", matching=0.97, waiting_time=10000):
                self.not_found("alteracaodovendedor")
            self.click_relative(164, 25)
            self.type_up()
            self.enter()
            
            if not self.find( "mostrarautomitensagregados", matching=0.97, waiting_time=10000):
                self.not_found("mostrarautomitensagregados")
            self.click_relative(162, 24)
            self.type_down()
            self.enter()
            if not self.find( "mostrarautomitensagregados", matching=0.97, waiting_time=10000):
                self.not_found("mostrarautomitensagregados")
            self.click_relative(162, 24)
            self.type_up()
            self.enter()
            
            if not self.find( "conferenciarecuperarvenda", matching=0.97, waiting_time=10000):
                self.not_found("conferenciarecuperarvenda")
            self.click_relative(164, 23)
            self.type_down()
            self.enter()
            if not self.find( "conferenciarecuperarvenda", matching=0.97, waiting_time=10000):
                self.not_found("conferenciarecuperarvenda")
            self.click_relative(164, 23)
            self.type_up()
            self.enter()
            
            if not self.find( "vendapdvfechapedidoimportado", matching=0.97, waiting_time=10000):
                self.not_found("vendapdvfechapedidoimportado")
            self.click_relative(161, 26)
            self.type_down()
            self.enter()
            if not self.find( "vendapdvfechapedidoimportado", matching=0.97, waiting_time=10000):
                self.not_found("vendapdvfechapedidoimportado")
            self.click_relative(161, 26)
            self.type_up()
            self.enter()
            
                            ####---ABAIXAR TELA---####
            
            if not self.find( "abaixatelaparametrosempresa", matching=0.97, waiting_time=10000):
                self.not_found("abaixatelaparametrosempresa")
            self.click()
            
            x=0
            while x<17:
                if not self.find( "abaixartelamarcadaparametrosempresa", matching=0.97, waiting_time=10000):
                    self.not_found("abaixartelamarcadaparametrosempresa")
                self.double_click()
                x=x+1
                
                            ####---PERMISSOES 1---####
                             
            if not self.find( "informardatavencimentoitem", matching=0.97, waiting_time=10000):
                self.not_found("informardatavencimentoitem")
            self.click_relative(161, 25)
            self.type_up()
            self.enter()
            if not self.find( "informardatavencimentoitem", matching=0.97, waiting_time=10000):
                self.not_found("informardatavencimentoitem")
            self.click_relative(161, 25)
            self.type_down()
            self.enter()
            
            if not self.find( "permitealterarquantidade", matching=0.97, waiting_time=10000):
                self.not_found("permitealterarquantidade")
            self.click_relative(162, 27)
            self.type_up()
            self.enter()
            if not self.find( "permitealterarquantidade", matching=0.97, waiting_time=10000):
                self.not_found("permitealterarquantidade")
            self.click_relative(162, 27)
            self.type_down()
            self.enter()
            
            if not self.find( "utilizarplanodeprecosdeitens", matching=0.97, waiting_time=10000):
                self.not_found("utilizarplanodeprecosdeitens")
            self.click_relative(163, 25)
            self.type_up()
            self.enter()
            if not self.find( "utilizarplanodeprecosdeitens", matching=0.97, waiting_time=10000):
                self.not_found("utilizarplanodeprecosdeitens")
            self.click_relative(163, 25)
            self.type_down()
            self.enter()
            
            if not self.find( "impressaodedocumentosposvenda", matching=0.97, waiting_time=10000):
                self.not_found("impressaodedocumentosposvenda")
            self.click_relative(163, 25)
            self.type_up()
            self.enter()
            if not self.find( "impressaodedocumentosposvenda", matching=0.97, waiting_time=10000):
                self.not_found("impressaodedocumentosposvenda")
            self.click_relative(163, 25)
            self.type_up()
            self.enter()
            x=0
            while x<3:
                if not self.find( "impressaodedocumentosposvenda", matching=0.97, waiting_time=10000):
                    self.not_found("impressaodedocumentosposvenda")
                self.click_relative(163, 25)
                self.type_down()
                self.enter()
                x=x+1
            if not self.find( "impressaoderecibodeentrada", matching=0.97, waiting_time=10000):
                self.not_found("impressaoderecibodeentrada")
            self.click_relative(165, 26)
            self.type_up()
            self.enter()
            if not self.find( "impressaoderecibodeentrada", matching=0.97, waiting_time=10000):
                self.not_found("impressaoderecibodeentrada")
            self.click_relative(165, 26)
            self.type_down()
            self.enter()
            
            if not self.find( "utilizarcartaodefechamento", matching=0.97, waiting_time=10000):
                self.not_found("utilizarcartaodefechamento")
            self.click_relative(164, 25)
            self.type_up()
            self.enter()
            if not self.find( "utilizarcartaodefechamento", matching=0.97, waiting_time=10000):
                self.not_found("utilizarcartaodefechamento")
            self.click_relative(164, 25)
            self.type_down()
            self.enter()
            if not self.find( "utilizarcartaodefechamento", matching=0.97, waiting_time=10000):
                self.not_found("utilizarcartaodefechamento")
            self.click_relative(164, 25)
            self.type_down()
            self.enter()
            
            if not self.find( "exigirobsparacheques", matching=0.97, waiting_time=10000):
                self.not_found("exigirobsparacheques")
            self.click_relative(164, 25)
            self.type_up()
            self.enter()
            if not self.find( "exigirobsparacheques", matching=0.97, waiting_time=10000):
                self.not_found("exigirobsparacheques")
            self.click_relative(164, 25)
            self.type_down()
            self.enter()
            
            x=0
            while x<3:
                if not self.find( "alterardescricaodoitem", matching=0.97, waiting_time=10000):
                    self.not_found("alterardescricaodoitem")
                self.click_relative(161, 26)
                self.type_up()
                self.enter()
                x=x+1
                
            if not self.find( "permitirdescontoindividual", matching=0.97, waiting_time=10000):
                self.not_found("permitirdescontoindividual")
            self.click_relative(162, 24)
            self.type_up()
            self.enter()
            
            x=0
            while x<3:
                if not self.find( "permitirdescontoindividual", matching=0.97, waiting_time=10000):
                    self.not_found("permitirdescontoindividual")
                self.click_relative(162, 24)
                self.type_down()
                self.enter()
                x=x+1
                
            self.type_keys_with_interval(1,'123')
            self.enter()
            self.type_keys_with_interval(1,'123')
            
            if not self.find( "quandoemofertabalcao", matching=0.97, waiting_time=10000):
                self.not_found("quandoemofertabalcao")
            self.click_relative(161, 24)
            self.type_down()
            self.enter()
            if not self.find( "quandoemofertabalcao", matching=0.97, waiting_time=10000):
                self.not_found("quandoemofertabalcao")
            self.click_relative(161, 24)
            self.type_down()
            self.enter()
            
            if not self.find( "permitirdescontogeralna", matching=0.97, waiting_time=10000):
                self.not_found("permitirdescontogeralna")
            self.click_relative(161, 27)
            self.type_up()
            self.enter()
            if not self.find( "permitirdescontogeralna", matching=0.97, waiting_time=10000):
                self.not_found("permitirdescontogeralna")
            self.click_relative(161, 27)
            self.type_down()
            self.enter()
            
            self.type_keys_with_interval(1,'123')
            if not self.find( "percentualmaximodescontogeral", matching=0.97, waiting_time=10000):
                self.not_found("percentualmaximodescontogeral")
            self.click_relative(160, 26)
            self.type_keys_with_interval(1,'123')
            
            if not self.find( "alteracaodeprecounitarioitem", matching=0.97, waiting_time=10000):
                self.not_found("alteracaodeprecounitarioitem")
            self.click_relative(165, 23)
            self.type_up()
            self.enter()
            if not self.find( "alteracaodeprecounitarioitem", matching=0.97, waiting_time=10000):
                self.not_found("alteracaodeprecounitarioitem")
            self.click_relative(165, 23)
            self.type_down()
            self.enter()
            if not self.find( "alteracaodeprecounitarioitem", matching=0.97, waiting_time=10000):
                self.not_found("alteracaodeprecounitarioitem")
            self.click_relative(165, 23)
            self.type_down()
            self.enter()
            
            if not self.find( "diasvalidadeorcamento1", matching=0.97, waiting_time=10000):
                self.not_found("diasvalidadeorcamento1")
            self.double_click_relative(162, 21)
            if not self.find( "diasvalidadeorcamento2", matching=0.97, waiting_time=10000):
                self.not_found("diasvalidadeorcamento2")
            self.click_relative(162, 30)
            self.backspace()
            self.backspace()
            self.type_keys_with_interval(1,'1')
            
            x=0
            while x<4:
                if not self.find( "precoaorecuperarorcamento", matching=0.97, waiting_time=10000):
                    self.not_found("precoaorecuperarorcamento")
                self.click_relative(161, 26)
                self.type_down()
                self.enter()
                x=x+1
            x=0
            while x<3:
                if not self.find( "precoaorecuperarorcamento", matching=0.97, waiting_time=10000):
                    self.not_found("precoaorecuperarorcamento")
                self.click_relative(161, 26)
                self.type_up()
                self.enter()
                x=x+1
                
            x=0
            while x<5:    
                if not self.find( "tipodoagrupamentodedesconto", matching=0.97, waiting_time=10000):
                    self.not_found("tipodoagrupamentodedesconto")
                self.click_relative(160, 26)
                self.type_down()
                self.enter()
                x=x+1
            x=0
            while x<5:    
                if not self.find( "tipodoagrupamentodedesconto", matching=0.97, waiting_time=10000):
                    self.not_found("tipodoagrupamentodedesconto")
                self.click_relative(160, 26)
                self.type_up()
                self.enter()
                x=x+1
                
            if not self.find( "alteracaovalorunitarioservico", matching=0.97, waiting_time=10000):
                self.not_found("alteracaovalorunitarioservico")
            self.click_relative(161, 25)
            self.type_down()
            self.enter()
            if not self.find( "alteracaovalorunitarioservico", matching=0.97, waiting_time=10000):
                self.not_found("alteracaovalorunitarioservico")
            self.click_relative(161, 25)
            self.type_down()
            self.enter()
            
            if not self.find( "vendaitemkit", matching=0.97, waiting_time=10000):
                self.not_found("vendaitemkit")
            self.click_relative(168, 25)
            self.type_down()
            self.enter()
            
            x=0
            while x<3:
                if not self.find( "vendaaprazo", matching=0.97, waiting_time=10000):
                    self.not_found("vendaaprazo")
                self.click_relative(161, 26)
                self.type_down()
                self.enter()
                x=x+1
                
            self.type_keys_with_interval(1,'123')
            if not self.find( "vendasemsenhaate", matching=0.97, waiting_time=10000):
                self.not_found("vendasemsenhaate")
            self.click_relative(161, 24)
            self.type_keys_with_interval(1,'123')
            self.enter()
            
            x=0
            while x<3:                 
                if not self.find( "validarquantidadeimportacaopedido", matching=0.97, waiting_time=10000):
                    self.not_found("validarquantidadeimportacaopedido")
                self.click_relative(160, 27)
                self.type_down()
                self.enter()
                x=x+1
             
                            ####---PERMISSOES 2---####
             
             
            x=0
            while x<4:                
                if not self.find( "itemsemestoque", matching=0.97, waiting_time=10000):
                    self.not_found("itemsemestoque")
                self.click_relative(159, 27)
                self.type_down()
                self.enter()
                x=x+1
            x=0
            while x<4:
                 if not self.find( "descontosuperioraolimiteunegeral", matching=0.97, waiting_time=10000):
                     self.not_found("descontosuperioraolimiteunegeral")
                 self.click_relative(162, 26)
                 self.type_down()
                 self.enter()
                 x=x+1
                 
                 
            x=0
            while x<2:    
                 if not self.find( "unitariovalortabelaminimo", matching=0.97, waiting_time=10000):
                     self.not_found("unitariovalortabelaminimo")
                 self.click_relative(161, 27)
                 self.type_down()
                 self.enter()
                 x=x+1
                 
            x=0
            while x<2:
                 if not self.find( "cancelarvendasostransformacao", matching=0.97, waiting_time=10000):
                     self.not_found("cancelarvendasostransformacao")
                 self.click_relative(162, 26)
                 self.type_down()
                 self.enter()
                 x=x+1
                 
            if not self.find( "alteracaodevaloresnabaixa", matching=0.97, waiting_time=10000):
                self.not_found("alteracaodevaloresnabaixa")
            self.click_relative(162, 26)
            self.type_up()
            self.enter()
            if not self.find( "alteracaodevaloresnabaixa", matching=0.97, waiting_time=10000):
                self.not_found("alteracaodevaloresnabaixa")
            self.click_relative(162, 26)
            self.type_down()
            self.enter()
            if not self.find( "alteracaodevaloresnabaixa", matching=0.97, waiting_time=10000):
                self.not_found("alteracaodevaloresnabaixa")
            self.click_relative(162, 26)
            self.type_down()
            self.enter()
            
            if not self.find( "usarcondicaoespecial", matching=0.97, waiting_time=10000):
                self.not_found("usarcondicaoespecial")
            self.click_relative(166, 27)
            self.type_up()
            self.enter()
            if not self.find( "usarcondicaoespecial", matching=0.97, waiting_time=10000):
                self.not_found("usarcondicaoespecial")
            self.click_relative(166, 27)
            self.type_down()
            self.enter()
            if not self.find( "datavencimentoparcialmaiorqueliberado", matching=0.97, waiting_time=10000):
                self.not_found("datavencimentoparcialmaiorqueliberado")
            self.click_relative(159, 26)
            self.type_up()
            self.enter()
            if not self.find( "datavencimentoparcialmaiorqueliberado", matching=0.97, waiting_time=10000):
                self.not_found("datavencimentoparcialmaiorqueliberado")
            self.click_relative(159, 26)
            self.type_down()
            self.enter()
            if not self.find( "acessoaocaixa", matching=0.97, waiting_time=10000):
                self.not_found("acessoaocaixa")
            self.click_relative(161, 28)
            self.type_up()
            self.enter()
            if not self.find( "acessoaocaixa", matching=0.97, waiting_time=10000):
                self.not_found("acessoaocaixa")
            self.click_relative(161, 28)
            self.type_down()
            self.enter()
            if not self.find( "recuperardevolvercondicionais", matching=0.97, waiting_time=10000):
                self.not_found("recuperardevolvercondicionais")
            self.click_relative(169, 30)
            self.type_up()
            self.enter()
            if not self.find( "recuperardevolvercondicionais", matching=0.97, waiting_time=10000):
                self.not_found("recuperardevolvercondicionais")
            self.click_relative(169, 30)
            self.type_down()
            self.enter()
            if not self.find( "reimpressaodevendasfechadasbalcao", matching=0.97, waiting_time=10000):
                self.not_found("reimpressaodevendasfechadasbalcao")
            self.click_relative(159, 23)
            self.type_up()
            self.enter()
            if not self.find( "reimpressaodevendasfechadasbalcao", matching=0.97, waiting_time=10000):
                self.not_found("reimpressaodevendasfechadasbalcao")
            self.click_relative(159, 23)
            self.type_down()
            self.enter()
            if not self.find( "tipoliberacoespedidos", matching=0.97, waiting_time=10000):
                self.not_found("tipoliberacoespedidos")
            self.click_relative(163, 28)
            self.type_down()
            self.enter()
            if not self.find( "tipoliberacoespedidos", matching=0.97, waiting_time=10000):
                self.not_found("tipoliberacoespedidos")
            self.click_relative(163, 28)
            self.type_down()
            self.enter()
            if not self.find( "tipoliberacoespedidos", matching=0.97, waiting_time=10000):
                self.not_found("tipoliberacoespedidos")
            self.click_relative(163, 28)
            self.type_up()
            self.enter()
            if not self.find( "tipoliberacoespedidos", matching=0.97, waiting_time=10000):
                self.not_found("tipoliberacoespedidos")
            self.click_relative(163, 28)
            self.type_up()
            self.enter()
            
            x=0
            while x<4:
                if not self.find( "itemsemestoqueorcamento", matching=0.97, waiting_time=10000):
                    self.not_found("itemsemestoqueorcamento")
                self.click_relative(163, 26)
                self.type_down()
                self.enter()
                x=x+1
            x=0
            while x<4:
                if not self.find( "itemsemestoqueorcamento", matching=0.97, waiting_time=10000):
                    self.not_found("itemsemestoqueorcamento")
                self.click_relative(163, 26)
                self.type_up()
                self.enter()
                x=x+1
            
            if not self.find( "alterametragenstelaconfirmacao", matching=0.97, waiting_time=10000):
                self.not_found("alterametragenstelaconfirmacao")
            self.click_relative(162, 24)
            self.type_up()
            self.enter()   
            if not self.find( "alterametragenstelaconfirmacao", matching=0.97, waiting_time=10000):
                self.not_found("alterametragenstelaconfirmacao")
            self.click_relative(162, 24)
            self.type_down()
            self.enter()
            
            if not self.find( "alteravendedorvendaos", matching=0.97, waiting_time=10000):
                self.not_found("alteravendedorvendaos")
            self.click_relative(161, 27)
            self.type_down()
            self.enter()
            if not self.find( "alteravendedorvendaos", matching=0.97, waiting_time=10000):
                self.not_found("alteravendedorvendaos")
            self.click_relative(161, 27)
            self.type_up()
            self.enter()
            
            if not self.find( "fechamentoorcamentovenda", matching=0.97, waiting_time=10000):
                self.not_found("fechamentoorcamentovenda")
            self.click_relative(160, 26)
            self.type_up()
            self.enter()
            if not self.find( "fechamentoorcamentovenda", matching=0.97, waiting_time=10000):
                self.not_found("fechamentoorcamentovenda")
            self.click_relative(160, 26)
            self.type_down()
            self.enter()
            
            if not self.find( "excluiralteraritensvendas", matching=0.97, waiting_time=10000):
                self.not_found("excluiralteraritensvendas")
            self.click_relative(161, 27)
            self.type_down()
            self.enter()
            if not self.find( "excluiralteraritensvendas", matching=0.97, waiting_time=10000):
                self.not_found("excluiralteraritensvendas")
            self.click_relative(161, 27)
            self.type_down()
            self.enter()
            if not self.find( "excluiralteraritensvendas", matching=0.97, waiting_time=10000):
                self.not_found("excluiralteraritensvendas")
            self.click_relative(161, 27)
            self.type_up()
            self.enter()
            if not self.find( "excluiralteraritensvendas", matching=0.97, waiting_time=10000):
                self.not_found("excluiralteraritensvendas")
            self.click_relative(161, 27)
            self.type_up()
            self.enter() 
            
                            ####---ABA5 COMPRAS---####
                             
            if not self.find( "aba5compras", matching=0.97, waiting_time=10000):
                self.not_found("aba5compras")
            self.click()
            
            x=0
            while x<3:
                if not self.find( "utilizarusuarioautorizadornocompras", matching=0.97, waiting_time=10000):
                    self.not_found("utilizarusuarioautorizadornocompras")
                self.click_relative(161, 25)
                self.type_down()
                self.enter()
                x=x+1
            x=0
            while x<3:
                if not self.find( "utilizarusuarioautorizadornocompras", matching=0.97, waiting_time=10000):
                    self.not_found("utilizarusuarioautorizadornocompras")
                self.click_relative(161, 25)
                self.type_up()
                self.enter()
                x=x+1
                
            if not self.find( "exigeliberacaorejeicaodanalisecotacao", matching=0.97, waiting_time=10000):
                self.not_found("exigeliberacaorejeicaodanalisecotacao")
            self.click_relative(161, 27)
            self.type_up()
            self.enter()    
            if not self.find( "exigeliberacaorejeicaodanalisecotacao", matching=0.97, waiting_time=10000):
                self.not_found("exigeliberacaorejeicaodanalisecotacao")
            self.click_relative(161, 27)
            self.type_down()
            self.enter()
            
            self.type_keys_with_interval(1,'123')
            if not self.find( "margenslibentrada", matching=0.97, waiting_time=10000):
                self.not_found("margenslibentrada")
            self.click_relative(110, 25)
            self.type_keys_with_interval(1,'123')
            self.enter()
            self.enter()
            self.type_keys_with_interval(1,'123')
            if not self.find( "cpedidocustoqtde", matching=0.97, waiting_time=10000):
                self.not_found("cpedidocustoqtde")
            self.click_relative(102, 26)
            self.type_keys_with_interval(1,'123')
            self.enter()
            if not self.find( "tipomargemliberacaoentrada", matching=0.97, waiting_time=10000):
                self.not_found("tipomargemliberacaoentrada")
            self.click_relative(160, 25)
            self.type_down()
            self.enter()
            if not self.find( "tipomargemliberacaoentrada", matching=0.97, waiting_time=10000):
                self.not_found("tipomargemliberacaoentrada")
            self.click_relative(160, 25)
            self.type_up()
            self.enter()
                 
            x=0
            while x<3:
                if not self.find( "itememcotacaoaberta", matching=0.97, waiting_time=10000):
                    self.not_found("itememcotacaoaberta")
                self.click_relative(76, 24)
                self.type_down()
                self.enter()
                x=x+1     
            x=0
            while x<3:
                if not self.find( "itememcotacaoaberta", matching=0.97, waiting_time=10000):
                    self.not_found("itememcotacaoaberta")
                self.click_relative(76, 24)
                self.type_up()
                self.enter()
                x=x+1 
            
            x=0
            while x<3:
                if not self.find( "itemempedidosabertos", matching=0.97, waiting_time=10000):
                    self.not_found("itemempedidosabertos")
                self.click_relative(74, 24)
                self.type_down()
                self.enter()
                x=x+1
            x=0
            while x<3:
                if not self.find( "itemempedidosabertos", matching=0.97, waiting_time=10000):
                    self.not_found("itemempedidosabertos")
                self.click_relative(74, 24)
                self.type_up()
                self.enter()
                x=x+1
            
            x=0
            while x<3:    
                if not self.find( "itememrequisicoesabertas", matching=0.97, waiting_time=10000):
                    self.not_found("itememrequisicoesabertas")
                self.click_relative(76, 24)
                self.type_down()
                self.enter()
                x=x+1
            if not self.find( "mostrarobsnaimportacao", matching=0.97, waiting_time=10000):
                self.not_found("mostrarobsnaimportacao")
            self.click_relative(161, 24)
            self.type_down()
            self.enter() 
            if not self.find( "mostrarobsnaimportacao", matching=0.97, waiting_time=10000):
                self.not_found("mostrarobsnaimportacao")
            self.click_relative(161, 24)
            self.type_down()
            self.enter()
            if not self.find( "mostrarobsnaimportacao", matching=0.97, waiting_time=10000):
                self.not_found("mostrarobsnaimportacao")
            self.click_relative(161, 24)
            self.type_up()
            self.enter()
            
            if not self.find( "codigodeoperacaonaimportacao", matching=0.97, waiting_time=10000):
                self.not_found("codigodeoperacaonaimportacao")
            self.click_relative(163, 26)
            self.type_down()
            self.enter()     
            if not self.find( "codigodeoperacaonaimportacao", matching=0.97, waiting_time=10000):
                self.not_found("codigodeoperacaonaimportacao")
            self.click_relative(163, 26)
            self.type_down()
            self.enter()
            if not self.find( "codigodeoperacaonaimportacao", matching=0.97, waiting_time=10000):
                self.not_found("codigodeoperacaonaimportacao")
            self.click_relative(163, 26)
            self.type_up()
            self.enter()
            
            x=0
            while x<3:     
                if not self.find( "bloquear1parcelamenoracond", matching=0.97, waiting_time=10000):
                    self.not_found("bloquear1parcelamenoracond")
                self.click_relative(164, 25)
                self.type_down()
                self.enter()
                x=x+1
            x=0
            while x<3:     
                if not self.find( "bloquear1parcelamenoracond", matching=0.97, waiting_time=10000):
                    self.not_found("bloquear1parcelamenoracond")
                self.click_relative(164, 25)
                self.type_up()
                self.enter()
                x=x+1
                
            if not self.find( "cotacaoautomaticaparaitensnaomarca", matching=0.97, waiting_time=10000):
                self.not_found("cotacaoautomaticaparaitensnaomarca")
            self.click_relative(159, 25)
            self.type_down()
            self.enter()
            if not self.find( "cotacaoautomaticaparaitensnaomarca", matching=0.97, waiting_time=10000):
                self.not_found("cotacaoautomaticaparaitensnaomarca")
            self.click_relative(159, 25)
            self.type_down()
            self.enter()
            if not self.find( "cotacaoautomaticaparaitensnaomarca", matching=0.97, waiting_time=10000):
                self.not_found("cotacaoautomaticaparaitensnaomarca")
            self.click_relative(159, 25)
            self.type_up()
            self.enter() 
            
            x=0
            while x<3:
                if not self.find( "liberacaolimitedecompra", matching=0.97, waiting_time=10000):
                    self.not_found("liberacaolimitedecompra")
                self.click_relative(162, 25)
                self.type_down()
                self.enter()
                x=x+1
                
            x=0
            while x<3:
                if not self.find( "liberacaolimitedecompra", matching=0.97, waiting_time=10000):
                    self.not_found("liberacaolimitedecompra")
                self.click_relative(162, 25)
                self.type_up()
                self.enter()
                x=x+1
                
            x=0
            while x<2:
                if not self.find( "bloqueiafornecedorimppedcomp", matching=0.97, waiting_time=10000):
                    self.not_found("bloqueiafornecedorimppedcomp")
                self.click_relative(161, 23)
                self.type_down()
                self.enter()
                x=x+1
            x=0
            while x<2:
                if not self.find( "bloqueiafornecedorimppedcomp", matching=0.97, waiting_time=10000):
                    self.not_found("bloqueiafornecedorimppedcomp")
                self.click_relative(161, 23)
                self.type_up()
                self.enter()
                x=x+1 
                
            
            x=0
            while x<2:
                if not self.find( "condicaopagtoimppedcomp", matching=0.97, waiting_time=10000):
                    self.not_found("condicaopagtoimppedcomp")
                self.click_relative(94, 23)
                self.type_up()
                self.enter()
                x=x+1
            x=0
            while x<2:
                if not self.find( "condicaopagtoimppedcomp", matching=0.97, waiting_time=10000):
                    self.not_found("condicaopagtoimppedcomp")
                self.click_relative(94, 23)
                self.type_down()
                self.enter()
                x=x+1
                
            
            x=0
            while x<2:
                if not self.find( "compradorimppedcompras", matching=0.97, waiting_time=10000):
                    self.not_found("compradorimppedcompras")
                self.click_relative(94, 22)
                self.type_down()
                self.enter()
                x=x+1
                
            if not self.find( "verificaipistdositens", matching=0.97, waiting_time=10000):
                self.not_found("verificaipistdositens")
            self.click_relative(162, 24)
            self.type_up()
            self.enter()        
            if not self.find( "verificaipistdositens", matching=0.97, waiting_time=10000):
                self.not_found("verificaipistdositens")
            self.click_relative(162, 24)
            self.type_down()
            self.enter()
            
            x=0
            while x<2:
                if not self.find( "exigirclassificacaopedidodecompra", matching=0.97, waiting_time=10000):
                    self.not_found("exigirclassificacaopedidodecompra")
                self.click_relative(162, 26)                
                self.type_down()
                self.enter()
                x=x+1    
            x=0
            while x<2:
                if not self.find( "exigirclassificacaopedidodecompra", matching=0.97, waiting_time=10000):
                    self.not_found("exigirclassificacaopedidodecompra")
                self.click_relative(162, 26)                
                self.type_up()
                self.enter()
                x=x+1
                
            x=0
            while x<6:
                if not self.find( "acordocialfinanceiropedidocompra", matching=0.97, waiting_time=10000):
                    self.not_found("acordocialfinanceiropedidocompra")
                self.click_relative(161, 23)                                
                self.type_down()
                self.enter()
                x=x+1
            x=0
            while x<6:
                if not self.find( "acordocialfinanceiropedidocompra", matching=0.97, waiting_time=10000):
                    self.not_found("acordocialfinanceiropedidocompra")
                self.click_relative(161, 23)                                
                self.type_up()
                self.enter()
                x=x+1
                
            x=0
            while x<3:
                if not self.find( "variacaonocustoentradas", matching=0.97, waiting_time=10000):
                    self.not_found("variacaonocustoentradas")
                self.click_relative(162, 23)
                self.type_down()
                self.enter()
                x=x+1
            x=0
            while x<3:
                if not self.find( "variacaonocustoentradas", matching=0.97, waiting_time=10000):
                    self.not_found("variacaonocustoentradas")
                self.click_relative(162, 23)
                self.type_up()
                self.enter()
                x=x+1        
            self.type_keys_with_interval(1,'123')
            if not self.find( "percentualmacvariacaocusto", matching=0.97, waiting_time=10000):
                self.not_found("percentualmacvariacaocusto")
            self.click_relative(113, 22)
            self.type_keys_with_interval(1,'123')
            
                            ####---ABA6 MENSAGENS---####
                             
            if not self.find( "aba6mensagens", matching=0.97, waiting_time=10000):
                self.not_found("aba6mensagens")
            self.click()
            self.type_keys_with_interval(1,'te12!@') 
            self.tab()
            self.type_keys_with_interval(1,'te12!@')
            self.tab()
            self.type_keys_with_interval(1,'te12!@')
            self.tab()
            self.type_keys_with_interval(1,'te12!@')
            self.tab()
            self.type_keys_with_interval(1,'te12!@')    
            
                            ####---ABA7 PRODUCAO, OS, CRM---####
                             
            if not self.find( "aba7producaooscrm", matching=0.97, waiting_time=10000):
                self.not_found("aba7producaooscrm")
            self.click()
            
                            ####---PRODUCAO/TRANSFORMACAO---####
                             
            if not self.find( "custoautilizarnoproducao", matching=0.97, waiting_time=10000):
                self.not_found("custoautilizarnoproducao")
            self.click_relative(160, 25)
            self.type_up()
            self.enter()
            
            x=0
            while x<4:    
                if not self.find( "custoautilizarnoproducao", matching=0.97, waiting_time=10000):
                    self.not_found("custoautilizarnoproducao")
                self.click_relative(160, 25)
                self.type_down()
                self.enter()
                x=x+1
            x=0
            while x<3:    
                if not self.find( "custoautilizarnoproducao", matching=0.97, waiting_time=10000):
                    self.not_found("custoautilizarnoproducao")
                self.click_relative(160, 25)
                self.type_up()
                self.enter()
                x=x+1
            if not self.find( "composicaosemestoque", matching=0.97, waiting_time=10000):
                self.not_found("composicaosemestoque")
            self.click_relative(164, 25)
            self.type_down()
            self.enter()
            if not self.find( "composicaosemestoque", matching=0.97, waiting_time=10000):
                self.not_found("composicaosemestoque")
            self.click_relative(164, 25)
            self.type_down()
            self.enter()
            if not self.find( "liberacaotransformacao", matching=0.97, waiting_time=10000):
                self.not_found("liberacaotransformacao")
            self.click_relative(161, 24)
            self.type_down()
            self.enter()
            if not self.find( "liberacaotransformacao", matching=0.97, waiting_time=10000):
                self.not_found("liberacaotransformacao")
            self.click_relative(161, 24)
            self.type_down()
            self.enter()
            
                            ####---PRODUCAO/TRANSFORMACAO/OSM---####
                             
            x=0
            while x<7:
                if not self.find( "gerarnovocontatoapartir", matching=0.97, waiting_time=10000):
                    self.not_found("gerarnovocontatoapartir")
                self.click_relative(160, 27)
                self.type_down()
                self.enter()
                x=x+1
            if not self.find( "gerarpusuario", matching=0.97, waiting_time=10000):
                self.not_found("gerarpusuario")
            self.click_relative(379, 24)
            self.type_down()
            self.enter()
            if not self.find( "gerarpusuario", matching=0.97, waiting_time=10000):
                self.not_found("gerarpusuario")
            self.click_relative(379, 24)
            self.backspace()
            self.backspace()
            if not self.find( "gerarpusuario3", matching=0.97, waiting_time=10000):
                self.not_found("gerarpusuario3")
            self.double_click_relative(82, 25)
            if not self.find( "gerarpusuario4", matching=0.97, waiting_time=10000):
                self.not_found("gerarpusuario4")
            self.click()
            if not self.find( "gerarpusuarioselecionar", matching=0.97, waiting_time=10000):
                self.not_found("gerarpusuarioselecionar")
            self.click()
            self.enter()
            self.enter()
            self.type_keys_with_interval(1,'123')
            if not self.find( "diasaposvendaocontato", matching=0.97, waiting_time=10000):
                self.not_found("diasaposvendaocontato")
            self.click_relative(160, 25)
            self.type_keys_with_interval(1,'123')
            if not self.find( "aofinalizaratendimentodotelemarkting", matching=0.97, waiting_time=10000):
                self.not_found("aofinalizaratendimentodotelemarkting")
            self.click_relative(161, 25)
            self.type_down()
            self.enter()
            if not self.find( "aofinalizaratendimentodotelemarkting", matching=0.97, waiting_time=10000):
                self.not_found("aofinalizaratendimentodotelemarkting")
            self.click_relative(161, 25)
            self.type_down()
            self.enter()
            if not self.find( "telemarketingexibenegociacao", matching=0.97, waiting_time=10000):
                self.not_found("telemarketingexibenegociacao")
            self.click_relative(161, 26)
            self.type_up()
            self.enter()
            if not self.find( "telemarketingexibenegociacao", matching=0.97, waiting_time=10000):
                self.not_found("telemarketingexibenegociacao")
            self.click_relative(161, 26)
            self.type_down()
            self.enter()
            if not self.find( "baixaitemsemestoqueosm", matching=0.97, waiting_time=10000):
                self.not_found("baixaitemsemestoqueosm")
            self.click_relative(162, 24)
            self.type_down()
            self.enter()
            if not self.find( "baixaitemsemestoqueosm", matching=0.97, waiting_time=10000):
                self.not_found("baixaitemsemestoqueosm")
            self.click_relative(162, 24)
            self.type_down()
            self.enter()
            
                            ####---GERAL---####

            x=0
            while x<4:
                if not self.find( "ramodeatividadeos", matching=0.97, waiting_time=10000):
                    self.not_found("ramodeatividadeos")
                self.click_relative(161, 25)
                self.type_down()
                self.enter()
                x=x+1
            x=0
            while x<4:
                if not self.find( "ramodeatividadeos", matching=0.97, waiting_time=10000):
                    self.not_found("ramodeatividadeos")
                self.click_relative(161, 25)
                self.type_up()
                self.enter()
                x=x+1
            
            self.type_keys_with_interval(1,'123')
            if not self.find( "acrescimonaos", matching=0.97, waiting_time=10000):
                self.not_found("acrescimonaos")
            self.click_relative(165, 26)
            self.type_up()
            self.enter()
            if not self.find( "acrescimonaos", matching=0.97, waiting_time=10000):
                self.not_found("acrescimonaos")
            self.click_relative(165, 26)
            self.type_down()
            self.enter()
            if not self.find( "linhasimpressaoformularioos", matching=0.97, waiting_time=10000):
                self.not_found("linhasimpressaoformularioos")
            self.double_click_relative(165, 19)
            if not self.find( "linhasimpressaoformularioos2", matching=0.97, waiting_time=10000):
                self.not_found("linhasimpressaoformularioos2")
            self.click_relative(164, 31)
            self.backspace()
            self.backspace()
            self.type_keys_with_interval(1,'1')
            
            if not self.find( "exigiralocacao", matching=0.97, waiting_time=10000):
                self.not_found("exigiralocacao")
            self.click_relative(161, 25)
            self.type_up()
            self.enter()
            if not self.find( "exigiralocacao", matching=0.97, waiting_time=10000):
                self.not_found("exigiralocacao")
            self.click_relative(161, 25)
            self.type_down()
            self.enter()
            if not self.find( "tipodanfdeservico", matching=0.97, waiting_time=10000):
                self.not_found("tipodanfdeservico")
            self.click_relative(163, 25)
            self.type_up()
            self.enter()
            if not self.find( "tipodanfdeservico", matching=0.97, waiting_time=10000):
                self.not_found("tipodanfdeservico")
            self.click_relative(163, 25)
            self.type_down()
            self.enter()
            
            if not self.find( "enviaremailosnassituacoes", matching=0.97, waiting_time=10000):
                self.not_found("enviaremailosnassituacoes")
            self.click_relative(160, 24)
            if not self.find( "fechadasemailos", matching=0.97, waiting_time=10000):
                self.not_found("fechadasemailos")
            self.click()
            if not self.find( "canceladasemailos", matching=0.97, waiting_time=10000):
                self.not_found("canceladasemailos")
            self.click()
            if not self.find( "finalizadooficinaemailos", matching=0.97, waiting_time=10000):
                self.not_found("finalizadooficinaemailos")
            self.click()
            if not self.find( "emandamentoemailos", matching=0.97, waiting_time=10000):
                self.not_found("emandamentoemailos")
            self.click()
            if not self.find( "abertasemailos", matching=0.97, waiting_time=10000):
                self.not_found("abertasemailos")
            self.click()
            if not self.find( "enviaremailosnassituacoes", matching=0.97, waiting_time=10000):
                self.not_found("enviaremailosnassituacoes")
            self.click_relative(160, 24)
            if not self.find( "enviaremailosnassituacoes", matching=0.97, waiting_time=10000):
                self.not_found("enviaremailosnassituacoes")
            self.click_relative(160, 24)
            if not self.find( "fechadasemailos2", matching=0.97, waiting_time=10000):
                self.not_found("fechadasemailos2")
            self.click()
            if not self.find( "canceladasemailos2", matching=0.97, waiting_time=10000):
                self.not_found("canceladasemailos2")
            self.click()
            if not self.find( "finalizadooficinaemailos2", matching=0.97, waiting_time=10000):
                self.not_found("finalizadooficinaemailos2")
            self.click()
            if not self.find( "emandamentoemailosmarcado", matching=0.97, waiting_time=10000):
                self.not_found("emandamentoemailosmarcado")
            self.click()      
            if not self.find( "enviaremailosaberta2", matching=0.97, waiting_time=10000):
                self.not_found("enviaremailosaberta2")
            self.click()
            
                       
                       
            x=0
            while x<3:
                if not self.find( "baixaparcialos", matching=0.97, waiting_time=10000):
                    self.not_found("baixaparcialos")
                self.click_relative(163, 27)
                self.type_down()
                self.enter()
                x=x+1
            x=0
            while x<3:
                if not self.find( "baixaparcialos", matching=0.97, waiting_time=10000):
                    self.not_found("baixaparcialos")
                self.click_relative(163, 27)
                self.type_up()
                self.enter()
                x=x+1
               
            x=0
            while x<2:
                if not self.find( "baixadoestoquecentraldepecas", matching=0.97, waiting_time=10000):
                    self.not_found("baixadoestoquecentraldepecas")
                self.click_relative(160, 25)
                self.type_down()
                self.enter()
                x=x+1
                
                            ####---DESCRICAO DOS CAMPOS DE EQUIP---####

            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
    
                            ####---CAMPOS DE CHECAGEM NA OS---####
            
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            self.enter()

                            ####---CUSTOM VANS---####

            self.type_keys_with_interval(1,'123')
            if not self.find( "percentualminimoentrada", matching=0.97, waiting_time=10000):
                self.not_found("percentualminimoentrada")
            self.click_relative(161, 24)
            self.type_keys_with_interval(1,'123')
            
                            ####---PARAMETROS NOTA FISCAL---####
                            ####---PRODUCAO/TRANSFORMACAO---####

            if not self.find( "aba8parametrosnotafiscal", matching=0.97, waiting_time=10000):
                self.not_found("aba8parametrosnotafiscal")
            self.click()
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(1,'te12@!')

                            ####---COMPRIMENTO M2---####

            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            self.enter()

                            ####---PARAMETRIZACAO---####

            self.type_keys_with_interval(1,'t1!')
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "aocancelarnotafiscalcereal", matching=0.97, waiting_time=10000):
                self.not_found("aocancelarnotafiscalcereal")
            self.click_relative(210, 26)
            self.type_up()
            self.enter()
            if not self.find( "aocancelarnotafiscalcereal", matching=0.97, waiting_time=10000):
                self.not_found("aocancelarnotafiscalcereal")
            self.click_relative(210, 26)
            self.type_down()
            self.enter()
            if not self.find( "acrescentarficatecnicadoitem", matching=0.97, waiting_time=10000):
                self.not_found("acrescentarficatecnicadoitem")
            self.click_relative(102, 26)
            self.type_down()
            self.enter()
            if not self.find( "acrescentarficatecnicadoitem", matching=0.97, waiting_time=10000):
                self.not_found("acrescentarficatecnicadoitem")
            self.click_relative(102, 26)
            self.type_down()
            self.enter()
            if not self.find( "localdeentregananotafiscal", matching=0.97, waiting_time=10000):
                self.not_found("localdeentregananotafiscal")
            self.click_relative(430, 25)
            self.type_down()
            self.enter()
            if not self.find( "localdeentregananotafiscal", matching=0.97, waiting_time=10000):
                self.not_found("localdeentregananotafiscal")
            self.click_relative(430, 25)
            self.type_down()
            self.enter()
            self.type_keys_with_interval(1,'t1!')

                            ####---FORMULARIO NF---####

            if not self.find( "formularionotafiscal", matching=0.97, waiting_time=10000):
                self.not_found("formularionotafiscal")
            self.click_relative(147, 46)
            self.type_down()
            self.enter() 

                            ####---LEVANTA TELA---####
            
            if not self.find( "levantatelanf", matching=0.97, waiting_time=10000):
                self.not_found("levantatelanf")
            self.click()
            x=0
            while x<7:
                if not self.find( "levantatelanf2", matching=0.97, waiting_time=10000):
                    self.not_found("levantatelanf2")
                self.double_click()
                x=x+1

                            ####---FORMULARIO NF---####

            if not self.find( "formularionotafiscal", matching=0.97, waiting_time=10000):
                self.not_found("formularionotafiscal")
            self.click_relative(147, 46)
            self.type_up()
            self.enter()

                            ####---NUMERACAO NOTA FISCAL---####
                
            if not self.find( "incluirnovoregistroparametrosnf", matching=0.97, waiting_time=10000):
                self.not_found("incluirnovoregistroparametrosnf")
            self.click()
            
            if not self.find( "oknumeronf", matching=0.97, waiting_time=10000):
                self.not_found("oknumeronf")
            self.click()
            
                            ####---ABA9 CODIGOS PADROES---####
                             
            if not self.find( "aba9codigospadroes", matching=0.97, waiting_time=10000):
                self.not_found("aba9codigospadroes")
            self.click()
            
                                ####---A5 P1---####
                                 
            if not self.find( "relacionadoaempresa", matching=0.97, waiting_time=10000):
                self.not_found("relacionadoaempresa")
            self.click_relative(94, 25)
            if not self.find( "achar", matching=0.97, waiting_time=10000):
                self.not_found("achar")
            self.click()
            if not self.find( "achacod1", matching=0.97, waiting_time=10000):
                self.not_found("achacod1")
            self.click()
            if not self.find( "escolhe", matching=0.97, waiting_time=10000):
                self.not_found("escolhe")
            self.click()
            self.wait(1000)
            if not self.find( "cadastromodelo", matching=0.97, waiting_time=10000):
                self.not_found("cadastromodelo")
            self.click_relative(96, 23)
            if not self.find( "achar", matching=0.97, waiting_time=10000):
                self.not_found("achar")
            self.click()
            if not self.find( "achacod1", matching=0.97, waiting_time=10000):
                self.not_found("achacod1")
            self.click()
            if not self.find( "escolhe", matching=0.97, waiting_time=10000):
                self.not_found("escolhe")
            self.click()
            self.wait(1000)
            if not self.find( "localestoquepadrao", matching=0.97, waiting_time=10000):
                self.not_found("localestoquepadrao")
            self.click_relative(80, 27)
            if not self.find( "achar", matching=0.97, waiting_time=10000):
                self.not_found("achar")
            self.click()
            if not self.find( "volta", matching=0.97, waiting_time=10000):
                self.not_found("volta")
            self.click()
            self.wait(1000)
                            ####---OPERACAO DE ENTRADA---####
                             
            if not self.find( "transformacaodeitens", matching=0.97, waiting_time=10000):
                self.not_found("transformacaodeitens")
            self.click_relative(84, 44)                                   
            if not self.find( "achar", matching=0.97, waiting_time=10000):
                self.not_found("achar")
            self.click()
            if not self.find( "achacod01menor", matching=0.97, waiting_time=10000):
                self.not_found("achacod01menor")
            self.click()
            if not self.find( "escolhe", matching=0.97, waiting_time=10000):
                self.not_found("escolhe")
            self.click()
            self.wait(1000)
            if not self.find( "inventarioentrada", matching=0.97, waiting_time=10000):
                self.not_found("inventarioentrada")
            self.click_relative(483, 45)
            
            if not self.find( "achar", matching=0.97, waiting_time=10000):
                self.not_found("achar")
            self.click()
            if not self.find( "achacod01menor", matching=0.97, waiting_time=10000):
                self.not_found("achacod01menor")
            self.click()
            if not self.find( "escolhe", matching=0.97, waiting_time=10000):
                self.not_found("escolhe")
            self.click()
            self.wait(1000)
            if not self.find( "producaoeosm", matching=0.97, waiting_time=10000):
                self.not_found("producaoeosm")
            self.click_relative(882, 44)                                    
            if not self.find( "achar", matching=0.97, waiting_time=10000):
                self.not_found("achar")
            self.click()
            if not self.find( "achacod01menor", matching=0.97, waiting_time=10000):
                self.not_found("achacod01menor")
            self.click()
            if not self.find( "escolhe", matching=0.97, waiting_time=10000):
                self.not_found("escolhe")
            self.click()
            self.wait(1000)
            if not self.find( "itemkit", matching=0.97, waiting_time=10000):
                self.not_found("itemkit")
            self.click_relative(-13, 87)
            if not self.find( "achar", matching=0.97, waiting_time=10000):
                self.not_found("achar")
            self.click()
            if not self.find( "achacod01menor", matching=0.97, waiting_time=10000):
                self.not_found("achacod01menor")
            self.click()
            if not self.find( "escolhe", matching=0.97, waiting_time=10000):
                self.not_found("escolhe")
            self.click()
            self.wait(1000)
            if not self.find( "itemmestreentrada", matching=0.97, waiting_time=10000):
                self.not_found("itemmestreentrada")
            self.click_relative(483, 88)
                                  
            if not self.find( "achar", matching=0.97, waiting_time=10000):
                self.not_found("achar")
            self.click()
            if not self.find( "achacod01menor", matching=0.97, waiting_time=10000):
                self.not_found("achacod01menor")
            self.click()
            if not self.find( "escolhe", matching=0.97, waiting_time=10000):
                self.not_found("escolhe")
            self.click()
            self.wait(1000)
            if not self.find( "almoxarifadoentrada", matching=0.97, waiting_time=10000):
                self.not_found("almoxarifadoentrada")
            self.click_relative(885, 88)
            
            if not self.find( "achar", matching=0.97, waiting_time=10000):
                self.not_found("achar")
            self.click()
            if not self.find( "achacod01menor", matching=0.97, waiting_time=10000):
                self.not_found("achacod01menor")
            self.click()
            if not self.find( "escolhe", matching=0.97, waiting_time=10000):
                self.not_found("escolhe")
            self.click()
            self.wait(1000)
            if not self.find( "desmembramentoitens", matching=0.97, waiting_time=10000):
                self.not_found("desmembramentoitens")
            self.click_relative(-11, 127)
            if not self.find( "achar", matching=0.97, waiting_time=10000):
                self.not_found("achar")
            self.click()
            if not self.find( "achacod01menor", matching=0.97, waiting_time=10000):
                self.not_found("achacod01menor")
            self.click()
            if not self.find( "escolhe", matching=0.97, waiting_time=10000):
                self.not_found("escolhe")
            self.click()
            self.wait(1000)
            if not self.find( "devolucaoitens", matching=0.97, waiting_time=10000):
                self.not_found("devolucaoitens")
            self.click_relative(388, 127)
            if not self.find( "achacod01menordif", matching=0.97, waiting_time=10000):
                self.not_found("achacod01menordif")
            self.click()
            if not self.find( "escolhe", matching=0.97, waiting_time=10000):
                self.not_found("escolhe")
            self.click()
            self.wait(1000)
            
                            ####---OPERACOES DE SAIDA---####
                             
            if not self.find( "transformacaoitenssaida", matching=0.97, waiting_time=10000):
                self.not_found("transformacaoitenssaida")
            self.click_relative(84, 46)
            
            if not self.find( "achar", matching=0.97, waiting_time=10000):
                self.not_found("achar")
            self.click()           
            if not self.find( "achacod02", matching=0.97, waiting_time=10000):
                self.not_found("achacod02")
            self.click()
            if not self.find( "escolhe", matching=0.97, waiting_time=10000):
                self.not_found("escolhe")
            self.click()
            self.wait(1000)
            if not self.find( "inventariosaida", matching=0.97, waiting_time=10000):
                self.not_found("inventariosaida")
            self.click_relative(483, 48)
                        
            if not self.find( "achar", matching=0.97, waiting_time=10000):
                self.not_found("achar")
            self.click()
            if not self.find( "achacod02", matching=0.97, waiting_time=10000):
                self.not_found("achacod02")
            self.click()
            if not self.find( "escolhe", matching=0.97, waiting_time=10000):
                self.not_found("escolhe")
            self.click()
            self.wait(1000)
            if not self.find( "producaoeosm2", matching=0.97, waiting_time=10000):
                self.not_found("producaoeosm2")
            self.click_relative(787, 43)
            if not self.find( "achar", matching=0.97, waiting_time=10000):
                self.not_found("achar")
            self.click()
            if not self.find( "achacod02", matching=0.97, waiting_time=10000):
                self.not_found("achacod02")
            self.click()
            if not self.find( "escolhe", matching=0.97, waiting_time=10000):
                self.not_found("escolhe")
            self.click()
            self.wait(1000)
            if not self.find( "operacoesdesaidaitemkit", matching=0.97, waiting_time=10000):
                self.not_found("operacoesdesaidaitemkit")
            self.click_relative(83, 86)
            
            if not self.find( "achar", matching=0.97, waiting_time=10000):
                self.not_found("achar")
            self.click()
            if not self.find( "achacod02", matching=0.97, waiting_time=10000):
                self.not_found("achacod02")
            self.click()
            if not self.find( "escolhe", matching=0.97, waiting_time=10000):
                self.not_found("escolhe")
            self.click()
            self.wait(1000)
            if not self.find( "itemmestresaida", matching=0.97, waiting_time=10000):
                self.not_found("itemmestresaida")
            self.click_relative(485, 86)
            
            if not self.find( "achar", matching=0.97, waiting_time=10000):
                self.not_found("achar")
            self.click()
            if not self.find( "achacod02", matching=0.97, waiting_time=10000):
                self.not_found("achacod02")
            self.click()
            if not self.find( "escolhe", matching=0.97, waiting_time=10000):
                self.not_found("escolhe")
            self.click()
            self.wait(1000)
            if not self.find( "almoxarifadosaida", matching=0.97, waiting_time=10000):
                self.not_found("almoxarifadosaida")
            self.click_relative(884, 88)
            
            if not self.find( "achar", matching=0.97, waiting_time=10000):
                self.not_found("achar")
            self.click()
            if not self.find( "achacod02", matching=0.97, waiting_time=10000):
                self.not_found("achacod02")
            self.click()
            if not self.find( "escolhe", matching=0.97, waiting_time=10000):
                self.not_found("escolhe")
            self.click()
            self.wait(1000)
            if not self.find( "desmembramentosaida", matching=0.97, waiting_time=10000):
                self.not_found("desmembramentosaida")
            self.click_relative(84, 129)
            
            if not self.find( "achar", matching=0.97, waiting_time=10000):
                self.not_found("achar")
            self.click()
            if not self.find( "achacod02", matching=0.97, waiting_time=10000):
                self.not_found("achacod02")
            self.click()
            if not self.find( "escolhe", matching=0.97, waiting_time=10000):
                self.not_found("escolhe")
            self.click()
            self.wait(1000)
            if not self.find( "centraldepecas", matching=0.97, waiting_time=10000):
                self.not_found("centraldepecas")
            self.click_relative(388, 129)
            if not self.find( "achar", matching=0.97, waiting_time=10000):
                self.not_found("achar")
            self.click()
            if not self.find( "achacod02", matching=0.97, waiting_time=10000):
                self.not_found("achacod02")
            self.click()
            if not self.find( "escolhe", matching=0.97, waiting_time=10000):
                self.not_found("escolhe")
            self.click()
            self.wait(1000)
            
                            ####---ABA5 P2---####

            if not self.find( "aba5p2pa", matching=0.97, waiting_time=10000):
                self.not_found("aba5p2pa")
            self.click()
            if not self.find( "clientepadraovendas", matching=0.97, waiting_time=10000):
                self.not_found("clientepadraovendas")
            self.click_relative(97, 26)
            if not self.find( "achar", matching=0.97, waiting_time=10000):
                self.not_found("achar")
            self.click()
            if not self.find( "achacod1", matching=0.97, waiting_time=10000):
                self.not_found("achacod1")
            self.click()
            if not self.find( "escolhe", matching=0.97, waiting_time=10000):
                self.not_found("escolhe")
            self.click()
            self.wait(1000)
            if not self.find( "vendedorpadraovendas", matching=0.97, waiting_time=10000):
                self.not_found("vendedorpadraovendas")
            self.click_relative(83, 26)
            if not self.find( "achar", matching=0.97, waiting_time=10000):
                self.not_found("achar")
            self.click()
            if not self.find( "cod101teste", matching=0.97, waiting_time=10000):
                self.not_found("cod101teste")
            self.click()           
            if not self.find( "escolhe", matching=0.97, waiting_time=10000):
                self.not_found("escolhe")
            self.click()
            self.wait(1000)
            if not self.find( "condicaodepagamentopadraovendas", matching=0.97, waiting_time=10000):
                self.not_found("condicaodepagamentopadraovendas")
            self.click_relative(81, 26)
            if not self.find( "achar", matching=0.97, waiting_time=10000):
                self.not_found("achar")
            self.click()
            if not self.find( "achacod01menor", matching=0.97, waiting_time=10000):
                self.not_found("achacod01menor")
            self.click()
            if not self.find( "escolhe", matching=0.97, waiting_time=10000):
                self.not_found("escolhe")
            self.click()
            self.wait(1000)
            
                            ####---PADROES OPERACOES FISCAIS---####

            if not self.find( "cfoppadraonfvendas", matching=0.97, waiting_time=10000):
                self.not_found("cfoppadraonfvendas")
            self.click_relative(83, 45)         
            self.backspace()
            if not self.find( "achar", matching=0.97, waiting_time=10000):
                self.not_found("achar")
            self.click()
            if not self.find( "cod1101", matching=0.97, waiting_time=10000):
                self.not_found("cod1101")
            self.click()
            if not self.find( "escolhe", matching=0.97, waiting_time=10000):
                self.not_found("escolhe")
            self.click()
            self.wait(1000)
            if not self.find( "operacaosaidapadraovendas", matching=0.97, waiting_time=10000):
                self.not_found("operacaosaidapadraovendas")
            self.click_relative(81, 24)
            if not self.find( "achar", matching=0.97, waiting_time=10000):
                self.not_found("achar")
            self.click()
            if not self.find( "achacod02", matching=0.97, waiting_time=10000):
                self.not_found("achacod02")
            self.click()
            if not self.find( "escolhe", matching=0.97, waiting_time=10000):
                self.not_found("escolhe")
            self.click()
            self.wait(1000)
            if not self.find( "operacaoparanfedecupomfiscal", matching=0.97, waiting_time=10000):
                self.not_found("operacaoparanfedecupomfiscal")
            self.click_relative(880, 41)                       
            if not self.find( "achar", matching=0.97, waiting_time=10000):
                self.not_found("achar")
            self.click()
            if not self.find( "achacod02", matching=0.97, waiting_time=10000):
                self.not_found("achacod02")
            self.click()
            if not self.find( "escolhe", matching=0.97, waiting_time=10000):
                self.not_found("escolhe")
            self.click()
            self.wait(1000)
            if not self.find( "operacaoparanfedopaf", matching=0.97, waiting_time=10000):
                self.not_found("operacaoparanfedopaf")
            self.click_relative(78, 23)
            if not self.find( "achar", matching=0.97, waiting_time=10000):
                self.not_found("achar")
            self.click()
            if not self.find( "achacod02", matching=0.97, waiting_time=10000):
                self.not_found("achacod02")
            self.click()
            if not self.find( "escolhe", matching=0.97, waiting_time=10000):
                self.not_found("escolhe")
            self.click()
            self.wait(1000)
            if not self.find( "operacaosaidapadraordemdeservico", matching=0.97, waiting_time=10000):
                self.not_found("operacaosaidapadraordemdeservico")
            self.click_relative(77, 22)
            if not self.find( "achar", matching=0.97, waiting_time=10000):
                self.not_found("achar")
            self.click()
            self.type_keys_with_interval(1,'te12')
            if not self.find( "escolhe", matching=0.97, waiting_time=10000):
                self.not_found("escolhe")
            self.click()
            self.wait(1000)
            
                            ####---PADROES ADICIONAIS---####
                             
            if not self.find( "pagamentoaddconsultitens", matching=0.97, waiting_time=10000):
                self.not_found("pagamentoaddconsultitens")
            self.click_relative(84, 46)
            if not self.find( "achar", matching=0.97, waiting_time=10000):
                self.not_found("achar")
            self.click()
            if not self.find( "achacod02", matching=0.97, waiting_time=10000):
                self.not_found("achacod02")
            self.click()
            if not self.find( "escolhe", matching=0.97, waiting_time=10000):
                self.not_found("escolhe")
            self.click()
            self.wait(1000)
            if not self.find( "vendedordeclientesdisponivel", matching=0.97, waiting_time=10000):
                self.not_found("vendedordeclientesdisponivel")
            self.click_relative(482, 46)
            if not self.find( "achar", matching=0.97, waiting_time=10000):
                self.not_found("achar")
            self.click()
            if not self.find( "cod101teste", matching=0.97, waiting_time=10000):
                self.not_found("cod101teste")
            self.click()           
            if not self.find( "escolhe", matching=0.97, waiting_time=10000):
                self.not_found("escolhe")
            self.click()
            self.wait(1000)
            if not self.find( "planoprecominimo", matching=0.97, waiting_time=10000):
                self.not_found("planoprecominimo")
            self.click_relative(79, 25)
            
            if not self.find( "achar", matching=0.97, waiting_time=10000):
                self.not_found("achar")
            self.click()
            if not self.find( "codnulo", matching=0.97, waiting_time=10000):
                self.not_found("codnulo")
            self.click()
            if not self.find( "escolhe", matching=0.97, waiting_time=10000):
                self.not_found("escolhe")
            self.click()
            self.backspace()
            self.wait(1000)
            if not self.find( "planoprecomaximo", matching=0.97, waiting_time=10000):
                self.not_found("planoprecomaximo")
            self.click_relative(-13, 25)                       
            if not self.find( "achar", matching=0.97, waiting_time=10000):
                self.not_found("achar")
            self.click()
            if not self.find( "codnulo", matching=0.97, waiting_time=10000):
                self.not_found("codnulo")
            self.click()
            if not self.find( "escolhe", matching=0.97, waiting_time=10000):
                self.not_found("escolhe")
            self.click()
            self.backspace()
            
                            ####---MAPA FISCAL---####
                             
            if not self.find( "mapafiscalcliente", matching=0.97, waiting_time=10000):
                self.not_found("mapafiscalcliente")
            self.click_relative(84, 45)
            
            if not self.find( "achar", matching=0.97, waiting_time=10000):
                self.not_found("achar")
            self.click()
            if not self.find( "achacod1", matching=0.97, waiting_time=10000):
                self.not_found("achacod1")
            self.click()
            if not self.find( "escolhe", matching=0.97, waiting_time=10000):
                self.not_found("escolhe")
            self.click()
            self.wait(1000)
            if not self.find( "operacaosaidamapafiscal", matching=0.97, waiting_time=10000):
                self.not_found("operacaosaidamapafiscal")
            self.click_relative(481, 44)            
            if not self.find( "achar", matching=0.97, waiting_time=10000):
                self.not_found("achar")
            self.click()
            if not self.find( "achacod02", matching=0.97, waiting_time=10000):
                self.not_found("achacod02")
            self.click()
            if not self.find( "escolhe", matching=0.97, waiting_time=10000):
                self.not_found("escolhe")
            self.click()
            self.wait(1000)
            if not self.find( "cfopmapafiscal", matching=0.97, waiting_time=10000):
                self.not_found("cfopmapafiscal")
            self.click_relative(80, 26)
            self.backspace()
            if not self.find( "achar", matching=0.97, waiting_time=10000):
                self.not_found("achar")
            self.click()
            if not self.find( "cod1101", matching=0.97, waiting_time=10000):
                self.not_found("cod1101")
            self.click()
            if not self.find( "escolhe", matching=0.97, waiting_time=10000):
                self.not_found("escolhe")
            self.click()
            self.wait(1000)
            if not self.find( "cfopsubstituicaotributaria", matching=0.97, waiting_time=10000):
                self.not_found("cfopsubstituicaotributaria")
            self.click_relative(81, 24)
            self.backspace()
            if not self.find( "achar", matching=0.97, waiting_time=10000):
                self.not_found("achar")
            self.click()
            if not self.find( "cod1101", matching=0.97, waiting_time=10000):
                self.not_found("cod1101")
            self.click()
            if not self.find( "escolhe", matching=0.97, waiting_time=10000):
                self.not_found("escolhe")
            self.click()
            self.wait(1000)
            if not self.find( "cfopiss", matching=0.97, waiting_time=10000):
                self.not_found("cfopiss")
            self.click_relative(80, 27)
            self.backspace()
            if not self.find( "achar", matching=0.97, waiting_time=10000):
                self.not_found("achar")
            self.click()
            if not self.find( "cod1101", matching=0.97, waiting_time=10000):
                self.not_found("cod1101")
            self.click()
            if not self.find( "escolhe", matching=0.97, waiting_time=10000):
                self.not_found("escolhe")
            self.click()
            self.wait(1000)
            if not self.find( "operacaosaidaiss", matching=0.97, waiting_time=10000):
                self.not_found("operacaosaidaiss")
            self.click_relative(81, 26)
            if not self.find( "achar", matching=0.97, waiting_time=10000):
                self.not_found("achar")
            self.click()
            if not self.find( "achacod02", matching=0.97, waiting_time=10000):
                self.not_found("achacod02")
            self.click()
            if not self.find( "escolhe", matching=0.97, waiting_time=10000):
                self.not_found("escolhe")
            self.click()
            self.wait(1000)
            if not self.find( "indiceiss", matching=0.97, waiting_time=10000):
                self.not_found("indiceiss")
            self.click_relative(21, 27)
            self.type_keys_with_interval(1,'t1')
            self.enter()
            if not self.find( "indiceiss", matching=0.97, waiting_time=10000):
                self.not_found("indiceiss")
            self.click_relative(21, 27)
            self.backspace()
            self.type_keys_with_interval(1,'!')
            
                            ####---ABA5 P3---####
                             
            if not self.find( "aba5p3pa", matching=0.97, waiting_time=10000):
                self.not_found("aba5p3pa")
            self.click()
            if not self.find( "classificacaocodpadrao", matching=0.97, waiting_time=10000):
                self.not_found("classificacaocodpadrao")
            self.click_relative(83, 43)
            if not self.find( "cod00184", matching=0.97, waiting_time=10000):
                self.not_found("cod00184")
            self.click()
            if not self.find( "escolhe", matching=0.97, waiting_time=10000):
                self.not_found("escolhe")
            self.click()
            self.wait(1000)
            if not self.find( "moedapadrao", matching=0.97, waiting_time=10000):
                self.not_found("moedapadrao")
            self.click_relative(82, 26)
            if not self.find( "cod001real", matching=0.97, waiting_time=10000):
                self.not_found("cod001real")
            self.click()
            if not self.find( "escolhe", matching=0.97, waiting_time=10000):
                self.not_found("escolhe")
            self.click()
            self.wait(1000)
            if not self.find( "adiantamentoosa9p3", matching=0.97, waiting_time=10000):
                self.not_found("adiantamentoosa9p3")
            self.click_relative(-24, 25)
            if not self.find( "cod002dinheiro", matching=0.97, waiting_time=10000):
                self.not_found("cod002dinheiro")
            self.click()
            if not self.find( "escolhe", matching=0.97, waiting_time=10000):
                self.not_found("escolhe")
            self.click()
            self.wait(1000)
            if not self.find( "tptrocoa9p3", matching=0.97, waiting_time=10000):
                self.not_found("tptrocoa9p3")
            self.click_relative(-22, 25)
            if not self.find( "cod002dinheiro", matching=0.97, waiting_time=10000):
                self.not_found("cod002dinheiro")
            self.click()
            if not self.find( "escolhe", matching=0.97, waiting_time=10000):
                self.not_found("escolhe")
            self.click()
            self.wait(1000)
            if not self.find( "tpentradasa9p3", matching=0.97, waiting_time=10000):
                self.not_found("tpentradasa9p3")
            self.click_relative(-22, 24)
            if not self.find( "cod001real", matching=0.97, waiting_time=10000):
                self.not_found("cod001real")
            self.click()
            if not self.find( "escolhe", matching=0.97, waiting_time=10000):
                self.not_found("escolhe")
            self.click()
            self.wait(1000)
            if not self.find( "tpsaidasa9p3", matching=0.97, waiting_time=10000):
                self.not_found("tpsaidasa9p3")
            self.click_relative(-22, 26)
            if not self.find( "cod002dinheiro", matching=0.97, waiting_time=10000):
                self.not_found("cod002dinheiro")
            self.click()
            if not self.find( "escolhe", matching=0.97, waiting_time=10000):
                self.not_found("escolhe")
            self.click()
            self.wait(1000)
            if not self.find( "tpbaixaadiantamentosa9p3", matching=0.97, waiting_time=10000):
                self.not_found("tpbaixaadiantamentosa9p3")
            self.click_relative(-24, 28)
            if not self.find( "cod001real", matching=0.97, waiting_time=10000):
                self.not_found("cod001real")
            self.click()
            if not self.find( "escolhe", matching=0.97, waiting_time=10000):
                self.not_found("escolhe")
            self.click()
            self.wait(1000)
            
                            ####---CHEQUES RECEBIDOS---####
                             
            if not self.find( "contachequerecebido", matching=0.97, waiting_time=10000):
                self.not_found("contachequerecebido")
            self.click_relative(84, 44)
            if not self.find( "achar", matching=0.97, waiting_time=10000):
                self.not_found("achar")
            self.click()
            if not self.find( "cod001contacheque", matching=0.97, waiting_time=10000):
                self.not_found("cod001contacheque")
            self.click()           
            if not self.find( "escolhe", matching=0.97, waiting_time=10000):
                self.not_found("escolhe")
            self.click()
            self.wait(1000)
            if not self.find( "tipopagamentochequerecebido", matching=0.97, waiting_time=10000):
                self.not_found("tipopagamentochequerecebido")
            self.click_relative(483, 46)
            if not self.find( "cod001real", matching=0.97, waiting_time=10000):
                self.not_found("cod001real")
            self.click()
            if not self.find( "escolhe", matching=0.97, waiting_time=10000):
                self.not_found("escolhe")
            self.click()
            self.wait(1000)
            if not self.find( "chequesrecebidosoperacao", matching=0.97, waiting_time=10000):
                self.not_found("chequesrecebidosoperacao")
            self.click_relative(883, 44)
            if not self.find( "achar", matching=0.97, waiting_time=10000):
                self.not_found("achar")
            self.click()
            if not self.find( "cod0024pagamentos", matching=0.97, waiting_time=10000):
                self.not_found("cod0024pagamentos")
            self.click()
            if not self.find( "escolhe", matching=0.97, waiting_time=10000):
                self.not_found("escolhe")
            self.click()
            self.wait(1000)
            
                            ####---ABA9 P4---####
                             
            if not self.find( "aba9p4", matching=0.97, waiting_time=10000):
                self.not_found("aba9p4")
            self.click()
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            
                            ####---ABA10 ECOMMERCE---####
                             
            if not self.find( "aba10ecommerce", matching=0.97, waiting_time=10000):
                self.not_found("aba10ecommerce")
            self.click()                                         
            if not self.find( "empresacomecommerce", matching=0.97, waiting_time=10000):
                self.not_found("empresacomecommerce")
            self.click_relative(163, 27)
            self.type_up()
            self.enter()
            if not self.find( "empresacomecommerce", matching=0.97, waiting_time=10000):
                self.not_found("empresacomecommerce")
            self.click_relative(163, 27)
            self.type_down()
            self.enter()
            
            if not self.find( "vendedorpadrao", matching=0.97, waiting_time=10000):
                self.not_found("vendedorpadrao")
            self.click_relative(79, 25)
            if not self.find( "cod00101testevendedorpadrao", matching=0.97, waiting_time=10000):
                self.not_found("cod00101testevendedorpadrao")
            self.click()
            if not self.find( "escolhe", matching=0.97, waiting_time=10000):
                self.not_found("escolhe")
            self.click()
            self.wait(1000)
            if not self.find( "operacaopadraoecommerce", matching=0.97, waiting_time=10000):
                self.not_found("operacaopadraoecommerce")
            self.click_relative(80, 24)
            self.type_keys_with_interval(1,'te12')
            if not self.find( "escolhe", matching=0.97, waiting_time=10000):
                self.not_found("escolhe")
            self.click()
            self.wait(1000)
            if not self.find( "condicaodepagamentopadraoecommerce", matching=0.97, waiting_time=10000):
                self.not_found("condicaodepagamentopadraoecommerce")
            self.click_relative(80, 25)
            if not self.find( "cod0002vendassaida", matching=0.97, waiting_time=10000):
                self.not_found("cod0002vendassaida")
            self.click()
            if not self.find( "escolhe", matching=0.97, waiting_time=10000):
                self.not_found("escolhe")
            self.click()
            self.wait(1000)
            if not self.find( "planoprecopadrao", matching=0.97, waiting_time=10000):
                self.not_found("planoprecopadrao")
            self.click_relative(80, 23)
            if not self.find( "codnulo", matching=0.97, waiting_time=10000):
                self.not_found("codnulo")
            self.click()
            if not self.find( "escolhe", matching=0.97, waiting_time=10000):
                self.not_found("escolhe")
            self.click()
            self.backspace()
            
                            ####---FINALIZACAO---####
                             
            if not self.find( "salvarfimpa", matching=0.97, waiting_time=10000):
                self.not_found("salvarfimpa")
            self.click()
            if not self.find( "retornarfimpa", matching=0.97, waiting_time=10000):
                self.not_found("retornarfimpa")
            self.click()
            if not self.find( "localizape", matching=0.97, waiting_time=10000):
                self.not_found("localizape")
            self.click()
            if not self.find( "cod0101ictusteste", matching=0.97, waiting_time=10000):
                self.not_found("cod0101ictusteste")
            self.click()
            
            if not self.find( "editarfimpa", matching=0.97, waiting_time=10000):
                self.not_found("editarfimpa")
            self.click()
            if not self.find( "excluirfimpa", matching=0.97, waiting_time=10000):
                self.not_found("excluirfimpa")
            self.click()
            #if not self.find( "botaosimexcluirfimpa", matching=0.97, waiting_time=10000):
            #    self.not_found("botaosimexcluirfimpa")
            #self.click()
            self.enter()
            if not self.find( "retornarfimpa", matching=0.97, waiting_time=10000):
                self.not_found("retornarfimpa")
            self.click()
            if not self.find( "localizape", matching=0.97, waiting_time=10000):
                self.not_found("localizape")
            self.click()
            if not self.find( "retornarfimpa", matching=0.97, waiting_time=10000):
                self.not_found("retornarfimpa")
            self.click()
                             
                            ####---LIBERACAO E BLOQUEIO---####

            if not self.find( "abrircadastros_abacadastro", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro")
            self.click()
            if not self.find( "parametros", matching=0.97, waiting_time=10000):
                self.not_found("parametros")
            self.click()
            if not self.find( "liberacaoebloqueiodeperiodos", matching=0.97, waiting_time=10000):
                self.not_found("liberacaoebloqueiodeperiodos")
            self.click()
            if not self.find( "localizape", matching=0.97, waiting_time=10000):
                self.not_found("localizape")
            self.click()
            if not self.find( "editarpe", matching=0.97, waiting_time=10000):
                self.not_found("editarpe")
            self.click()
            self.wait(3500)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()
            if not self.find( "buscarempresaplb", matching=0.97, waiting_time=10000):
                self.not_found("buscarempresaplb")
            self.click()            
            if not self.find( "cod0101Bteste", matching=0.97, waiting_time=10000):
                self.not_found("cod0101Bteste")
            self.click()            
            if not self.find( "escolhe", matching=0.97, waiting_time=10000):
                self.not_found("escolhe")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
            if not self.find( "contasareceberpagaremissao", matching=0.97, waiting_time=10000):
                self.not_found("contasareceberpagaremissao")
            self.click_relative(213, 28)
            if not self.find( "carregarano", matching=0.97, waiting_time=10000):
                self.not_found("carregarano")
            self.click()
            if not self.find( "anoatual", matching=0.97, waiting_time=10000):
                self.not_found("anoatual")
            self.click()
            if not self.find( "contasareceberpagarvencimento", matching=0.97, waiting_time=10000):
                self.not_found("contasareceberpagarvencimento")
            self.click_relative(215, 28)
            if not self.find( "carregarano", matching=0.97, waiting_time=10000):
                self.not_found("carregarano")
            self.click()
            if not self.find( "anoatual", matching=0.97, waiting_time=10000):
                self.not_found("anoatual")
            self.click()
            if not self.find( "contasareceberpagarbaixa", matching=0.97, waiting_time=10000):
                self.not_found("contasareceberpagarbaixa")
            self.click_relative(213, 25)
            if not self.find( "carregarano", matching=0.97, waiting_time=10000):
                self.not_found("carregarano")
            self.click()
            if not self.find( "anoatual", matching=0.97, waiting_time=10000):
                self.not_found("anoatual")
            self.click()
            if not self.find( "movtodecontasemissao", matching=0.97, waiting_time=10000):
                self.not_found("movtodecontasemissao")
            self.click_relative(212, 26)
            if not self.find( "carregarano", matching=0.97, waiting_time=10000):
                self.not_found("carregarano")
            self.click()
            if not self.find( "anoatual", matching=0.97, waiting_time=10000):
                self.not_found("anoatual")
            self.click()
            if not self.find( "movtodecontasvencimento", matching=0.97, waiting_time=10000):
                self.not_found("movtodecontasvencimento")
            self.click_relative(213, 25)
            if not self.find( "carregarano", matching=0.97, waiting_time=10000):
                self.not_found("carregarano")
            self.click()
            if not self.find( "anoatual", matching=0.97, waiting_time=10000):
                self.not_found("anoatual")
            self.click()
            if not self.find( "movtodecontasbaixa", matching=0.97, waiting_time=10000):
                self.not_found("movtodecontasbaixa")
            self.click_relative(214, 28)
            if not self.find( "carregarano", matching=0.97, waiting_time=10000):
                self.not_found("carregarano")
            self.click()
            if not self.find( "anoatual", matching=0.97, waiting_time=10000):
                self.not_found("anoatual")
            self.click()
            if not self.find( "chequesrecebidosemissao", matching=0.97, waiting_time=10000):
                self.not_found("chequesrecebidosemissao")
            self.click_relative(213, 27)
            if not self.find( "carregarano", matching=0.97, waiting_time=10000):
                self.not_found("carregarano")
            self.click()
            if not self.find( "anoatual", matching=0.97, waiting_time=10000):
                self.not_found("anoatual")
            self.click()
            if not self.find( "chequesrecebidosvencimento", matching=0.97, waiting_time=10000):
                self.not_found("chequesrecebidosvencimento")
            self.click_relative(214, 26)
            if not self.find( "carregarano", matching=0.97, waiting_time=10000):
                self.not_found("carregarano")
            self.click()
            if not self.find( "anoatual", matching=0.97, waiting_time=10000):
                self.not_found("anoatual")
            self.click()
            if not self.find( "chequesrecebidosbaixa", matching=0.97, waiting_time=10000):
                self.not_found("chequesrecebidosbaixa")
            self.click_relative(215, 27)
            if not self.find( "carregarano", matching=0.97, waiting_time=10000):
                self.not_found("carregarano")
            self.click()
            if not self.find( "anoatual", matching=0.97, waiting_time=10000):
                self.not_found("anoatual")
            self.click()
            
                            ####---ABA2 CONTABIL E PATRIMONIO---####
            
            if not self.find( "aba2contabilepatrimonio", matching=0.97, waiting_time=10000):
                self.not_found("aba2contabilepatrimonio")
            self.click()
            if not self.find( "movimentocontabilintegracoes", matching=0.97, waiting_time=10000):
                self.not_found("movimentocontabilintegracoes")
            self.click_relative(113, 28)
            if not self.find( "carregarano", matching=0.97, waiting_time=10000):
                self.not_found("carregarano")
            self.click()
            if not self.find( "anoatual", matching=0.97, waiting_time=10000):
                self.not_found("anoatual")
            self.click()
            if not self.find( "movimentopatrimonio", matching=0.97, waiting_time=10000):
                self.not_found("movimentopatrimonio")
            self.click_relative(215, 28)            
            if not self.find( "carregarano", matching=0.97, waiting_time=10000):
                self.not_found("carregarano")
            self.click()
            if not self.find( "anoatual", matching=0.97, waiting_time=10000):
                self.not_found("anoatual")
            self.click()
            if not self.find( "movimentocontabillancamentos", matching=0.97, waiting_time=10000):
                self.not_found("movimentocontabillancamentos")
            self.click_relative(111, 27)
            if not self.find( "carregarano", matching=0.97, waiting_time=10000):
                self.not_found("carregarano")
            self.click()
            if not self.find( "anoatual", matching=0.97, waiting_time=10000):
                self.not_found("anoatual")
            self.click()
            
                            ####---ABA3 FISCAL---####
                             
            if not self.find( "aba3fiscalplb", matching=0.97, waiting_time=10000):
                self.not_found("aba3fiscalplb")
            self.click()
            if not self.find( "movimentofiscalintegracoes", matching=0.97, waiting_time=10000):
                self.not_found("movimentofiscalintegracoes")
            self.click_relative(213, 27)
            
            if not self.find( "carregarano", matching=0.97, waiting_time=10000):
                self.not_found("carregarano")
            self.click()
            if not self.find( "anoatual", matching=0.97, waiting_time=10000):
                self.not_found("anoatual")
            self.click()
            if not self.find( "movimentofiscallancamentos", matching=0.97, waiting_time=10000):
                self.not_found("movimentofiscallancamentos")
            self.click_relative(215, 28)
            
            if not self.find( "carregarano", matching=0.97, waiting_time=10000):
                self.not_found("carregarano")
            self.click()
            if not self.find( "anoatual", matching=0.97, waiting_time=10000):
                self.not_found("anoatual")
            self.click()
            
                            ####---ABA4 MOVIMENTO DE ITENS---####

            if not self.find( "aba4movimentosplb", matching=0.97, waiting_time=10000):
                self.not_found("aba4movimentosplb")
            self.click()
            if not self.find( "emissaoplb", matching=0.97, waiting_time=10000):
                self.not_found("emissaoplb")
            self.click_relative(36, 29)
            if not self.find( "carregarano", matching=0.97, waiting_time=10000):
                self.not_found("carregarano")
            self.click()
            if not self.find( "anoatual", matching=0.97, waiting_time=10000):
                self.not_found("anoatual")
            self.click()
            if not self.find( "movimentodeitensenfmovimento", matching=0.97, waiting_time=10000):
                self.not_found("movimentodeitensenfmovimento")
            self.click_relative(213, 28)
            
            if not self.find( "carregarano", matching=0.97, waiting_time=10000):
                self.not_found("carregarano")
            self.click()
            if not self.find( "anoatual", matching=0.97, waiting_time=10000):
                self.not_found("anoatual")
            self.click()
            
                            ####---ABA5 RH---####
            
            if not self.find( "aba5rhplb", matching=0.97, waiting_time=10000):
                self.not_found("aba5rhplb")
            self.click()                    
            if not self.find( "folhadepagamentopagamento", matching=0.97, waiting_time=10000):
                self.not_found("folhadepagamentopagamento")
            self.click_relative(215, 27)
            if not self.find( "carregarano", matching=0.97, waiting_time=10000):
                self.not_found("carregarano")
            self.click()
            if not self.find( "anoatual", matching=0.97, waiting_time=10000):
                self.not_found("anoatual")
            self.click()
            
                            ####---ABA6 BLOQUEIOS---####
                             
            if not self.find( "aba6bloqueiosplb", matching=0.97, waiting_time=10000):
                self.not_found("aba6bloqueiosplb")
            self.click()
            if not self.find( "contasareceberpagarvencimentobloqueios", matching=0.97, waiting_time=10000):
                self.not_found("contasareceberpagarvencimentobloqueios")
            self.click_relative(218, 30)
            if not self.find( "carregarano", matching=0.97, waiting_time=10000):
                self.not_found("carregarano")
            self.click()
            if not self.find( "anoatual", matching=0.97, waiting_time=10000):
                self.not_found("anoatual")
            self.click()
            
                            ####---ABA7 TRANSPORTES---####

            if not self.find( "aba7transportesplb", matching=0.97, waiting_time=10000):
                self.not_found("aba7transportesplb")
            self.click()
            if not self.find( "abastecimentosa7plb", matching=0.97, waiting_time=10000):
                self.not_found("abastecimentosa7plb")
            self.click_relative(213, 28)
            if not self.find( "carregarano", matching=0.97, waiting_time=10000):
                self.not_found("carregarano")
            self.click()
            if not self.find( "anoatual", matching=0.97, waiting_time=10000):
                self.not_found("anoatual")
            self.click()
            if not self.find( "ordemdeservicoa7plb", matching=0.97, waiting_time=10000):
                self.not_found("ordemdeservicoa7plb")
            self.click_relative(213, 27)
            if not self.find( "carregarano", matching=0.97, waiting_time=10000):
                self.not_found("carregarano")
            self.click()
            if not self.find( "anoatual", matching=0.97, waiting_time=10000):
                self.not_found("anoatual")
            self.click()
            if not self.find( "acertodeviagema7plb", matching=0.97, waiting_time=10000):
                self.not_found("acertodeviagema7plb")
            self.click_relative(214, 26)
            if not self.find( "carregarano", matching=0.97, waiting_time=10000):
                self.not_found("carregarano")
            self.click()
            if not self.find( "anoatual", matching=0.97, waiting_time=10000):
                self.not_found("anoatual")
            self.click()
            
                            ####---FIM PLB---####

            if not self.find( "salvarfimpa", matching=0.97, waiting_time=10000):
                self.not_found("salvarfimpa")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizape", matching=0.97, waiting_time=10000):
                self.not_found("localizape")
            self.click()
            if not self.find( "cod0101ictusteste", matching=0.97, waiting_time=10000):
                self.not_found("cod0101ictusteste")
            self.click()           
            if not self.find( "editarfimpa", matching=0.97, waiting_time=10000):
                self.not_found("editarfimpa")
            self.click()
            if not self.find( "excluirfimpa", matching=0.97, waiting_time=10000):
                self.not_found("excluirfimpa")
            self.click()
            #if not self.find( "botaosimexcluirfimpa", matching=0.97, waiting_time=10000):
            #    self.not_found("botaosimexcluirfimpa")
            #self.click()
            self.enter()
            if not self.find( "retornarfimpa", matching=0.97, waiting_time=10000):
                self.not_found("retornarfimpa")
            self.click()
            if not self.find( "localizape", matching=0.97, waiting_time=10000):
                self.not_found("localizape")
            self.click()
            if not self.find( "retornarfimpa", matching=0.97, waiting_time=10000):
                self.not_found("retornarfimpa")
            self.click()

                            ####---RECEITUARIO---####
                
            if not self.find( "abrircadastros_abacadastro", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro")
            self.click()
            if not self.find( "parametros", matching=0.97, waiting_time=10000):
                self.not_found("parametros")
            self.click()
            if not self.find( "receituario", matching=0.97, waiting_time=10000):
                self.not_found("receituario")
            self.click()
            if not self.find( "localizape", matching=0.97, waiting_time=10000):
                self.not_found("localizape")
            self.click()
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()
            if not self.find( "empresareceituario", matching=0.97, waiting_time=10000):
                self.not_found("empresareceituario")
            self.click_relative(97, 4)
            if not self.find( "cod0101comnometeste", matching=0.97, waiting_time=10000):
                self.not_found("cod0101comnometeste")
            self.click()            
            if not self.find( "escolhe", matching=0.97, waiting_time=10000):
                self.not_found("escolhe")
            self.click()
            if not self.find( "usuarioreceituario", matching=0.97, waiting_time=10000):
                self.not_found("usuarioreceituario")
            self.click_relative(61, 5)
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "senhareceituario", matching=0.97, waiting_time=10000):
                self.not_found("senhareceituario")
            self.click_relative(70, 4)
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "chavereceituario", matching=0.97, waiting_time=10000):
                self.not_found("chavereceituario")
            self.click_relative(76, 4)
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "agronomoreceituario", matching=0.97, waiting_time=10000):
                self.not_found("agronomoreceituario")
            self.click_relative(116, 4)
            if not self.find( "localizape", matching=0.97, waiting_time=10000):
                self.not_found("localizape")
            self.click()
            if not self.find( "cod0081260agroreceituario", matching=0.97, waiting_time=10000):
                self.not_found("cod0081260agroreceituario")
            self.click()
            if not self.find( "escolhe", matching=0.97, waiting_time=10000):
                self.not_found("escolhe")
            self.click()
            if not self.find( "agronomoreceituario2", matching=0.97, waiting_time=10000):
                self.not_found("agronomoreceituario2")
            self.click_relative(76, 5)
            self.type_keys_with_interval(1,'0081260')
            self.enter()
            if not self.find( "aplicacaoreceituario1", matching=0.97, waiting_time=10000):
                self.not_found("aplicacaoreceituario1")
            self.click_relative(9, 26)
            if not self.find( "aplicacaoreceituario2", matching=0.97, waiting_time=10000):
                self.not_found("aplicacaoreceituario2")
            self.click_relative(92, 27)
            if not self.find( "dosereceituario1", matching=0.97, waiting_time=10000):
                self.not_found("dosereceituario1")
            self.click_relative(8, 26)
            if not self.find( "dosereceituario2", matching=0.97, waiting_time=10000):
                self.not_found("dosereceituario2")
            self.click_relative(92, 26)
            if not self.find( "salvarfimpa", matching=0.97, waiting_time=10000):
                self.not_found("salvarfimpa")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizape", matching=0.97, waiting_time=10000):
                self.not_found("localizape")
            self.click()
            if not self.find( "cod0101Aprteste", matching=0.97, waiting_time=10000):
                self.not_found("cod0101Aprteste")
            self.click()            
            if not self.find( "editarfimpa", matching=0.97, waiting_time=10000):
                self.not_found("editarfimpa")
            self.click()
            if not self.find( "excluirfimpa", matching=0.97, waiting_time=10000):
                self.not_found("excluirfimpa")
            self.click()
            #if not self.find( "botaosimexcluirfimpa", matching=0.97, waiting_time=10000):
            #    self.not_found("botaosimexcluirfimpa")
            #self.click()
            self.enter()
            if not self.find( "retornarfimpa", matching=0.97, waiting_time=10000):
                self.not_found("retornarfimpa")
            self.click()
            if not self.find( "localizape", matching=0.97, waiting_time=10000):
                self.not_found("localizape")
            self.click()
            if not self.find( "retornarfimpa", matching=0.97, waiting_time=10000):
                self.not_found("retornarfimpa")
            self.click()
            
             
                            ####---PAISES---#### 

            if not self.find( "abrircadastros_abacadastro", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro")
            self.click()
            if not self.find( "parametrosfiscais", matching=0.97, waiting_time=10000):
                self.not_found("parametrosfiscais")
            self.click()
            if not self.find( "regionalizacao", matching=0.97, waiting_time=10000):
                self.not_found("regionalizacao")
            self.click()
            if not self.find( "paises", matching=0.97, waiting_time=10000):
                self.not_found("paises")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()            
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            self.wait(500)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(1,'te12')
            self.enter()
            self.type_keys_with_interval(1,'te12')
            self.enter()
            if not self.find( "salvarpaises", matching=0.97, waiting_time=10000):
                self.not_found("salvarpaises")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()            
            if not self.find( "acharpaises", matching=0.97, waiting_time=10000):
                self.not_found("acharpaises")
            self.click()            
            if not self.find( "paisteste", matching=0.97, waiting_time=10000):
                self.not_found("paisteste")
            self.click()
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            if not self.find( "excluirpaisteste", matching=0.97, waiting_time=10000):
                self.not_found("excluirpaisteste")
            self.click()
            #if not self.find( "simexcluirteste", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirteste")
            #self.click()
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---REGIOES---####
                             
            if not self.find( "abrircadastros_abacadastro", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro")
            self.click()
            if not self.find( "parametrosfiscais", matching=0.97, waiting_time=10000):
                self.not_found("parametrosfiscais")
            self.click()
            if not self.find( "regionalizacao", matching=0.97, waiting_time=10000):
                self.not_found("regionalizacao")
            self.click()
            if not self.find( "regioes", matching=0.97, waiting_time=10000):
                self.not_found("regioes")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            self.wait(500)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "buscarpais", matching=0.97, waiting_time=10000):
                self.not_found("buscarpais")
            self.click_relative(68, 6)
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "selecionarpais", matching=0.97, waiting_time=10000):
                self.not_found("selecionarpais")
            self.click()
            if not self.find( "entradaestadual", matching=0.97, waiting_time=10000):
                self.not_found("entradaestadual")
            self.click()
            if not self.find( "entradainterestadual", matching=0.97, waiting_time=10000):
                self.not_found("entradainterestadual")
            self.click()
            if not self.find( "entradaimportacao", matching=0.97, waiting_time=10000):
                self.not_found("entradaimportacao")
            self.click()
            if not self.find( "saidaestadual", matching=0.97, waiting_time=10000):
                self.not_found("saidaestadual")
            self.click()
            if not self.find( "saidainterestadual", matching=0.97, waiting_time=10000):
                self.not_found("saidainterestadual")
            self.click()
            if not self.find( "saidaimportacao", matching=0.97, waiting_time=10000):
                self.not_found("saidaimportacao")
            self.click()
            if not self.find( "salvarpaises", matching=0.97, waiting_time=10000):
                self.not_found("salvarpaises")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "paisteste", matching=0.97, waiting_time=10000):
                self.not_found("paisteste")
            self.click()
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            if not self.find( "excluirpaisteste", matching=0.97, waiting_time=10000):
                self.not_found("excluirpaisteste")
            self.click()
            #if not self.find( "simexcluirteste", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirteste")
            #self.click()
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---ESTADOS---####
                                         
            if not self.find( "abrircadastros_abacadastro", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro")
            self.click()
            if not self.find( "parametrosfiscais", matching=0.97, waiting_time=10000):
                self.not_found("parametrosfiscais")
            self.click()
            if not self.find( "regionalizacao", matching=0.97, waiting_time=10000):
                self.not_found("regionalizacao")
            self.click()
            if not self.find( "estados", matching=0.97, waiting_time=10000):
                self.not_found("estados")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            self.wait(500)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()
            self.type_keys_with_interval(1,'te12!@')
            
            x=0
            while x<27:
                if not self.find( "sigla", matching=0.97, waiting_time=10000):
                    self.not_found("sigla")
                self.click_relative(174, 4)
                self.type_down()
                self.enter()
                x=x+1
                
            if not self.find( "regiaobuscar", matching=0.97, waiting_time=10000):
                self.not_found("regiaobuscar")
            self.click_relative(81, 6)
            if not self.find( "cod001bpararegiao", matching=0.97, waiting_time=10000):
                self.not_found("cod001bpararegiao")
            self.click()
            if not self.find( "selecionarpais", matching=0.97, waiting_time=10000):
                self.not_found("selecionarpais")
            self.click()
            
            x=0
            while x<28:
                if not self.find( "codigoibge", matching=0.97, waiting_time=10000):
                    self.not_found("codigoibge")
                self.click_relative(210, 8)
                self.type_down()
                self.enter()
                x=x+1
            
            if not self.find( "salvarpaises", matching=0.97, waiting_time=10000):
                self.not_found("salvarpaises")
            self.click()
            
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "digiteparalocalizar", matching=0.97, waiting_time=10000):
                self.not_found("digiteparalocalizar")
            self.click_relative(36, 31)
            self.type_keys_with_interval(1,'te')
            self.enter()
            if not self.find( "codtesteestados", matching=0.97, waiting_time=10000):
                self.not_found("codtesteestados")
            self.click()
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            if not self.find( "excluirpaisteste", matching=0.97, waiting_time=10000):
                self.not_found("excluirpaisteste")
            self.click()
            #if not self.find( "simexcluirteste", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirteste")
            #self.click()
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---MUNICIPIOS---####
                             
            if not self.find( "abrircadastros_abacadastro", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro")
            self.click()
            if not self.find( "parametrosfiscais", matching=0.97, waiting_time=10000):
                self.not_found("parametrosfiscais")
            self.click()
            if not self.find( "regionalizacao", matching=0.97, waiting_time=10000):
                self.not_found("regionalizacao")
            self.click()
            if not self.find( "municipios", matching=0.97, waiting_time=10000):
                self.not_found("municipios")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                    self.not_found("editarfim")
            self.click()
            self.wait(500)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "buscarestado", matching=0.97, waiting_time=10000):
                self.not_found("buscarestado")
            self.click_relative(79, 4)
            if not self.find( "cod001pestado", matching=0.97, waiting_time=10000):
                self.not_found("cod001pestado")
            self.click()
            if not self.find( "selecionarpais", matching=0.97, waiting_time=10000):
                self.not_found("selecionarpais")
            self.click()
            self.enter()
            self.enter()
            self.type_keys_with_interval(1,'123')
            self.enter()
            self.type_keys_with_interval(1,'123')
            self.enter()
            self.type_keys_with_interval(1,'123')
            self.enter()
            self.type_keys_with_interval(1,'123')
            self.enter()
            self.type_keys_with_interval(1,'123')
            self.enter()
            self.type_keys_with_interval(1,'123')
            self.enter()
            self.type_keys_with_interval(1,'1')
            if not self.find( "feriadosmunicipais", matching=0.97, waiting_time=10000):
                self.not_found("feriadosmunicipais")
            self.click()
            if not self.find( "salvarpaises", matching=0.97, waiting_time=10000):
                self.not_found("salvarpaises")
            self.click()
            if not self.find( "incluirregistroferiado", matching=0.97, waiting_time=10000):
                self.not_found("incluirregistroferiado")
            self.click()
            
            x=0
            while x<31:
                if not self.find( "dia", matching=0.97, waiting_time=10000):
                    self.not_found("dia")
                self.click_relative(84, 7)
                self.type_down()
                self.enter()
                x=x+1
                
            x=0
            while x<12:
                if not self.find( "mes", matching=0.97, waiting_time=10000):
                    self.not_found("mes")
                self.click_relative(160, 6)
                self.type_down()
                self.enter()
                x=x+1
           
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            if not self.find( "savecommit", matching=0.97, waiting_time=10000):
                self.not_found("savecommit")
            self.click()
            if not self.find( "excluirferiado", matching=0.97, waiting_time=10000):
                self.not_found("excluirferiado")
            self.click()
            self.enter()
            #if not self.find( "simexcluirferiado", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirferiado")
            #self.click()
            if not self.find( "excluirpaisteste", matching=0.97, waiting_time=10000):
                self.not_found("excluirpaisteste")
            self.click()
            self.enter()
            #if not self.find( "simexcluirteste", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirteste")
            #self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---GRUPO FISCAL DE ITENS---####
                             
            if not self.find( "abrircadastros_abacadastro", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro")
            self.click()
            if not self.find( "parametrosfiscais", matching=0.97, waiting_time=10000):
                self.not_found("parametrosfiscais")
            self.click()
            if not self.find( "grupofiscaldeitens", matching=0.97, waiting_time=10000):
                self.not_found("grupofiscaldeitens")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                    self.not_found("editarfim")
            self.click()
            self.wait(500)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.enter()
            self.type_keys_with_interval(1,'99')
            self.enter()
            if not self.find( "salvarpaises", matching=0.97, waiting_time=10000):
                self.not_found("salvarpaises")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "codtesteestados", matching=0.97, waiting_time=10000):
                self.not_found("codtesteestados")
            self.click()
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            if not self.find( "excluirpaisteste", matching=0.97, waiting_time=10000):
                self.not_found("excluirpaisteste")
            self.click()
            self.enter()
            #if not self.find( "simexcluirteste", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirteste")
            #self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---CODIGOS DE OPERACAO---####
                             
            if not self.find( "abrircadastros_abacadastro", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro")
            self.click()
            if not self.find( "parametrosfiscais", matching=0.97, waiting_time=10000):
                self.not_found("parametrosfiscais")
            self.click()
            if not self.find( "codigosdeoperacao", matching=0.97, waiting_time=10000):
                self.not_found("codigosdeoperacao")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            self.wait(500)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            self.wait(500)
            if not self.find( "incluirco", matching=0.97, waiting_time=10000):
                self.not_found("incluirco")
            self.click()           
            #if not self.find( "naoimportarcodigooperacao", matching=0.97, waiting_time=10000):
            #    self.not_found("naoimportarcodigooperacao")
            #self.click()
            self.type_right()
            self.enter()
            if not self.find( "descricao", matching=0.97, waiting_time=10000):
                self.not_found("descricao")
            self.click_relative(20, 30)
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "tipo", matching=0.97, waiting_time=10000):
                self.not_found("tipo")
            self.click_relative(108, 25)
            self.type_up()
            self.enter()    
            if not self.find( "tipo", matching=0.97, waiting_time=10000):
                self.not_found("tipo")
            self.click_relative(108, 25)
            self.type_down()
            self.enter() 
            if not self.find( "tipo", matching=0.97, waiting_time=10000):
                self.not_found("tipo")
            self.click_relative(108, 25)
            self.type_down()
            self.enter()
            if not self.find( "tipo", matching=0.97, waiting_time=10000):
                self.not_found("tipo")
            self.click_relative(108, 25)
            self.type_up()
            self.enter()
            if not self.find( "dadosdaoperacao", matching=0.97, waiting_time=10000):
                self.not_found("dadosdaoperacao")
            self.click()
            if not self.find( "operacaoestoque", matching=0.97, waiting_time=10000):
                self.not_found("operacaoestoque")
            self.click_relative(99, 27)
            self.type_up()
            self.enter()
            if not self.find( "operacaoestoque", matching=0.97, waiting_time=10000):
                self.not_found("operacaoestoque")
            self.click_relative(99, 27)
            self.type_down()
            self.enter()
            if not self.find( "operacaoestoque", matching=0.97, waiting_time=10000):
                self.not_found("operacaoestoque")
            self.click_relative(99, 27)
            self.type_down()
            self.enter()
            if not self.find( "operacaoestoque", matching=0.97, waiting_time=10000):
                self.not_found("operacaoestoque")
            self.click_relative(99, 27)
            self.type_up()
            self.enter()
            if not self.find( "operacaocomissao", matching=0.97, waiting_time=10000):
                self.not_found("operacaocomissao")
            self.click_relative(99, 28)
            self.type_down()
            self.enter()
            if not self.find( "operacaocomissao", matching=0.97, waiting_time=10000):
                self.not_found("operacaocomissao")
            self.click_relative(99, 28)
            self.type_down()
            self.enter()
            if not self.find( "operacaocomissao", matching=0.97, waiting_time=10000):
                self.not_found("operacaocomissao")
            self.click_relative(99, 28)
            self.type_up()
            self.enter()
            if not self.find( "operacaocomissao", matching=0.97, waiting_time=10000):
                self.not_found("operacaocomissao")
            self.click_relative(99, 28)
            self.type_up()
            self.enter()
            
            x=0
            while x<3:
                if not self.find( "tipodofinanceiro", matching=0.97, waiting_time=10000):
                    self.not_found("tipodofinanceiro")
                self.click_relative(120, 26)
                self.type_down()
                self.enter()
                x=x+1
           
            x=0
            while x<3:
                if not self.find( "tipodofinanceiro", matching=0.97, waiting_time=10000):
                    self.not_found("tipodofinanceiro")
                self.click_relative(120, 26)
                self.type_up()
                self.enter()
                x=x+1
            
            x=0
            while x<32:
                if not self.find( "tipodemovimentacao", matching=0.97, waiting_time=10000):
                    self.not_found("tipodemovimentacao")
                self.click_relative(213, 23)
                self.type_down()
                self.enter()
                x=x+1
                
            if not self.find( "valomovimentacao", matching=0.97, waiting_time=10000):
                self.not_found("valomovimentacao")
            self.click_relative(107, 26)
            self.type_down()
            self.enter()
            
            x=0
            while x<7:
                if not self.find( "valomovimentacao", matching=0.97, waiting_time=10000):
                    self.not_found("valomovimentacao")
                self.click_relative(107, 26)
                self.type_up()
                self.enter()
                x=x+1
                
            x=0
            while x<3:         
                if not self.find( "subtotalizacaonota", matching=0.97, waiting_time=10000):
                    self.not_found("subtotalizacaonota")
                self.click_relative(89, 26)
                self.type_down()
                self.enter()
                x=x+1
                
            if not self.find( "tipodoemitente", matching=0.97, waiting_time=10000):
                self.not_found("tipodoemitente")
            self.click_relative(144, 28)
            self.type_down()
            self.enter()
            if not self.find( "tipodoemitente", matching=0.97, waiting_time=10000):
                self.not_found("tipodoemitente")
            self.click_relative(144, 28)
            self.type_down()
            self.enter()
            
            if not self.find( "tipolanctodmed", matching=0.97, waiting_time=10000):
                self.not_found("tipolanctodmed")
            self.click_relative(105, 25)
            self.type_down()
            self.enter()
            if not self.find( "tipolanctodmed", matching=0.97, waiting_time=10000):
                self.not_found("tipolanctodmed")
            self.click_relative(105, 25)
            self.type_down()
            self.enter()
            
            x=0
            while x<2:
                if not self.find( "tipolanctodmed", matching=0.97, waiting_time=10000):
                    self.not_found("tipolanctodmed")
                self.click_relative(105, 25)
                self.type_up()
                self.enter()
                x=x+1
                
            x=0
            while x<3:
                if not self.find( "tipodocumentoefdreinf", matching=0.97, waiting_time=10000):
                    self.not_found("tipodocumentoefdreinf")
                self.click_relative(108, 23)
                self.type_down()
                self.enter()
                x=x+1
                
            x=0
            while x<3:
                if not self.find( "tipodocumentoefdreinf", matching=0.97, waiting_time=10000):
                    self.not_found("tipodocumentoefdreinf")
                self.click_relative(108, 23)
                self.type_up()
                self.enter()
                x=x+1
                
            x=0
            while x<2:
                if not self.find( "tipodocontroledesaldo", matching=0.97, waiting_time=10000):
                    self.not_found("tipodocontroledesaldo")
                self.click_relative(147, 28)
                self.type_up()
                self.enter()
                x=x+1
            x=0
            while x<2:
                if not self.find( "tipodocontroledesaldo", matching=0.97, waiting_time=10000):
                    self.not_found("tipodocontroledesaldo")
                self.click_relative(147, 28)
                self.type_down()
                self.enter()
                x=x+1 
                
            x=0
            while x<6:
                if not self.find( "naturezaoperaacomunicipal", matching=0.97, waiting_time=10000):
                    self.not_found("naturezaoperaacomunicipal")
                self.click_relative(163, 25)
                self.type_down()
                self.enter()
                x=x+1
            x=0
            while x<7:
                if not self.find( "indicadordanaturezadofretecontratado", matching=0.97, waiting_time=10000):
                    self.not_found("indicadordanaturezadofretecontratado")
                self.click_relative(210, 27)
                self.type_down()
                self.enter()
                x=x+1
                
            if not self.find( "indicadordepresenca", matching=0.97, waiting_time=10000):
                self.not_found("indicadordepresenca")
            self.click_relative(210, 25)
            self.type_up()
            self.enter()
            
            x=0
            while x<6:
                if not self.find( "indicadordepresenca", matching=0.97, waiting_time=10000):
                    self.not_found("indicadordepresenca")
                self.click_relative(210, 25)
                self.type_down()
                self.enter()
                x=x+1
               
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            
            x=0
            while x<6:
                if not self.find( "custopedidocompranota", matching=0.97, waiting_time=10000):
                    self.not_found("custopedidocompranota")
                self.click_relative(120, 27)
                self.type_up()
                self.enter()
                x=x+1
                
                            ####---INDICADORES E ALIQUOTAS---####
                             
            if not self.find( "tipofunrural", matching=0.97, waiting_time=10000):
                self.not_found("tipofunrural")
            self.click_relative(107, 28)
            self.type_down()
            self.enter()
            if not self.find( "tipofunrural", matching=0.97, waiting_time=10000):
                self.not_found("tipofunrural")
            self.click_relative(107, 28)
            self.type_up()
            self.enter()
            if not self.find( "tipofunrural", matching=0.97, waiting_time=10000):
                self.not_found("tipofunrural")
            self.click_relative(107, 28)
            self.type_up()
            self.enter()
            if not self.find( "tipofunrural", matching=0.97, waiting_time=10000):
                self.not_found("tipofunrural")
            self.click_relative(107, 28)
            self.type_down()
            self.enter()
            self.type_keys_with_interval(1,'123')
            
            x=0
            while x<3:
                if not self.find( "tiposenar", matching=0.97, waiting_time=10000):
                    self.not_found("tiposenar")
                self.click_relative(111, 25)
                self.type_down()
                self.enter()
                x=x+1
                
            if not self.find( "tiposenar", matching=0.97, waiting_time=10000):
                self.not_found("tiposenar")
            self.click_relative(111, 25)
            self.type_up()
            self.enter()
            
            self.type_keys_with_interval(1,'123')
            
            if not self.find( "quotacapitalfethab", matching=0.97, waiting_time=10000):
                self.not_found("quotacapitalfethab")
            self.click_relative(109, 27)
            self.type_up()
            self.enter()
            if not self.find( "quotacapitalfethab", matching=0.97, waiting_time=10000):
                self.not_found("quotacapitalfethab")
            self.click_relative(109, 27)
            self.type_down()
            self.enter()
            if not self.find( "quotacapitalfethab", matching=0.97, waiting_time=10000):
                self.not_found("quotacapitalfethab")
            self.click_relative(109, 27)
            self.type_down()
            self.enter()
            if not self.find( "quotacapitalfethab", matching=0.97, waiting_time=10000):
                self.not_found("quotacapitalfethab")
            self.click_relative(109, 27)
            self.type_up()
            self.enter()
            self.type_keys_with_interval(1,'123')
            
            if not self.find( "tipodespadmfacs", matching=0.97, waiting_time=10000):
                self.not_found("tipodespadmfacs")
            self.click_relative(112, 24)
            self.type_up()
            self.enter()
            if not self.find( "tipodespadmfacs", matching=0.97, waiting_time=10000):
                self.not_found("tipodespadmfacs")
            self.click_relative(112, 24)
            self.type_down()
            self.enter()
            if not self.find( "tipodespadmfacs", matching=0.97, waiting_time=10000):
                self.not_found("tipodespadmfacs")
            self.click_relative(112, 24)
            self.type_down()
            self.enter()
            self.type_keys_with_interval(1,'123')
            self.enter()
            self.type_keys_with_interval(1,'123')
            self.enter()
            self.type_keys_with_interval(1,'123')
            self.enter()
            self.type_keys_with_interval(1,'123')
            
            x=0
            while x<3:
                if not self.find( "calcularicmssimples", matching=0.97, waiting_time=10000):
                    self.not_found("calcularicmssimples")
                self.click_relative(100, 28)
                self.type_down()
                self.enter()
                x=x+1
                
            x=0
            while x<6:
                if not self.find( "piscofinsnaturezadaretencao", matching=0.97, waiting_time=10000):
                    self.not_found("piscofinsnaturezadaretencao")
                self.click_relative(152, 27)
                self.type_down()
                self.enter()
                x=x+1
                
            x=0
            while x<2:
                if not self.find( "piscofinsnaturezadareceita", matching=0.97, waiting_time=10000):
                    self.not_found("piscofinsnaturezadareceita")
                self.click_relative(192, 27)
                self.type_down()
                self.enter()
                x=x+1
                
                            ####---BASES ADICIONAIS ICMS E ICMS ST---####
            
            x=0
            while x<4:                 
                if not self.find( "basesadicionaisicmseicmsst", matching=0.97, waiting_time=10000):
                    self.not_found("basesadicionaisicmseicmsst")
                self.click_relative(147, 46)
                self.type_down()
                self.enter()
                x=x+1
                
            x=0
            while x<4:
                if not self.find( "baiist", matching=0.97, waiting_time=10000):
                    self.not_found("baiist")
                self.click_relative(309, 46)
                self.type_down()
                self.enter()
                x=x+1
            
            x=0
            while x<4:    
                if not self.find( "baiist", matching=0.97, waiting_time=10000):
                    self.not_found("baiist")
                self.click_relative(469, 45)
                self.type_down()
                self.enter()
                x=x+1
            
            x=0
            while x<4:   
                if not self.find( "bapc", matching=0.97, waiting_time=10000):
                    self.not_found("bapc")
                self.click_relative(139, 45)
                self.type_down()
                self.enter()
                x=x+1
                
            x=0
            while x<4:
                if not self.find( "bapc", matching=0.97, waiting_time=10000):
                    self.not_found("bapc")
                self.click_relative(299, 44)
                self.type_down()
                self.enter()
                x=x+1
                
            x=0
            while x<4:
                if not self.find( "bapc", matching=0.97, waiting_time=10000):
                    self.not_found("bapc")
                self.click_relative(462, 46)
                self.type_down()
                self.enter()
                x=x+1
            
                            ####---CONTABILIZACAO---####
                             
            x=0
            while x<3:
                if not self.find( "contabilizacaoporitemservico", matching=0.97, waiting_time=10000):
                    self.not_found("contabilizacaoporitemservico")
                self.click_relative(229, 25)
                self.type_down()
                self.enter()
                x=x+1
            x=0
            while x<3:
                if not self.find( "contabilizacaoporitemservico", matching=0.97, waiting_time=10000):
                    self.not_found("contabilizacaoporitemservico")
                self.click_relative(229, 25)
                self.type_up()
                self.enter()
                x=x+1
                
            if not self.find( "contabilizacaoliquido", matching=0.97, waiting_time=10000):
                self.not_found("contabilizacaoliquido")
            self.click()           
            if not self.find( "contabilizacaoliquidomarcado", matching=0.97, waiting_time=10000):
                self.not_found("contabilizacaoliquidomarcado")
            self.click()            
            if not self.find( "contabilizacaoporrcm", matching=0.97, waiting_time=10000):
                self.not_found("contabilizacaoporrcm")
            self.click()
            if not self.find( "contabilizacaoporrcmmarcado", matching=0.97, waiting_time=10000):
                self.not_found("contabilizacaoporrcmmarcado")
            self.click()
            
            
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            
                            ####---ABAIXANDO TELA---####
            
            if not self.find( "abaixartelaco", matching=0.97, waiting_time=10000):
                self.not_found("abaixartelaco")
            self.click()
            
            x=0
            while x<5:                 
                if not self.find( "abaixartelacomarcado", matching=0.97, waiting_time=10000):
                    self.not_found("abaixartelacomarcado")
                self.double_click()
                x=x+1       
            
                            ####---MARCADORES---####
            
            if not self.find( "nfdeimpostos", matching=0.97, waiting_time=10000):
               self.not_found("nfdeimpostos")
            self.click()
            if not self.find( "nfdeimpostosmarcado", matching=0.97, waiting_time=10000):
               self.not_found("nfdeimpostosmarcado")
            self.click()
            if not self.find( "nfpermitealterarimpostos", matching=0.97, waiting_time=10000):
               self.not_found("nfpermitealterarimpostos")
            self.click()
            if not self.find( "nfpermitealterarimpostosmarcado", matching=0.97, waiting_time=10000):
               self.not_found("nfpermitealterarimpostosmarcado")
            self.click()          
            if not self.find( "movimentacaodeativoimobilizad", matching=0.97, waiting_time=10000):
               self.not_found("movimentacaodeativoimobilizad")
            self.click()
            if not self.find( "movimentacaodeativoimobilizadmarcado", matching=0.97, waiting_time=10000):
               self.not_found("movimentacaodeativoimobilizadmarcado")
            self.click()
            if not self.find( "nfdecupomfiscal", matching=0.97, waiting_time=10000):
               self.not_found("nfdecupomfiscal")
            self.click()
            if not self.find( "nfdecupomfiscalmarcado", matching=0.97, waiting_time=10000):
               self.not_found("nfdecupomfiscalmarcado")
            self.click()
            if not self.find( "nfdeaquisicaofpm", matching=0.97, waiting_time=10000):
                self.not_found("nfdeaquisicaofpm")
            self.click()
            if not self.find( "nfdeaquisicaofpmmarcado", matching=0.97, waiting_time=10000):
                self.not_found("nfdeaquisicaofpmmarcado")
            self.click()
            if not self.find( "descontargestaoleite", matching=0.97, waiting_time=10000):
                 self.not_found("descontargestaoleite")
            self.click()
            if not self.find( "descontargestaoleitemarcado", matching=0.97, waiting_time=10000):
                self.not_found("descontargestaoleitemarcado")
            self.click()
            if not self.find( "gerareceituario", matching=0.97, waiting_time=10000):
                self.not_found("gerareceituario")
            self.click()
            if not self.find( "gerareceituariomarcado", matching=0.97, waiting_time=10000):
                self.not_found("gerareceituariomarcado")
            self.click()
            if not self.find( "gerareceituariosemnada", matching=0.97, waiting_time=10000):
                self.not_found("gerareceituariosemnada")
            self.click()
            if not self.find( "geracontacorrente", matching=0.97, waiting_time=10000):
                self.not_found("geracontacorrente")
            self.click()
            if not self.find( "geracontacorrentemarcado", matching=0.97, waiting_time=10000):
                self.not_found("geracontacorrentemarcado")
            self.click()
            if not self.find( "gerademandasaida", matching=0.97, waiting_time=10000):
                self.not_found("gerademandasaida")
            self.click()
            if not self.find( "gerademandasaidamarcado", matching=0.97, waiting_time=10000):
                self.not_found("gerademandasaidamarcado")
            self.click()
            if not self.find( "operacaovendacompraefetiva", matching=0.97, waiting_time=10000):
                self.not_found("operacaovendacompraefetiva")
            self.click()
            if not self.find( "operacaodevendacompraefetivamarcado", matching=0.97, waiting_time=10000):
                self.not_found("operacaodevendacompraefetivamarcado")
            self.click()
            if not self.find( "movimentosomentecompedido", matching=0.97, waiting_time=10000):
                self.not_found("movimentosomentecompedido")
            self.click()
            if not self.find( "movimentosomentecompedidomarcado", matching=0.97, waiting_time=10000):
                self.not_found("movimentosomentecompedidomarcado")
            self.click()
            if not self.find( "calcularcustomedio", matching=0.97, waiting_time=10000):
                self.not_found("calcularcustomedio")
            self.click()
            if not self.find( "calcularcustomediomarcado", matching=0.97, waiting_time=10000):
                self.not_found("calcularcustomediomarcado")
            self.click()
            if not self.find( "atualizarmargem", matching=0.97, waiting_time=10000):
                self.not_found("atualizarmargem")
            self.click()
            if not self.find( "atualizarmargemmarcado", matching=0.97, waiting_time=10000):
                self.not_found("atualizarmargemmarcado")
            self.click()
            if not self.find( "validarunitdesconto1", matching=0.97, waiting_time=10000):
                self.not_found("validarunitdesconto1")
            self.click()
            if not self.find( "validarunitdescontomarcado", matching=0.97, waiting_time=10000):
                self.not_found("validarunitdescontomarcado")
            self.click()
            if not self.find( "validarunitdesconto", matching=0.97, waiting_time=10000):
                self.not_found("validarunitdesconto")
            self.click()
            if not self.find( "descontarvaloricmsdototalnf", matching=0.97, waiting_time=10000):
                self.not_found("descontarvaloricmsdototalnf")
            self.click()
            if not self.find( "descontarvaloricmsdototalnfmarcado", matching=0.97, waiting_time=10000):
                self.not_found("descontarvaloricmsdototalnfmarcado")
            self.click()
            if not self.find( "retencaoiss1", matching=0.97, waiting_time=10000):
                self.not_found("retencaoiss1")
            self.click()
            if not self.find( "retencaoissmarcado", matching=0.97, waiting_time=10000):
                self.not_found("retencaoissmarcado")
            self.click()
            if not self.find( "retencaoiss", matching=0.97, waiting_time=10000):
                self.not_found("retencaoiss")
            self.click()
            if not self.find( "atualizarprecodevenda", matching=0.97, waiting_time=10000):
                self.not_found("atualizarprecodevenda")
            self.click()
            if not self.find( "atualizarprecodevendamarcado", matching=0.97, waiting_time=10000):
                self.not_found("atualizarprecodevendamarcado")
            self.click()
            if not self.find( "atualizartabeladepreco", matching=0.97, waiting_time=10000):
                self.not_found("atualizartabeladepreco")
            self.click()
            if not self.find( "atualizartabeladeprecomarcado", matching=0.97, waiting_time=10000):
                self.not_found("atualizartabeladeprecomarcado")
            self.click()
            if not self.find( "geralivrosfiscais", matching=0.97, waiting_time=10000):
                self.not_found("geralivrosfiscais")
            self.click()
            if not self.find( "geralivrosfiscaismarcado", matching=0.97, waiting_time=10000):
                self.not_found("geralivrosfiscaismarcado")
            self.click()
            if not self.find( "gerardesdobrlf1", matching=0.97, waiting_time=10000):
                self.not_found("gerardesdobrlf1")
            self.click()
            if not self.find( "gerardesdoblfmarcado", matching=0.97, waiting_time=10000):
                self.not_found("gerardesdoblfmarcado")
            self.click()
            if not self.find( "gerardesdoblf", matching=0.97, waiting_time=10000):
                self.not_found("gerardesdoblf")
            self.click()
            if not self.find( "atualizarcustos", matching=0.97, waiting_time=10000):
                self.not_found("atualizarcustos")
            self.click()
            if not self.find( "atualizarcustosmarcado", matching=0.97, waiting_time=10000):
                self.not_found("atualizarcustosmarcado")
            self.click()
            if not self.find( "exigeliberacaosupervisor", matching=0.97, waiting_time=10000):
                self.not_found("exigeliberacaosupervisor")
            self.click()
            if not self.find( "exigeliberacaosupervisormarcado", matching=0.97, waiting_time=10000):
                self.not_found("exigeliberacaosupervisormarcado")
            self.click()
            if not self.find( "baseliquidaipi1", matching=0.97, waiting_time=10000):
                self.not_found("baseliquidaipi1")
            self.click()
            if not self.find( "baseliquidaipimarcado", matching=0.97, waiting_time=10000):
                self.not_found("baseliquidaipimarcado")
            self.click()
            if not self.find( "baseliquidaipi", matching=0.97, waiting_time=10000):
                self.not_found("baseliquidaipi")
            self.click()
            if not self.find( "valoripioutras1", matching=0.97, waiting_time=10000):
                self.not_found("valoripioutras1")
            self.click()
            if not self.find( "valoripiicmsmarcado", matching=0.97, waiting_time=10000):
                self.not_found("valoripiicmsmarcado")
            self.click()
            if not self.find( "valoripiicms", matching=0.97, waiting_time=10000):
                self.not_found("valoripiicms")
            self.click()
            if not self.find( "exigeveiculoautocenter", matching=0.97, waiting_time=10000):
                self.not_found("exigeveiculoautocenter")
            self.click()
            if not self.find( "exigeveiculoautocentermarcado", matching=0.97, waiting_time=10000):
                self.not_found("exigeveiculoautocentermarcado")
            self.click()
            if not self.find( "exigedref1", matching=0.97, waiting_time=10000):
                self.not_found("exigedref1")
            self.click()
            if not self.find( "exigedrefmarcado", matching=0.97, waiting_time=10000):
                self.not_found("exigedrefmarcado")
            self.click()
            if not self.find( "exigedref", matching=0.97, waiting_time=10000):
                self.not_found("exigedref")
            self.click()
            
                            ####---DADOS ADICIONAIS---####
                             
            if not self.find( "dadosadicionais", matching=0.97, waiting_time=10000):
                self.not_found("dadosadicionais")
            self.click()
            if not self.find( "cfoppadraomovimento", matching=0.97, waiting_time=10000):
                self.not_found("cfoppadraomovimento")
            self.click_relative(65, 27)
            if not self.find( "cod1352b", matching=0.97, waiting_time=10000):
                self.not_found("cod1352b")
            self.click()
            if not self.find( "selecionarcfoppadrao", matching=0.97, waiting_time=10000):
                self.not_found("selecionarcfoppadrao")
            self.click()
            if not self.find( "tabeladeprecositens", matching=0.97, waiting_time=10000):
                self.not_found("tabeladeprecositens")
            self.click_relative(69, 30)
            if not self.find( "cod00000tabela", matching=0.97, waiting_time=10000):
                self.not_found("cod00000tabela")
            self.click()
            if not self.find( "selecionarcfoppadrao", matching=0.97, waiting_time=10000):
                self.not_found("selecionarcfoppadrao")
            self.click()
            self.backspace()
            self.backspace()
            if not self.find( "tabeladeprecosservicos", matching=0.97, waiting_time=10000):
                self.not_found("tabeladeprecosservicos")
            self.click_relative(61, 25)
            if not self.find( "cod00000tabela", matching=0.97, waiting_time=10000):
                self.not_found("cod00000tabela")
            self.click()
            if not self.find( "selecionarcfoppadrao", matching=0.97, waiting_time=10000):
                self.not_found("selecionarcfoppadrao")
            self.click()
            self.backspace()
            self.backspace()
            if not self.find( "macrosparaobservacao", matching=0.97, waiting_time=10000):
                self.not_found("macrosparaobservacao")
            self.click_relative(28, 30)
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "camposdisponiveis", matching=0.97, waiting_time=10000):
                self.not_found("camposdisponiveis")
            self.click_relative(-13, 33)
            if not self.find( "clientesefornecedores", matching=0.97, waiting_time=10000):
                self.not_found("clientesefornecedores")
            self.click()
            if not self.find( "empresacodigo", matching=0.97, waiting_time=10000):
                self.not_found("empresacodigo")
            self.click()
            if not self.find( "inserir", matching=0.97, waiting_time=10000):
                self.not_found("inserir")
            self.click()
            if not self.find( "camposdisponiveis", matching=0.97, waiting_time=10000):
                self.not_found("camposdisponiveis")
            self.click_relative(-13, 33)
            if not self.find( "camposdevendedores", matching=0.97, waiting_time=10000):
                self.not_found("camposdevendedores")
            self.click()
            if not self.find( "empresacodigo", matching=0.97, waiting_time=10000):
                self.not_found("empresacodigo")
            self.click()
            if not self.find( "inserir", matching=0.97, waiting_time=10000):
                self.not_found("inserir")
            self.click()
            if not self.find( "camposdisponiveis", matching=0.97, waiting_time=10000):
                self.not_found("camposdisponiveis")
            self.click_relative(-13, 33)
            if not self.find( "condicaopagamento", matching=0.97, waiting_time=10000):
                self.not_found("condicaopagamento")
            self.click()
            if not self.find( "condicaocodigo", matching=0.97, waiting_time=10000):
                self.not_found("condicaocodigo")
            self.click()
            if not self.find( "inserir", matching=0.97, waiting_time=10000):
                self.not_found("inserir")
            self.click()
            
                            ####---FINALIZANDO CO---####
            
            if not self.find( "salvarco", matching=0.97, waiting_time=10000):
                self.not_found("salvarco")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "digiteparalocalizar", matching=0.97, waiting_time=10000):
                self.not_found("digiteparalocalizar")
            self.click_relative(36, 31)
            self.type_keys_with_interval(1,'te')
            self.enter()
            """
            if not self.find( "codtesteestados", matching=0.97, waiting_time=10000):
                self.not_found("codtesteestados")
            self.click()
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            if not self.find( "excluirpaisteste", matching=0.97, waiting_time=10000):
                self.not_found("excluirpaisteste")
            self.click()
            if not self.find( "simexcluirteste", matching=0.97, waiting_time=10000):
                self.not_found("simexcluirteste")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            """
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---CODIGOS FISCAIS---####
            
            if not self.find( "abrircadastros_abacadastro", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro")
            self.click()
            if not self.find( "parametrosfiscais", matching=0.97, waiting_time=10000):
                self.not_found("parametrosfiscais")
            self.click()
            if not self.find( "codigosfiscaiscfop", matching=0.97, waiting_time=10000):
                self.not_found("codigosfiscaiscfop")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "incluirco", matching=0.97, waiting_time=10000):
                self.not_found("incluirco")
            self.click()
            self.type_keys_with_interval(1,'8748')
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "operacaobuscacfop", matching=0.97, waiting_time=10000):
                self.not_found("operacaobuscacfop")
            self.click_relative(66, 48)
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "cod0001cfop", matching=0.97, waiting_time=10000):
                self.not_found("cod0001cfop")
            self.click()
            if not self.find( "selecionarcfoppadrao", matching=0.97, waiting_time=10000):
                self.not_found("selecionarcfoppadrao")
            self.click()
            if not self.find( "informacoesdagia", matching=0.97, waiting_time=10000):
                self.not_found("informacoesdagia")
            self.click_relative(21, 44)
            self.type_keys_with_interval(1,'t1')
            self.enter()
            self.type_keys_with_interval(1,'t!')
            self.enter()
            if not self.find( "valorcontabilincidenabasenagia", matching=0.97, waiting_time=10000):
                self.not_found("valorcontabilincidenabasenagia")
            self.click()
            
            if not self.find( "valorcontabilincidenabasenagiamarcado", matching=0.97, waiting_time=10000):
                self.not_found("valorcontabilincidenabasenagiamarcado")
            self.click()
            if not self.find( "seentradadeduzir", matching=0.97, waiting_time=10000):
                self.not_found("seentradadeduzir")
            self.click()
            if not self.find( "seentradadeduzirmarcado2", matching=0.97, waiting_time=10000):
                self.not_found("seentradadeduzirmarcado2")
            self.click()            
            if not self.find( "seentradadeduzirmarcado", matching=0.97, waiting_time=10000):
                self.not_found("seentradadeduzirmarcado")
            self.click()
            if not self.find( "ativoimobilizado", matching=0.97, waiting_time=10000):
                self.not_found("ativoimobilizado")
            self.click()
            if not self.find( "ativoimobilizadomarcado2", matching=0.97, waiting_time=10000):
                self.not_found("ativoimobilizadomarcado2")
            self.click()            
            if not self.find( "ativoimobilizadomarcado", matching=0.97, waiting_time=10000):
                self.not_found("ativoimobilizadomarcado")
            self.click()
            if not self.find( "materialdeusoeconsumolimpo", matching=0.97, waiting_time=10000):
                self.not_found("materialdeusoeconsumolimpo")
            self.click()            
            if not self.find( "materialdeusoeconsumo", matching=0.97, waiting_time=10000):
                self.not_found("materialdeusoeconsumo")
            self.click()           
            if not self.find( "materialdeusoeconsumomarcado", matching=0.97, waiting_time=10000):
                self.not_found("materialdeusoeconsumomarcado")
            self.click()
            if not self.find( "geraretencao", matching=0.97, waiting_time=10000):
                self.not_found("geraretencao")
            self.click()
            if not self.find( "geraretencaomarcado2", matching=0.97, waiting_time=10000):
                self.not_found("geraretencaomarcado2")
            self.click()           
            if not self.find( "geraretencaomarcado", matching=0.97, waiting_time=10000):
                self.not_found("geraretencaomarcado")
            self.click()
            if not self.find( "coddfc", matching=0.97, waiting_time=10000):
                self.not_found("coddfc")
            self.click_relative(12, 27)
            self.type_keys_with_interval(1,'t1!')
            self.enter()
            if not self.find( "ignorarnomovimentoerelatorio", matching=0.97, waiting_time=10000):
                self.not_found("ignorarnomovimentoerelatorio")
            self.click()
            if not self.find( "ignorarnomovimentoerelatoriomarcado", matching=0.97, waiting_time=10000):
                self.not_found("ignorarnomovimentoerelatoriomarcado")
            self.click()
            if not self.find( "industrializacao", matching=0.97, waiting_time=10000):
                self.not_found("industrializacao")
            self.click()
            if not self.find( "insdustrializacaomarcado2", matching=0.97, waiting_time=10000):
                self.not_found("insdustrializacaomarcado2")
            self.click()
            
            if not self.find( "industrializacaomarcado", matching=0.97, waiting_time=10000):
                self.not_found("industrializacaomarcado")
            self.click()
            if not self.find( "transporte", matching=0.97, waiting_time=10000):
                self.not_found("transporte")
            self.click()
            if not self.find( "transportemarcado2", matching=0.97, waiting_time=10000):
                self.not_found("transportemarcado2")
            self.click()
            
            if not self.find( "transportemarcado", matching=0.97, waiting_time=10000):
                self.not_found("transportemarcado")
            self.click()
            if not self.find( "externo", matching=0.97, waiting_time=10000):
                self.not_found("externo")
            self.click()
            if not self.find( "interno", matching=0.97, waiting_time=10000):
                self.not_found("interno")
            self.click()
            if not self.find( "insumos", matching=0.97, waiting_time=10000):
                self.not_found("insumos")
            self.click()
            if not self.find( "outros", matching=0.97, waiting_time=10000):
                self.not_found("outros")
            self.click()
            if not self.find( "mercadorias", matching=0.97, waiting_time=10000):
                self.not_found("mercadorias")
            self.click()
            if not self.find( "salvarco", matching=0.97, waiting_time=10000):
                self.not_found("salvarco")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "digiteparalocalizar", matching=0.97, waiting_time=10000):
                self.not_found("digiteparalocalizar")
            self.click_relative(36, 31)
            self.type_keys_with_interval(1,'te')
            self.enter()
            if not self.find( "codtesteestados", matching=0.97, waiting_time=10000):
                self.not_found("codtesteestados")
            self.click()
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            if not self.find( "excluirpaisteste", matching=0.97, waiting_time=10000):
                self.not_found("excluirpaisteste")
            self.click()
            self.enter()
            #if not self.find( "simexcluirteste", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirteste")
            #self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---CODIGOS FISCAIS IMP---####
                             
            if not self.find( "abrircadastros_abacadastro", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro")
            self.click()
            if not self.find( "parametrosfiscais", matching=0.97, waiting_time=10000):
                self.not_found("parametrosfiscais")
            self.click()
            if not self.find( "codigosfiscaisimportacao", matching=0.97, waiting_time=10000):
                self.not_found("codigosfiscaisimportacao")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            self.wait(500)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "incluirco", matching=0.97, waiting_time=10000):
                self.not_found("incluirco")
            self.click()
            if not self.find( "origem", matching=0.97, waiting_time=10000):
                self.not_found("origem")
            self.click_relative(102, 6)
            self.backspace()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "cod1911", matching=0.97, waiting_time=10000):
                self.not_found("cod1911")
            self.click()
            if not self.find( "selecionarcfoppadrao", matching=0.97, waiting_time=10000):
                self.not_found("selecionarcfoppadrao")
            self.click()
            self.wait(500)
            if not self.find( "destino", matching=0.97, waiting_time=10000):
                self.not_found("destino")
            self.click_relative(102, 5)
            self.backspace()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "cod1911", matching=0.97, waiting_time=10000):
                self.not_found("cod1911")
            self.click()
            if not self.find( "selecionarcfoppadrao", matching=0.97, waiting_time=10000):
                self.not_found("selecionarcfoppadrao")
            self.click()
            if not self.find( "salvarco", matching=0.97, waiting_time=10000):
                self.not_found("salvarco")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "cod1911", matching=0.97, waiting_time=10000):
                self.not_found("cod1911")
            self.click()
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            if not self.find( "excluirpaisteste", matching=0.97, waiting_time=10000):
                self.not_found("excluirpaisteste")
            self.click()
            self.enter()
            #if not self.find( "simexcluirteste", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirteste")
            #self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---DECRETOS E OBSERVACOES---####
                             
            if not self.find( "abrircadastros_abacadastro", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro")
            self.click()
            if not self.find( "parametrosfiscais", matching=0.97, waiting_time=10000):
                self.not_found("parametrosfiscais")
            self.click()
            if not self.find( "decretoseobservacoes", matching=0.97, waiting_time=10000):
                self.not_found("decretoseobservacoes")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            self.wait(500)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "incluirco", matching=0.97, waiting_time=10000):
                self.not_found("incluirco")
            self.click()
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "tipos", matching=0.97, waiting_time=10000):
                self.not_found("tipos")
            self.click_relative(372, 28)
            if not self.find( "tipos", matching=0.97, waiting_time=10000):
                self.not_found("tipos")
            self.click_relative(719, 27)
            if not self.find( "tipos", matching=0.97, waiting_time=10000):
                self.not_found("tipos")
            self.click_relative(1055, 26)
            if not self.find( "tipos", matching=0.97, waiting_time=10000):
                self.not_found("tipos")
            self.click_relative(30, 28)
            if not self.find( "salvarco", matching=0.97, waiting_time=10000):
                self.not_found("salvarco")
            self.click()
            if not self.find( "camposdecretos", matching=0.97, waiting_time=10000):
                self.not_found("camposdecretos")
            self.click_relative(59, -2)
            if not self.find( "camposdeclintes", matching=0.97, waiting_time=10000):
                self.not_found("camposdeclintes")
            self.click()
            if not self.find( "bancocodigodecreto", matching=0.97, waiting_time=10000):
                self.not_found("bancocodigodecreto")
            self.click()
            if not self.find( "inserirdecreto", matching=0.97, waiting_time=10000):
                self.not_found("inserirdecreto")
            self.click()
            if not self.find( "salvarco", matching=0.97, waiting_time=10000):
                self.not_found("salvarco")
            self.click()
            if not self.find( "camposdecretos", matching=0.97, waiting_time=10000):
                self.not_found("camposdecretos")
            self.click_relative(59, -2)
            if not self.find( "camposnfdecreto", matching=0.97, waiting_time=10000):
                self.not_found("camposnfdecreto")
            self.click()
            if not self.find( "bancocodigodecreto", matching=0.97, waiting_time=10000):
                self.not_found("bancocodigodecreto")
            self.click()
            if not self.find( "inserirdecreto", matching=0.97, waiting_time=10000):
                self.not_found("inserirdecreto")
            self.click()
            if not self.find( "salvarco", matching=0.97, waiting_time=10000):
                self.not_found("salvarco")
            self.click()
            if not self.find( "camposdecretos", matching=0.97, waiting_time=10000):
                self.not_found("camposdecretos")
            self.click_relative(59, -2)
            if not self.find( "camposdepedidosdevendadecreto", matching=0.97, waiting_time=10000):
                self.not_found("camposdepedidosdevendadecreto")
            self.click()
            if not self.find( "autenticodecreto", matching=0.97, waiting_time=10000):
                self.not_found("autenticodecreto")
            self.click()
            if not self.find( "inserirdecreto", matching=0.97, waiting_time=10000):
                self.not_found("inserirdecreto")
            self.click()
            if not self.find( "salvarco", matching=0.97, waiting_time=10000):
                self.not_found("salvarco")
            self.click()
            if not self.find( "camposdecretos", matching=0.97, waiting_time=10000):
                self.not_found("camposdecretos")
            self.click_relative(59, -2)
            if not self.find( "camposdeconhecimentosdecreto", matching=0.97, waiting_time=10000):
                self.not_found("camposdeconhecimentosdecreto")
            self.click()
            if not self.find( "anttconsigdecreto", matching=0.97, waiting_time=10000):
                self.not_found("anttconsigdecreto")
            self.click()
            if not self.find( "inserirdecreto", matching=0.97, waiting_time=10000):
                self.not_found("inserirdecreto")
            self.click()
            if not self.find( "salvarco", matching=0.97, waiting_time=10000):
                self.not_found("salvarco")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "descricaodecretoteste", matching=0.97, waiting_time=10000):
                self.not_found("descricaodecretoteste")
            self.click()
            
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            if not self.find( "excluirpaisteste", matching=0.97, waiting_time=10000):
                self.not_found("excluirpaisteste")
            self.click()
            self.enter()
            #if not self.find( "simexcluirteste", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirteste")
            #self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---SITUACOES---####
            
            if not self.find( "abrircadastros_abacadastro", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro")
            self.click()
            if not self.find( "parametrosfiscais", matching=0.97, waiting_time=10000):
                self.not_found("parametrosfiscais")
            self.click()
            if not self.find( "situacoes", matching=0.97, waiting_time=10000):
                self.not_found("situacoes")
            self.click()           
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            self.wait(500)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "incluirco", matching=0.97, waiting_time=10000):
                self.not_found("incluirco")
            self.click()
            if not self.find( "operacaosituacao", matching=0.97, waiting_time=10000):
                self.not_found("operacaosituacao")
            self.click_relative(50, 27)
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "buscarcoddeop", matching=0.97, waiting_time=10000):
                self.not_found("buscarcoddeop")
            self.click_relative(43, 29)
            self.type_keys_with_interval(1,'0048')
            self.enter()
            
            if not self.find( "codop0048", matching=0.97, waiting_time=10000):
                self.not_found("codop0048")
            self.click()
            if not self.find( "selecionarcfoppadrao", matching=0.97, waiting_time=10000):
                self.not_found("selecionarcfoppadrao")
            self.click()
            self.wait(500)
            if not self.find( "regiaosituacao", matching=0.97, waiting_time=10000):
                self.not_found("regiaosituacao")
            self.click_relative(47, 26)
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "nordestesituacao", matching=0.97, waiting_time=10000):
                self.not_found("nordestesituacao")
            self.click()                                  
            if not self.find( "selecionarcfoppadrao", matching=0.97, waiting_time=10000):
                self.not_found("selecionarcfoppadrao")
            self.click()
            self.wait(500)
            if not self.find( "grupofiscalsituacao", matching=0.97, waiting_time=10000):
                self.not_found("grupofiscalsituacao")
            self.click_relative(51, 30)
            if not self.find( "cod001btributado", matching=0.97, waiting_time=10000):
                self.not_found("cod001btributado")
            self.click()
            if not self.find( "selecionarcfoppadrao", matching=0.97, waiting_time=10000):
                self.not_found("selecionarcfoppadrao")
            self.click()
            
                            ####---ICMS---####
                             
            if not self.find( "icmsbasecalculo", matching=0.97, waiting_time=10000):
                self.not_found("icmsbasecalculo")
            self.click_relative(146, 50)            
            self.type_keys_with_interval(1,'123')
            if not self.find( "icmsbasecalculo", matching=0.97, waiting_time=10000):
                self.not_found("icmsbasecalculo")
            self.click_relative(140, 29)
            self.type_keys_with_interval(1,'123')
            x=0
            while x<5:
                if not self.find( "icmstipo", matching=0.97, waiting_time=10000):
                    self.not_found("icmstipo")
                self.click_relative(621, 47)
                self.type_down()
                self.enter()
                x=x+1
            x=0
            while x<5:
                if not self.find( "icmstipo", matching=0.97, waiting_time=10000):
                    self.not_found("icmstipo")
                self.click_relative(621, 47)
                self.type_up()
                self.enter()
                x=x+1
            if not self.find( "redutoraliquotabase", matching=0.97, waiting_time=10000):
                self.not_found("redutoraliquotabase")
            self.click_relative(140, 27)
            self.type_keys_with_interval(1,'123')
            if not self.find( "saldobasereduzicms", matching=0.97, waiting_time=10000):
                self.not_found("saldobasereduzicms")
            self.click_relative(142, 31)
            self.type_down()
            self.enter()
            if not self.find( "saldobasereduzicms", matching=0.97, waiting_time=10000):
                self.not_found("saldobasereduzicms")
            self.click_relative(142, 31)
            self.type_down()
            self.enter()
            if not self.find( "saldobasereduzicms", matching=0.97, waiting_time=10000):
                self.not_found("saldobasereduzicms")
            self.click_relative(142, 31)
            self.type_down()
            self.enter()
            x=0
            while x<4:
                if not self.find( "icmsmodalidade", matching=0.97, waiting_time=10000):
                    self.not_found("icmsmodalidade")
                self.click_relative(1261, 45)
                self.type_down()
                self.enter()
                x=x+1
            x=0
            while x<3:
                if not self.find( "icmsmodalidade", matching=0.97, waiting_time=10000):
                    self.not_found("icmsmodalidade")
                self.click_relative(1261, 45)
                self.type_up()
                self.enter()
                x=x+1
            x=0
            while x<20:
                if not self.find( "situacaotributariaicms", matching=0.97, waiting_time=10000):
                    self.not_found("situacaotributariaicms")
                self.click_relative(300, 96)
                self.type_down()
                self.enter()
                x=x+1
              
            if not self.find( "baseicmsdiferencaliquota", matching=0.97, waiting_time=10000):
                self.not_found("baseicmsdiferencaliquota")
            self.click_relative(141, 27)
            self.type_keys_with_interval(1,'123')
            if not self.find( "aliquotadiferencialicms", matching=0.97, waiting_time=10000):
                self.not_found("aliquotadiferencialicms")
            self.click_relative(142, 27)
            self.type_keys_with_interval(1,'123')
            if not self.find( "aliquotaicmsdesoneracao", matching=0.97, waiting_time=10000):
                self.not_found("aliquotaicmsdesoneracao")
            self.click_relative(141, 30)           
            self.type_keys_with_interval(1,'123')
            self.enter()
            
            x=0
            while x<12:
                if not self.find( "motivodesoneracaoicms", matching=0.97, waiting_time=10000):
                    self.not_found("motivodesoneracaoicms")
                self.click_relative(296, 26)
                self.type_down()
                self.enter()
                x=x+1
            self.enter()    
            if not self.find( "descontadovalortotalicms", matching=0.97, waiting_time=10000):
                self.not_found("descontadovalortotalicms")
            self.click()
            if not self.find( "descontadovalortotalmarcado", matching=0.97, waiting_time=10000):
                self.not_found("descontadovalortotalmarcado")
            self.click()
            if not self.find( "descontadovalortotal1", matching=0.97, waiting_time=10000):
                self.not_found("descontadovalortotal1")
            self.click()
            if not self.find( "calculardiferimentoicms", matching=0.97, waiting_time=10000):
                self.not_found("calculardiferimentoicms")
            self.click()
            if not self.find( "calculardiferimentomarcado", matching=0.97, waiting_time=10000):
                self.not_found("calculardiferimentomarcado")
            self.click()
            if not self.find( "calculardiferimento1", matching=0.97, waiting_time=10000):
                self.not_found("calculardiferimento1")
            self.click()
            if not self.find( "cteemoutrasuf", matching=0.97, waiting_time=10000):
                self.not_found("cteemoutrasuf")
            self.click()
            if not self.find( "cteemoutrasufmarcado", matching=0.97, waiting_time=10000):
                self.not_found("cteemoutrasufmarcado")
            self.click()
            if not self.find( "possuidiferencialaliquota", matching=0.97, waiting_time=10000):
                self.not_found("possuidiferencialaliquota")
            self.click()
            if not self.find( "possuidiferencialaliquotamarcado", matching=0.97, waiting_time=10000):
                self.not_found("possuidiferencialaliquotamarcado")
            self.click()
            if not self.find( "icmsstdifinterno", matching=0.97, waiting_time=10000):
                self.not_found("icmsstdifinterno")
            self.click_relative(197, 25)
            self.type_down()
            self.enter()
            if not self.find( "icmsstdifinterno", matching=0.97, waiting_time=10000):
                self.not_found("icmsstdifinterno")
            self.click_relative(197, 25)
            self.type_down()
            self.enter()
            
                            ####---ICMS SUBS TRIBU---####  
              
            if not self.find( "icmssubstrib", matching=0.97, waiting_time=10000):
                self.not_found("icmssubstrib")
            self.click_relative(143, 46)
            self.type_keys_with_interval(1,'123')
            if not self.find( "icmssubstibaliq", matching=0.97, waiting_time=10000):
                self.not_found("icmssubstibaliq")
            self.click_relative(305, 46)
            self.type_keys_with_interval(1,'123')
            if not self.find( "stnototaldodocumento", matching=0.97, waiting_time=10000):
                self.not_found("stnototaldodocumento")
            self.click_relative(140, 28)
            self.type_up()
            self.enter()
            if not self.find( "stnototaldodocumento", matching=0.97, waiting_time=10000):
                self.not_found("stnototaldodocumento")
            self.click_relative(140, 28)
            self.type_down()
            self.enter()
            if not self.find( "stnototaldodocumento", matching=0.97, waiting_time=10000):
                self.not_found("stnototaldodocumento")
            self.click_relative(140, 28)
            self.type_down()
            self.enter()
            self.enter()
            if not self.find( "reduzirvalordoicms", matching=0.97, waiting_time=10000):
                self.not_found("reduzirvalordoicms")
            self.click()
            if not self.find( "reduzirvalordoicmsmarcado", matching=0.97, waiting_time=10000):
                self.not_found("reduzirvalordoicmsmarcado")
            self.click()
            x=0
            while x<5:
                if not self.find( "tipoantecipacaovalida", matching=0.97, waiting_time=10000):
                    self.not_found("tipoantecipacaovalida")
                self.click_relative(295, 27)
                self.type_down()
                self.enter()
                x=x+1
            x=0
            while x<7:
                if not self.find( "modalidadeicmssubtrib", matching=0.97, waiting_time=10000):
                    self.not_found("modalidadeicmssubtrib")
                self.click_relative(1259, 46)
                self.type_down()
                self.enter()
                x=x+1
            if not self.find( "percentualreducaobaseicmsst", matching=0.97, waiting_time=10000):
                self.not_found("percentualreducaobaseicmsst")
            self.click_relative(175, 23)
            self.type_keys_with_interval(1,'123')
            if not self.find( "baseicmsdifst", matching=0.97, waiting_time=10000):
                self.not_found("baseicmsdifst")
            self.click_relative(140, 30)
            self.type_keys_with_interval(1,'123')
            if not self.find( "aliquotadiferencialst", matching=0.97, waiting_time=10000):
                self.not_found("aliquotadiferencialst")
            self.click_relative(142, 30)
            self.type_keys_with_interval(1,'123')              
            
                            ####---ICMS SUB TRIB RETIDA---####   
            
            if not self.find( "icmsretida", matching=0.97, waiting_time=10000):
                self.not_found("icmsretida")
            self.click_relative(144, 46)
            self.type_keys_with_interval(1,'123')
            if not self.find( "fecharcalculadorasituacao", matching=0.97, waiting_time=10000):
                self.not_found("fecharcalculadorasituacao")
            self.click()            
            if not self.find( "icmsretida", matching=0.97, waiting_time=10000):
                self.not_found("icmsretida")
            self.click_relative(303, 46)
            self.type_keys_with_interval(1,'123')
            if not self.find( "fecharcalculadorasituacao", matching=0.97, waiting_time=10000):
                self.not_found("fecharcalculadorasituacao")
            self.click()
            x=0
            while x<7:
                if not self.find( "valororigembasedecalculo", matching=0.97, waiting_time=10000):
                    self.not_found("valororigembasedecalculo")
                self.click_relative(297, 25)
                self.type_down()
                self.enter()
                x=x+1
            if not self.find( "aliquotafcpretida", matching=0.97, waiting_time=10000):
                self.not_found("aliquotafcpretida")
            self.click_relative(140, 32)
            self.type_keys_with_interval(1,'123')
            
                            ####---IPI---####
            
            if not self.find( "IPIbasecalculo", matching=0.97, waiting_time=10000):
                self.not_found("IPIbasecalculo")
            self.click_relative(143, 47)
            self.type_keys_with_interval(1,'123')
            if not self.find( "fecharcalculadorasituacao", matching=0.97, waiting_time=10000):
                self.not_found("fecharcalculadorasituacao")
            self.click()
            
            if not self.find( "ipialiquota", matching=0.97, waiting_time=10000):
                self.not_found("ipialiquota")
            self.click_relative(303, 46)
            self.type_keys_with_interval(1,'1')
            self.backspace()
            self.type_keys_with_interval(1,'0')
            if not self.find( "fecharcalculadorasituacao", matching=0.97, waiting_time=10000):
                self.not_found("fecharcalculadorasituacao")
            self.click()
            
            x=0
            while x<6:
                if not self.find( "ipitipo", matching=0.97, waiting_time=10000):
                    self.not_found("ipitipo")
                self.click_relative(624, 46)
                self.type_down()
                self.enter()
                x=x+1
            if not self.find( "enquadramentoipi", matching=0.97, waiting_time=10000):
                self.not_found("enquadramentoipi")
            self.click_relative(40, 27)
            self.type_keys_with_interval(1,'t1!')
            if not self.find( "ipirsquantidade", matching=0.97, waiting_time=10000):
                self.not_found("ipirsquantidade")
            self.click_relative(141, 27)
            self.type_keys_with_interval(1,'123')
            x=0
            while x<14:
                if not self.find( "ipisituacaotributaria", matching=0.97, waiting_time=10000):
                    self.not_found("ipisituacaotributaria")
                self.click_relative(1260, 44)
                self.type_down()
                self.enter()
                x=x+1
            if not self.find( "ipibaseicms", matching=0.97, waiting_time=10000):
                self.not_found("ipibaseicms")
            self.click()
            if not self.find( "ipibaseicmsmarcado", matching=0.97, waiting_time=10000):
                self.not_found("ipibaseicmsmarcado")
            self.click()
            self.enter()
            if not self.find( "ipibasepiscofins", matching=0.97, waiting_time=10000):
                self.not_found("ipibasepiscofins")
            self.click()
            if not self.find( "ipibasepiscofinsmarcado", matching=0.97, waiting_time=10000):
                self.not_found("ipibasepiscofinsmarcado")
            self.click()
            if not self.find( "ipibaseicmsdif", matching=0.97, waiting_time=10000):
                self.not_found("ipibaseicmsdif")
            self.click()
            if not self.find( "ipibaseicmsdifmarcado", matching=0.97, waiting_time=10000):
                self.not_found("ipibaseicmsdifmarcado")
            self.click()
            if not self.find( "fretebasedoipi", matching=0.97, waiting_time=10000):
                self.not_found("fretebasedoipi")
            self.click()
            if not self.find( "fretebasedoipimarcado", matching=0.97, waiting_time=10000):
                self.not_found("fretebasedoipimarcado")
            self.click()
            if not self.find( "ipibasesubstituicao", matching=0.97, waiting_time=10000):
                self.not_found("ipibasesubstituicao")
            self.click()
            if not self.find( "ipibasesubstituicaomarcado", matching=0.97, waiting_time=10000):
                self.not_found("ipibasesubstituicaomarcado")
            self.click()
            self.enter()
            if not self.find( "indicevariacaopreco", matching=0.97, waiting_time=10000):
                self.not_found("indicevariacaopreco")
            self.click_relative(140, 30)
            self.type_keys_with_interval(1,'123')
            if not self.find( "cancelacalculadoraipi", matching=0.97, waiting_time=10000):
                self.not_found("cancelacalculadoraipi")
            self.click()
            
            if not self.find( "basepresumidomapafiscal", matching=0.97, waiting_time=10000):
                self.not_found("basepresumidomapafiscal")
            self.click_relative(140, 26)
            self.type_keys_with_interval(1,'123')
            if not self.find( "cancelacalculadoraipi", matching=0.97, waiting_time=10000):
                self.not_found("cancelacalculadoraipi")
            self.click()
            
            x=0
            while x<8:
                if not self.find( "atividadepresumido", matching=0.97, waiting_time=10000):
                    self.not_found("atividadepresumido")
                self.click_relative(300, 28)
                self.type_down()
                self.enter()
                x=x+1
            if not self.find( "aliquotaecf", matching=0.97, waiting_time=10000):
                self.not_found("aliquotaecf")
            self.click_relative(40, 27)
            self.type_keys_with_interval(1,'t1')
            self.enter()
            self.type_keys_with_interval(1,'t1!')
            if not self.find( "datadevalidadeipi", matching=0.97, waiting_time=10000):
                self.not_found("datadevalidadeipi")
            self.click_relative(140, 25)
            if not self.find( "diadatavalidade", matching=0.97, waiting_time=10000):
                self.not_found("diadatavalidade")
            self.click_relative(97, 74)
            
                            ####---ABAIXANDO TELA---####
                             
            if not self.find( "abaixandotelasituacao1", matching=0.97, waiting_time=10000):
                self.not_found("abaixandotelasituacao1")
            self.click()
            x=0
            while x<11:
                if not self.find( "abaixandotelasituacao2", matching=0.97, waiting_time=10000):
                    self.not_found("abaixandotelasituacao2")
                self.click()
                x=x+1
            
                            ####---AJUSTE SPED ICMS C197---####
                             
            if not self.find( "codigo", matching=0.97, waiting_time=10000):
                 self.not_found("codigo")
            self.click_relative(22, 28)
            self.type_keys_with_interval(1,'t1!')
            if not self.find( "descricaoajuste", matching=0.97, waiting_time=10000):
                 self.not_found("descricaoajuste")
            self.click_relative(188, 44)
            self.type_keys_with_interval(1,'te12!@')    
            
                            ####---PIS, COFINS, ISS---####
                             
            if not self.find( "aba2piscofinsiss", matching=0.97, waiting_time=10000):
                self.not_found("aba2piscofinsiss")
            self.click()
            if not self.find( "pisbasecalculo", matching=0.97, waiting_time=10000):
                self.not_found("pisbasecalculo")
            self.click_relative(145, 46)
            self.type_keys_with_interval(1,'123')
            if not self.find( "pisaliquota", matching=0.97, waiting_time=10000):
                self.not_found("pisaliquota")
            self.click_relative(304, 47)
            self.type_keys_with_interval(1,'123')
            
            x=0
            while x<5:
                if not self.find( "tipopis", matching=0.97, waiting_time=10000):
                    self.not_found("tipopis")
                self.click_relative(625, 47)
                self.type_up()
                self.enter()
                x=x+1
            
            if not self.find( "pisvalordeunidade", matching=0.97, waiting_time=10000):
                self.not_found("pisvalordeunidade")
            self.click_relative(786, 46)
            self.type_keys_with_interval(1,'123')
            
            x=0
            while x<33:
                if not self.find( "pissituacaotributaria", matching=0.97, waiting_time=10000):
                    self.not_found("pissituacaotributaria")
                self.click_relative(1101, 47)
                self.type_down()
                self.enter()
                x=x+1
                
            x=0
            while x<4:
                if not self.find( "pisrateiocreditocomuns", matching=0.97, waiting_time=10000):
                    self.not_found("pisrateiocreditocomuns")
                self.click_relative(304, 94)
                self.type_down()
                self.enter()
                x=x+1
                
            if not self.find( "descontarvaloricmsbase", matching=0.97, waiting_time=10000):
                self.not_found("descontarvaloricmsbase")
            self.click()
            if not self.find( "descontarvaloricmsbasemarcado", matching=0.97, waiting_time=10000):
                self.not_found("descontarvaloricmsbasemarcado")
            self.click()
            if not self.find( "basesobrelucro", matching=0.97, waiting_time=10000):
                self.not_found("basesobrelucro")
            self.click()
            if not self.find( "basesobrelucromarcado", matching=0.97, waiting_time=10000):
                self.not_found("basesobrelucromarcado")
            self.click()
                
                            ####---COFINS---####
                             
            if not self.find( "cofinsbase", matching=0.97, waiting_time=10000):
                self.not_found("cofinsbase")
            self.click_relative(145, 46)
            self.type_keys_with_interval(1,'123')
            if not self.find( "cofinsbase", matching=0.97, waiting_time=10000):
                self.not_found("cofinsbase")
            self.click_relative(304, 47)
            self.type_keys_with_interval(1,'123')
            x=0
            while x<5:
                if not self.find( "cofinsbase", matching=0.97, waiting_time=10000):
                    self.not_found("cofinsbase")
                self.click_relative(625, 47)
                self.type_up()
                self.enter()
                x=x+1
            if not self.find( "cofinsbase", matching=0.97, waiting_time=10000):
                    self.not_found("cofinsbase")
            self.click_relative(786, 46)
            self.type_keys_with_interval(1,'123')
            
            x=0
            while x<33:
                if not self.find( "cofinsbase", matching=0.97, waiting_time=10000):
                    self.not_found("cofinsbase")
                self.click_relative(1101, 47)
                self.type_down()
                self.enter()
                x=x+1
           
            x=0
            while x<19:
                if not self.find( "cofinsbase", matching=0.97, waiting_time=10000):
                    self.not_found("cofinsbase")
                self.click_relative(304, 94)
                self.type_down()
                self.enter()
                x=x+1
                
                            ####---ISS---####
                             
            if not self.find( "issbasecalculo", matching=0.97, waiting_time=10000):
                self.not_found("issbasecalculo")
            self.click_relative(145, 48)
            self.type_keys_with_interval(1,'123')
            self.enter()
            self.enter()
            self.type_keys_with_interval(1,'123')
            self.enter()
            
            self.type_keys_with_interval(1,'t1!')
            
            x=0
            while x<8:
                if not self.find( "issexigiblidade", matching=0.97, waiting_time=10000):
                    self.not_found("issexigiblidade")
                self.click_relative(787, 47)
                self.type_down()
                self.enter()
                x=x+1
                
                            ####---OUTROS IMPOSTOS---####
                             
            if not self.find( "outrosimpostossuframa", matching=0.97, waiting_time=10000):
                self.not_found("outrosimpostossuframa")
            self.click_relative(145, 46)
            self.type_keys_with_interval(1,'123')
            self.enter()
            self.enter()
            self.type_keys_with_interval(1,'123')
            self.enter()
            
            self.type_keys_with_interval(1,'123')
            self.enter()
            
            self.type_keys_with_interval(1,'123')
            self.enter()
            
            
                            ####---RETENCOES---####
                             
            if not self.find( "retencoesaliquotairrf", matching=0.97, waiting_time=10000):
                self.not_found("retencoesaliquotairrf")
            self.click_relative(144, 49)
            self.type_keys_with_interval(1,'123')
            self.enter()
            self.enter()
            self.type_keys_with_interval(1,'123')
            self.enter()
            
            self.type_keys_with_interval(1,'123')
            self.enter()
            
            self.type_keys_with_interval(1,'123')
            self.enter()
            
            self.type_keys_with_interval(1,'123')
            self.enter()
            
            self.type_keys_with_interval(1,'123')
            self.enter()
            
            
                            ####---DECRETOS E OBSERVACOES---####
                             
            if not self.find( "decretoseobservacoesemsituacao", matching=0.97, waiting_time=10000):
                self.not_found("decretoseobservacoesemsituacao")
            self.click()
            if not self.find( "decretonf1", matching=0.97, waiting_time=10000):
                self.not_found("decretonf1")
            self.click_relative(43, 28)
            if not self.find( "cod001bdecretonf", matching=0.97, waiting_time=10000):
                self.not_found("cod001bdecretonf")
            self.click()
            if not self.find( "selecionarcfoppadrao", matching=0.97, waiting_time=10000):
                self.not_found("selecionarcfoppadrao")
            self.click()
            if not self.find( "decretonf2", matching=0.97, waiting_time=10000):
                self.not_found("decretonf2")
            self.click_relative(43, 25)
            if not self.find( "cod001bdecretonf", matching=0.97, waiting_time=10000):
                self.not_found("cod001bdecretonf")
            self.click()
            if not self.find( "selecionarcfoppadrao", matching=0.97, waiting_time=10000):
                self.not_found("selecionarcfoppadrao")
            self.click()
            
            if not self.find( "observacaonf1", matching=0.97, waiting_time=10000):
                self.not_found("observacaonf1")
            self.click_relative(43, 26)
            if not self.find( "cod001bdecretonf", matching=0.97, waiting_time=10000):
                self.not_found("cod001bdecretonf")
            self.click()
            if not self.find( "selecionarcfoppadrao", matching=0.97, waiting_time=10000):
                self.not_found("selecionarcfoppadrao")
            self.click()
            if not self.find( "observacaonf2", matching=0.97, waiting_time=10000):
                self.not_found("observacaonf2")
            self.click_relative(44, 29)
            if not self.find( "cod001bdecretonf", matching=0.97, waiting_time=10000):
                self.not_found("cod001bdecretonf")
            self.click()
            if not self.find( "selecionarcfoppadrao", matching=0.97, waiting_time=10000):
                self.not_found("selecionarcfoppadrao")
            self.click()
            
            if not self.find( "cfopsituacao1", matching=0.97, waiting_time=10000):
                self.not_found("cfopsituacao1")
            self.click_relative(58, 25)
            self.backspace()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "buscarcfop", matching=0.97, waiting_time=10000):
                self.not_found("buscarcfop")
            self.click_relative(59, 30)
            self.type_keys_with_interval(1,'9.999')
            self.enter()
            if not self.find( "cod9999cfop", matching=0.97, waiting_time=10000):
                self.not_found("cod9999cfop")
            self.click()            
            if not self.find( "selecionarcfoppadrao", matching=0.97, waiting_time=10000):
                self.not_found("selecionarcfoppadrao")
            self.click()
            
            if not self.find( "observacaocfop", matching=0.97, waiting_time=10000):
                self.not_found("observacaocfop")
            self.click_relative(24, 50)
            self.type_keys_with_interval(1,'te12!@')
            
                            ####---GNRE---####
                             
            if not self.find( "gnresituacao", matching=0.97, waiting_time=10000):
                self.not_found("gnresituacao")
            self.click()
            if not self.find( "incluirnovoregistrognresituacao", matching=0.97, waiting_time=10000):
                self.not_found("incluirnovoregistrognresituacao")
            self.click()
            if not self.find( "cancelargnre", matching=0.97, waiting_time=10000):
                self.not_found("cancelargnre")
            self.click()
                
                            ####---FINALIZACAO SITUACAO---###
                             
            if not self.find( "salvarsituacao", matching=0.97, waiting_time=10000):
                self.not_found("salvarsituacao")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "buscarcfop", matching=0.97, waiting_time=10000):
                self.not_found("buscarcfop")
            self.click_relative(59, 30)
            self.type_keys_with_interval(1,'0048')
            self.enter()
            if not self.find( "nordestesituacao", matching=0.97, waiting_time=10000):
                self.not_found("nordestesituacao")
            self.click()
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            
            if not self.find( "excluirpaisteste", matching=0.97, waiting_time=10000):
                self.not_found("excluirpaisteste")
            self.click()
            self.enter()
            #if not self.find( "simexcluirteste", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirteste")
            #self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            

            if not self.find( "abrircadastros_abacadastro", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro")
            self.click()
            if not self.find( "clientes,fornecedoresetransportadores", matching=0.97, waiting_time=10000):
                self.not_found("clientes,fornecedoresetransportadores")
            self.click()            
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            self.wait(7500)            
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            self.wait(5000)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()
            self.wait(2000)
            
            if not self.find( "codigonome", matching=0.97, waiting_time=10000):
                self.not_found("codigonome")
            self.click_relative(136, 29)
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "pessoa", matching=0.97, waiting_time=10000):
                self.not_found("pessoa")
            self.click_relative(72, 30)
            if not self.find( "pessoa", matching=0.97, waiting_time=10000):
                self.not_found("pessoa")
            self.click_relative(6, 27)
            if not self.find( "cpfcadastrocliente", matching=0.97, waiting_time=10000):
                self.not_found("cpfcadastrocliente")
            self.click_relative(3, 25)
            self.type_keys_with_interval(100,'086.580.33902')
            self.enter()
            self.type_keys_with_interval(1,'14.734.534-8')
            self.enter()
            self.type_keys_with_interval(1,'t1!')
            self.enter()
            self.type_keys_with_interval(100,'01012022')
            self.enter()
            self.enter()
            
            
            
                            ####---ABA1 CADASTRO---####
                             
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(10,'8505 5370')
            if not self.find( "procurarcep", matching=0.97, waiting_time=10000):
                self.not_found("procurarcep")
            self.click()
            if not self.find( "endprinproximo", matching=0.97, waiting_time=10000):
                self.not_found("endprinproximo")
            self.click_relative(12, 88)
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "municipioendprin", matching=0.97, waiting_time=10000):
                self.not_found("municipioendprin")
            self.click_relative(403, 86)
            self.backspace()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=100000):
                self.not_found("localizarpaises")
            self.click()
            self.wait(2000)
            if not self.find( "cod0001ccft", matching=0.97, waiting_time=10000):
                self.not_found("cod0001ccft")
            self.click()
            self.type_down()
            if not self.find( "selecionarcft", matching=0.97, waiting_time=10000):
                self.not_found("selecionarcft")
            self.click()
            self.wait(500)
            if not self.find( "telefoneendprin", matching=0.97, waiting_time=10000):
                self.not_found("telefoneendprin")
            self.click_relative(829, 88)
            self.type_keys_with_interval(1,'984119244')
            self.enter()
            
            x=0
            while x<7:
                if not self.find( "operadoraendprin", matching=0.97, waiting_time=10000):
                    self.not_found("operadoraendprin")
                self.click_relative(1068, 86)
                self.type_down()
                self.enter()
                x=x+1
                
            if not self.find( "telempendprin", matching=0.97, waiting_time=10000):
                self.not_found("telempendprin")
            self.click_relative(9, 129)
            self.type_keys_with_interval(1,'984119244')
            
            x=0
            while x<7:
                if not self.find( "operadorateleemp", matching=0.97, waiting_time=10000):
                    self.not_found("operadorateleemp")
                self.click_relative(260, 129)               
                self.type_down()
                self.enter()
                x=x+1
                
            if not self.find( "telcelendprin", matching=0.97, waiting_time=10000):
                self.not_found("telcelendprin")
            self.click_relative(293, 130)
            self.type_keys_with_interval(1,'984119244')
            
            x=0
            while x<8:
                if not self.find( "operadoratelcel", matching=0.97, waiting_time=10000):
                    self.not_found("operadoratelcel")
                self.click_relative(533, 131)                              
                self.type_down()
                self.enter()
                x=x+1
                
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "longaltgoogle", matching=0.97, waiting_time=10000):
                self.not_found("longaltgoogle")
            self.click()
            self.wait(5000)
            
                            ####---PESSOA FISICA---####
                             
            if not self.find( "nomefantasiapessoafisica", matching=0.97, waiting_time=10000):
                self.not_found("nomefantasiapessoafisica")
            self.click_relative(13, 45)
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            x=0
            while x<3:
                if not self.find( "indicadorie", matching=0.97, waiting_time=10000):
                    self.not_found("indicadorie")
                self.click_relative(124, 25)
                self.type_down()
                self.enter()
                x=x+1
            
            if not self.find( "sexopessoafisica", matching=0.97, waiting_time=10000):
                self.not_found("sexopessoafisica")
            self.click_relative(74, 26)
            self.type_down()
            self.enter()
            if not self.find( "sexopessoafisica", matching=0.97, waiting_time=10000):
                self.not_found("sexopessoafisica")
            self.click_relative(74, 26)
            self.type_down()
            self.enter()
            
            x=0
            while x<5:
                if not self.find( "estadocivilpessoafisica", matching=0.97, waiting_time=10000):
                    self.not_found("estadocivilpessoafisica")
                self.click_relative(92, 26)
                self.type_down()
                self.enter()
                x=x+1
            
            if not self.find( "pessoafisicaresponsavel", matching=0.97, waiting_time=10000):
                self.not_found("pessoafisicaresponsavel")
            self.click_relative(13, 32)
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            
                            ####---DATAS---####
                             
            self.enter()
            self.type_keys_with_interval(100,'01012022')
            self.enter()
            self.enter()
            self.type_keys_with_interval(100,'01012022')
            self.enter()
            self.type_keys_with_interval(100,'01012022')
            self.enter()
            self.type_keys_with_interval(1,'t')
            self.backspace()
            self.type_keys_with_interval(1,'1')
            self.backspace()
            self.type_keys_with_interval(1,'!')
            self.backspace()
            self.type_keys_with_interval(1,'a')
            if not self.find( "controledatas", matching=0.97, waiting_time=10000):
                self.not_found("controledatas")
            self.click_relative(6, 25)
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "integracaodatas", matching=0.97, waiting_time=10000):
                self.not_found("integracaodatas")
            self.click_relative(95, 27)
            self.type_down()
            self.enter()
            if not self.find( "integracaodatas", matching=0.97, waiting_time=10000):
                self.not_found("integracaodatas")
            self.click_relative(95, 27)
            self.type_up()
            self.enter()
            
            if not self.find( "conveniodiadovencimento", matching=0.97, waiting_time=10000):
                self.not_found("conveniodiadovencimento")
            self.double_click_relative(60, 20)
            if not self.find( "conveniodiadovencimento2", matching=0.97, waiting_time=10000):
                self.not_found("conveniodiadovencimento2")
            self.click_relative(60, 32)
            self.backspace()
            self.backspace()
            self.type_keys_with_interval(1,'874')
            
                            ####---ENDERECO DE COBRANCA ALTERNATIVO---####
                             
            if not self.find( "enderecocomnumeroca", matching=0.97, waiting_time=10000):
                self.not_found("enderecocomnumeroca")
            self.click_relative(7, 27)
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "enderecodecobrancaalternativo", matching=0.97, waiting_time=10000):
                self.not_found("enderecodecobrancaalternativo")
            self.click_relative(54, 87)
            self.type_keys_with_interval(1,'Guarapuava')
            if not self.find( "cod0001guarapuavab", matching=0.97, waiting_time=10000):
                self.not_found("cod0001guarapuavab")
            self.click()
            if not self.find( "selecionarcft", matching=0.97, waiting_time=10000):
                self.not_found("selecionarcft")
            self.click()
            self.enter()
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            
                            ####---ABAIXANDO TELA---####
                             
            if not self.find( "abaixartelacft1", matching=0.97, waiting_time=10000):
                self.not_found("abaixartelacft1")
            self.click()
            
            x=0
            while x<10:
                if not self.find( "abaixandotelacft2", matching=0.97, waiting_time=10000):
                    self.not_found("abaixandotelacft2")
                self.double_click()
                x=x+1
            
                            ####---DADOS DE CONTATO---####
                             
            if not self.find( "emailcft", matching=0.97, waiting_time=10000):
                self.not_found("emailcft")
            self.click_relative(10, 28)
            self.type_keys_with_interval(1,'emailtesteteorema123@gmail.com')
            
            if not self.find( "botaoemail", matching=0.97, waiting_time=10000):
                self.not_found("botaoemail")
            self.click_relative(426, 47)
            if not self.find( "addcontaemailcft", matching=0.97, waiting_time=10000):
                self.not_found("addcontaemailcft")
            self.click_relative(424, 6)
            if not self.find( "fechartelaemailcft", matching=0.97, waiting_time=10000):
                self.not_found("fechartelaemailcft")
            self.click()
            if not self.find( "emaildocecft", matching=0.97, waiting_time=10000):
                self.not_found("emaildocecft")
            self.click_relative(9, 27)
            self.type_keys_with_interval(1,'emailtesteteorema123@gmail.com')
            if not self.find( "botaoemail2cft", matching=0.97, waiting_time=10000):
                self.not_found("botaoemail2cft")
            self.click_relative(868, 43)
            if not self.find( "addcontaemailcft", matching=0.97, waiting_time=10000):
                self.not_found("addcontaemailcft")
            self.click_relative(424, 6)
            if not self.find( "fechartelaemailcft", matching=0.97, waiting_time=10000):
                self.not_found("fechartelaemailcft")
            self.click()
            if not self.find( "skypecft", matching=0.97, waiting_time=10000):
                self.not_found("skypecft")
            self.click_relative(21, 25)           
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(1,'www.google.com.br')
            if not self.find( "abrirsiteinternetexp", matching=0.97, waiting_time=10000):
                self.not_found("abrirsiteinternetexp")
            self.click()
            if not self.find( "fechargooglecerto", matching=0.97, waiting_time=10000):
                self.not_found("fechargooglecerto")
            self.click_relative(1260, 6)            
            if not self.find( "idmarketplace", matching=0.97, waiting_time=10000):
                self.not_found("idmarketplace")
            self.click_relative(10, 28)
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "contatodadosdecontato", matching=0.97, waiting_time=10000):
                self.not_found("contatodadosdecontato")
            self.click_relative(925, 89)
            self.type_keys_with_interval(1,'te12!@')
            
                            ####---MARCADORES---####
                             
            if not self.find( "clientemarcadores", matching=0.97, waiting_time=10000):
                self.not_found("clientemarcadores")
            self.click()
            """
            if not self.find( "clientemarcadocft", matching=0.97, waiting_time=10000):
                self.not_found("clientemarcadocft")
            self.click()
            if not self.find( "fornecedorcft", matching=0.97, waiting_time=10000):
                self.not_found("fornecedorcft")
            self.click()
            if not self.find( "fornecedorcft1", matching=0.97, waiting_time=10000):
                self.not_found("fornecedorcft1")
            self.click()            
            if not self.find( "fornecedorcftmarcado", matching=0.97, waiting_time=10000):
                self.not_found("fornecedorcftmarcado")
            self.click()
            if not self.find( "transportadorcfta1", matching=0.97, waiting_time=10000):
                self.not_found("transportadorcfta1")
            self.click_relative(163, 30)
            if not self.find( "transportadorcfta1", matching=0.97, waiting_time=10000):
                self.not_found("transportadorcfta1")
            self.click_relative(163, 30)
            if not self.find( "transportadorcfta1", matching=0.97, waiting_time=10000):
                self.not_found("transportadorcfta1")
            self.click_relative(163, 30)
            if not self.find( "prospectcft", matching=0.97, waiting_time=10000):
                self.not_found("prospectcft")
            self.click()
            if not self.find( "prospectcft1", matching=0.97, waiting_time=10000):
                self.not_found("prospectcft1")
            self.click()       
            if not self.find( "prospectmarcadocft", matching=0.97, waiting_time=10000):
                self.not_found("prospectmarcadocft")
            self.click()
            if not self.find( "prestadorservicocft", matching=0.97, waiting_time=10000):
                self.not_found("prestadorservicocft")
            self.click()
                       
            if not self.find( "prestadorservicocftmarcado", matching=0.97, waiting_time=10000):
                self.not_found("prestadorservicocftmarcado")
            self.click()
            if not self.find( "clienteinternocft", matching=0.97, waiting_time=10000):
                self.not_found("clienteinternocft")
            self.click_relative(286, 51)
            if not self.find( "clienteinternocft", matching=0.97, waiting_time=10000):
                self.not_found("clienteinternocft")
            self.click_relative(286, 51)
            
            if not self.find( "concorrentecft", matching=0.97, waiting_time=10000):
                self.not_found("concorrentecft")
            self.click()
            if not self.find( "concorrentecft1", matching=0.97, waiting_time=10000):
                self.not_found("concorrentecft1")
            self.click()            
            if not self.find( "concorrentecftmarcado", matching=0.97, waiting_time=10000):
                self.not_found("concorrentecftmarcado")
            self.click()
            if not self.find( "consumidorfinalcft1", matching=0.97, waiting_time=10000):
                self.not_found("consumidorfinalcft1")
            self.click()
            if not self.find( "consumidorfinalcft2", matching=0.97, waiting_time=10000):
                self.not_found("consumidorfinalcft2")
            self.click()           
            if not self.find( "consumidorfinalcftmarcado", matching=0.97, waiting_time=10000):
                self.not_found("consumidorfinalcftmarcado")
            self.click()
            if not self.find( "consumidorfinalcft", matching=0.97, waiting_time=10000):
                self.not_found("consumidorfinalcft")
            self.click()
            if not self.find( "calculofunrural", matching=0.97, waiting_time=10000):
                self.not_found("calculofunrural")
            self.click()
                        
            if not self.find( "calculofunruralcftmarcado", matching=0.97, waiting_time=10000):
                self.not_found("calculofunruralcftmarcado")
            self.click()
            if not self.find( "calculosenarcft1", matching=0.97, waiting_time=10000):
                self.not_found("calculosenarcft1")
            self.click()
            if not self.find( "calculosenarcft2", matching=0.97, waiting_time=10000):
                self.not_found("calculosenarcft2")
            self.click()                       
            if not self.find( "calculosenarcftmarcado", matching=0.97, waiting_time=10000):
                self.not_found("calculosenarcftmarcado")
            self.click()
            if not self.find( "calculosenarcft", matching=0.97, waiting_time=10000):
                self.not_found("calculosenarcft")
            self.click()
            if not self.find( "quotacapitalcft", matching=0.97, waiting_time=10000):
                self.not_found("quotacapitalcft")
            self.click()
            if not self.find( "quotacapitalcft2", matching=0.97, waiting_time=10000):
                self.not_found("quotacapitalcft2")
            self.click()
            
            if not self.find( "quotacapitalcftmarcado", matching=0.97, waiting_time=10000):
                self.not_found("quotacapitalcftmarcado")
            self.click()
            if not self.find( "consumidorcrmcft", matching=0.97, waiting_time=10000):
                self.not_found("consumidorcrmcft")
            self.click_relative(649, 51)
            if not self.find( "consumidorcrmcft", matching=0.97, waiting_time=10000):
                self.not_found("consumidorcrmcft")
            self.click_relative(649, 51)
                       
            
            if not self.find( "itemcontroladocft1", matching=0.97, waiting_time=10000):
                self.not_found("itemcontroladocft1")
            self.click()
            if not self.find( "itemcontroladocftmarcado", matching=0.97, waiting_time=10000):
                self.not_found("itemcontroladocftmarcado")
            self.click()
            if not self.find( "itemcontroladocft", matching=0.97, waiting_time=10000):
                self.not_found("itemcontroladocft")
            self.click()
            if not self.find( "art19cft", matching=0.97, waiting_time=10000):
                self.not_found("art19cft")
            self.click()
            if not self.find( "art19cftmarcado", matching=0.97, waiting_time=10000):
                self.not_found("art19cftmarcado")
            self.click()
            if not self.find( "simplesnacionalcft", matching=0.97, waiting_time=10000):
                self.not_found("simplesnacionalcft")
            self.click()
            if not self.find( "simplesnacionalcftmarcado", matching=0.97, waiting_time=10000):
                self.not_found("simplesnacionalcftmarcado")
            self.click()
            if not self.find( "integrarconcreteiracft", matching=0.97, waiting_time=10000):
                self.not_found("integrarconcreteiracft")
            self.click()
            if not self.find( "integrarconcreteiracftmarcado", matching=0.97, waiting_time=10000):
                self.not_found("integrarconcreteiracftmarcado")
            self.click()
            if not self.find( "seguradorasiglacft1", matching=0.97, waiting_time=10000):
                self.not_found("seguradorasiglacft1")
            self.click()
            if not self.find( "seguradorasiglacftmarcado", matching=0.97, waiting_time=10000):
                self.not_found("seguradorasiglacftmarcado")
            self.click()
            if not self.find( "seguradorasiglacft", matching=0.97, waiting_time=10000):
                self.not_found("seguradorasiglacft")
            self.click()
            if not self.find( "siglaseguradora", matching=0.97, waiting_time=10000):
                self.not_found("siglaseguradora")
            self.click_relative(6, 26)
            self.type_keys_with_interval(1,'t1!')
            """
            x=0
            while x<17:
                    self.tab()
                    self.space()
                    self.space()
                    x=x+1
                    
                            ####---ABA2 AGRUPAMENTO---####
                             
            if not self.find( "aba2agrupamentocft", matching=0.97, waiting_time=10000):
                self.not_found("aba2agrupamentocft")
            self.click()
            if not self.find( "localdecobrancacft", matching=0.97, waiting_time=10000):
                self.not_found("localdecobrancacft")
            self.click_relative(67, 25)
            if not self.find( "cod00001cft", matching=0.97, waiting_time=10000):
                self.not_found("cod00001cft")
            self.click()
            if not self.find( "selecionarcft", matching=0.97, waiting_time=10000):
                self.not_found("selecionarcft")
            self.click()
            if not self.find( "vendedorcompradorcft", matching=0.97, waiting_time=10000):
                self.not_found("vendedorcompradorcft")
            self.click_relative(64, 26)
            if not self.find( "cod00101cft", matching=0.97, waiting_time=10000):
                self.not_found("cod00101cft")
            self.click()
            if not self.find( "selecionarcft", matching=0.97, waiting_time=10000):
                self.not_found("selecionarcft")
            self.click()
            if not self.find( "classificacaocft", matching=0.97, waiting_time=10000):
                self.not_found("classificacaocft")
            self.click_relative(69, 25)
            if not self.find( "cod00184cft", matching=0.97, waiting_time=10000):
                self.not_found("cod00184cft")
            self.click()
            if not self.find( "selecionarcft", matching=0.97, waiting_time=10000):
                self.not_found("selecionarcft")
            self.click()
            if not self.find( "codcontabilfixocft", matching=0.97, waiting_time=10000):
                self.not_found("codcontabilfixocft")
            self.click_relative(65, 25)
            if not self.find( "cod00051cft", matching=0.97, waiting_time=10000):
                self.not_found("cod00051cft")
            self.click()
            if not self.find( "selecionarcft", matching=0.97, waiting_time=10000):
                self.not_found("selecionarcft")
            self.click()
            if not self.find( "tabeladeprecositenscft", matching=0.97, waiting_time=10000):
                self.not_found("tabeladeprecositenscft")
            self.click_relative(66, 25)
            if not self.find( "cod00000cft", matching=0.97, waiting_time=10000):
                self.not_found("cod00000cft")
            self.click()
            if not self.find( "selecionarcft", matching=0.97, waiting_time=10000):
                self.not_found("selecionarcft")
            self.click()
            self.backspace()
            if not self.find( "transportadoragrupamentocft", matching=0.97, waiting_time=10000):
                self.not_found("transportadoragrupamentocft")
            self.click_relative(86, 256)            
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "cod0081260cft", matching=0.97, waiting_time=10000):
                self.not_found("cod0081260cft")
            self.click()
            if not self.find( "selecionarcft", matching=0.97, waiting_time=10000):
                self.not_found("selecionarcft")
            self.click()
            if not self.find( "ramodeatividadecft", matching=0.97, waiting_time=10000):
                self.not_found("ramodeatividadecft")
            self.click_relative(68, 24)
            if not self.find( "cod00001cft", matching=0.97, waiting_time=10000):
                self.not_found("cod00001cft")
            self.click()
            if not self.find( "selecionarcft", matching=0.97, waiting_time=10000):
                self.not_found("selecionarcft")
            self.click()
            if not self.find( "planofinanceirocft", matching=0.97, waiting_time=10000):
                self.not_found("planofinanceirocft")
            self.click_relative(83, 26)
            if not self.find( "cod002001002cft", matching=0.97, waiting_time=10000):
                self.not_found("cod002001002cft")
            self.click()
            if not self.find( "selecionarcft", matching=0.97, waiting_time=10000):
                self.not_found("selecionarcft")
            self.click()
            if not self.find( "contacorrentecft", matching=0.97, waiting_time=10000):
                self.not_found("contacorrentecft")
            self.click_relative(68, 26)
            if not self.find( "cod001cft", matching=0.97, waiting_time=10000):
                self.not_found("cod001cft")
            self.click()
            if not self.find( "selecionarcft", matching=0.97, waiting_time=10000):
                self.not_found("selecionarcft")
            self.click()
            if not self.find( "segmentocft", matching=0.97, waiting_time=10000):
                self.not_found("segmentocft")
            self.click_relative(66, 24)
            if not self.find( "cod00001cft", matching=0.97, waiting_time=10000):
                self.not_found("cod00001cft")
            self.click()
            if not self.find( "selecionarcft", matching=0.97, waiting_time=10000):
                self.not_found("selecionarcft")
            self.click()
            if not self.find( "tabeladeprecosservicoscft", matching=0.97, waiting_time=10000):
                self.not_found("tabeladeprecosservicoscft")
            self.click_relative(66, 31)
            if not self.find( "cod00000cft", matching=0.97, waiting_time=10000):
                self.not_found("cod00000cft")
            self.click()
            if not self.find( "selecionarcft", matching=0.97, waiting_time=10000):
                self.not_found("selecionarcft")
            self.click()
            self.backspace()
            if not self.find( "condicaodepagamento", matching=0.97, waiting_time=10000):
                self.not_found("condicaodepagamento")
            self.click_relative(67, 26)
            if not self.find( "cod0048cft", matching=0.97, waiting_time=10000):
                self.not_found("cod0048cft")
            self.click()
            if not self.find( "selecionarcft", matching=0.97, waiting_time=10000):
                self.not_found("selecionarcft")
            self.click()
            if not self.find( "comissaocft", matching=0.97, waiting_time=10000):
                self.not_found("comissaocft")
            self.click_relative(68, 27)
            if not self.find( "cod001cft", matching=0.97, waiting_time=10000):
                self.not_found("cod001cft")
            self.click()
            if not self.find( "selecionarcft", matching=0.97, waiting_time=10000):
                self.not_found("selecionarcft")
            self.click()
            if not self.find( "centrodecustocft", matching=0.97, waiting_time=10000):
                self.not_found("centrodecustocft")
            self.click_relative(85, 27)
            if not self.find( "cod001cft", matching=0.97, waiting_time=10000):
                self.not_found("cod001cft")
            self.click()
            if not self.find( "selecionarcft", matching=0.97, waiting_time=10000):
                self.not_found("selecionarcft")
            self.click()
            self.backspace()
            if not self.find( "codigocontabilfixocft", matching=0.97, waiting_time=10000):
                self.not_found("codigocontabilfixocft")
            self.click_relative(66, 26)
            if not self.find( "cod00051cft", matching=0.97, waiting_time=10000):
                self.not_found("cod00051cft")
            self.click()
            if not self.find( "selecionarcft", matching=0.97, waiting_time=10000):
                self.not_found("selecionarcft")
            self.click()
            if not self.find( "linhacft", matching=0.97, waiting_time=10000):
                self.not_found("linhacft")
            self.click_relative(67, 26)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "operacaopdvbalcaocft", matching=0.97, waiting_time=10000):
                self.not_found("operacaopdvbalcaocft")
            self.click_relative(67, 26)
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "cod0002cft", matching=0.97, waiting_time=10000):
                self.not_found("cod0002cft")
            self.click()
            if not self.find( "selecionarcft", matching=0.97, waiting_time=10000):
                self.not_found("selecionarcft")
            self.click()
            
                            ####---ABA2 P2 CFT---####
                
            if not self.find( "aba2p2cft", matching=0.97, waiting_time=10000):
                self.not_found("aba2p2cft")
            self.click()
            if not self.find( "codigocontabilclientescft", matching=0.97, waiting_time=10000):
                self.not_found("codigocontabilclientescft")
            self.click_relative(63, 27)
            if not self.find( "cod00051cft", matching=0.97, waiting_time=10000):
                self.not_found("cod00051cft")
            self.click()
            if not self.find( "selecionarcft", matching=0.97, waiting_time=10000):
                self.not_found("selecionarcft")
            self.click()
            if not self.find( "codigocontabilfornecedorescft", matching=0.97, waiting_time=10000):
                self.not_found("codigocontabilfornecedorescft")
            self.click_relative(65, 25)
            if not self.find( "cod00051cft", matching=0.97, waiting_time=10000):
                self.not_found("cod00051cft")
            self.click()
            if not self.find( "selecionarcft", matching=0.97, waiting_time=10000):
                self.not_found("selecionarcft")
            self.click()
            
                            ####---CODIGOS CONTABEIS MULTIEMPRESA---####
                             
            if not self.find( "aba2p3cft", matching=0.97, waiting_time=10000):
                self.not_found("aba2p3cft")
            self.click()
            if not self.find( "aba4cft", matching=0.97, waiting_time=10000):
                    self.not_found("aba4cft")
            self.click()
            x=0
            while x<7:
                if not self.find( "situacaoespecialtipoassinantecft", matching=0.97, waiting_time=10000):
                    self.not_found("situacaoespecialtipoassinantecft")
                self.click_relative(290, 26)
                self.type_down()
                self.enter()
                x=x+1
            #if not self.find( "aba8transportadoresconfig", matching=0.97, waiting_time=10000):
            #    self.not_found("aba8transportadoresconfig")
            #self.click()
            #if not self.find( "codidentinsstransportadoresa8", matching=0.97, waiting_time=10000):
            #    self.not_found("codidentinsstransportadoresa8")
            #self.click_relative(139, 87)
            #self.type_keys_with_interval(1,'12312312312')
            if not self.find( "aba2cftparte2", matching=0.97, waiting_time=10000):
                self.not_found("aba2cftparte2")
            self.click()          
            if not self.find( "incluirnovoregistrocft", matching=0.97, waiting_time=10000):
                self.not_found("incluirnovoregistrocft")
            self.click()
            self.enter()
            if not self.find( "aba2cftparte2", matching=0.97, waiting_time=10000):
                self.not_found("aba2cftparte2")
            self.click()           
            if not self.find( "codcontabilclientecft", matching=0.97, waiting_time=10000):
                self.not_found("codcontabilclientecft")
            self.click_relative(-110, 50)
            self.enter()           
            if not self.find( "cod00051cft", matching=0.97, waiting_time=10000):
                self.not_found("cod00051cft")
            self.click()
            if not self.find( "selecionarcft", matching=0.97, waiting_time=10000):
                self.not_found("selecionarcft")
            self.click()
            self.wait(500)
            self.enter()
            self.wait(500)
            self.enter()
            if not self.find( "codigocontabilfornecedor", matching=0.97, waiting_time=10000):
                self.not_found("codigocontabilfornecedor")
            self.click_relative(60, 26)
            self.enter()
            if not self.find( "cod00051cft", matching=0.97, waiting_time=10000):
                self.not_found("cod00051cft")
            self.click()
            if not self.find( "selecionarcft", matching=0.97, waiting_time=10000):
                self.not_found("selecionarcft")
            self.click()
            self.enter()
            self.wait(500)
            self.enter()
            if not self.find( "commitcodcontabilcft", matching=0.97, waiting_time=10000):
                self.not_found("commitcodcontabilcft")
            self.click_relative(9, 7)            
            if not self.find( "excluir_a2p2_cft", matching=0.97, waiting_time=10000):
                self.not_found("excluir_a2p2_cft")
            self.click_relative(12, 188)
            self.enter()                                               
            #if not self.find( "simexcluircommit", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluircommit")
            #self.click()
            self.wait(500)
            self.enter()
            
                            ####---ABA3 PESSOA FISICA---####
                             
            if not self.find( "aba3cft", matching=0.97, waiting_time=10000):
                self.not_found("aba3cft")
            self.click()
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(100,'01012022')
            self.enter()                 
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(1,'874')
            self.enter()
            self.enter()
            x=0
            while x<6:
                if not self.find( "telefoneaba3cft", matching=0.97, waiting_time=10000):
                    self.not_found("telefoneaba3cft")
                self.click_relative(262, 26)
                self.type_down()
                self.enter()
                x=x+1
            
                            ####---MORADIA E OUTRAS RENDAS---####
                             
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(1,'874')
            if not self.find( "casapropriacft", matching=0.97, waiting_time=10000):
                self.not_found("casapropriacft")
            self.click()
            if not self.find( "casapropriacft1", matching=0.97, waiting_time=10000):
                self.not_found("casapropriacft1")
            self.click()
            if not self.find( "possuiautomovela3cft", matching=0.97, waiting_time=10000):
                self.not_found("possuiautomovela3cft")
            self.click_relative(710, 49)
            if not self.find( "possuiautomovela3cft", matching=0.97, waiting_time=10000):
                self.not_found("possuiautomovela3cft")
            self.click_relative(710, 49)
            
            
            
                            ####---INFORMACOES SOBRE PAI/MAE---####
                             
            if not self.find( "infopaimaecft", matching=0.97, waiting_time=10000):
                self.not_found("infopaimaecft")
            self.click_relative(13, 43)
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            
                            ####---INFORMACOES SOBRE CONJUGE---####
                             
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(100,'01012000')
            self.enter()
            self.type_keys_with_interval(100,'08658033902')
            self.enter()
            self.type_keys_with_interval(100,'147345348')
            self.enter()
            self.type_keys_with_interval(1,'t1!')
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(100,'984119244')
            x=0
            while x<5:
                if not self.find( "telefoneservicocft", matching=0.97, waiting_time=10000):
                    self.not_found("telefoneservicocft")
                self.click_relative(201, 26)
                self.type_down()
                self.enter()
                x=x+1
            self.type_keys_with_interval(1,'874')
            self.enter()
            
                            ####---ABAIXANDO TELA---####
                             
            if not self.find( "abaixartelacft1", matching=0.97, waiting_time=10000):
                self.not_found("abaixartelacft1")
            self.click()
            
            x=0
            while x<5:
                if not self.find( "abaixandotelacft2", matching=0.97, waiting_time=10000):
                    self.not_found("abaixandotelacft2")
                self.double_click()
                x=x+1
            
                            ####---FOTO---####
                             
            if not self.find( "inserirfotocft", matching=0.97, waiting_time=10000):
                self.not_found("inserirfotocft")
            self.click()
            self.key_esc()
            #if not self.find( "fotocft", matching=0.97, waiting_time=10000):
            #    self.not_found("fotocft")
            #self.click()
            #if not self.find( "abrirfotocft", matching=0.97, waiting_time=10000):
            #    self.not_found("abrirfotocft")
            #self.click()
            #if not self.find( "excluirfotocft", matching=0.97, waiting_time=10000):
            #    self.not_found("excluirfotocft")
            #self.click()
            if not self.find( "outrasrendascft2", matching=0.97, waiting_time=10000):
                self.not_found("outrasrendascft2")
            self.click_relative(11, 28)
            self.type_keys_with_interval(1,'874')
            
                            ####---ABA4 CFT---####
                             
            if not self.find( "aba4cft2", matching=0.97, waiting_time=10000):
                self.not_found("aba4cft2")
            self.click()
            if not self.find( "rotadeentregacft", matching=0.97, waiting_time=10000):
                self.not_found("rotadeentregacft")
            self.click_relative(66, 46)
            if not self.find( "cod00002cftrota", matching=0.97, waiting_time=10000):
                self.not_found("cod00002cftrota")
            self.click()
            if not self.find( "selecionarcft", matching=0.97, waiting_time=10000):
                self.not_found("selecionarcft")
            self.click()
            
            x=0
            while x<6:
                if not self.find( "tipofretecft", matching=0.97, waiting_time=10000):
                    self.not_found("tipofretecft")
                self.click_relative(619, 47)
                self.type_down()
                self.enter()
                x=x+1
                
                            ####---ROTA DIAS DA SEMANA---####    
                
            if not self.find( "rotadiasdasemana", matching=0.97, waiting_time=10000):
                self.not_found("rotadiasdasemana")
            self.click_relative(14, 29)
            if not self.find( "rotadiasdasemana", matching=0.97, waiting_time=10000):
                self.not_found("rotadiasdasemana")
            self.click_relative(14, 29)
            if not self.find( "rotadiasdasemana", matching=0.97, waiting_time=10000):
                self.not_found("rotadiasdasemana")
            self.click_relative(14, 29)
            if not self.find( "rotadiasdasemana2", matching=0.97, waiting_time=10000):
                self.not_found("rotadiasdasemana2")
            self.click_relative(16, 48)
            if not self.find( "rotadiasdasemana2", matching=0.97, waiting_time=10000):
                self.not_found("rotadiasdasemana2")
            self.click_relative(16, 48)
            if not self.find( "rotadiasdasemana2", matching=0.97, waiting_time=10000):
                self.not_found("rotadiasdasemana2")
            self.click_relative(16, 48)
            if not self.find( "rotadiasdasemana2", matching=0.97, waiting_time=10000):
                self.not_found("rotadiasdasemana2")
            self.click_relative(16, 48)
            if not self.find( "rotadiasdasemana3", matching=0.97, waiting_time=10000):
                self.not_found("rotadiasdasemana3")
            self.click_relative(97, 29)
            if not self.find( "rotadiasdasemana3", matching=0.97, waiting_time=10000):
                self.not_found("rotadiasdasemana3")
            self.click_relative(97, 29)
            if not self.find( "rotadiasdasemana3", matching=0.97, waiting_time=10000):
                self.not_found("rotadiasdasemana3")
            self.click_relative(97, 29)
            if not self.find( "rotadiasdasemana3", matching=0.97, waiting_time=10000):
                self.not_found("rotadiasdasemana3")
            self.click_relative(97, 29)
            if not self.find( "rotadiasdasemana4", matching=0.97, waiting_time=10000):
                self.not_found("rotadiasdasemana4")
            self.click_relative(96, 48)
            if not self.find( "rotadiasdasemana4", matching=0.97, waiting_time=10000):
                self.not_found("rotadiasdasemana4")
            self.click_relative(96, 48)
            if not self.find( "rotadiasdasemana4", matching=0.97, waiting_time=10000):
                self.not_found("rotadiasdasemana4")
            self.click_relative(96, 48)
            if not self.find( "rotadiasdasemana4", matching=0.97, waiting_time=10000):
                self.not_found("rotadiasdasemana4")
            self.click_relative(96, 48)
            if not self.find( "rotadiasdasemana5", matching=0.97, waiting_time=10000):
                self.not_found("rotadiasdasemana5")
            self.click_relative(176, 30)
            if not self.find( "rotadiasdasemana5", matching=0.97, waiting_time=10000):
                self.not_found("rotadiasdasemana5")
            self.click_relative(176, 30)
            if not self.find( "rotadiasdasemana5", matching=0.97, waiting_time=10000):
                self.not_found("rotadiasdasemana5")
            self.click_relative(176, 30)
            if not self.find( "rotadiasdasemana5", matching=0.97, waiting_time=10000):
                self.not_found("rotadiasdasemana5")
            self.click_relative(176, 30)
            if not self.find( "rotadiasdasemana6", matching=0.97, waiting_time=10000):
                self.not_found("rotadiasdasemana6")
            self.click_relative(177, 45)
            if not self.find( "rotadiasdasemana6", matching=0.97, waiting_time=10000):
                self.not_found("rotadiasdasemana6")
            self.click_relative(177, 45)
            if not self.find( "rotadiasdasemana6", matching=0.97, waiting_time=10000):
                self.not_found("rotadiasdasemana6")
            self.click_relative(177, 45)
            if not self.find( "rotadiasdasemana6", matching=0.97, waiting_time=10000):
                self.not_found("rotadiasdasemana6")
            self.click_relative(177, 45)
            if not self.find( "rotadiasdasemana7", matching=0.97, waiting_time=10000):
                self.not_found("rotadiasdasemana7")
            self.click_relative(257, 30)
            if not self.find( "rotadiasdasemana7", matching=0.97, waiting_time=10000):
                self.not_found("rotadiasdasemana7")
            self.click_relative(257, 30)
            if not self.find( "rotadiasdasemana7", matching=0.97, waiting_time=10000):
                self.not_found("rotadiasdasemana7")
            self.click_relative(257, 30)
            if not self.find( "rotadiasdasemana7", matching=0.97, waiting_time=10000):
                self.not_found("rotadiasdasemana7")
            self.click_relative(257, 30)
            if not self.find( "diasdociclocft", matching=0.97, waiting_time=10000):
                self.not_found("diasdociclocft")
            self.click_relative(57, 28)
            self.type_keys_with_interval(1,'123')
            self.enter()
            self.type_keys_with_interval(1,'123')
            self.enter()
            self.type_keys_with_interval(1,'123')
            self.enter()
            self.type_keys_with_interval(1,'123')
            self.enter()
            self.type_keys_with_interval(1,'123')
            self.enter()
            self.type_keys_with_interval(1,'123')
            self.enter()
            self.type_keys_with_interval(1,'123')
            self.enter()
            self.type_keys_with_interval(1,'123')
            
                            ####---INFORMACOES ADICIONAIS---####
            
            x=0
            while x<7:                 
                if not self.find( "indicadorpaacft", matching=0.97, waiting_time=10000):
                    self.not_found("indicadorpaacft")
                self.click_relative(159, 26)
                self.type_down()
                self.enter()
                x=x+1
                
            x=0
            while x<5:
                if not self.find( "indicadorcomcft", matching=0.97, waiting_time=10000):
                    self.not_found("indicadorcomcft")
                self.click_relative(157, 26)
                self.type_down()
                self.enter()
                x=x+1
                
            self.type_keys_with_interval(1,'te12!')
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            
                            ####---DADOS DO CONTABILISTA---####
                             
            if not self.find( "crccontabilistacft", matching=0.97, waiting_time=10000):
                self.not_found("crccontabilistacft")
            self.click_relative(9, 28)
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(1,'12312312313212')
            
                            ####---DADOS DO COOPERADO---####
                             
            if not self.find( "cooperadocft", matching=0.97, waiting_time=10000):
                self.not_found("cooperadocft")
            self.click_relative(11, 35)
            if not self.find( "cooperadocft", matching=0.97, waiting_time=10000):
                self.not_found("cooperadocft")
            self.click_relative(11, 35)
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(100,'01012022')
            self.enter()
            self.type_keys_with_interval(100,'01012022')
            
                            ####---OBSERVACAO---####
                             
            if not self.find( "observacaocft", matching=0.97, waiting_time=10000):
                self.not_found("observacaocft")
            self.click_relative(20, 50)
            self.type_keys_with_interval(1,'te12!@')
            self.tab()
            self.type_keys_with_interval(1,'te12!@')
            
                            ####---ABA5 CFT---####
                             
            if not self.find( "aba5cft", matching=0.97, waiting_time=10000):
                self.not_found("aba5cft")
            self.click()
            if not self.find( "limiteultrapassadocft", matching=0.97, waiting_time=10000):
                self.not_found("limiteultrapassadocft")
            self.click()
            if not self.find( "ultrapassouprazocft", matching=0.97, waiting_time=10000):
                self.not_found("ultrapassouprazocft")
            self.click()
            if not self.find( "chequedevolvidocft", matching=0.97, waiting_time=10000):
                self.not_found("chequedevolvidocft")
            self.click()
            if not self.find( "chequeroubadocft", matching=0.97, waiting_time=10000):
                self.not_found("chequeroubadocft")
            self.click()
            if not self.find( "vendasomenteavistacft", matching=0.97, waiting_time=10000):
                self.not_found("vendasomenteavistacft")
            self.click()
            if not self.find( "spcpempresacft", matching=0.97, waiting_time=10000):
                self.not_found("spcpempresacft")
            self.click()
            if not self.find( "bloqueadocft", matching=0.97, waiting_time=10000):
                self.not_found("bloqueadocft")
            self.click()
            if not self.find( "clientevipcft", matching=0.97, waiting_time=10000):
                self.not_found("clientevipcft")
            self.click()
            
                            ####---LIMITE DE CRÉDITO---###
            
            if not self.find( "limitecrédito", matching=0.97, waiting_time=10000):
                self.not_found("limitecrédito")
            self.click_relative(103, 44)
            self.type_keys_with_interval(1,'123')
            self.enter()
            self.enter()
            self.type_keys_with_interval(1,'123')
            self.enter()
            self.enter()
            
                            ####---VMP---####
                             
            self.enter()
            self.type_keys_with_interval(1,'123')
            
                            ####---VENCIMENTOS DIAS DA SEMANA---####
                             
            if not self.find( "vencimentossegundacft", matching=0.97, waiting_time=10000):
                self.not_found("vencimentossegundacft")
            self.click_relative(12, 26)
            if not self.find( "vencimentossegundacft", matching=0.97, waiting_time=10000):
                self.not_found("vencimentossegundacft")
            self.click_relative(12, 26)
            if not self.find( "vencimentostercacft", matching=0.97, waiting_time=10000):
                self.not_found("vencimentostercacft")
            self.click_relative(13, 48)
            if not self.find( "vencimentostercacft", matching=0.97, waiting_time=10000):
                self.not_found("vencimentostercacft")
            self.click_relative(13, 48)
            if not self.find( "vencimentosquartacft", matching=0.97, waiting_time=10000):
                self.not_found("vencimentosquartacft")
            self.click_relative(134, 28)
            if not self.find( "vencimentosquartacft", matching=0.97, waiting_time=10000):
                self.not_found("vencimentosquartacft")
            self.click_relative(134, 28)
            if not self.find( "vencimentosquintacft", matching=0.97, waiting_time=10000):
                self.not_found("vencimentosquintacft")
            self.click_relative(130, 46)
            if not self.find( "vencimentosquintacft", matching=0.97, waiting_time=10000):
                self.not_found("vencimentosquintacft")
            self.click_relative(130, 46)
            if not self.find( "vencimentossextacft", matching=0.97, waiting_time=10000):
                self.not_found("vencimentossextacft")
            self.click_relative(252, 26)
            if not self.find( "vencimentossextacft", matching=0.97, waiting_time=10000):
                self.not_found("vencimentossextacft")
            self.click_relative(252, 26)
            
            x=0
            while x<3:
                if not self.find( "gerarvencimentos", matching=0.97, waiting_time=10000):
                    self.not_found("gerarvencimentos")
                self.click_relative(478, 43)
                self.type_down()
                self.enter()
                x=x+1
                
            if not self.find( "descontoporcentagemboletocft", matching=0.97, waiting_time=10000):
                self.not_found("descontoporcentagemboletocft")
            self.click_relative(100, 43)
            self.type_keys_with_interval(1,'123')
            if not self.find( "descontovalorcft", matching=0.97, waiting_time=10000):
                self.not_found("descontovalorcft")
            self.click_relative(303, 46)
            self.type_keys_with_interval(1,'123')
            
                            ####---ABA5 P2 CFT---####
                             
            if not self.find( "aba5p2cft", matching=0.97, waiting_time=10000):
                self.not_found("aba5p2cft")
            self.click()
            self.type_keys_with_interval(1,'te12!@')
            self.tab()
            self.type_keys_with_interval(1,'te12!@')
            self.tab()
            self.type_keys_with_interval(1,'te12!@')
            
                            ####---ABA5 P3 CFT---####
                             
            if not self.find( "aba5p3cft", matching=0.97, waiting_time=10000):
                self.not_found("aba5p3cft")
            self.click()
            self.type_keys_with_interval(1,'te12!@')
            self.tab()
            self.type_keys_with_interval(1,'te12!@')
            self.tab()
            self.type_keys_with_interval(1,'te12!@')
            self.tab()
            self.type_keys_with_interval(1,'te12!@')
            
                            ####---ABA5 P4 CFT---####
                             
            if not self.find( "aba5p4cft", matching=0.97, waiting_time=10000):
                self.not_found("aba5p4cft")
            self.click()
            self.type_keys_with_interval(1,'te12!@')
            self.tab()
            self.type_keys_with_interval(1,'te12!@')
            self.tab()
            self.type_keys_with_interval(1,'te12!@')
            
                            ####---ABA6 P1 CFT---####
                             
            if not self.find( "aba6cft", matching=0.97, waiting_time=10000):
                self.not_found("aba6cft")
            self.click()
            if not self.find( "commitspccft", matching=0.97, waiting_time=10000):
                self.not_found("commitspccft")
            self.click_relative(-17, 8)          
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "salvarcommitspccft", matching=0.97, waiting_time=10000):
                self.not_found("salvarcommitspccft")
            self.click()            
            if not self.find( "excluirspccft", matching=0.97, waiting_time=10000):
                self.not_found("excluirspccft")
            self.click_relative(-20, 32)
            #if not self.find( "simexcluircft1", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluircft1")
            #self.click()
            self.enter()

                            ####---ABA6 P2---####
            
            if not self.find( "aba6p2", matching=0.97, waiting_time=10000):
                self.not_found("aba6p2")
            self.click()
            if not self.find( "addregisrepresentantesa6p2cft", matching=0.97, waiting_time=10000):
                self.not_found("addregisrepresentantesa6p2cft")
            self.click_relative(-47, 10)            
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(1,'08658033902')
            self.enter()
            self.type_keys_with_interval(1,'147345348')
            if not self.find( "municipioa6p2cft", matching=0.97, waiting_time=10000):
                self.not_found("municipioa6p2cft")
            self.click_relative(99, 4)
            if not self.find( "cod0525cft", matching=0.97, waiting_time=10000):
                self.not_found("cod0525cft")
            self.click()
            if not self.find( "selecionarcft", matching=0.97, waiting_time=10000):
                self.not_found("selecionarcft")
            self.click()
            self.enter()
            self.enter()
            self.type_keys_with_interval(100,'85055370')
            if not self.find( "a6p2acharcep", matching=0.97, waiting_time=10000):
                self.not_found("a6p2acharcep")
            self.click()
            if not self.find( "complementoa6p2cft", matching=0.97, waiting_time=10000):
                self.not_found("complementoa6p2cft")
            self.click_relative(82, 4)
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(1,'123123123123')
            self.enter()
            self.type_keys_with_interval(1,'123123123123')
            x=0
            while x<7:
                if not self.find( "celulara6p2cft", matching=0.97, waiting_time=10000):
                    self.not_found("celulara6p2cft")
                self.click_relative(290, 5)
                self.type_down()
                self.enter()
                x=x+1
            if not self.find( "faxa6p2cft", matching=0.97, waiting_time=10000):
                self.not_found("faxa6p2cft")
            self.click_relative(38, 4)
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "salvara6p2", matching=0.97, waiting_time=10000):
                self.not_found("salvara6p2")
            self.click_relative(-50, 53)
            if not self.find( "exxcluira6p2cft", matching=0.97, waiting_time=10000):
                self.not_found("exxcluira6p2cft")
            self.click_relative(-50, 34)
            #if not self.find( "simexcluircft1", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluircft1")
            #self.click()
            self.enter()

                            ####---ABA6 P3---####
                             
            if not self.find( "a6p3cft", matching=0.97, waiting_time=10000):
                self.not_found("a6p3cft")
            self.click()
            
            if not self.find( "novoregistroa6p3cft", matching=0.97, waiting_time=10000):
                self.not_found("novoregistroa6p3cft")
            self.click_relative(-133, 9)
            #if not self.find( "simexcluircft1", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluircft1")
            #self.click()
            self.enter()
            if not self.find( "salvara6p3cft", matching=0.97, waiting_time=10000):
                self.not_found("salvara6p3cft")
            self.click_relative(-136, 52)
            if not self.find( "excluira6p3cft", matching=0.97, waiting_time=10000):
                self.not_found("excluira6p3cft")
            self.click_relative(-137, 35)
            #if not self.find( "simexcluircft1", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluircft1")
            #self.click()
            self.enter()

                            ####---ABA6 P4---####
                             
            if not self.find( "aba6p4cft", matching=0.97, waiting_time=10000):
                self.not_found("aba6p4cft")
            self.click()
            if not self.find( "novoregistroa6p4cft", matching=0.97, waiting_time=10000):
                self.not_found("novoregistroa6p4cft")
            self.click_relative(-226, 9)
            if not self.find( "tipodocontatocft", matching=0.97, waiting_time=10000):
                self.not_found("tipodocontatocft")
            self.click_relative(79, 56)
            x=0
            while x<6:
                if not self.find( "tipodocontatocfta6p4", matching=0.97, waiting_time=10000):
                    self.not_found("tipodocontatocfta6p4")
                self.click_relative(232, 61)
                self.type_down()
                self.enter()
                x=x+1
            self.type_keys_with_interval(100,'08658033902')
            self.enter()
            self.type_keys_with_interval(100,'147345348')
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(100,'01012000')
            self.enter()
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(100,'85055370')
            if not self.find( "buscarcepa6p4", matching=0.97, waiting_time=10000):
                self.not_found("buscarcepa6p4")
            self.click_relative(132, 4)
            if not self.find( "crca6p4cft", matching=0.97, waiting_time=10000):
                self.not_found("crca6p4cft")
            self.click_relative(60, 3)
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "botaobuscarmunicipioa6p4cft", matching=0.97, waiting_time=10000):
                self.not_found("botaobuscarmunicipioa6p4cft")
            self.click_relative(106, 6)
            if not self.find( "cod0525cft", matching=0.97, waiting_time=10000):
                self.not_found("cod0525cft")
            self.click()
            if not self.find( "selecionarcft", matching=0.97, waiting_time=10000):
                self.not_found("selecionarcft")
            self.click()
            self.enter()
            self.enter()
            self.type_keys_with_interval(1,'123123123123')
            x=0
            while x<8:
                if not self.find( "operadoracelular1a6p4cft", matching=0.97, waiting_time=10000):
                    self.not_found("operadoracelular1a6p4cft")
                self.click_relative(236, 190)
                self.type_down()
                self.enter()
                x=x+1
            self.type_keys_with_interval(1,'123123123123')
            x=0
            while x<7:
                if not self.find( "operadora2a6p4cft", matching=0.97, waiting_time=10000):
                    self.not_found("operadora2a6p4cft")
                self.click_relative(633, 189)
                self.type_down()
                self.enter()
                x=x+1
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(1,'123123123123')
            self.enter()
            x=0
            while x<5:
                self.type_down()
                x=x+1
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            if not self.find( "recebeemaila6p4cft", matching=0.97, waiting_time=10000):
                self.not_found("recebeemaila6p4cft")
            self.click_relative(564, 6)
            if not self.find( "recebemaila6p4cft", matching=0.97, waiting_time=10000):
                self.not_found("recebemaila6p4cft")
            self.click()
            if not self.find( "recebemaildocecfta6p4", matching=0.97, waiting_time=10000):
                self.not_found("recebemaildocecfta6p4")
            self.click()
            if not self.find( "recebemailvendascfta6p4", matching=0.97, waiting_time=10000):
                self.not_found("recebemailvendascfta6p4")
            self.click()
            if not self.find( "recebemailcomprascfta6p4", matching=0.97, waiting_time=10000):
                self.not_found("recebemailcomprascfta6p4")
            self.click()
            if not self.find( "recebemailfinana6p4cft", matching=0.97, waiting_time=10000):
                self.not_found("recebemailfinana6p4cft")
            self.click()
            if not self.find( "recebemailrhcfta6p4", matching=0.97, waiting_time=10000):
                self.not_found("recebemailrhcfta6p4")
            self.click()
            if not self.find( "recebemailfiscalcfta6p4", matching=0.97, waiting_time=10000):
                self.not_found("recebemailfiscalcfta6p4")
            self.click()
            if not self.find( "recebemailcontabilcfta6p4", matching=0.97, waiting_time=10000):
                self.not_found("recebemailcontabilcfta6p4")
            self.click()
            self.type_down()
            if not self.find( "recebemailcontratoa6p4cft", matching=0.97, waiting_time=10000):
                self.not_found("recebemailcontratoa6p4cft")
            self.click()
            if not self.find( "recontratocfta6p4", matching=0.97, waiting_time=10000):
                self.not_found("recontratocfta6p4")
            self.click()
            if not self.find( "recontabilcfta6p4", matching=0.97, waiting_time=10000):
                self.not_found("recontabilcfta6p4")
            self.click()
            if not self.find( "refiscalcfta6p4", matching=0.97, waiting_time=10000):
                self.not_found("refiscalcfta6p4")
            self.click()
            if not self.find( "rerhcfta6p4", matching=0.97, waiting_time=10000):
                self.not_found("rerhcfta6p4")
            self.click()
            if not self.find( "refinanceirocft2", matching=0.97, waiting_time=10000):
                self.not_found("refinanceirocft2")
            self.click()            
            if not self.find( "recomprascft2", matching=0.97, waiting_time=10000):
                self.not_found("recomprascft2")
            self.click()           
            if not self.find( "revendascfta6p4", matching=0.97, waiting_time=10000):
                self.not_found("revendascfta6p4")
            self.click()
            if not self.find( "redocecfta6p4", matching=0.97, waiting_time=10000):
                self.not_found("redocecfta6p4")
            self.click()
            self.type_up()
            if not self.find( "retodoscfta6p4", matching=0.97, waiting_time=10000):
                self.not_found("retodoscfta6p4")
            self.click()
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "salvara6p4", matching=0.97, waiting_time=10000):
                self.not_found("salvara6p4")
            self.click_relative(-224, 55)
            if not self.find( "excluira6p4", matching=0.97, waiting_time=10000):
                self.not_found("excluira6p4")
            self.click_relative(-226, 32)
            #if not self.find( "simexcluircft1", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluircft1")
            #self.click()
            self.enter()

                            ####---ABA6 P5---####
                             
            if not self.find( "a6p5cft", matching=0.97, waiting_time=10000):
                self.not_found("a6p5cft")
            self.click()
            if not self.find( "addregistroa6p5", matching=0.97, waiting_time=10000):
                self.not_found("addregistroa6p5")
            self.click_relative(-328, 9)
            if not self.find( "procuraavaliacaoa6p5", matching=0.97, waiting_time=10000):
                self.not_found("procuraavaliacaoa6p5")
            self.click_relative(113, 45)
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "selecionarcft", matching=0.97, waiting_time=10000):
                self.not_found("selecionarcft")
            self.click()
            if not self.find( "dataa6p5", matching=0.97, waiting_time=10000):
                self.not_found("dataa6p5")
            self.click_relative(466, 44)
            self.type_keys_with_interval(100,'01012022')
            if not self.find( "commita6p5", matching=0.97, waiting_time=10000):
                self.not_found("commita6p5")
            self.click_relative(-17, 31)
            if not self.find( "oka6p5cft", matching=0.97, waiting_time=10000):
                self.not_found("oka6p5cft")
            self.click()
            if not self.find( "cancelarcfta6p5", matching=0.97, waiting_time=10000):
                self.not_found("cancelarcfta6p5")
            self.click_relative(-17, 52)
            
                            ####---ABA6 P6---####
                             
            if not self.find( "a6p6cft", matching=0.97, waiting_time=10000):
                self.not_found("a6p6cft")
            self.click()
            if not self.find( "adda6p6cft", matching=0.97, waiting_time=10000):
                self.not_found("adda6p6cft")
            self.click_relative(-387, 9)
            if not self.find( "codtestecfta6p6", matching=0.97, waiting_time=10000):
                self.not_found("codtestecfta6p6")
            self.click_relative(-98, 7)
            if not self.find( "selecionarcft", matching=0.97, waiting_time=10000):
                self.not_found("selecionarcft")
            self.click()
            if not self.find( "excluira6p6", matching=0.97, waiting_time=10000):
                self.not_found("excluira6p6")
            self.click_relative(-389, 32)
            #if not self.find( "simexcluircft1", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluircft1")
            #self.click()
            self.enter()

                            ####---ABA6 P7---####
                             
            if not self.find( "a6p7cft", matching=0.97, waiting_time=10000):
                self.not_found("a6p7cft")
            self.click()
            if not self.find( "adda6p7cft", matching=0.97, waiting_time=10000):
                self.not_found("adda6p7cft")
            self.click_relative(-501, 9)
            if not self.find( "procurarquivoacfta6", matching=0.97, waiting_time=10000):
                self.not_found("procurarquivoacfta6")
            self.click() 
            self.wait(500)           
            #if not self.find( "selecionararquivoa6p7cft", matching=0.97, waiting_time=10000):
            #    self.not_found("selecionararquivoa6p7cft")
            #self.click_relative(145, 120)
            #if not self.find( "abrirarquivocfta6", matching=0.97, waiting_time=10000):
            #    self.not_found("abrirarquivocfta6")
            #self.click()
            self.key_esc()
            self.wait(500)          
            if not self.find( "tipoa6p7cft", matching=0.97, waiting_time=10000):
                self.not_found("tipoa6p7cft")
            self.click_relative(709, 31)
            self.enter()
            if not self.find( "obsa6p7cft", matching=0.97, waiting_time=10000):
                self.not_found("obsa6p7cft")
            self.click_relative(9, 31)
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "anexoarquivocfta6p7", matching=0.97, waiting_time=10000):
                self.not_found("anexoarquivocfta6p7")
            self.click_relative(7, 142)
            if not self.find( "cancelaarqteste1", matching=0.97, waiting_time=10000):
                self.not_found("cancelaarqteste1")
            self.click_relative(5, 184)
            if not self.find( "retornaanexoarqteste1", matching=0.97, waiting_time=10000):
                self.not_found("retornaanexoarqteste1")
            self.click_relative(25, 41)          
            #if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
            #    self.not_found("retornarpe")
            #self.click()
            if not self.find( "excluira6p7cft", matching=0.97, waiting_time=10000):
                self.not_found("excluira6p7cft")
            self.click_relative(-502, 32)
            #if not self.find( "simexcluircft1", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluircft1")
            #self.click()
            self.enter()

                            ####---ABA6 P8---####
                             
            if not self.find( "a6p8cft", matching=0.97, waiting_time=10000):
                self.not_found("a6p8cft")
            self.click()
            if not self.find( "addcfta6p8", matching=0.97, waiting_time=10000):
                self.not_found("addcfta6p8")
            self.click_relative(-572, 9)
            #if not self.find( "simexcluircft1", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluircft1")
            #self.click()
            self.enter()
            self.type_keys_with_interval(100,'01012022')
            self.enter()
            self.type_keys_with_interval(1,'123')
            self.enter()
            self.type_keys_with_interval(1,'12')
            self.enter()
            self.type_keys_with_interval(100,'01012022')
            self.enter()
            self.type_keys_with_interval(100,'01012022')
            self.enter()
            self.type_keys_with_interval(1,'123')
            if not self.find( "gerarfinanceironfcfta6", matching=0.97, waiting_time=10000):
                self.not_found("gerarfinanceironfcfta6")
            self.click_relative(1125, 45)
            if not self.find( "gerarfinanceironfcfta6", matching=0.97, waiting_time=10000):
                self.not_found("gerarfinanceironfcfta6")
            self.click_relative(1125, 45)
            self.enter()
            self.type_keys_with_interval(1,'123')
            if not self.find( "tipovalorimplantacao", matching=0.97, waiting_time=10000):
                self.not_found("tipovalorimplantacao")
            self.click_relative(115, 87)
            self.type_down()
            self.enter()
            if not self.find( "tipovalorimplantacao", matching=0.97, waiting_time=10000):
                self.not_found("tipovalorimplantacao")
            self.click_relative(115, 87)
            self.type_up()
            self.enter()
            if not self.find( "tipodocontrato", matching=0.97, waiting_time=10000):
                self.not_found("tipodocontrato")
            self.click_relative(62, 44)
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "comissaocfta6p8", matching=0.97, waiting_time=10000):
                self.not_found("comissaocfta6p8")
            self.click_relative(462, 45)
            if not self.find( "cod001cft", matching=0.97, waiting_time=10000):
                self.not_found("cod001cft")
            self.click()
            if not self.find( "selecionarcft", matching=0.97, waiting_time=10000):
                self.not_found("selecionarcft")
            self.click()
            if not self.find( "obscontratuaisa6p8", matching=0.97, waiting_time=10000):
                self.not_found("obscontratuaisa6p8")
            self.click_relative(10, 31)
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "commita6p8cft", matching=0.97, waiting_time=10000):
                self.not_found("commita6p8cft")
            self.click_relative(-571, 53)
            if not self.find( "excluira6p8cft", matching=0.97, waiting_time=10000):
                self.not_found("excluira6p8cft")
            self.click_relative(-570, 30)
            #if not self.find( "simexcluircft1", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluircft1")
            #self.click()
            self.enter()

                            ####---ABA6 P9---####
                             
            if not self.find( "a6p9cft", matching=0.97, waiting_time=10000):
                self.not_found("a6p9cft")
            self.click()
            if not self.find( "adda6p9", matching=0.97, waiting_time=10000):
                self.not_found("adda6p9")
            self.click_relative(-627, 8)
            if not self.find( "procuraclientea6p9", matching=0.97, waiting_time=10000):
                self.not_found("procuraclientea6p9")
            self.click_relative(-442, 41)
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            self.wait(1500)
            if not self.find( "cod0081260a6p9", matching=0.97, waiting_time=10000):
                self.not_found("cod0081260a6p9")
            self.click()
            if not self.find( "selecionarcft", matching=0.97, waiting_time=10000):
                self.not_found("selecionarcft")
            self.click()
            self.enter()
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "commita6p9cft", matching=0.97, waiting_time=10000):
                self.not_found("commita6p9cft")
            self.click_relative(-627, 52)
            if not self.find( "excluira6p9cft", matching=0.97, waiting_time=10000):
                self.not_found("excluira6p9cft")
            self.click_relative(-627, 32)
            #if not self.find( "simexcluircft1", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluircft1")
            #self.click()
            self.enter()

                            ####---ABA6 P10---####
                             
            if not self.find( "a6p10cft", matching=0.97, waiting_time=10000):
                self.not_found("a6p10cft")
            self.click()
            if not self.find( "adda6p10cft", matching=0.97, waiting_time=10000):
                self.not_found("adda6p10cft")
            self.click_relative(-730, 9)
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---ABA6 P11---####
                             
            if not self.find( "a6p11rateiocft", matching=0.97, waiting_time=10000):
                self.not_found("a6p11rateiocft")
            self.click()
            
            if not self.find( "addrateioa6p11cft", matching=0.97, waiting_time=10000):
                self.not_found("addrateioa6p11cft")
            self.click_relative(-842, 9)            
            if not self.find( "buscacfta6p11", matching=0.97, waiting_time=10000):
                self.not_found("buscacfta6p11")
            self.click_relative(-646, 44)
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            self.enter()
            self.enter()
            self.type_keys_with_interval(1,'90')
            #if not self.find( "commitcfta6p11", matching=0.97, waiting_time=10000):
            #    self.not_found("commitcfta6p11")
            #self.click_relative(-844, 53)
            if not self.find( "cancelara6p11cft", matching=0.97, waiting_time=10000):
                self.not_found("cancelara6p11cft")
            self.click_relative(-843, 72)
            
                            ####---ABA6 P12---####
                             
            if not self.find( "a6p12", matching=0.97, waiting_time=10000):
                self.not_found("a6p12")
            self.click()
            
            if not self.find( "adda6p12cft", matching=0.97, waiting_time=10000):
                self.not_found("adda6p12cft")
            self.click_relative(-964, 11)
                                   
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            if not self.find( "commita6p12cft", matching=0.97, waiting_time=10000):
                self.not_found("commita6p12cft")
            self.click_relative(-965, 56)
            
            if not self.find( "excluira6p12cft", matching=0.97, waiting_time=10000):
                self.not_found("excluira6p12cft")
            self.click_relative(-965, 32)
            
            #if not self.find( "simexcluircft1", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluircft1")
            #self.click()
            self.enter()

                            ####---ABA6 P13---####
                             
            if not self.find( "a6p12cft", matching=0.97, waiting_time=10000):
                self.not_found("a6p12cft")
            self.click()
            if not self.find( "adda6p13cft", matching=0.97, waiting_time=10000):
                self.not_found("adda6p13cft")
            self.click_relative(-1018, 34)            
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            if not self.find( "commita6p13cft", matching=0.97, waiting_time=10000):
                self.not_found("commita6p13cft")
            self.click_relative(-1016, 101)
            
            if not self.find( "excluira6p13cft", matching=0.97, waiting_time=10000):
                self.not_found("excluira6p13cft")
            self.click_relative(-1017, 77)
            
            self.enter()
            
            
                            ####---ABA7---####
                             
            if not self.find( "aba7cft", matching=0.97, waiting_time=10000):
                self.not_found("aba7cft")
            self.click()
            if not self.find( "periodoaba7cft", matching=0.97, waiting_time=10000):
                self.not_found("periodoaba7cft")
            self.click_relative(220, 27)
            if not self.find( "carregardiaaba7", matching=0.97, waiting_time=10000):
                self.not_found("carregardiaaba7")
            self.click()
            if not self.find( "carregardiaatualaba7", matching=0.97, waiting_time=10000):
                self.not_found("carregardiaatualaba7")
            self.click()
            if not self.find( "visualizarmovimentoevetivo1", matching=0.97, waiting_time=10000):
                self.not_found("visualizarmovimentoevetivo1")
            self.click_relative(89, 35)
            if not self.find( "visualizarmovimentoefetivo2", matching=0.97, waiting_time=10000):
                self.not_found("visualizarmovimentoefetivo2")
            self.click_relative(170, 31)
            if not self.find( "visualizarmovimentoefetivo3", matching=0.97, waiting_time=10000):
                self.not_found("visualizarmovimentoefetivo3")
            self.click_relative(8, 33)
            if not self.find( "movagrupadoitensaba7", matching=0.97, waiting_time=10000):
                self.not_found("movagrupadoitensaba7")
            self.click()
            if not self.find( "consultarmvtfinanceiroaba7", matching=0.97, waiting_time=10000):
                self.not_found("consultarmvtfinanceiroaba7")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---FINALIZAR CFT---####
                             
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "procurarcft", matching=0.97, waiting_time=10000):
                self.not_found("procurarcft")
            self.click_relative(20, 32)
            self.type_keys_with_interval(1,'te12')
            self.enter()
            if not self.find( "achoucftteste", matching=0.97, waiting_time=10000):
                self.not_found("achoucftteste")
            self.click()
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            self.wait(5000)
            if not self.find( "excluircft1", matching=0.97, waiting_time=10000):
                self.not_found("excluircft1")
            self.click()
            #if not self.find( "simexcluircft1", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluircft1")
            #self.click()
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "fecharsistemacft", matching=0.97, waiting_time=10000):
                self.not_found("fecharsistemacft")
            self.click()                
            
             
                            ####---REDES SOCIAIS---#### 
            
            if not self.find( "abrircadastros_abacadastro", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro")
            self.click()
            if not self.find( "redessociais", matching=0.97, waiting_time=10000):
                self.not_found("redessociais")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()            
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()
            self.type_keys_with_interval(1,'te12!@')
            
            x=0
            while x<13:
                if not self.find( "iconers", matching=0.97, waiting_time=10000):
                    self.not_found("iconers")
                self.click_relative(184, 8)
                self.type_down()
                self.enter()
                x=x+1
                
            if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
                self.not_found("salvarrs")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "redesocialteste", matching=0.97, waiting_time=10000):
                self.not_found("redesocialteste")
            self.click()
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                self.not_found("excluirrs")
            self.click()
            #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirrs")
            #self.click()
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---AVALIACOES ISO---####
                             
            if not self.find( "abrircadastros_abacadastro", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro")
            self.click()
            if not self.find( "avaliacoesiso", matching=0.97, waiting_time=10000):
                self.not_found("avaliacoesiso")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "salvaravaliacao", matching=0.97, waiting_time=10000):
                self.not_found("salvaravaliacao")
            self.click()
            if not self.find( "addnovaenquete", matching=0.97, waiting_time=10000):
                self.not_found("addnovaenquete")
            self.click_relative(8, 33)
            if not self.find( "buscarenquete", matching=0.97, waiting_time=10000):
                self.not_found("buscarenquete")
            self.click_relative(134, 157)
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "selecionarenquete", matching=0.97, waiting_time=10000):
                self.not_found("selecionarenquete")
            self.click()
            if not self.find( "ordemcima", matching=0.97, waiting_time=10000):
                self.not_found("ordemcima")
            self.double_click_relative(67, 0)
            if not self.find( "ordembaixo", matching=0.97, waiting_time=10000):
                self.not_found("ordembaixo")
            self.click_relative(69, 11)
            if not self.find( "cancelarenquete", matching=0.97, waiting_time=10000):
                self.not_found("cancelarenquete")
            self.click_relative(-598, 66)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "redesocialteste", matching=0.97, waiting_time=10000):
                self.not_found("redesocialteste")
            self.click()
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                self.not_found("excluirrs")
            self.click()
            #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirrs")
            #self.click()
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---LINHAS, RAMOS, ATIVIDADES ETC---####
                             
            if not self.find( "abrircadastros_abacadastro", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro")
            self.click()
            if not self.find( "linhasramosetc", matching=0.97, waiting_time=10000):
                self.not_found("linhasramosetc")
            self.click()
            if not self.find( "linha", matching=0.97, waiting_time=10000):
                self.not_found("linha")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "salvaravaliacao", matching=0.97, waiting_time=10000):
                self.not_found("salvaravaliacao")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "redesocialteste", matching=0.97, waiting_time=10000):
                self.not_found("redesocialteste")
            self.click()
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                self.not_found("excluirrs")
            self.click()
            #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirrs")
            #self.click()
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
            
            
                        
            if not self.find( "abrircadastros_abacadastro", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro")
            self.click()
            if not self.find( "linhasramosetc", matching=0.97, waiting_time=10000):
                self.not_found("linhasramosetc")
            self.click()
            if not self.find( "ramodeatividade", matching=0.97, waiting_time=10000):
                self.not_found("ramodeatividade")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "salvaravaliacao", matching=0.97, waiting_time=10000):
                self.not_found("salvaravaliacao")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()            
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "localizaramo", matching=0.97, waiting_time=10000):
                self.not_found("localizaramo")
            self.click_relative(17, 26)
            self.type_keys_with_interval(1,'te12')
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "redesocialteste", matching=0.97, waiting_time=10000):
                self.not_found("redesocialteste")
            self.click()
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                self.not_found("excluirrs")
            self.click()
            #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirrs")
            #self.click()
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
            
            
            
            if not self.find( "abrircadastros_abacadastro", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro")
            self.click()
            if not self.find( "linhasramosetc", matching=0.97, waiting_time=10000):
                self.not_found("linhasramosetc")
            self.click()
            if not self.find( "rotasdeentrega", matching=0.97, waiting_time=10000):
                self.not_found("rotasdeentrega")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "salvaravaliacao", matching=0.97, waiting_time=10000):
                self.not_found("salvaravaliacao")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()            
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "localizaramo", matching=0.97, waiting_time=10000):
                self.not_found("localizaramo")
            self.click_relative(17, 26)
            self.type_keys_with_interval(1,'te12')
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "redesocialteste", matching=0.97, waiting_time=10000):
                self.not_found("redesocialteste")
            self.click()
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                self.not_found("excluirrs")
            self.click()
            #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirrs")
            #self.click()
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
            
            
            
            if not self.find( "abrircadastros_abacadastro", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro")
            self.click()
            if not self.find( "linhasramosetc", matching=0.97, waiting_time=10000):
                self.not_found("linhasramosetc")
            self.click()
            if not self.find( "segmento", matching=0.97, waiting_time=10000):
                self.not_found("segmento")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "salvaravaliacao", matching=0.97, waiting_time=10000):
                self.not_found("salvaravaliacao")
            self.click()  
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()                    
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "redesocialteste", matching=0.97, waiting_time=10000):
                self.not_found("redesocialteste")
            self.click()
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                self.not_found("excluirrs")
            self.click()
            #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirrs")
            #self.click()
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
            
            
            
            if not self.find( "abrircadastros_abacadastro", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro")
            self.click()
            if not self.find( "linhasramosetc", matching=0.97, waiting_time=10000):
                self.not_found("linhasramosetc")
            self.click()
            if not self.find( "tiposdecontratos", matching=0.97, waiting_time=10000):
                self.not_found("tiposdecontratos")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "salvaravaliacao", matching=0.97, waiting_time=10000):
                self.not_found("salvaravaliacao")
            self.click()  
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()                    
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "redesocialteste", matching=0.97, waiting_time=10000):
                self.not_found("redesocialteste")
            self.click()
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                self.not_found("excluirrs")
            self.click()
            #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirrs")
            #self.click()
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---VENDEDORES, COMPRADORES---####
            
            if not self.find( "abrircadastros_abacadastro", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro")
            self.click()
            if not self.find( "vendedorescompradores", matching=0.97, waiting_time=10000):
                self.not_found("vendedorescompradores")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(100,'08658033902')
            self.enter()
            self.type_keys_with_interval(100,'147345348')
            if not self.find( "vcrjuridica", matching=0.97, waiting_time=10000):
                self.not_found("vcrjuridica")
            self.click()
            if not self.find( "vcrfisica", matching=0.97, waiting_time=10000):
                self.not_found("vcrfisica")
            self.click()
            if not self.find( "vcrinativo", matching=0.97, waiting_time=10000):
                self.not_found("vcrinativo")
            self.click()
            if not self.find( "vcrativo", matching=0.97, waiting_time=10000):
                self.not_found("vcrativo")
            self.click()
            if not self.find( "vendedorvcr", matching=0.97, waiting_time=10000):
                self.not_found("vendedorvcr")
            self.click()
            if not self.find( "vendedorvcr2", matching=0.97, waiting_time=10000):
                self.not_found("vendedorvcr2")
            self.click()
            if not self.find( "compradorvcr", matching=0.97, waiting_time=10000):
                self.not_found("compradorvcr")
            self.click_relative(746, -23)
            if not self.find( "compradorvcr", matching=0.97, waiting_time=10000):
                self.not_found("compradorvcr")
            self.click_relative(746, -23)
            if not self.find( "enderecovcr", matching=0.97, waiting_time=10000):
                self.not_found("enderecovcr")
            self.click_relative(9, 43)
            self.type_keys_with_interval(100,'85055370')
            self.enter()
            self.enter()
            self.type_keys_with_interval(1,'874')
            self.enter()
            self.type_keys_with_interval(1,'casa')
            if not self.find( "municipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("municipiovcr")
            self.click_relative(59, 25)
            self.backspace()
            self.enter()
            self.wait(2000)
            self.type_down()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=100000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            if not self.find( "telefonevcr", matching=0.97, waiting_time=10000):
                self.not_found("telefonevcr")
            self.click_relative(553, 90)
            self.type_keys_with_interval(1,'123123123123')
            self.enter()
            self.type_keys_with_interval(1,'123123123123')
            self.enter()
            self.type_keys_with_interval(1,'testeteorema@testeteorema.com.br')
            if not self.find( "botaoemailvcr", matching=0.97, waiting_time=10000):
                self.not_found("botaoemailvcr")
            self.click_relative(344, 22)
            if not self.find( "fecharaddcontavcr", matching=0.97, waiting_time=10000):
                self.not_found("fecharaddcontavcr")
            self.click_relative(428, 7)
            if not self.find( "fecharaddemailvcr2", matching=0.97, waiting_time=10000):
                self.not_found("fecharaddemailvcr2")
            self.click_relative(493, -236)
            
            if not self.find( "familiacomprasvcr", matching=0.97, waiting_time=10000):
                self.not_found("familiacomprasvcr")
            self.click_relative(63, 42)
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            if not self.find( "datacadastrovcr", matching=0.97, waiting_time=10000):
                self.not_found("datacadastrovcr")
            self.click_relative(545, 44)
            if not self.find( "diadatavcr", matching=0.97, waiting_time=10000):
                self.not_found("diadatavcr")
            self.click_relative(100, 60)
            self.enter()
            
            x=0
            while x<3:
                if not self.find( "ratioosvcr", matching=0.97, waiting_time=10000):
                    self.not_found("ratioosvcr")
                self.click_relative(92, 28)
                self.type_down()
                self.enter()
                x=x+1
                
            if not self.find( "bancovcr", matching=0.97, waiting_time=10000):
                self.not_found("bancovcr")
            self.click_relative(65, 46)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.enter()
            self.enter()
            self.type_keys_with_interval(1,'t1!')
            self.enter()
            self.type_keys_with_interval(1,'t1!')
            if not self.find( "clientevcr", matching=0.97, waiting_time=10000):
                self.not_found("clientevcr")
            self.click_relative(843, 43)
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            self.wait(1500)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            if not self.find( "nivelcomissaovcr", matching=0.97, waiting_time=10000):
                self.not_found("nivelcomissaovcr")
            self.click_relative(60, 47)
            self.type_keys_with_interval(1,'123')
            self.enter()
            self.type_keys_with_interval(1,'123')
            self.enter()
            self.type_keys_with_interval(1,'123')
            self.enter()
            self.type_keys_with_interval(1,'123')
            self.enter()
            self.type_keys_with_interval(1,'123')
            self.enter()
            if not self.find( "fatovcr", matching=0.97, waiting_time=10000):
                self.not_found("fatovcr")
            self.click_relative(670, 42)
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "obsvcr", matching=0.97, waiting_time=10000):
                self.not_found("obsvcr")
            self.click_relative(14, 42)
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "salvarvcr", matching=0.97, waiting_time=10000):
                self.not_found("salvarvcr")
            self.click()
            if not self.find( "aba2gerenciavsr", matching=0.97, waiting_time=10000):
                self.not_found("aba2gerenciavsr")
            self.click()
            if not self.find( "addregistroaba2vcr", matching=0.97, waiting_time=10000):
                self.not_found("addregistroaba2vcr")
            self.click_relative(-50, 35)
            if not self.find( "buscargerenciavcr", matching=0.97, waiting_time=10000):
                self.not_found("buscargerenciavcr")
            self.click_relative(116, 4)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            
            x=0
            while x<2:
                if not self.find( "tipovcr", matching=0.97, waiting_time=10000):
                    self.not_found("tipovcr")
                self.click_relative(127, 6)
                self.type_down()
                self.enter()
                x=x+1
                
            self.type_keys_with_interval(1,'10')
            self.enter()
            if not self.find( "salvaraba2vcr", matching=0.97, waiting_time=10000):
                self.not_found("salvaraba2vcr")
            self.click()
            if not self.find( "apagaraba2gerenciavcr", matching=0.97, waiting_time=10000):
                self.not_found("apagaraba2gerenciavcr")
            self.click_relative(-54, 57)
            if not self.find( "confirmaexcluiraba2vcr", matching=0.97, waiting_time=10000):
                self.not_found("confirmaexcluiraba2vcr")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "redesocialteste", matching=0.97, waiting_time=10000):
                self.not_found("redesocialteste")
            self.click()
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                self.not_found("excluirrs")
            self.click()
            #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
            #   self.not_found("simexcluirrs")
            #self.click()
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---ENQUETES---####
            
            if not self.find( "abrircadastros_abacadastro", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro")
            self.click()
            if not self.find( "enquetes", matching=0.97, waiting_time=10000):
                self.not_found("enquetes")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()
            self.type_keys_with_interval(1,'te12!@')
            
            x=0
            while x<5:
                if not self.find( "tipodeutilizacao1", matching=0.97, waiting_time=10000):
                    self.not_found("tipodeutilizacao1")
                self.click_relative(276, 51)
                self.type_down()
                self.enter()
                x=x+1
             
            if not self.find( "tiporesposta", matching=0.97, waiting_time=10000):
                self.not_found("tiporesposta")
            self.click_relative(271, 31)
            self.type_up()
            self.enter()
            
            if not self.find( "buscarempresaenquete", matching=0.97, waiting_time=10000):
                self.not_found("buscarempresaenquete")
            self.click_relative(53, 32)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            if not self.find( "periodoenquete", matching=0.97, waiting_time=10000):
                self.not_found("periodoenquete")
            self.click_relative(73, 31)
            if not self.find( "diaperiodoenquete1", matching=0.97, waiting_time=10000):
                self.not_found("diaperiodoenquete1")
            self.click_relative(94, 58)
            if not self.find( "periodoenquete2", matching=0.97, waiting_time=10000):
                self.not_found("periodoenquete2")
            self.click_relative(180, 30)
            if not self.find( "dataenquete2", matching=0.97, waiting_time=10000):
                self.not_found("dataenquete2")
            self.click_relative(59, 91)
            if not self.find( "questoesenquete", matching=0.97, waiting_time=10000):
                self.not_found("questoesenquete")
            self.click_relative(15, 46)
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "salvarenquete", matching=0.97, waiting_time=10000):
                self.not_found("salvarenquete")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "redesocialteste", matching=0.97, waiting_time=10000):
                self.not_found("redesocialteste")
            self.click()
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                self.not_found("excluirrs")
            self.click()
            #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirrs")
            #self.click()
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---ITENS DE ESTOQUE---####
                             
            if not self.find( "abrircadastros_abacadastro", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro")
            self.click()
            if not self.find( "itensdeestoque", matching=0.97, waiting_time=10000):
                self.not_found("itensdeestoque")
            self.click()
            if not self.find( "agrupamentoie", matching=0.97, waiting_time=10000):
                self.not_found("agrupamentoie")
            self.click()
            if not self.find( "familiasIE", matching=0.97, waiting_time=10000):
                self.not_found("familiasIE")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "salvarenquete", matching=0.97, waiting_time=10000):
                self.not_found("salvarenquete")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "redesocialteste", matching=0.97, waiting_time=10000):
                self.not_found("redesocialteste")
            self.click()
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                self.not_found("excluirrs")
            self.click()
            #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirrs")
            #self.click()
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
            if not self.find( "abrircadastros_abacadastro", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro")
            self.click()
            if not self.find( "itensdeestoque", matching=0.97, waiting_time=10000):
                self.not_found("itensdeestoque")
            self.click()
            if not self.find( "agrupamentoie", matching=0.97, waiting_time=10000):
                self.not_found("agrupamentoie")
            self.click()
            if not self.find( "gruposIE", matching=0.97, waiting_time=10000):
                self.not_found("gruposIE")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "grupofiscalIE", matching=0.97, waiting_time=10000):
                self.not_found("grupofiscalIE")
            self.click_relative(73, 46)
            if not self.find( "cod006IE", matching=0.97, waiting_time=10000):
                self.not_found("cod006IE")
            self.click()            
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            if not self.find( "salvarenquete", matching=0.97, waiting_time=10000):
                self.not_found("salvarenquete")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "achargrupoteste", matching=0.97, waiting_time=10000):
                self.not_found("achargrupoteste")
            self.click_relative(5, 30)
            self.type_keys_with_interval(1,'te12')
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "redesocialteste", matching=0.97, waiting_time=10000):
                self.not_found("redesocialteste")
            self.click()
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                self.not_found("excluirrs")
            self.click()
            #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirrs")
            #self.click()
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
            if not self.find( "abrircadastros_abacadastro", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro")
            self.click()
            if not self.find( "itensdeestoque", matching=0.97, waiting_time=10000):
                self.not_found("itensdeestoque")
            self.click()
            if not self.find( "agrupamentoie", matching=0.97, waiting_time=10000):
                self.not_found("agrupamentoie")
            self.click()
            if not self.find( "subgruposIE", matching=0.97, waiting_time=10000):
                self.not_found("subgruposIE")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "salvarenquete", matching=0.97, waiting_time=10000):
                self.not_found("salvarenquete")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "achargrupoteste", matching=0.97, waiting_time=10000):
                self.not_found("achargrupoteste")
            self.click_relative(5, 30)
            self.type_keys_with_interval(1,'te12')
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "redesocialteste", matching=0.97, waiting_time=10000):
                self.not_found("redesocialteste")
            self.click()
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                self.not_found("excluirrs")
            self.click()
            #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirrs")
            #self.click()
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
            if not self.find( "abrircadastros_abacadastro", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro")
            self.click()
            if not self.find( "itensdeestoque", matching=0.97, waiting_time=10000):
                self.not_found("itensdeestoque")
            self.click()
            if not self.find( "agrupamentoie", matching=0.97, waiting_time=10000):
                self.not_found("agrupamentoie")
            self.click()
            if not self.find( "marcasIE", matching=0.97, waiting_time=10000):
                self.not_found("marcasIE")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "salvarenquete", matching=0.97, waiting_time=10000):
                self.not_found("salvarenquete")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "achargrupoteste", matching=0.97, waiting_time=10000):
                self.not_found("achargrupoteste")
            self.click_relative(5, 30)
            self.type_keys_with_interval(1,'te12')
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "redesocialteste", matching=0.97, waiting_time=10000):
                self.not_found("redesocialteste")
            self.click()
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                self.not_found("excluirrs")
            self.click()
            #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirrs")
            #self.click()
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
            if not self.find( "abrircadastros_abacadastro", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro")
            self.click()
            if not self.find( "itensdeestoque", matching=0.97, waiting_time=10000):
                self.not_found("itensdeestoque")
            self.click()
            if not self.find( "agrupamentoie", matching=0.97, waiting_time=10000):
                self.not_found("agrupamentoie")
            self.click()
            if not self.find( "unidadesIE", matching=0.97, waiting_time=10000):
                self.not_found("unidadesIE")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            if not self.find( "cancelareditarIE", matching=0.97, waiting_time=10000):
                self.not_found("cancelareditarIE")
            self.click()
            #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirrs")
            #self.click()
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "salvarenquete", matching=0.97, waiting_time=10000):
                self.not_found("salvarenquete")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "achargrupoteste", matching=0.97, waiting_time=10000):
                self.not_found("achargrupoteste")
            self.click_relative(5, 30)
            self.type_keys_with_interval(1,'te12')
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "unidadeteste", matching=0.97, waiting_time=10000):
                self.not_found("unidadeteste")
            self.click()            
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                self.not_found("excluirrs")
            self.click()
            #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirrs")
            #self.click()
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
            if not self.find( "abrircadastros_abacadastro", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro")
            self.click()
            if not self.find( "itensdeestoque", matching=0.97, waiting_time=10000):
                self.not_found("itensdeestoque")
            self.click()
            if not self.find( "agrupamentoie", matching=0.97, waiting_time=10000):
                self.not_found("agrupamentoie")
            self.click()
            if not self.find( "cadeiadeprecosIE", matching=0.97, waiting_time=10000):
                self.not_found("cadeiadeprecosIE")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "preçovenda1", matching=0.97, waiting_time=10000):
                self.not_found("preçovenda1")
            self.click_relative(11, 33)
            if not self.find( "preçovenda1", matching=0.97, waiting_time=10000):
                self.not_found("preçovenda1")
            self.click_relative(11, 33)
            if not self.find( "precosugestao1", matching=0.97, waiting_time=10000):
                self.not_found("precosugestao1")
            self.click_relative(11, 65)
            if not self.find( "precosugestao1", matching=0.97, waiting_time=10000):
                self.not_found("precosugestao1")
            self.click_relative(11, 65)
            if not self.find( "custoprodutoIE", matching=0.97, waiting_time=10000):
                self.not_found("custoprodutoIE")
            self.click_relative(16, 34)
            if not self.find( "custoprodutoIE", matching=0.97, waiting_time=10000):
                self.not_found("custoprodutoIE")
            self.click_relative(16, 34)
            if not self.find( "custodiretoIE", matching=0.97, waiting_time=10000):
                self.not_found("custodiretoIE")
            self.click_relative(15, 63)
            if not self.find( "custodiretoIE", matching=0.97, waiting_time=10000):
                self.not_found("custodiretoIE")
            self.click_relative(15, 63)
            if not self.find( "custosimplesIE", matching=0.97, waiting_time=10000):
                self.not_found("custosimplesIE")
            self.click_relative(174, 34)
            if not self.find( "custosimplesIE", matching=0.97, waiting_time=10000):
                self.not_found("custosimplesIE")
            self.click_relative(174, 34)
            if not self.find( "custorealIE", matching=0.97, waiting_time=10000):
                self.not_found("custorealIE")
            self.click_relative(176, 65)
            if not self.find( "custorealIE", matching=0.97, waiting_time=10000):
                self.not_found("custorealIE")
            self.click_relative(176, 65)
            if not self.find( "custousuarioIE", matching=0.97, waiting_time=10000):
                self.not_found("custousuarioIE")
            self.click_relative(355, 33)
            if not self.find( "custousuarioIE", matching=0.97, waiting_time=10000):
                self.not_found("custousuarioIE")
            self.click_relative(355, 33)
            if not self.find( "salvarenquete", matching=0.97, waiting_time=10000):
                self.not_found("salvarenquete")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "achargrupoteste", matching=0.97, waiting_time=10000):
                self.not_found("achargrupoteste")
            self.click_relative(5, 30)
            self.type_keys_with_interval(1,'te12')
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "redesocialteste", matching=0.97, waiting_time=10000):
                self.not_found("redesocialteste")
            self.click()           
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                self.not_found("excluirrs")
            self.click()
            #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirrs")
            #self.click()
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
            if not self.find( "abrircadastros_abacadastro", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro")
            self.click()
            if not self.find( "itensdeestoque", matching=0.97, waiting_time=10000):
                self.not_found("itensdeestoque")
            self.click()
            if not self.find( "agrupamentoie", matching=0.97, waiting_time=10000):
                self.not_found("agrupamentoie")
            self.click()
            if not self.find( "tabeladeprecosIE", matching=0.97, waiting_time=10000):
                self.not_found("tabeladeprecosIE")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            if not self.find( "cancelareditarIE", matching=0.97, waiting_time=10000):
                self.not_found("cancelareditarIE")
            self.click()
            #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirrs")
            #self.click()
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.enter()
            self.type_keys_with_interval(1,'123')
            self.enter()
            x=0
            while x<8:
                if not self.find( "valorbaseIE", matching=0.97, waiting_time=10000):
                    self.not_found("valorbaseIE")
                self.click_relative(157, 26)
                self.type_down()
                self.enter()
                x=x+1
            if not self.find( "atualizaprecoIE1", matching=0.97, waiting_time=10000):
                self.not_found("atualizaprecoIE1")
            self.click_relative(103, 30)
            if not self.find( "atualizaprecoIE2", matching=0.97, waiting_time=10000):
                self.not_found("atualizaprecoIE2")
            self.click_relative(7, 30)
            if not self.find( "salvarenquete", matching=0.97, waiting_time=10000):
                self.not_found("salvarenquete")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "achargrupoteste", matching=0.97, waiting_time=10000):
                self.not_found("achargrupoteste")
            self.click_relative(5, 30)
            self.type_keys_with_interval(1,'te12')
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "redesocialteste", matching=0.97, waiting_time=10000):
                self.not_found("redesocialteste")
            self.click()           
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                self.not_found("excluirrs")
            self.click()
            #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirrs")
            #self.click()
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
                
            if not self.find( "abrircadastros_abacadastro", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro")
            self.click()
            if not self.find( "itensdeestoque", matching=0.97, waiting_time=10000):
                self.not_found("itensdeestoque")
            self.click()
            if not self.find( "agrupamentoie", matching=0.97, waiting_time=10000):
                self.not_found("agrupamentoie")
            self.click()
            if not self.find( "tiposIE", matching=0.97, waiting_time=10000):
                self.not_found("tiposIE")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "salvarenquete", matching=0.97, waiting_time=10000):
                self.not_found("salvarenquete")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "achargrupoteste", matching=0.97, waiting_time=10000):
                self.not_found("achargrupoteste")
            self.click_relative(5, 30)
            self.type_keys_with_interval(1,'te12')
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "redesocialteste", matching=0.97, waiting_time=10000):
                self.not_found("redesocialteste")
            self.click()           
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                self.not_found("excluirrs")
            self.click()
            #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirrs")
            #self.click()
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
            if not self.find( "abrircadastros_abacadastro", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro")
            self.click()
            if not self.find( "itensdeestoque", matching=0.97, waiting_time=10000):
                self.not_found("itensdeestoque")
            self.click()
            if not self.find( "agrupamentoie", matching=0.97, waiting_time=10000):
                self.not_found("agrupamentoie")
            self.click()
            if not self.find( "subtiposIE", matching=0.97, waiting_time=10000):
                self.not_found("subtiposIE")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "salvarenquete", matching=0.97, waiting_time=10000):
                self.not_found("salvarenquete")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "achargrupoteste", matching=0.97, waiting_time=10000):
                self.not_found("achargrupoteste")
            self.click_relative(5, 30)
            self.type_keys_with_interval(1,'te12')
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "redesocialteste", matching=0.97, waiting_time=10000):
                self.not_found("redesocialteste")
            self.click()           
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                self.not_found("excluirrs")
            self.click()
            #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirrs")
            #self.click()
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
            if not self.find( "abrircadastros_abacadastro", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro")
            self.click()
            if not self.find( "itensdeestoque", matching=0.97, waiting_time=10000):
                self.not_found("itensdeestoque")
            self.click()
            if not self.find( "agrupamentoie", matching=0.97, waiting_time=10000):
                self.not_found("agrupamentoie")
            self.click()
            if not self.find( "controlesIE", matching=0.97, waiting_time=10000):
                self.not_found("controlesIE")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "salvarenquete", matching=0.97, waiting_time=10000):
                self.not_found("salvarenquete")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "achargrupoteste", matching=0.97, waiting_time=10000):
                self.not_found("achargrupoteste")
            self.click_relative(5, 30)
            self.type_keys_with_interval(1,'te12')
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "redesocialteste", matching=0.97, waiting_time=10000):
                self.not_found("redesocialteste")
            self.click()           
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                self.not_found("excluirrs")
            self.click()
            #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirrs")
            #self.click()
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
            if not self.find( "abrircadastros_abacadastro", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro")
            self.click()
            if not self.find( "itensdeestoque", matching=0.97, waiting_time=10000):
                self.not_found("itensdeestoque")
            self.click()
            if not self.find( "agrupamentoie", matching=0.97, waiting_time=10000):
                self.not_found("agrupamentoie")
            self.click()
            if not self.find( "NCMIE", matching=0.97, waiting_time=10000):
                self.not_found("NCMIE")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            if not self.find( "cancelareditarIE", matching=0.97, waiting_time=10000):
                self.not_found("cancelareditarIE")
            self.click()
            #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirrs")
            #self.click()
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "descricaoIENCM", matching=0.97, waiting_time=10000):
                self.not_found("descricaoIENCM")
            self.click_relative(66, 5)
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "salvarenquete", matching=0.97, waiting_time=10000):
                self.not_found("salvarenquete")
            self.click()
            if not self.find( "addnovoregistroNCMIE", matching=0.97, waiting_time=10000):
                self.not_found("addnovoregistroNCMIE")
            self.click_relative(5, 33)
            if not self.find( "EstadoNCMIE", matching=0.97, waiting_time=10000):
                self.not_found("EstadoNCMIE")
            self.click_relative(47, 28)
            if not self.find( "cod001NCMIE", matching=0.97, waiting_time=10000):
                self.not_found("cod001NCMIE")
            self.click()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.enter()
            self.enter()
            self.type_keys_with_interval(1,'123')
            self.enter()
            self.type_keys_with_interval(1,'123')
            self.enter()
            self.type_keys_with_interval(1,'123')
            self.enter()
            self.type_keys_with_interval(1,'123')
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(1,'123')
            self.enter()
            self.type_keys_with_interval(1,'123')
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "gravarNCMIE", matching=0.97, waiting_time=10000):
                self.not_found("gravarNCMIE")
            self.click()
            if not self.find( "paranaNCMIE", matching=0.97, waiting_time=10000):
                self.not_found("paranaNCMIE")
            self.click()
            if not self.find( "excluirregistroNCMIE", matching=0.97, waiting_time=10000):
                self.not_found("excluirregistroNCMIE")
            self.click_relative(7, 57)
            #if not self.find( "simexcluirNCMIE", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirNCMIE")
            #self.click()
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "achargrupoteste", matching=0.97, waiting_time=10000):
                self.not_found("achargrupoteste")
            self.click_relative(5, 30)
            self.type_keys_with_interval(1,'te12')
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "cadastroncmteste", matching=0.97, waiting_time=10000):
                self.not_found("cadastroncmteste")
            self.click()                      
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                self.not_found("excluirrs")
            self.click()
            #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirrs")
            #self.click()
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
            if not self.find( "abrircadastros_abacadastro", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro")
            self.click()
            if not self.find( "itensdeestoque", matching=0.97, waiting_time=10000):
                self.not_found("itensdeestoque")
            self.click()
            if not self.find( "agrupamentoie", matching=0.97, waiting_time=10000):
                self.not_found("agrupamentoie")
            self.click()
            if not self.find( "enderecodeestoque", matching=0.97, waiting_time=10000):
                self.not_found("enderecodeestoque")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_down()
            if not self.find( "salvarenquete", matching=0.97, waiting_time=10000):
                self.not_found("salvarenquete")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "achargrupoteste", matching=0.97, waiting_time=10000):
                self.not_found("achargrupoteste")
            self.click_relative(5, 30)
            self.type_keys_with_interval(1,'te12')
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "redesocialteste", matching=0.97, waiting_time=10000):
                self.not_found("redesocialteste")
            self.click()           
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                self.not_found("excluirrs")
            self.click()
            #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirrs")
            #self.click()
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---CADASTRO DE ITENS---####
            
                             
            if not self.find( "abrircadastros_abacadastro", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro")
            self.click()
            if not self.find( "itensdeestoque", matching=0.97, waiting_time=10000):
                self.not_found("itensdeestoque")
            self.click()
            if not self.find( "cadastrodeitens", matching=0.97, waiting_time=10000):
                self.not_found("cadastrodeitens")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            self.wait(3000)
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            self.wait(6000)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            self.wait(3000)
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()
            self.type_right()
            self.enter()
            #if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
            #    self.not_found("selecionarmunicipiovcr")
            #self.click()
            #if not self.find( "retornarconsultaitensgambiarra", matching=0.97, waiting_time=10000):
            #    self.not_found("retornarconsultaitensgambiarra")
            #self.click_relative(42, -77)
            self.type_keys_with_interval(1,'te12!@')
            self.tab()
            self.type_keys_with_interval(1,'1231231231')
            self.tab()
            #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirrs")
            #self.click()
            self.enter()
            if not self.find( "cadastroitensreferencia", matching=0.97, waiting_time=10000):
                self.not_found("cadastroitensreferencia")
            self.click_relative(718, 91)
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.enter()
            #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirrs")
            #self.click()
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "referencia2cadastroitens", matching=0.97, waiting_time=10000):
                self.not_found("referencia2cadastroitens")
            self.click_relative(883, 89)
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "subirtelaCI", matching=0.97, waiting_time=10000):
                self.not_found("subirtelaCI")
            self.click()
            x=0
            while x<10:
                if not self.find( "subirtelaCI2", matching=0.97, waiting_time=10000):
                    self.not_found("subirtelaCI2")
                self.double_click()
                x=x+1
            
                            ####---ABA1 P1---####
            
            if not self.find( "Descricaodadosprincipais", matching=0.97, waiting_time=10000):
                self.not_found("Descricaodadosprincipais")
            self.click_relative(11, 46)
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(1,'87487487')
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(1,'t1!')
            self.tab()
            self.tab()
            x=0
            while x<12:
                if not self.find( "tipodoitemsped1", matching=0.97, waiting_time=10000):
                    self.not_found("tipodoitemsped1")
                self.click_relative(223, 27)
                self.type_down()
                self.enter()
                x=x+1
            
            self.type_down()    
            self.type_up()
            self.enter()
                   
            x=0
            while x<250:
                self.type_down()
                x=x+1
            
                           ####---A1P1 PRECOS E CUSTOS---####
                            
            if not self.find( "custounitario", matching=0.97, waiting_time=10000):
                self.not_found("custounitario")
            self.click_relative(77, 45)
            self.type_keys_with_interval(1,'123')
            self.enter()
            self.type_keys_with_interval(1,'123')
            self.enter()
            self.type_keys_with_interval(1,'123')
            self.enter()
            self.type_keys_with_interval(1,'123')
            self.enter()
            self.type_keys_with_interval(1,'123')
            self.enter()
            self.type_keys_with_interval(1,'123')
            self.enter()
            self.type_keys_with_interval(1,'123')
            self.enter()
            self.type_keys_with_interval(1,'123')
            self.enter()
            self.type_keys_with_interval(1,'123')
            self.enter()
            self.type_keys_with_interval(1,'123')
            self.enter()
            self.enter()
            if not self.find( "operacaocalculoprecoci", matching=0.97, waiting_time=10000):
                self.not_found("operacaocalculoprecoci")
            self.click_relative(55, 23)
            
            
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            if not self.find( "regiaocalculoprecoci", matching=0.97, waiting_time=10000):
                self.not_found("regiaocalculoprecoci")
            self.click_relative(52, 25)
            self.wait(500)
            if not self.find( "cod001ci", matching=0.97, waiting_time=10000):
                self.not_found("cod001ci")
            self.click()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            if not self.find( "grupofiscalcalculodeprecoci", matching=0.97, waiting_time=10000):
                self.not_found("grupofiscalcalculodeprecoci")
            self.click_relative(668, 199)           
            if not self.find( "cod001ci", matching=0.97, waiting_time=10000):
                self.not_found("cod001ci")
            self.click()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            self.tab()
            self.enter()
            if not self.find( "tabelaprecooperacaoci", matching=0.97, waiting_time=10000):
                self.not_found("tabelaprecooperacaoci")
            self.click_relative(340, 25)
            self.enter()
            if not self.find( "regiaotabelaprecocadastroitens", matching=0.97, waiting_time=10000):
                self.not_found("regiaotabelaprecocadastroitens")
            self.click_relative(268, 27)
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.enter()
            self.type_keys_with_interval(1,'123')
            self.enter()
            self.type_keys_with_interval(1,'123')
            
                            ####---A1P1 AGRUPAMENTO---#### 
            
            if not self.find( "familiaCI", matching=0.97, waiting_time=10000):
                self.not_found("familiaCI")
            self.click_relative(49, 43)
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "marcaCI", matching=0.97, waiting_time=10000):
                self.not_found("marcaCI")
            self.click_relative(51, 85)
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "controleCI", matching=0.97, waiting_time=10000):
                self.not_found("controleCI")
            self.click_relative(49, 128)
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "unidadetributariaCI", matching=0.97, waiting_time=10000):
                self.not_found("unidadetributariaCI")
            self.click_relative(50, 163)
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "codcaixa", matching=0.97, waiting_time=10000):
                self.not_found("codcaixa")
            self.click()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "centrocustosCI", matching=0.97, waiting_time=10000):
                self.not_found("centrocustosCI")
            self.click_relative(85, 204)
            self.backspace()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            if not self.find( "grupoCI", matching=0.97, waiting_time=10000):
                self.not_found("grupoCI")
            self.click_relative(452, 44)
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(1000)
            if not self.find( "tipoCI", matching=0.97, waiting_time=10000):
                self.not_found("tipoCI")
            self.click_relative(451, 83)
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "unidadeestoqueCI", matching=0.97, waiting_time=10000):
                self.not_found("unidadeestoqueCI")
            self.click_relative(448, 125)
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "codcaixa", matching=0.97, waiting_time=10000):
                self.not_found("codcaixa")
            self.click()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "cadeiaprecoCI", matching=0.97, waiting_time=10000):
                self.not_found("cadeiaprecoCI")
            self.click_relative(451, 165)
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "cod00001testeparadouble", matching=0.97, waiting_time=10000):
                self.not_found("cod00001testeparadouble")
            self.click()           
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            if not self.find( "picontas97CI", matching=0.97, waiting_time=10000):
                self.not_found("picontas97CI")
            self.click_relative(452, 206)
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "cod110103001planocontas", matching=0.97, waiting_time=10000):
                self.not_found("cod110103001planocontas")
            self.click()           
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "subgrupoci", matching=0.97, waiting_time=10000):
                self.not_found("subgrupoci")
            self.click_relative(851, 43)
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "subtipoci", matching=0.97, waiting_time=10000):
                self.not_found("subtipoci")
            self.click_relative(850, 84)
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "unidadeetiquetaCI", matching=0.97, waiting_time=10000):
                self.not_found("unidadeetiquetaCI")
            self.click_relative(850, 124)
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "codcaixa", matching=0.97, waiting_time=10000):
                self.not_found("codcaixa")
            self.click()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "grupofiscalCI", matching=0.97, waiting_time=10000):
                self.not_found("grupofiscalCI")
            self.click_relative(850, 167)
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "picontas80CI", matching=0.97, waiting_time=10000):
                self.not_found("picontas80CI")
            self.click_relative(851, 204)
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "cod110103001planocontas", matching=0.97, waiting_time=10000):
                self.not_found("cod110103001planocontas")
            self.click()           
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.tab()
            self.tab()
            if not self.find( "moldesCI", matching=0.97, waiting_time=10000):
                self.not_found("moldesCI")
            self.click_relative(50, 246)
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "ncmCI", matching=0.97, waiting_time=10000):
                self.not_found("ncmCI")
            self.click_relative(503, 241)
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            self.type_down()
            self.type_down()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.tab()
            self.type_keys_with_interval(1,'t1')
            self.backspace()
            self.type_keys_with_interval(1,'!')
            self.tab()
            self.type_keys_with_interval(1,'te12!@')
            self.tab()
            
                            ####---A1P1 MARCADORES---####
            
            if not self.find( "materiaprimaci", matching=0.97, waiting_time=10000):
                self.not_found("materiaprimaci")
            self.click_relative(14, 27)
            self.space()
            self.tab()
            self.space()
            self.space()
            x=0
            while x<14:
                self.tab()
                self.space()
                self.space()
                x=x+1
            self.tab()
            self.type_keys_with_interval(1,'87487487487487')
            self.tab()
            x=0
            while x<3:
                self.type_down()
                x=x+1    
            
                            ####---ABA1 P2---####
                             
            if not self.find( "aba1p2CI", matching=0.97, waiting_time=10000):
                self.not_found("aba1p2CI")
            self.click()
            x=0
            while x<7:
                self.type_down()
                x=x+1
            x=0
            while x<7:
                self.type_up()
                x=x+1
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.backspace()
            self.backspace()
            self.backspace()
            self.type_keys_with_interval(1,'0')            
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.backspace()
            self.backspace()
            self.backspace()
            self.type_keys_with_interval(1,'0')
            self.tab()
            x=0
            while x<5:
                self.type_down()
                x=x+1
            x=0
            while x<2:
                self.type_up()
                x=x+1
            self.tab()
            self.type_down()
            self.type_up()
            self.type_up()
            self.backspace()
            self.type_keys_with_interval(1,'0')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'te12!@')
            self.tab()
            self.type_keys_with_interval(1,'t1!')
            self.tab()
            self.tab()
            x=0
            while x<8:
                self.type_down()
                x=x+1
            x=0
            while x<4:
                self.tab()
                self.type_keys_with_interval(1,'te12!@')
                x=x+1

                            ####---ABA1 P3---####
                             
            if not self.find( "a1p3CI", matching=0.97, waiting_time=10000):
                self.not_found("a1p3CI")
            self.click()
            if not self.find( "a1p3.2CI", matching=0.97, waiting_time=10000):
                self.not_found("a1p3.2CI")
            self.click()
            if not self.find( "a1p3.3CI", matching=0.97, waiting_time=10000):
                self.not_found("a1p3.3CI")
            self.click()
            if not self.find( "a1p4CI", matching=0.97, waiting_time=10000):
                self.not_found("a1p4CI")
            self.click()
            if not self.find( "possuiloteCI", matching=0.97, waiting_time=10000):
                self.not_found("possuiloteCI")
            self.click_relative(29, 73)
            self.tab()
            x=0
            while x<6:
                self.type_down()
                x=x+1
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            x=0
            while x<3:
                self.type_down()
                x=x+1
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            if not self.find( "a1p4.2CI", matching=0.97, waiting_time=10000):
                self.not_found("a1p4.2CI")
            self.click()
            if not self.find( "a1p4.1CInovo", matching=0.97, waiting_time=10000):
                self.not_found("a1p4.1CInovo")
            self.click()
            if not self.find( "a1p4.1CInovo", matching=0.97, waiting_time=10000):
                self.not_found("a1p4.1CInovo")
            self.click_relative(29, 73)
            
            
            
            
            
                            ####---A1 P5---####
                             
            if not self.find( "a1p5CI", matching=0.97, waiting_time=10000):
                self.not_found("a1p5CI")
            self.click()
            if not self.find( "embalagemCI", matching=0.97, waiting_time=10000):
                self.not_found("embalagemCI")
            self.click_relative(8, 45)
            self.type_keys_with_interval(1,'te12!@')
            self.tab()
            self.type_keys_with_interval(1,'te12!@')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'12')
            self.tab()
            self.type_keys_with_interval(1,'12')
            self.tab()
            self.type_keys_with_interval(1,'te12!@')
            self.tab()
            self.type_keys_with_interval(1,'te12!@')
            self.tab()
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            x=0
            while x<10:
                self.type_keys_with_interval(1,'123')
                self.tab()
                x=x+1
            x=0
            while x<5:
                self.type_down()
                x=x+1
            self.tab()
            self.space()
            self.space()
            self.tab()
            self.type_keys_with_interval(1,'12')
            self.tab()
            x=0
            while x<6:
                self.type_keys_with_interval(1,'te12!@')    
                self.tab()
                x=x+1
            self.space()
            self.space()
            self.space()
            self.wait(500)
            self.tab()
            self.space()
            self.space()
            self.space() 
            self.tab()
            x=0
            while x<7:
                self.type_keys_with_interval(1,'t1!')
                self.tab()
                x=x+1
            self.space()
            self.space()
            self.tab()
            self.type_keys_with_interval(1,'te12!@')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'te12!@')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'te12!@')
            self.tab()
            self.type_down()
            self.type_up()
            self.type_up()
            if not self.find( "outrasinegracoes1ci", matching=0.97, waiting_time=10000):
                self.not_found("outrasinegracoes1ci")
            self.click_relative(14, 44)
            if not self.find( "outrasintegracoes2ci", matching=0.97, waiting_time=10000):
                self.not_found("outrasintegracoes2ci")
            self.click_relative(147, 45)
            
                            ####---ABA 2---####
                                          
            if not self.find( "aba2CI", matching=0.97, waiting_time=10000):
                self.not_found("aba2CI")
            self.click()
            if not self.find( "salvarenquete", matching=0.97, waiting_time=10000):
                self.not_found("salvarenquete")
            self.click()
            self.enter()
            if not self.find( "salvaraba2CI", matching=0.97, waiting_time=10000):
                self.not_found("salvaraba2CI")
            self.click_relative(-68, 34)
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            if not self.find( "commit_registro_a2p2_CI", matching=0.97, waiting_time=10000):
                self.not_found("commit_registro_a2p2_CI")
            self.click_relative(16, 184)
            
            if not self.find( "excluir_a2p1_CI", matching=0.97, waiting_time=10000):
                self.not_found("excluir_a2p1_CI")
            self.click_relative(15, 162)
            
            self.enter()
            
            
            
                            ####---ABA2 P2---####
                             
            if not self.find( "aba2p2CI", matching=0.97, waiting_time=10000):
                self.not_found("aba2p2CI")
            self.click()
            if not self.find( "salvaraba2CI", matching=0.97, waiting_time=10000):
                self.not_found("salvaraba2CI")
            self.click_relative(-68, 34)
            if not self.find( "procuraritensCI", matching=0.97, waiting_time=10000):
                self.not_found("procuraritensCI")
            self.click_relative(10, 34)
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            self.wait(4000)
            self.type_keys_with_interval(1,'agulha gengival')
            self.enter()
            self.type_down()
            self.type_down()
            self.type_down()
            self.type_down()
            self.wait(500)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            #if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
            #    self.not_found("selecionarmunicipiovcr")
            #self.click()
            #self.wait(500)
            #if not self.find( "quantidade_lancitens", matching=0.97, waiting_time=10000):
            #    self.not_found("quantidade_lancitens")
            #self.click_relative(336, 280)
            #self.backspace()
            #self.enter()
            #x=0
            #while x<31:
            #    self.type_down()
            #    x=x+1
            #if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
            #    self.not_found("selecionarmunicipiovcr")
            #self.click()
            self.wait(500)
            self.type_keys_with_interval(1,'1')
            if not self.find( "botaoconfirmaritensreqcompras", matching=0.97, waiting_time=10000):
                self.not_found("botaoconfirmaritensreqcompras")
            self.click()
            self.wait(3000)
            
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "excluirregistroa2p2.1_CI", matching=0.97, waiting_time=10000):
                self.not_found("excluirregistroa2p2.1_CI")
            self.click_relative(17, 163)           
            #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirrs")
            #self.click()
            self.enter()
            if not self.find( "aba2p2.2CI", matching=0.97, waiting_time=10000):
                self.not_found("aba2p2.2CI")
            self.click()
            
                            ####---ABA2 P3---####
             
            if not self.find( "aba2p3CI", matching=0.97, waiting_time=10000):
                 self.not_found("aba2p3CI")
            self.click()
            if not self.find( "salvaraba2CI", matching=0.97, waiting_time=10000):
                self.not_found("salvaraba2CI")
            self.click_relative(-68, 34)
            if not self.find( "procuraritensCI", matching=0.97, waiting_time=10000):
                self.not_found("procuraritensCI")
            self.click_relative(10, 34)
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            self.wait(4000)
            self.type_keys_with_interval(1,'agulha gengival')
            self.enter()
            self.type_down()
            self.type_down()
            self.type_down()
            self.type_down()
            self.wait(500)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            #if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
            #    self.not_found("selecionarmunicipiovcr")
            #self.click()
            #self.wait(500)
            #if not self.find( "quantidade_lancitens", matching=0.97, waiting_time=10000):
            #    self.not_found("quantidade_lancitens")
            #self.click_relative(336, 280)
            #self.backspace()
            #self.enter()
            #x=0
            #while x<31:
            #    self.type_down()
            #    x=x+1
            #if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
            #    self.not_found("selecionarmunicipiovcr")
            #self.click()
            self.wait(500)
            self.type_keys_with_interval(1,'1')
            if not self.find( "botaoconfirmaritensreqcompras", matching=0.97, waiting_time=10000):
                self.not_found("botaoconfirmaritensreqcompras")
            self.click()
            self.wait(3000)
            
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "excluirregistroa2p2.1_CI", matching=0.97, waiting_time=10000):
                self.not_found("excluirregistroa2p2.1_CI")
            self.click_relative(17, 163)
            self.enter()
            
                            ####---ABA2 P4---####                             
                                          
            if not self.find( "aba2p4CI", matching=0.97, waiting_time=10000):
                self.not_found("aba2p4CI")
            self.click()
            if not self.find( "salvaraba2CI", matching=0.97, waiting_time=10000):
                self.not_found("salvaraba2CI")
            self.click_relative(-68, 34)
            if not self.find( "procuraritensCI", matching=0.97, waiting_time=10000):
                self.not_found("procuraritensCI")
            self.click_relative(10, 34)
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            self.wait(4000)
            self.type_keys_with_interval(1,'agulha gengival')
            self.enter()
            self.type_down()
            self.type_down()
            self.type_down()
            self.type_down()
            self.wait(500)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            #if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
            #    self.not_found("selecionarmunicipiovcr")
            #self.click()
            #self.wait(500)
            #if not self.find( "quantidade_lancitens", matching=0.97, waiting_time=10000):
            #    self.not_found("quantidade_lancitens")
            #self.click_relative(336, 280)
            #self.backspace()
            #self.enter()
            #x=0
            #while x<31:
            #    self.type_down()
            #    x=x+1
            #if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
            #    self.not_found("selecionarmunicipiovcr")
            #self.click()
            self.wait(500)
            self.type_keys_with_interval(1,'1')
            if not self.find( "botaoconfirmaritensreqcompras", matching=0.97, waiting_time=10000):
                self.not_found("botaoconfirmaritensreqcompras")
            self.click()
            self.wait(3000)
            
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "excluirregistroa2p4_CI", matching=0.97, waiting_time=10000):
                self.not_found("excluirregistroa2p4_CI")
            self.click_relative(16, 187)
                       
            #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirrs")
            #self.click()
            self.enter()
            if not self.find( "aba2p4.2CI", matching=0.97, waiting_time=10000):
                self.not_found("aba2p4.2CI")
            self.click()
            if not self.find( "salvaraba2CI", matching=0.97, waiting_time=10000):
                self.not_found("salvaraba2CI")
            self.click_relative(-68, 34) 
            if not self.find( "buscarservicoa2p4.2CI", matching=0.97, waiting_time=10000):
                self.not_found("buscarservicoa2p4.2CI")
            self.click_relative(16, 99)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.tab()
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.space()
            self.space()
            if not self.find( "cancelara2p4.2CI", matching=0.97, waiting_time=10000):
                self.not_found("cancelara2p4.2CI")
            self.click()           
            #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirrs")
            #self.click()
            self.enter()
            
            if not self.find( "a2p4.3CI", matching=0.97, waiting_time=10000):
                self.not_found("a2p4.3CI")
            self.click()
            if not self.find( "salvaraba2CI", matching=0.97, waiting_time=10000):
                self.not_found("salvaraba2CI")
            self.click_relative(-68, 34) 
            if not self.find( "buscarservicoa2p4.2CI", matching=0.97, waiting_time=10000):
                self.not_found("buscarservicoa2p4.2CI")
            self.click_relative(16, 99)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.tab()
            self.tab()
            if not self.find( "cancelara2p4.3CI", matching=0.97, waiting_time=10000):
                self.not_found("cancelara2p4.3CI")
            self.click()
            #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirrs")
            #self.click()
            self.enter()

                            ####---ABA2 P5---####
                             
            if not self.find( "a2p5CI", matching=0.97, waiting_time=10000):
                self.not_found("a2p5CI")
            self.click()
            if not self.find( "salvaraba2CI", matching=0.97, waiting_time=10000):
                self.not_found("salvaraba2CI")
            self.click_relative(-68, 34)
            if not self.find( "fornecedorclientea2p5CI", matching=0.97, waiting_time=10000):
                self.not_found("fornecedorclientea2p5CI")
            self.click_relative(16, 77)
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.tab()
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'te12!@')           
            if not self.find( "unidadea2p5CI", matching=0.97, waiting_time=10000):
                self.not_found("unidadea2p5CI")
            self.click_relative(17, 120)
            self.tab()
            self.wait(200)
            self.tab()
            self.wait(200)
            self.tab()
            self.wait(200)
            self.type_down()                 
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.tab()
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'t1!')
            self.tab()
            self.type_keys_with_interval(1,'123')
            if not self.find( "salvarregistro_a2p5_CI", matching=0.97, waiting_time=10000):
                self.not_found("salvarregistro_a2p5_CI")
            self.click_relative(16, 183)
            if not self.find( "cancelarregistro_a2p5_CI", matching=0.97, waiting_time=10000):
                self.not_found("cancelarregistro_a2p5_CI")
            self.click_relative(16, 206)
            self.enter() 
            if not self.find( "excluirregistro_a2p5_CI", matching=0.97, waiting_time=10000):
                self.not_found("excluirregistro_a2p5_CI")
            self.click_relative(15, 164)
            
            #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirrs")
            #self.click()
            self.enter()
                
                            ####---ABA2 P6---####
                                 
            if not self.find( "aba2p6CI", matching=0.97, waiting_time=10000):
                self.not_found("aba2p6CI")
            self.click()
            if not self.find( "salvaraba2CI", matching=0.97, waiting_time=10000):
                self.not_found("salvaraba2CI")
            self.click_relative(-68, 34)
            if not self.find( "a2p6.1addregis", matching=0.97, waiting_time=10000):
                self.not_found("a2p6.1addregis")
            self.click_relative(12, 102)
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.tab()
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.enter()
            if not self.find( "a2p6.2CI", matching=0.97, waiting_time=10000):
                self.not_found("a2p6.2CI")
            self.click()
            if not self.find( "salvaraba2CI", matching=0.97, waiting_time=10000):
                self.not_found("salvaraba2CI")
            self.click_relative(-68, 34)
            if not self.find( "addregistroa2p6.2CI", matching=0.97, waiting_time=10000):
                self.not_found("addregistroa2p6.2CI")
            self.click_relative(10, 101)
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            if not self.find( "voltarparacodigoa2p6.2ci", matching=0.97, waiting_time=10000):
                self.not_found("voltarparacodigoa2p6.2ci")
            self.click_relative(-63, 53)          
            self.tab()
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.enter()
            if not self.find( "excluirregistroa2p2.1_CI", matching=0.97, waiting_time=10000):
                self.not_found("excluirregistroa2p2.1_CI")
            self.click_relative(17, 163)
            #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirrs")
            #self.click()
            self.enter()
            
                            ####---ABA2 P7---####
                             
            if not self.find( "a2p7CI", matching=0.97, waiting_time=10000):
                self.not_found("a2p7CI")
            self.click()
            if not self.find( "salvaraba2CI", matching=0.97, waiting_time=10000):
                self.not_found("salvaraba2CI")
            self.click_relative(-68, 34)
            if not self.find( "unidadeadicionala2p7ci", matching=0.97, waiting_time=10000):
                self.not_found("unidadeadicionala2p7ci")
            self.click_relative(314, 123)
            if not self.find( "codcxunidadea2p7ci", matching=0.97, waiting_time=10000):
                self.not_found("codcxunidadea2p7ci")
            self.click()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.tab()
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.space()
            self.space()
            self.tab()
            self.tab()
            self.enter()
            if not self.find( "excluirregistroa2p2.1_CI", matching=0.97, waiting_time=10000):
                self.not_found("excluirregistroa2p2.1_CI")
            self.click_relative(17, 163)
            #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirrs")
            #self.click()
            self.enter()

                            ####---ABA2 P8---####
                             
            if not self.find( "a2p8CI", matching=0.97, waiting_time=10000):
                self.not_found("a2p8CI")
            self.click()
            if not self.find( "salvaraba2CI", matching=0.97, waiting_time=10000):
                self.not_found("salvaraba2CI")
            self.click_relative(-68, 34)
            self.type_keys_with_interval(1,'te12!@')
            x=0
            while x<6:
                self.backspace()
                x=x+1
            self.tab()
            self.space()
            self.space()
            self.tab()
            self.type_keys_with_interval(1,'te12!@')
            self.tab()
            self.enter() 
            if not self.find( "excluir_foto_a2p8_CI", matching=0.97, waiting_time=10000):
                self.not_found("excluir_foto_a2p8_CI")
            self.click_relative(16, 184)
            
            
            self.enter()
            
                            ####---ABA2 P9---#####
                             
            if not self.find( "aba2p10CI", matching=0.97, waiting_time=10000):
                self.not_found("aba2p10CI")
            self.click()
            if not self.find( "salvaraba2CI", matching=0.97, waiting_time=10000):
                self.not_found("salvaraba2CI")
            self.click_relative(-68, 34)
            self.type_keys_with_interval(1,'12312312312312')
            self.tab()
            #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirrs")
            #self.click() 
            self.enter()
            self.tab()
            self.type_keys_with_interval(1,'te12!@')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.enter()
            if not self.find( "excluirregistroa2p2.1_CI", matching=0.97, waiting_time=10000):
                self.not_found("excluirregistroa2p2.1_CI")
            self.click_relative(17, 163)
            #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirrs")
            #self.click()
            self.enter()

                            ####---ABA2 P10---####
                             
            if not self.find( "aba2p10CIcontagemcerta", matching=0.97, waiting_time=10000):
                self.not_found("aba2p10CIcontagemcerta")
            self.click()
            if not self.find( "salvaraba2CI", matching=0.97, waiting_time=10000):
                self.not_found("salvaraba2CI")
            self.click_relative(-68, 34)
            if not self.find( "addenderecoa2p10ci", matching=0.97, waiting_time=10000):
                self.not_found("addenderecoa2p10ci")
            self.click_relative(5, 75)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.tab()
            self.tab()
            self.enter()             
            
                            ####---ABA2 P11---####
                             
            if not self.find( "a2p11CI", matching=0.97, waiting_time=10000):
                self.not_found("a2p11CI")
            self.click()
            if not self.find( "salvaraba2CI", matching=0.97, waiting_time=10000):
                self.not_found("salvaraba2CI")
            self.click_relative(-68, 34)           
            if not self.find( "addenderecoa2p10ci", matching=0.97, waiting_time=10000):
                self.not_found("addenderecoa2p10ci")
            self.click_relative(15, 75)
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            x=0
            while x<18:
                self.type_down()
                x=x+1
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.tab()
            self.tab()
            self.type_keys_with_interval(1,'te12!@')
            self.tab()
            self.enter()
            if not self.find( "excluirregistroa2p2.1_CI", matching=0.97, waiting_time=10000):
                self.not_found("excluirregistroa2p2.1_CI")
            self.click_relative(17, 163)
            #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirrs")
            #self.click()
            self.enter()

                            ####---ABA2 P12---####
                             
            if not self.find( "a2p12CI", matching=0.97, waiting_time=10000):
                self.not_found("a2p12CI")
            self.click()
            if not self.find( "salvaraba2CI", matching=0.97, waiting_time=10000):
                self.not_found("salvaraba2CI")
            self.click_relative(-68, 34)
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.enter()
            if not self.find( "excluirregistroa2p2.1_CI", matching=0.97, waiting_time=10000):
                self.not_found("excluirregistroa2p2.1_CI")
            self.click_relative(17, 163)
            #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirrs")
            #self.click()
            self.enter()

                            ####---A2 P13---####
                             
            if not self.find( "a2p13ci", matching=0.97, waiting_time=10000):
                self.not_found("a2p13ci")
            self.click()
            if not self.find( "salvaraba2CI", matching=0.97, waiting_time=10000):
                self.not_found("salvaraba2CI")
            self.click_relative(-68, 34)
            self.wait(1500)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            self.wait(1500)
                                              
                                                                                       
                            ####---ABA 3---####
            
            if not self.find( "aba3CI", matching=0.97, waiting_time=10000):
                self.not_found("aba3CI")
            self.click()
            if not self.find( "documentoaba3CI", matching=0.97, waiting_time=10000):
                self.not_found("documentoaba3CI")
            self.click_relative(-167, 56)
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            if not self.find( "periodoaba3ci", matching=0.97, waiting_time=10000):
                self.not_found("periodoaba3ci")
            self.click_relative(31, 11)
            if not self.find( "carregaranoaba3", matching=0.97, waiting_time=10000):
                self.not_found("carregaranoaba3")
            self.click()
            if not self.find( "anoatualaba3CI", matching=0.97, waiting_time=10000):
                self.not_found("anoatualaba3CI")
            self.click()
            self.tab()
            x=0
            while x<11:
                self.type_down()
                x=x+1
            if not self.find( "localestoqueba3CI", matching=0.97, waiting_time=10000):
                self.not_found("localestoqueba3CI")
            self.click_relative(450, 54)
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            self.tab()
            self.tab()
            self.space()
            self.space()
            self.tab()
            self.space()
            self.space()
            self.tab()
            self.space()
            self.space()
            self.tab()
            self.space()
            self.space()
            
                            ####---FINALIZACAO---####
            
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarcodte12!@CI", matching=0.97, waiting_time=10000):
                self.not_found("localizarcodte12!@CI")
            self.click_relative(4, 33)
            self.type_keys_with_interval(1,'te12')
            self.enter()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                self.not_found("excluirrs")
            self.click()
            #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirrs")
            #self.click()
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
            
            
                            ####---FORMULAS---####
                             
            if not self.find( "abrircadastros_abacadastro", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro")
            self.click()
            if not self.find( "itensdeestoque", matching=0.97, waiting_time=10000):
                self.not_found("itensdeestoque")
            self.click()
            if not self.find( "formulas", matching=0.97, waiting_time=10000):
                self.not_found("formulas")
            self.click()
            if not self.find( "buscarempresaformulas", matching=0.97, waiting_time=10000):
                self.not_found("buscarempresaformulas")
            self.click_relative(178, 38)           
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.tab()
            self.tab()
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "salvarenquete", matching=0.97, waiting_time=10000):
                self.not_found("salvarenquete")
            self.click()
            if not self.find( "deixarpadrão", matching=0.97, waiting_time=10000):
                self.not_found("deixarpadrão")
            self.click()
            self.click()
            if not self.find( "cancelarformula", matching=0.97, waiting_time=10000):
                self.not_found("cancelarformula")
            self.click()           
            if not self.find( "simabandonar", matching=0.97, waiting_time=10000):
                self.not_found("simabandonar")
            self.click()
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()
            #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirrs")
            #self.click()
            self.enter()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            if not self.find( "salvarenquete", matching=0.97, waiting_time=10000):
                self.not_found("salvarenquete")
            self.click()
            if not self.find( "okformulas", matching=0.97, waiting_time=10000):
                self.not_found("okformulas")
            self.click()
            if not self.find( "cancelarformula", matching=0.97, waiting_time=10000):
                self.not_found("cancelarformula")
            self.click()    
            if not self.find( "simabandonar", matching=0.97, waiting_time=10000):
                self.not_found("simabandonar")
            self.click()
            if not self.find( "consultaform", matching=0.97, waiting_time=10000):
                self.not_found("consultaform")
            self.click()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---LOCAL DE ESTOQUE---####
                             
            if not self.find( "abrircadastros_abacadastro", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro")
            self.click()
            if not self.find( "itensdeestoque", matching=0.97, waiting_time=10000):
                self.not_found("itensdeestoque")
            self.click()
            if not self.find( "localdeestoque", matching=0.97, waiting_time=10000):
                self.not_found("localdeestoque")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()
            self.type_keys_with_interval(1,'te12!@')
            self.tab()
            self.type_down()
            if not self.find( "salvarenquete", matching=0.97, waiting_time=10000):
                self.not_found("salvarenquete")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            x=0
            while x<7:
                if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                    self.not_found("localizarpaises")
                self.click()
                if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                    self.not_found("editarfim")
                self.click()
                self.tab()
                self.type_down()
                if not self.find( "salvarenquete", matching=0.97, waiting_time=10000):
                    self.not_found("salvarenquete")
                self.click()
                if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                    self.not_found("retornarpe")
                self.click()
                x=x+1
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                self.not_found("excluirrs")
            self.click()
            #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirrs")
            #self.click()
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---DESCONTO POR AGRUPAMENTO---####
                             
            if not self.find( "abrircadastros_abacadastro", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro")
            self.click()
            if not self.find( "itensdeestoque", matching=0.97, waiting_time=10000):
                self.not_found("itensdeestoque")
            self.click()
            if not self.find( "descontoporagrupamento", matching=0.97, waiting_time=10000):
                self.not_found("descontoporagrupamento")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "okformulas", matching=0.97, waiting_time=10000):
                self.not_found("okformulas")
            self.click()
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()
            if not self.find( "okformulas", matching=0.97, waiting_time=10000):
                self.not_found("okformulas")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---TIPO DO ITEM/CONTA CONTABIL---####
                             
            if not self.find( "abrircadastros_abacadastro", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro")
            self.click()
            if not self.find( "itensdeestoque", matching=0.97, waiting_time=10000):
                self.not_found("itensdeestoque")
            self.click()
            if not self.find( "tipodoitemcontacontabil", matching=0.97, waiting_time=10000):
                self.not_found("tipodoitemcontacontabil")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()
            x=0
            while x<12:
                self.type_down()
                x=x+1
            if not self.find( "contagrupocontabilentrada", matching=0.97, waiting_time=10000):
                self.not_found("contagrupocontabilentrada")
            self.click_relative(515, 6)
            self.type_down()
            self.enter()
            if not self.find( "saidaspedcitc", matching=0.97, waiting_time=10000):
                self.not_found("saidaspedcitc")
            self.click_relative(389, 7)
            self.type_down()
            self.enter()
            if not self.find( "salvarenquete", matching=0.97, waiting_time=10000):
                self.not_found("salvarenquete")
            self.click()    
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                self.not_found("excluirrs")
            self.click()
            #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirrs")
            #self.click()
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---SERVIÇOS---####
                             
            if not self.find( "abrircadastros_abacadastro", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro")
            self.click()
            if not self.find( "servicos", matching=0.97, waiting_time=10000):
                self.not_found("servicos")
            self.click()
            y=0                
            while y<2:                 
                if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                    self.not_found("localizarpaises")
                self.click()
                if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                    self.not_found("incluirpe")
                self.click()
                self.type_keys_with_interval(1,'te12!@')
                self.tab()
                self.tab()
                self.type_keys_with_interval(1,'123')
                self.tab()
                self.type_keys_with_interval(1,'123')
                self.tab()
                self.type_keys_with_interval(1,'123')
                self.tab()
                x=0
                while x<7:
                    self.type_down()
                    x=x+1
                self.tab()
                self.type_keys_with_interval(1,'123')
                self.tab()
                self.type_keys_with_interval(1,'t1!')
                self.tab()
                self.tab()
                self.space()
                self.space()
                self.tab()
                if not self.find( "codigostributacoes", matching=0.97, waiting_time=10000):
                    self.not_found("codigostributacoes")
                self.click_relative(550, 50)
                x=0
                while x<5:
                    self.type_down()
                    x=x+1
                self.enter()
                self.type_keys_with_interval(1,'te12!@')
                self.tab()
                x=0
                while x<31:
                    self.type_down()
                    x=x+1
                self.tab()
                x=0
                while x<100:
                    self.type_down()
                    x=x+1
                self.tab()
                if not self.find( "unidadeCS", matching=0.97, waiting_time=10000):
                    self.not_found("unidadeCS")
                self.click_relative(57, 47)
                if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                    self.not_found("localizarpaises")
                self.click()
                self.type_down()
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(1000)
                if not self.find( "grupoCS", matching=0.97, waiting_time=10000):
                    self.not_found("grupoCS")
                self.click_relative(59, 93)
                if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                    self.not_found("retornarpe")
                self.click()
                self.wait(500)
                if not self.find( "planodecontasCS", matching=0.97, waiting_time=10000):
                    self.not_found("planodecontasCS")
                self.click_relative(59, 138)
                if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                    self.not_found("retornarpe")
                self.click()
                self.wait(500)
                if not self.find( "grupofiscalCS", matching=0.97, waiting_time=10000):
                    self.not_found("grupofiscalCS")
                self.click_relative(436, 47)
                if not self.find( "cod006fiCS", matching=0.97, waiting_time=10000):
                    self.not_found("cod006fiCS")
                self.click()
                if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                    self.not_found("selecionarmunicipiovcr")
                self.click()
                self.wait(500)
                if not self.find( "subgrupoCS", matching=0.97, waiting_time=10000):
                    self.not_found("subgrupoCS")
                self.click_relative(439, 90)
                if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                    self.not_found("retornarpe")
                self.click()
                self.wait(500)
                if not self.find( "ncmCS", matching=0.97, waiting_time=10000):
                    self.not_found("ncmCS")
                self.click_relative(490, 138)
                if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                    self.not_found("retornarpe")
                self.click()
                self.wait(500)
                if not self.find( "familiaCS", matching=0.97, waiting_time=10000):
                    self.not_found("familiaCS")
                self.click_relative(820, 46)
                if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                    self.not_found("retornarpe")
                self.click()
                self.wait(500)
                if not self.find( "marcaCS", matching=0.97, waiting_time=10000):
                    self.not_found("marcaCS")
                self.click_relative(818, 94)
                if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                    self.not_found("retornarpe")
                self.click()
                self.wait(500)
                if not self.find( "centrocustoCS", matching=0.97, waiting_time=10000):
                    self.not_found("centrocustoCS")
                self.click_relative(846, 141)
                if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                    self.not_found("retornarpe")
                self.click()
                
                
                                ####---ABA2 CS---####
                                
                if not self.find( "aba2CS", matching=0.97, waiting_time=10000):
                    self.not_found("aba2CS")
                self.click()
                if not self.find( "dataselecaocardex", matching=0.97, waiting_time=10000):
                    self.not_found("dataselecaocardex")
                self.click_relative(170, 47)
                if not self.find( "carregaranoCS", matching=0.97, waiting_time=10000):
                    self.not_found("carregaranoCS")
                self.click()
                if not self.find( "selecionaranoatualCS", matching=0.97, waiting_time=10000):
                    self.not_found("selecionaranoatualCS")
                self.click()
                if not self.find( "consultarcardexCS", matching=0.97, waiting_time=10000):
                    self.not_found("consultarcardexCS")
                self.click()
                
                                ####---ABA3 PRECOS---####
                
                if not self.find( "aba3precosCS", matching=0.97, waiting_time=10000):
                    self.not_found("aba3precosCS")
                self.click()
                if not self.find( "salvarenquete", matching=0.97, waiting_time=10000):
                    self.not_found("salvarenquete")
                self.click()
                self.wait(1000)    
                if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                    self.not_found("retornarpe")
                self.click()
                y=y+2
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                self.not_found("excluirrs")
            self.click()
            #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirrs")
            #self.click()
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            


                            ####---CADASTROS AUXILIARES---####
                             
            if not self.find( "abrircadastros_abacadastro", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro")
            self.click()
            if not self.find( "cadastrosauxiliares", matching=0.97, waiting_time=10000):
                self.not_found("cadastrosauxiliares")
            self.click()
            if not self.find( "fasesdeproducao", matching=0.97, waiting_time=10000):
                self.not_found("fasesdeproducao")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "salvarenquete", matching=0.97, waiting_time=10000):
                self.not_found("salvarenquete")
            self.click()    
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                self.not_found("excluirrs")
            self.click()
            #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirrs")
            #self.click()
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
            if not self.find( "abrircadastros_abacadastro", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro")
            self.click()
            if not self.find( "cadastrosauxiliares", matching=0.97, waiting_time=10000):
                self.not_found("cadastrosauxiliares")
            self.click()
            if not self.find( "statusCA", matching=0.97, waiting_time=10000):
                self.not_found("statusCA")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            self.wait(500)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()
            self.type_keys_with_interval(1,'te12!@')
            self.tab()
            self.tab()
            self.space()
            self.type_down()
            self.type_down()
            self.space()
            x=0
            while x<8:
                self.type_down()
                self.space()
                x=x+1
            x=0
            while x<9:
                self.space()
                self.type_up() 
                x=x+1
            self.tab()
            if not self.find( "fechamentosituacaostatus", matching=0.97, waiting_time=10000):
                self.not_found("fechamentosituacaostatus")
            self.click()
            if not self.find( "situacaoproduzirstatus", matching=0.97, waiting_time=10000):
                self.not_found("situacaoproduzirstatus")
            self.click()
            if not self.find( "situacaoemproducaostatus", matching=0.97, waiting_time=10000):
                self.not_found("situacaoemproducaostatus")
            self.click()
            if not self.find( "situacaocancelamentostatus", matching=0.97, waiting_time=10000):
                self.not_found("situacaocancelamentostatus")
            self.click()
            if not self.find( "estoquereservarstatus", matching=0.97, waiting_time=10000):
                self.not_found("estoquereservarstatus")
            self.click()
            if not self.find( "reservarnaoreservarstatus", matching=0.97, waiting_time=10000):
                self.not_found("reservarnaoreservarstatus")
            self.click()
            if not self.find( "situacaoaberturastatus", matching=0.97, waiting_time=10000):
                self.not_found("situacaoaberturastatus")
            self.click()
            if not self.find( "reservaseminfluenciastatus", matching=0.97, waiting_time=10000):
                self.not_found("reservaseminfluenciastatus")
            self.click()
            if not self.find( "salvarenquete", matching=0.97, waiting_time=10000):
                self.not_found("salvarenquete")
            self.click() 
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "codte12Cstatus", matching=0.97, waiting_time=10000):
                self.not_found("codte12Cstatus")
            self.click()
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                self.not_found("excluirrs")
            self.click()
            #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirrs")
            #self.click()
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
            
            if not self.find( "abrircadastros_abacadastro", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro")
            self.click()
            if not self.find( "cadastrosauxiliares", matching=0.97, waiting_time=10000):
                self.not_found("cadastrosauxiliares")
            self.click()
            if not self.find( "motivosdequebraCaux", matching=0.97, waiting_time=10000):
                self.not_found("motivosdequebraCaux")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "salvarenquete", matching=0.97, waiting_time=10000):
                self.not_found("salvarenquete")
            self.click() 
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "codte12Cstatus", matching=0.97, waiting_time=10000):
                self.not_found("codte12Cstatus")
            self.click()
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                self.not_found("excluirrs")
            self.click()
            #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirrs")
            #self.click()
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
            if not self.find( "abrircadastros_abacadastro", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro")
            self.click()
            if not self.find( "cadastrosauxiliares", matching=0.97, waiting_time=10000):
                self.not_found("cadastrosauxiliares")
            self.click()
            if not self.find( "moldesCaux", matching=0.97, waiting_time=10000):
                self.not_found("moldesCaux")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()
            self.type_keys_with_interval(1,'te12!@')
            self.tab()
            self.type_up()
            self.type_up()
            self.type_down()
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            if not self.find( "fornecedormoldes", matching=0.97, waiting_time=10000):
                self.not_found("fornecedormoldes")
            self.click_relative(128, 4)
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            x=0
            while x<3:
                self.tab()
                x=x+1
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "salvarenquete", matching=0.97, waiting_time=10000):
                self.not_found("salvarenquete")
            self.click() 
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "codte12Cstatus", matching=0.97, waiting_time=10000):
                self.not_found("codte12Cstatus")
            self.click()
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                self.not_found("excluirrs")
            self.click()
            #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirrs")
            #self.click()
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---PLANO DE CONTAS, CUSTOS E FINANCEIRO---####
                             
            if not self.find( "abrircadastros_abacadastro", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro")
            self.click()
            if not self.find( "planodecontas,custos,financeiro", matching=0.97, waiting_time=10000):
                self.not_found("planodecontas,custos,financeiro")
            self.click()
            if not self.find( "planodecustos", matching=0.97, waiting_time=10000):
                self.not_found("planodecustos")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()                 
            self.wait(1500)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()
            if not self.find( "inserirnumeracaoPC", matching=0.97, waiting_time=10000):
                self.not_found("inserirnumeracaoPC")
            self.click()
            self.type_keys_with_interval(1,'te12!@')
            self.tab()
            self.space()
            self.space()
            self.tab()
            self.space()
            self.space()
            self.tab()
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "salvarenquete", matching=0.97, waiting_time=10000):
                self.not_found("salvarenquete")
            self.click() 
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "codte12Cstatus", matching=0.97, waiting_time=10000):
                self.not_found("codte12Cstatus")
            self.click()
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                self.not_found("excluirrs")
            self.click()
            #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirrs")
            #self.click()
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
            if not self.find( "abrircadastros_abacadastro", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro")
            self.click()
            if not self.find( "planodecontas,custos,financeiro", matching=0.97, waiting_time=10000):
                self.not_found("planodecontas,custos,financeiro")
            self.click()
            if not self.find( "planofinanceiroC", matching=0.97, waiting_time=10000):
                self.not_found("planofinanceiroC")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()                 
            self.wait(1500)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()
            if not self.find( "inserirnumeracaoPC", matching=0.97, waiting_time=10000):
                self.not_found("inserirnumeracaoPC")
            self.click()
            self.type_keys_with_interval(1,'te12!@')
            self.tab()
            self.space()
            self.space()
            self.tab()
            self.space()
            self.space()
            self.tab()
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "salvarenquete", matching=0.97, waiting_time=10000):
                self.not_found("salvarenquete")
            self.click() 
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "codte12Cstatus", matching=0.97, waiting_time=10000):
                self.not_found("codte12Cstatus")
            self.click()
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                self.not_found("excluirrs")
            self.click()
            #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirrs")
            #self.click()
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
            if not self.find( "abrircadastros_abacadastro", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro")
            self.click()
            if not self.find( "planodecontas,custos,financeiro", matching=0.97, waiting_time=10000):
                self.not_found("planodecontas,custos,financeiro")
            self.click()
            if not self.find( "planocontabilC", matching=0.97, waiting_time=10000):
                self.not_found("planocontabilC")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()                 
            self.wait(1500)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()
            self.type_keys_with_interval(1,'13')
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            self.tab()
            self.tab()
            x=0
            while x<6:
                self.type_down()
                x=x+1
            if not self.find( "inativasimpc", matching=0.97, waiting_time=10000):
                self.not_found("inativasimpc")
            self.click()
            if not self.find( "inativanaoPC", matching=0.97, waiting_time=10000):
                self.not_found("inativanaoPC")
            self.click()
            if not self.find( "centrodecustoinicialPC", matching=0.97, waiting_time=10000):
                self.not_found("centrodecustoinicialPC")
            self.click_relative(143, 18)
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            if not self.find( "okerronaoencontrado", matching=0.97, waiting_time=10000):
                self.not_found("okerronaoencontrado")
            self.click()
            self.backspace()
            if not self.find( "centrodecustofinalPC", matching=0.97, waiting_time=10000):
                self.not_found("centrodecustofinalPC")
            self.click_relative(142, 40)
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            if not self.find( "okerronaoencontrado", matching=0.97, waiting_time=10000):
                self.not_found("okerronaoencontrado")
            self.click()
            self.backspace()
            if not self.find( "grupodeempresaPC", matching=0.97, waiting_time=10000):
                self.not_found("grupodeempresaPC")
            self.click_relative(44, 31)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "salvarenquete", matching=0.97, waiting_time=10000):
                self.not_found("salvarenquete")
            self.click() 
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            self.type_keys_with_interval(1,'te12')
            self.enter()
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                self.not_found("excluirrs")
            self.click()
            #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirrs")
            #self.click()
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
            
            if not self.find( "abrircadastros_abacadastro", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro")
            self.click()
            if not self.find( "classificacoes", matching=0.97, waiting_time=10000):
                self.not_found("classificacoes")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()            
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
                self.not_found("salvarrs")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "buscarcodteteste", matching=0.97, waiting_time=10000):
                self.not_found("buscarcodteteste")
            self.click_relative(12, 29)
            self.type_keys_with_interval(1,'te12')
            self.enter()
            if not self.find( "redesocialteste", matching=0.97, waiting_time=10000):
                self.not_found("redesocialteste")
            self.click()
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                self.not_found("excluirrs")
            self.click()
            #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirrs")
            #self.click()
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---CONDICAO PAGAMENTO---####
                             
            if not self.find( "abrircadastros_abacadastro", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro")
            self.click()
            if not self.find( "condicoesdepagamento", matching=0.97, waiting_time=10000):
                self.not_found("condicoesdepagamento")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()            
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()
            self.type_keys_with_interval(1,'te12!@')
            self.tab()
            self.space()
            self.space()
            self.tab()
            self.tab()
            self.type_up()
            self.type_down()
            self.tab()
            self.type_up()
            self.type_up()
            self.type_down()
            self.type_down()
            x=0
            while x<4:
                self.tab()
                self.type_keys_with_interval(1,'123')
                x=x+1
            self.tab()    
            self.type_down()
            self.type_down()
            self.type_up()
            self.tab()
            self.type_down()
            self.type_up()
            self.type_down()
            x=0
            while x<5:
                self.tab()
                self.type_keys_with_interval(1,'123')
                x=x+1
            if not self.find( "somenteavistadesconto", matching=0.97, waiting_time=10000):
                self.not_found("somenteavistadesconto")
            self.click()
            if not self.find( "permitirsempredesconto", matching=0.97, waiting_time=10000):
                self.not_found("permitirsempredesconto")
            self.click()
            if not self.find( "naopermitedesconto", matching=0.97, waiting_time=10000):
                self.not_found("naopermitedesconto")
            self.click()
            self.tab()
            self.type_keys_with_interval(1,'123')
            x=0
            while x<2:
                self.tab()
                self.space()
                self.space()
                x=x+1
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_down()
            self.type_down()
            self.type_up()
            self.type_up()
            self.tab()
            x=0
            while x<4:
                self.type_down()
                x=x+1
            x=0
            while x<3:
                self.type_up()
                x=x+1
            x=0
            while x<3:
                self.tab()
                self.space()
                self.space()
                x=x+1
            self.tab()
            self.type_down()
            self.type_down()
            self.type_up()
            self.type_up()
            if not self.find( "tipodepagamentoprevisto", matching=0.97, waiting_time=10000):
                self.not_found("tipodepagamentoprevisto")
            self.click_relative(60, 47)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "operacaobaixafinanceiro", matching=0.97, waiting_time=10000):
                self.not_found("operacaobaixafinanceiro")
            self.click_relative(58, 87)
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "planofinanceiro", matching=0.97, waiting_time=10000):
                self.not_found("planofinanceiro")
            self.click_relative(487, 46)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "comissaoCP", matching=0.97, waiting_time=10000):
                self.not_found("comissaoCP")
            self.click_relative(461, 88)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "oplancfinanceiroCP", matching=0.97, waiting_time=10000):
                self.not_found("oplancfinanceiroCP")
            self.click_relative(859, 46)
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "localcobrancaCP", matching=0.97, waiting_time=10000):
                self.not_found("localcobrancaCP")
            self.click_relative(862, 89)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
                self.not_found("salvarrs")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "buscarcodteteste", matching=0.97, waiting_time=10000):
                self.not_found("buscarcodteteste")
            self.click_relative(12, 29)
            self.type_keys_with_interval(1,'te12')
            self.enter()
            if not self.find( "redesocialteste", matching=0.97, waiting_time=10000):
                self.not_found("redesocialteste")
            self.click()
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                self.not_found("excluirrs")
            self.click()
            #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirrs")
            #self.click()
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---COMISSOES---####
                             
            if not self.find( "abrircadastros_abacadastro", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro")
            self.click()
            if not self.find( "comissoesC", matching=0.97, waiting_time=10000):
                self.not_found("comissoesC")
            self.click()
            if not self.find( "comissoesCOMC", matching=0.97, waiting_time=10000):
                self.not_found("comissoesCOMC")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()            
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()
            self.type_keys_with_interval(1,'te12!@')
            self.tab()
            self.type_keys_with_interval(1,'123')
            if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
                self.not_found("salvarrs")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "buscarcodteteste", matching=0.97, waiting_time=10000):
                self.not_found("buscarcodteteste")
            self.click_relative(12, 29)
            self.type_keys_with_interval(1,'te12')
            self.enter()
            if not self.find( "redesocialteste", matching=0.97, waiting_time=10000):
                self.not_found("redesocialteste")
            self.click()
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                self.not_found("excluirrs")
            self.click()
            #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirrs")
            #self.click()
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "abrircadastros_abacadastro", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro")
            self.click()
            if not self.find( "comissoesC", matching=0.97, waiting_time=10000):
                self.not_found("comissoesC")
            self.click()
            if not self.find( "fatoresdecomissoesC", matching=0.97, waiting_time=10000):
                self.not_found("fatoresdecomissoesC")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
                self.not_found("salvarrs")
            self.click()
            if not self.find( "addregistrofaixas", matching=0.97, waiting_time=10000):
                self.not_found("addregistrofaixas")
            self.click_relative(8, 32)
            x=0
            while x<3:
                self.type_keys_with_interval(1,'123')
                self.tab()
                x=x+1
            if not self.find( "gravarnovoregistro", matching=0.97, waiting_time=10000):
                self.not_found("gravarnovoregistro")
            self.click()
            if not self.find( "excluirfaixa", matching=0.97, waiting_time=10000):
                self.not_found("excluirfaixa")
            self.click_relative(12, 54)
            #if not self.find( "simexcluirfaixa", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirfaixa")
            #self.click()
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "buscarcodteteste", matching=0.97, waiting_time=10000):
                self.not_found("buscarcodteteste")
            self.click_relative(12, 29)
            self.type_keys_with_interval(1,'te12')
            self.enter()
            if not self.find( "redesocialteste", matching=0.97, waiting_time=10000):
                self.not_found("redesocialteste")
            self.click()
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                self.not_found("excluirrs")
            self.click()
            #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
            #   self.not_found("simexcluirrs")
            #self.click()
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---FUNCOES---####
                             
            if not self.find( "abrircadastros_abacadastro", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro")
            self.click()
            if not self.find( "funcoesC", matching=0.97, waiting_time=10000):
                self.not_found("funcoesC")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()            
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()
            self.type_keys_with_interval(1,'te12!@')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.space()
            self.space()
            self.tab()
            self.type_keys_with_interval(1,'te12!@')
            self.tab()
            self.type_keys_with_interval(1,'t1!')
            self.tab()
            self.type_keys_with_interval(1,'t1!')
            self.tab()
            x=0
            while x<6:
                self.type_keys_with_interval(1,'te12!@')
                self.tab()
                x=x+1
            if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
                self.not_found("salvarrs")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "buscarcodteteste", matching=0.97, waiting_time=10000):
                self.not_found("buscarcodteteste")
            self.click_relative(12, 29)
            self.type_keys_with_interval(1,'te12')
            self.enter()
            if not self.find( "redesocialteste", matching=0.97, waiting_time=10000):
                self.not_found("redesocialteste")
            self.click()
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                self.not_found("excluirrs")
            self.click()
            #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirrs")
            #self.click()
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---BANCOS---####
                             
            if not self.find( "abrircadastros_abacadastro", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro")
            self.click()
            if not self.find( "bancosC", matching=0.97, waiting_time=10000):
                self.not_found("bancosC")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()            
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()
            self.type_keys_with_interval(1,'8748')
            self.tab()
            self.type_keys_with_interval(1,'te12!@')
            self.tab()
            self.type_keys_with_interval(1,'te12!@')
            self.tab()
            self.type_keys_with_interval(1,'t1!')
            self.tab()
            self.type_keys_with_interval(1,'t1!')
            self.tab()
            self.type_keys_with_interval(1,'te12!@')
            self.tab()
            self.space()
            self.space()
            self.tab()
            self.type_keys_with_interval(1,'te12!@')
            self.tab()
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
                self.not_found("salvarrs")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "buscarcodteteste", matching=0.97, waiting_time=10000):
                self.not_found("buscarcodteteste")
            self.click_relative(12, 29)
            self.type_keys_with_interval(1,'te12')
            self.enter()
            if not self.find( "redesocialteste", matching=0.97, waiting_time=10000):
                self.not_found("redesocialteste")
            self.click()
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                self.not_found("excluirrs")
            self.click()
            #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirrs")
            #self.click()
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---CONTAS---####
                             
            if not self.find( "abrircadastros_abacadastro", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro")
            self.click()
            if not self.find( "contasC", matching=0.97, waiting_time=10000):
                self.not_found("contasC")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()            
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()
            self.type_keys_with_interval(1,'te12!@')
            self.tab()
            self.space()
            self.space()
            if not self.find( "ccbancaria", matching=0.97, waiting_time=10000):
                self.not_found("ccbancaria")
            self.click()
            if not self.find( "cclientesfornecedores", matching=0.97, waiting_time=10000):
                self.not_found("cclientesfornecedores")
            self.click()
            if not self.find( "numerarioemtransito", matching=0.97, waiting_time=10000):
                self.not_found("numerarioemtransito")
            self.click()
            if not self.find( "bancoCC", matching=0.97, waiting_time=10000):
                self.not_found("bancoCC")
            self.click_relative(453, 47)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "codigocontabilcontaCC", matching=0.97, waiting_time=10000):
                self.not_found("codigocontabilcontaCC")
            self.click_relative(865, 47)
            if not self.find( "cod00245pcCC", matching=0.97, waiting_time=10000):
                self.not_found("cod00245pcCC")
            self.click()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "empresaCC", matching=0.97, waiting_time=10000):
                self.not_found("empresaCC")
            self.click_relative(49, 95)
            self.backspace()
            self.enter()
            self.type_down()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.tab()
            self.tab()
            self.type_keys_with_interval(1,'t1!')
            self.tab()
            self.type_keys_with_interval(1,'t1!')
            self.tab()
            self.type_keys_with_interval(1,'t1')
            self.backspace()
            self.type_keys_with_interval(1,'!')
            self.tab()
            self.type_keys_with_interval(1,'t')
            self.backspace()
            self.type_keys_with_interval(1,'1')
            self.backspace()
            self.type_keys_with_interval(1,'!')
            self.tab()
            self.type_down()
            self.type_down()
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.space()
            self.space()
            self.tab()
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
                self.not_found("salvarrs")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "buscarcodteteste", matching=0.97, waiting_time=10000):
                self.not_found("buscarcodteteste")
            self.click_relative(12, 29)
            self.type_keys_with_interval(1,'te12')
            self.enter()
            if not self.find( "redesocialteste", matching=0.97, waiting_time=10000):
                self.not_found("redesocialteste")
            self.click()
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                self.not_found("excluirrs")
            self.click()
            #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirrs")
            #self.click()
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---LOCAIS DE COBRANCA---####
                             
            if not self.find( "abrircadastros_abacadastro", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro")
            self.click()
            if not self.find( "locaisdecobranca", matching=0.97, waiting_time=10000):
                self.not_found("locaisdecobranca")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()            
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
                self.not_found("salvarrs")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "buscarcodteteste", matching=0.97, waiting_time=10000):
                self.not_found("buscarcodteteste")
            self.click_relative(12, 29)
            self.type_keys_with_interval(1,'te12')
            self.enter()
            if not self.find( "redesocialteste", matching=0.97, waiting_time=10000):
                self.not_found("redesocialteste")
            self.click()
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                self.not_found("excluirrs")
            self.click()
            #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirrs")
            #self.click()
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---MOEDAS---####
                             
            if not self.find( "abrircadastros_abacadastro", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro")
            self.click()
            if not self.find( "moedasC", matching=0.97, waiting_time=10000):
                self.not_found("moedasC")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()            
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()
            self.type_keys_with_interval(1,'te12!@')
            self.tab()
            self.type_keys_with_interval(1,'t1!')
            self.tab()
            x=0
            while x<2:
                self.type_down()
                x=x+1
            x=0
            while x<2:
                self.type_up()
                x=x+1
            self.tab()
            x=0
            while x<12:
                self.type_down()
                x=x+1
            x=0
            while x<12:
                self.type_up()
                x=x+1
            if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
                self.not_found("salvarrs")
            self.click()
            if not self.find( "addcotacaodiaria", matching=0.97, waiting_time=10000):
                self.not_found("addcotacaodiaria")
            self.click_relative(10, 32)
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.enter()
            if not self.find( "excluircotacaodiaria", matching=0.97, waiting_time=10000):
                self.not_found("excluircotacaodiaria")
            self.click_relative(10, 55)
            #if not self.find( "simexcluirfaixa", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirfaixa")
            #self.click()
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "buscarcodteteste", matching=0.97, waiting_time=10000):
                self.not_found("buscarcodteteste")
            self.click_relative(12, 29)
            self.type_keys_with_interval(1,'te12')
            self.enter()
            if not self.find( "redesocialteste", matching=0.97, waiting_time=10000):
                self.not_found("redesocialteste")
            self.click()
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                self.not_found("excluirrs")
            self.click()
            #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirrs")
            #self.click()
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---TIPOS DE PAGAMENTO---####
                             
            if not self.find( "abrircadastros_abacadastro", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro")
            self.click()
            if not self.find( "tiposdepagamento", matching=0.97, waiting_time=10000):
                self.not_found("tiposdepagamento")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()            
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()
            self.type_keys_with_interval(1,'te12!@')
            self.tab()
            self.type_down()
            self.type_up()
            self.tab()
            self.type_down()
            self.type_up()
            self.tab()
            x=0
            while x<11:
                self.type_down()
                x=x+1
            x=0
            while x<9:
                self.type_up()
                x=x+1    
            self.tab()
            x=0
            while x<15:
                self.type_down()
                x=x+1
            self.tab()
            self.space()
            self.space()
            self.tab()
            self.space()
            self.space()
            self.tab()
            if not self.find( "agrupamentocontaTP", matching=0.97, waiting_time=10000):
                self.not_found("agrupamentocontaTP")
            self.click_relative(55, 42)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "agrupamentooperacaoTP", matching=0.97, waiting_time=10000):
                self.not_found("agrupamentooperacaoTP")
            self.click_relative(475, 42)
            self.enter()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "admcartaoplanofinanceiroTP", matching=0.97, waiting_time=10000):
                self.not_found("admcartaoplanofinanceiroTP")
            self.click_relative(86, 39)
            self.backspace()
            self.enter()
            self.type_down()
            self.type_down()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "admclientecartaoTP", matching=0.97, waiting_time=10000):
                self.not_found("admclientecartaoTP")
            self.click_relative(70, 85)
            self.enter()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "tipopagamentoTP", matching=0.97, waiting_time=10000):
                self.not_found("tipopagamentoTP")
            self.click_relative(539, 40)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.tab()
            self.tab()
            self.type_keys_with_interval(1,'99')
            self.tab()
            self.tab()
            self.tab()
            self.type_up()
            self.type_up()
            self.type_down()
            self.tab()
            x=0
            while x<7:
                self.type_up()
                x=x+1
            if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
                self.not_found("salvarrs")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "buscarcodteteste", matching=0.97, waiting_time=10000):
                self.not_found("buscarcodteteste")
            self.click_relative(12, 29)
            self.type_keys_with_interval(1,'te12')
            self.enter()
            if not self.find( "redesocialteste", matching=0.97, waiting_time=10000):
                self.not_found("redesocialteste")
            self.click()
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                self.not_found("excluirrs")
            self.click()
            #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirrs")
            #self.click()
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---TABELA DE IMPOSTOS---####
                             
            if not self.find( "abrircadastros_abacadastro", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro")
            self.click()
            if not self.find( "tabeladeimpostos", matching=0.97, waiting_time=10000):
                self.not_found("tabeladeimpostos")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()            
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()
            x=0
            while x<4:
                self.tab()
                x=x+1
            x=0
            while x<65:
                self.type_keys_with_interval(1,'123')
                self.tab()
                x=x+1
            self.space()
            self.space()
            self.space()
            x=0
            while x<4:
                self.type_keys_with_interval(1,'123')
                self.tab()
                x=x+1
            self.type_up()
            self.type_up()
            self.type_down()
            if not self.find( "dsrexpoagentenocivo", matching=0.97, waiting_time=10000):
                self.not_found("dsrexpoagentenocivo")
            self.click()
            x=0
            while x<30:
                self.type_keys_with_interval(1,'123')
                self.tab()
                x=x+1
            x=0
            p=24
            if not self.find( "dia01completo", matching=0.97, waiting_time=10000):
                self.not_found("dia01completo")
            self.click_relative(8, p)
            if not self.find( "dia01metade", matching=0.97, waiting_time=10000):
                self.not_found("dia01metade")
            self.click_relative(85, p)
            if not self.find( "dia01nulo", matching=0.97, waiting_time=10000):
                self.not_found("dia01nulo")
            self.click_relative(167, p)
            while x<14:                
                y=p+30
                if not self.find( "dia01completo", matching=0.97, waiting_time=10000):
                    self.not_found("dia01completo")
                self.click_relative(8, y)
                if not self.find( "dia01metade", matching=0.97, waiting_time=10000):
                    self.not_found("dia01metade")
                self.click_relative(85, y)
                if not self.find( "dia01nulo", matching=0.97, waiting_time=10000):
                    self.not_found("dia01nulo")
                self.click_relative(167, y)
                p=p+30
                x=x+1
            if not self.find( "abaixartelatabelas", matching=0.97, waiting_time=10000):
                self.not_found("abaixartelatabelas")
            self.click()
            x=0
            while x<2:
                if not self.find( "abaixartelatabelas2", matching=0.97, waiting_time=10000):
                    self.not_found("abaixartelatabelas2")
                self.double_click()
                x=x+1
            if not self.find( "dia16completo", matching=0.97, waiting_time=10000):
                self.not_found("dia16completo")
            self.click_relative(-175, -35)
            if not self.find( "dia16metade", matching=0.97, waiting_time=10000):
                self.not_found("dia16metade")
            self.click_relative(-96, -35)
            if not self.find( "dia16nulo", matching=0.97, waiting_time=10000):
                self.not_found("dia16nulo")
            self.click_relative(-18, -35)            
            if not self.find( "subirtelatabela", matching=0.97, waiting_time=10000):
                self.not_found("subirtelatabela")
            self.click()
            x=0
            while x<2:
                if not self.find( "subirtelatabela2", matching=0.97, waiting_time=10000):
                    self.not_found("subirtelatabela2")
                self.double_click()
                x=x+1
            if not self.find( "subirtelatabela2", matching=0.97, waiting_time=10000):
                self.not_found("subirtelatabela2")
            self.click()    
            x=0
            p=24
            if not self.find( "dia01completo", matching=0.97, waiting_time=10000):
                self.not_found("dia01completo")
            self.click_relative(260, p)
            if not self.find( "dia01metade", matching=0.97, waiting_time=10000):
                self.not_found("dia01metade")
            self.click_relative(338, p)
            if not self.find( "dia01nulo", matching=0.97, waiting_time=10000):
                self.not_found("dia01nulo")
            self.click_relative(417, p)
            while x<14:                
                y=p+30
                if not self.find( "dia01completo", matching=0.97, waiting_time=10000):
                    self.not_found("dia01completo")
                self.click_relative(260, y)
                if not self.find( "dia01metade", matching=0.97, waiting_time=10000):
                    self.not_found("dia01metade")
                self.click_relative(338, y)
                if not self.find( "dia01nulo", matching=0.97, waiting_time=10000):
                    self.not_found("dia01nulo")
                self.click_relative(417, y)
                p=p+30
                x=x+1
            if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
                self.not_found("salvarrs")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                self.not_found("excluirrs")
            self.click()
            #if not self.find( "simexcluirfaixa", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirfaixa")
            #self.click()
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---CATEGORIAS DE CAMPANHA---####
                             
            if not self.find( "abrircadastros_abacadastro", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro")
            self.click()
            if not self.find( "categoriasdecampanhas", matching=0.97, waiting_time=10000):
                self.not_found("categoriasdecampanhas")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()            
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
                self.not_found("salvarrs")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "buscarcodteteste", matching=0.97, waiting_time=10000):
                self.not_found("buscarcodteteste")
            self.click_relative(12, 29)
            self.type_keys_with_interval(1,'te12')
            self.enter()
            if not self.find( "redesocialteste", matching=0.97, waiting_time=10000):
                self.not_found("redesocialteste")
            self.click()
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                self.not_found("excluirrs")
            self.click()
            #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirrs")
            #self.click()
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---AUTORIZADORES---####
                             
            if not self.find( "abrircadastros_abacadastro", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro")
            self.click()
            if not self.find( "autorizadores", matching=0.97, waiting_time=10000):
                self.not_found("autorizadores")
            self.click()
            if not self.find( "okparametronaodefinido", matching=0.97, waiting_time=10000):
                self.not_found("okparametronaodefinido")
            self.click()
            
                            ####---CONFIGURACOES---####
                             
            if not self.find( "abrircadastros_abacadastro", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro")
            self.click()
            if not self.find( "configuracoes", matching=0.97, waiting_time=10000):
                self.not_found("configuracoes")
            self.click()
            if not self.find( "configuracoesdeformularios", matching=0.97, waiting_time=10000):
                self.not_found("configuracoesdeformularios")
            self.click()
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()
            self.type_keys_with_interval(1,'te12!@')
            self.tab()
            x=0
            while x<9:
                self.type_down()
                x=x+1
            if not self.find( "LPPsexto", matching=0.97, waiting_time=10000):
                self.not_found("LPPsexto")
            self.click_relative(8, 31)
            if not self.find( "LPPoitavos", matching=0.97, waiting_time=10000):
                self.not_found("LPPoitavos")
            self.click_relative(76, 30)
            if not self.find( "CPP1296", matching=0.97, waiting_time=10000):
                self.not_found("CPP1296")
            self.click_relative(8, 38)
            if not self.find( "CPP17136", matching=0.97, waiting_time=10000):
                self.not_found("CPP17136")
            self.click_relative(118, 23)
            if not self.find( "CPP20160", matching=0.97, waiting_time=10000):
                self.not_found("CPP20160")
            self.click_relative(119, 36)
            if not self.find( "CPP1080", matching=0.97, waiting_time=10000):
                self.not_found("CPP1080")
            self.click_relative(8, 23)
            if not self.find( "alturalarguramm", matching=0.97, waiting_time=10000):
                self.not_found("alturalarguramm")
            self.click_relative(22, 26)
            self.backspace()
            self.backspace()
            self.backspace()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            if not self.find( "aba2camposFormularios", matching=0.97, waiting_time=10000):
                self.not_found("aba2camposFormularios")
            self.click()
            if not self.find( "addregistroaba2campos", matching=0.97, waiting_time=10000):
                self.not_found("addregistroaba2campos")
            self.click_relative(-44, 36)
            self.type_keys_with_interval(1,'te12!@')
            self.tab()                 
            x=0
            while x<23:
                self.type_down()
                x=x+1
            self.tab()    
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            x=0
            while x<16:
                self.type_down()
                x=x+1
            self.tab()
            x=0
            while x<5:
                self.type_down()
                x=x+1
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_up()
            self.type_down()
            self.type_down()
            self.tab()
            x=0
            while x<3:
                self.type_down()
                x=x+1    
            self.tab()
            self.type_down()
            self.type_down()
            self.tab()
            x=0
            while x<16:
                self.type_down()
                x=x+1
            x=0
            while x<4:
                self.tab()
                self.space()
                self.space()
                x=x+1
            self.tab()
            self.enter()
            if not self.find( "excluiraba2campos", matching=0.97, waiting_time=10000):
                self.not_found("excluiraba2campos")
            self.click_relative(-45, 156)
            #if not self.find( "simexcluirfaixa", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirfaixa")
            #self.click()
            self.enter()
            if not self.find( "aba3listaformularios", matching=0.97, waiting_time=10000):
                self.not_found("aba3listaformularios")
            self.click()
            if not self.find( "aba4copiarconfigforms", matching=0.97, waiting_time=10000):
                self.not_found("aba4copiarconfigforms")
            self.click()
            x=0
            while x<6:
                self.type_down()
                x=x+1
            self.tab()
            self.type_keys_with_interval(1,'te12!@')
            self.tab()
            self.enter()
            self.enter()
            self.enter()
            if not self.find( "aba5ajustesforms", matching=0.97, waiting_time=10000):
                self.not_found("aba5ajustesforms")
            self.click()
            x=0
            while x<4:
                self.type_down()
                self.enter()
                self.enter()
                self.type_up()
                self.type_up()
                self.tab()
                x=x+1
            self.enter()
            self.enter()
            self.enter()
            self.wait(500)
            self.enter()
            if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
                self.not_found("salvarrs")
            self.click()
            self.wait(500)
            if not self.find( "cancelarformulariosagrvai", matching=0.97, waiting_time=10000):
                self.not_found("cancelarformulariosagrvai")
            self.click()
            
            if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                self.not_found("excluirrs")
            self.click()
            #if not self.find( "simexcluirfaixa", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirfaixa")
            #self.click()
            self.enter()
            self.enter()
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---IMPRESSORA DE CODIGO DE BARRAS---####
                             
            if not self.find( "abrircadastros_abacadastro", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro")
            self.click()
            if not self.find( "configuracoes", matching=0.97, waiting_time=10000):
                self.not_found("configuracoes")
            self.click()
            if not self.find( "impressoradecodigodebarras", matching=0.97, waiting_time=10000):
                self.not_found("impressoradecodigodebarras")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()            
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()
            self.type_keys_with_interval(1,'te12!@')
            self.tab()
            x=0
            while x<10:
                self.type_down()
                x=x+1
            self.tab()
            x=0
            while x<6:
                self.type_down()
                x=x+1
            self.tab()
            self.tab()
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "aba2impressoratermica", matching=0.97, waiting_time=10000):
                self.not_found("aba2impressoratermica")
            self.click()
            if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
                self.not_found("salvarrs")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "buscarcodteteste", matching=0.97, waiting_time=10000):
                self.not_found("buscarcodteteste")
            self.click_relative(12, 29)
            self.type_keys_with_interval(1,'te12')
            self.enter()
            if not self.find( "redesocialteste", matching=0.97, waiting_time=10000):
                self.not_found("redesocialteste")
            self.click()
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                self.not_found("excluirrs")
            self.click()
            #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirrs")
            #self.click()
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---CONFIG IMPORTACAO EMPORIUM---####
                             
            if not self.find( "abrircadastros_abacadastro", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro")
            self.click()
            if not self.find( "configuracoes", matching=0.97, waiting_time=10000):
                self.not_found("configuracoes")
            self.click()
            if not self.find( "configimpoemporium", matching=0.97, waiting_time=10000):
                self.not_found("configimpoemporium")
            self.click()
            if not self.find( "buscarclientecofigemporium", matching=0.97, waiting_time=10000):
                self.not_found("buscarclientecofigemporium")
            self.click_relative(157, 82)
            self.enter()
            if not self.find( "cod0081260selecaocliente", matching=0.97, waiting_time=10000):
                self.not_found("cod0081260selecaocliente")
            self.click()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "opentradabuscar", matching=0.97, waiting_time=10000):
                self.not_found("opentradabuscar")
            self.click_relative(151, 2)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "operacaosaidaimpemporium", matching=0.97, waiting_time=10000):
                self.not_found("operacaosaidaimpemporium")
            self.click_relative(139, 3)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "ecfimpemporium", matching=0.97, waiting_time=10000):
                self.not_found("ecfimpemporium")
            self.click_relative(81, 2)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.tab()
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'t1')
            self.backspace()
            self.type_keys_with_interval(1,'!')
            self.tab()
            self.space()
            self.space()
            self.tab()
            if not self.find( "cnddepagamentoimpemp", matching=0.97, waiting_time=10000):
                self.not_found("cnddepagamentoimpemp")
            self.click_relative(163, 0)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "tiporecpagtimpemp", matching=0.97, waiting_time=10000):
                self.not_found("tiporecpagtimpemp")
            self.click_relative(142, 2)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "itemimpemp", matching=0.97, waiting_time=10000):
                self.not_found("itemimpemp")
            self.click_relative(89, 3)
            self.wait(1000)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "opvendascanceladasimpemp", matching=0.97, waiting_time=10000):
                self.not_found("opvendascanceladasimpemp")
            self.click_relative(208, 6)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "cfopimpemp", matching=0.97, waiting_time=10000):
                self.not_found("cfopimpemp")
            self.click_relative(95, 4)
            if not self.find( "vendedorimpemp", matching=0.97, waiting_time=10000):
                self.not_found("vendedorimpemp")
            self.click_relative(113, 4)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "tipoimpemp", matching=0.97, waiting_time=10000):
                self.not_found("tipoimpemp")
            self.click_relative(226, 36)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "empresaimpemp", matching=0.97, waiting_time=10000):
                self.not_found("empresaimpemp")
            self.click_relative(113, 57)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "clienteimpemptiposreceb", matching=0.97, waiting_time=10000):
                self.not_found("clienteimpemptiposreceb")
            self.click_relative(113, 82)
            self.enter()
            if not self.find( "cod0081260selecaocliente", matching=0.97, waiting_time=10000):
                self.not_found("cod0081260selecaocliente")
            self.click()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "aba2impemp", matching=0.97, waiting_time=10000):
                self.not_found("aba2impemp")
            self.click()
            if not self.find( "buscarcontaimpemp", matching=0.97, waiting_time=10000):
                self.not_found("buscarcontaimpemp")
            self.click_relative(73, 42)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "aba3bancosimpemp", matching=0.97, waiting_time=10000):
                self.not_found("aba3bancosimpemp")
            self.click()
            if not self.find( "buscarbancoimpemp", matching=0.97, waiting_time=10000):
                self.not_found("buscarbancoimpemp")
            self.click_relative(157, 42)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "aba4impemp", matching=0.97, waiting_time=10000):
                self.not_found("aba4impemp")
            self.click()
            if not self.find( "buscarecfimpemp", matching=0.97, waiting_time=10000):
                self.not_found("buscarecfimpemp")
            self.click_relative(109, 42)
            if not self.find( "aba5impemp", matching=0.97, waiting_time=10000):
                self.not_found("aba5impemp")
            self.click()
            x=0
            while x<5:
                self.type_keys_with_interval(1,'te12!@')
                self.tab()
                x=x+1
            if not self.find( "aba6impemp", matching=0.97, waiting_time=10000):
                self.not_found("aba6impemp")
            self.click()
            if not self.find( "buscarempresaaba6impemp", matching=0.97, waiting_time=10000):
                self.not_found("buscarempresaaba6impemp")
            self.click_relative(-141, 49)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "buscarempresaclienteaba6impemp", matching=0.97, waiting_time=10000):
                self.not_found("buscarempresaclienteaba6impemp")
            self.click_relative(-138, 74)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "buscarempresaitensaba6impemp", matching=0.97, waiting_time=10000):
                self.not_found("buscarempresaitensaba6impemp")
            self.click_relative(-139, 96)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.tab()
            self.tab()
            self.tab()
            self.type_keys_with_interval(1,'te12!@')
            self.tab()
            self.type_keys_with_interval(1,'te12!@')
            self.tab()
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "aba7impemp", matching=0.97, waiting_time=10000):
                self.not_found("aba7impemp")
            self.click()
            if not self.find( "buscarempresaaba7impemp", matching=0.97, waiting_time=10000):
                self.not_found("buscarempresaaba7impemp")
            self.click_relative(-413, 36)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "aba8impemp", matching=0.97, waiting_time=10000):
                self.not_found("aba8impemp")
            self.click()
            if not self.find( "buscarempresaaba8impemp", matching=0.97, waiting_time=10000):
                self.not_found("buscarempresaaba8impemp")
            self.click_relative(-536, 43)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "aba9impemp", matching=0.97, waiting_time=10000):
                self.not_found("aba9impemp")
            self.click()
            if not self.find( "buscartabelaimpemp", matching=0.97, waiting_time=10000):
                self.not_found("buscartabelaimpemp")
            self.click_relative(-351, 40)
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "aba10impemp", matching=0.97, waiting_time=10000):
                self.not_found("aba10impemp")
            self.click()
            if not self.find( "buscarempresaaba10impemp", matching=0.97, waiting_time=10000):
                self.not_found("buscarempresaaba10impemp")
            self.click_relative(-736, 40)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "buscarvendedoraba10impemp", matching=0.97, waiting_time=10000):
                self.not_found("buscarvendedoraba10impemp")
            self.click_relative(-211, 37)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
                self.not_found("salvarrs")
            self.click()
            if not self.find( "excluirimpemp", matching=0.97, waiting_time=10000):
                self.not_found("excluirimpemp")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---CONFIG EMP NOVO---####
                                              
            if not self.find( "abrircadastros_abacadastro", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro")
            self.click()
            if not self.find( "configuracoes", matching=0.97, waiting_time=10000):
                self.not_found("configuracoes")
            self.click()
            if not self.find( "configemporiumnovo", matching=0.97, waiting_time=10000):
                self.not_found("configemporiumnovo")
            self.click()
            self.enter()
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()
            if not self.find( "buscarclienteconfigemp", matching=0.97, waiting_time=10000):
                self.not_found("buscarclienteconfigemp")
            self.click_relative(73, 97)
            self.enter()
            if not self.find( "cod0081260selecaocliente", matching=0.97, waiting_time=10000):
                self.not_found("cod0081260selecaocliente")
            self.click()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "buscaritemconfigemp", matching=0.97, waiting_time=10000):
                self.not_found("buscaritemconfigemp")
            self.click_relative(71, 143)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "buscarecfconfigemp", matching=0.97, waiting_time=10000):
                self.not_found("buscarecfconfigemp")
            self.click_relative(50, 186)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "buscacondpagconfigemp", matching=0.97, waiting_time=10000):
                self.not_found("buscacondpagconfigemp")
            self.click_relative(468, 99)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "buscarvendedorconfigemp", matching=0.97, waiting_time=10000):
                self.not_found("buscarvendedorconfigemp")
            self.click_relative(469, 143)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "buscatipopagamentoconfigemp", matching=0.97, waiting_time=10000):
                self.not_found("buscatipopagamentoconfigemp")
            self.click_relative(872, 95)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "buscarcfopconfigemp", matching=0.97, waiting_time=10000):
                self.not_found("buscarcfopconfigemp")
            self.click_relative(871, 144)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.tab()
            self.tab()
            self.tab()
            self.tab()
            self.type_keys_with_interval(1,'t1')
            self.backspace()
            self.type_keys_with_interval(1,'!')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.space()
            self.space()
            if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
                self.not_found("salvarrs")
            self.click()
            if not self.find( "addregisconfigemp", matching=0.97, waiting_time=10000):
                self.not_found("addregisconfigemp")
            self.click_relative(10, 223)            
            if not self.find( "registpconfigemp", matching=0.97, waiting_time=10000):
                self.not_found("registpconfigemp")
            self.click_relative(186, 270)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "regisempresaconfigemp", matching=0.97, waiting_time=10000):
                self.not_found("regisempresaconfigemp")
            self.click_relative(576, 270)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "regisclienteconfigemp", matching=0.97, waiting_time=10000):
                self.not_found("regisclienteconfigemp")
            self.click_relative(102, 314)
            self.enter()
            if not self.find( "cod0081260selecaocliente", matching=0.97, waiting_time=10000):
                self.not_found("cod0081260selecaocliente")
            self.click()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.tab()
            self.tab()
            self.type_down()
            self.type_down()
            self.type_down()
            if not self.find( "excluirregistroconfigemp", matching=0.97, waiting_time=10000):
                self.not_found("excluirregistroconfigemp")
            self.click_relative(12, 266)
            if not self.find( "excluirregisconfigemp", matching=0.97, waiting_time=10000):
                self.not_found("excluirregisconfigemp")
            self.click_relative(12, 246)
            #if not self.find( "simexcluirfaixa", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirfaixa")
            #self.click()
            self.enter()

            #ABA2
            if not self.find( "aba2regisconfigemp", matching=0.97, waiting_time=10000):
                self.not_found("aba2regisconfigemp")
            self.click()
            if not self.find( "addregisconfigemp", matching=0.97, waiting_time=10000):
                self.not_found("addregisconfigemp")
            self.click_relative(10, 223)
            if not self.find( "addregiscontaaba2cemp", matching=0.97, waiting_time=10000):
                self.not_found("addregiscontaaba2cemp")
            self.click_relative(152, 269)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "excluirregistroconfigemp", matching=0.97, waiting_time=10000):
                self.not_found("excluirregistroconfigemp")
            self.click_relative(12, 266)
            if not self.find( "excluirregisconfigemp", matching=0.97, waiting_time=10000):
                self.not_found("excluirregisconfigemp")
            self.click_relative(12, 246)
            #if not self.find( "simexcluirfaixa", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirfaixa")
            #self.click()
            self.enter()

            #ABA3
            if not self.find( "aba3configemp", matching=0.97, waiting_time=10000):
                self.not_found("aba3configemp")
            self.click()
            if not self.find( "addregisconfigemp", matching=0.97, waiting_time=10000):
                self.not_found("addregisconfigemp")
            self.click_relative(10, 223)
            if not self.find( "addregiscontaaba2cemp", matching=0.97, waiting_time=10000):
                self.not_found("addregiscontaaba2cemp")
            self.click_relative(152, 269)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "excluirregistroconfigemp", matching=0.97, waiting_time=10000):
                self.not_found("excluirregistroconfigemp")
            self.click_relative(12, 266)
            if not self.find( "excluirregisconfigemp", matching=0.97, waiting_time=10000):
                self.not_found("excluirregisconfigemp")
            self.click_relative(12, 246)
            #if not self.find( "simexcluirfaixa", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirfaixa")
            #self.click()
            self.enter()

            #ABA4
            if not self.find( "aba4configemp", matching=0.97, waiting_time=10000):
                self.not_found("aba4configemp")
            self.click()
            if not self.find( "addregisconfigemp", matching=0.97, waiting_time=10000):
                self.not_found("addregisconfigemp")
            self.click_relative(10, 223)
            if not self.find( "addregiscontaaba2cemp", matching=0.97, waiting_time=10000):
                self.not_found("addregiscontaaba2cemp")
            self.click_relative(152, 269)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "excluirregistroconfigemp", matching=0.97, waiting_time=10000):
                self.not_found("excluirregistroconfigemp")
            self.click_relative(12, 266)
            if not self.find( "excluirregisconfigemp", matching=0.97, waiting_time=10000):
                self.not_found("excluirregisconfigemp")
            self.click_relative(12, 246)
            #if not self.find( "simexcluirfaixa", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirfaixa")
            #self.click()
            self.enter()

            #ABA5
            if not self.find( "aba5configemp", matching=0.97, waiting_time=10000):
                self.not_found("aba5configemp")
            self.click()
            if not self.find( "addregisconfigemp", matching=0.97, waiting_time=10000):
                self.not_found("addregisconfigemp")
            self.click_relative(10, 223)
            if not self.find( "buscaempresaaba5cemp", matching=0.97, waiting_time=10000):
                self.not_found("buscaempresaaba5cemp")
            self.click_relative(291, 268)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "excluirregistroconfigemp", matching=0.97, waiting_time=10000):
                self.not_found("excluirregistroconfigemp")
            self.click_relative(12, 266)
            if not self.find( "excluirregisconfigemp", matching=0.97, waiting_time=10000):
                self.not_found("excluirregisconfigemp")
            self.click_relative(12, 246)
            #if not self.find( "simexcluirfaixa", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirfaixa")
            #self.click()
            self.enter()

            #ABA6
            if not self.find( "aba6configemp", matching=0.97, waiting_time=10000):
                self.not_found("aba6configemp")
            self.click()
            if not self.find( "addregisconfigemp", matching=0.97, waiting_time=10000):
                self.not_found("addregisconfigemp")
            self.click_relative(10, 223)
            if not self.find( "buscaempresaaba6configemp", matching=0.97, waiting_time=10000):
                self.not_found("buscaempresaaba6configemp")
            self.click_relative(92, 269)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "excluirregistroconfigemp", matching=0.97, waiting_time=10000):
                self.not_found("excluirregistroconfigemp")
            self.click_relative(12, 266)
            if not self.find( "excluirregisconfigemp", matching=0.97, waiting_time=10000):
                self.not_found("excluirregisconfigemp")
            self.click_relative(12, 246)
            #if not self.find( "simexcluirfaixa", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirfaixa")
            #self.click()
            self.enter()

            #ABA7
            if not self.find( "aba7regisconfigemp", matching=0.97, waiting_time=10000):
                self.not_found("aba7regisconfigemp")
            self.click()
            if not self.find( "addregisconfigemp", matching=0.97, waiting_time=10000):
                self.not_found("addregisconfigemp")
            self.click_relative(10, 223)
            if not self.find( "addregiscontaaba2cemp", matching=0.97, waiting_time=10000):
                self.not_found("addregiscontaaba2cemp")
            self.click_relative(152, 269)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "excluirregistroconfigemp", matching=0.97, waiting_time=10000):
                self.not_found("excluirregistroconfigemp")
            self.click_relative(12, 266)
            if not self.find( "excluirregisconfigemp", matching=0.97, waiting_time=10000):
                self.not_found("excluirregisconfigemp")
            self.click_relative(12, 246)
            #if not self.find( "simexcluirfaixa", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirfaixa")
            #self.click()
            self.enter()

            #ABA8
            if not self.find( "aba8configemp", matching=0.97, waiting_time=10000):
                self.not_found("aba8configemp")
            self.click()
            if not self.find( "addregisconfigemp", matching=0.97, waiting_time=10000):
                self.not_found("addregisconfigemp")
            self.click_relative(10, 223)
            if not self.find( "addregiscontaaba2cemp", matching=0.97, waiting_time=10000):
                self.not_found("addregiscontaaba2cemp")
            self.click_relative(152, 269)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "buscavendedoraba8configemp", matching=0.97, waiting_time=10000):
                self.not_found("buscavendedoraba8configemp")
            self.click_relative(545, 266)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "excluirregistroconfigemp", matching=0.97, waiting_time=10000):
                self.not_found("excluirregistroconfigemp")
            self.click_relative(12, 266)
            if not self.find( "excluirregisconfigemp", matching=0.97, waiting_time=10000):
                self.not_found("excluirregisconfigemp")
            self.click_relative(12, 246)
            #if not self.find( "simexcluirfaixa", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirfaixa")
            #self.click()
            self.enter()

            #ABA9
            if not self.find( "aba9regisconfigemp", matching=0.97, waiting_time=10000):
                self.not_found("aba9regisconfigemp")
            self.click()
            if not self.find( "addregisconfigemp", matching=0.97, waiting_time=10000):
                self.not_found("addregisconfigemp")
            self.click_relative(10, 223)
            if not self.find( "buscaempresaaba9cemp", matching=0.97, waiting_time=10000):
                self.not_found("buscaempresaaba9cemp")
            self.click_relative(94, 290)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "buscaoperacaoaba9cemp", matching=0.97, waiting_time=10000):
                self.not_found("buscaoperacaoaba9cemp")
            self.click_relative(491, 294)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "excluirregistroconfigemp", matching=0.97, waiting_time=10000):
                self.not_found("excluirregistroconfigemp")
            self.click_relative(12, 266)
            if not self.find( "excluirregisconfigemp", matching=0.97, waiting_time=10000):
                self.not_found("excluirregisconfigemp")
            self.click_relative(12, 246)
            #if not self.find( "simexcluirfaixa", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirfaixa")
            #self.click()
            self.enter()

            #ABA10
            if not self.find( "aba10configemp", matching=0.97, waiting_time=10000):
                self.not_found("aba10configemp")
            self.click()
            if not self.find( "balancaaba10configemp", matching=0.97, waiting_time=10000):
                self.not_found("balancaaba10configemp")
            self.click_relative(-662, 52)
            x=0
            while x<5:
                self.type_keys_with_interval(1,'te12!@')
                self.tab()
                x=x+1
            
            #ABA11
            if not self.find( "aba11configemp", matching=0.97, waiting_time=10000):
                self.not_found("aba11configemp")
            self.click()
            if not self.find( "buscaempresaaba11cemp", matching=0.97, waiting_time=10000):
                self.not_found("buscaempresaaba11cemp")
            self.click_relative(90, 265)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "buscaCFaba11cemp", matching=0.97, waiting_time=10000):
                self.not_found("buscaCFaba11cemp")
            self.click_relative(489, 265)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "buscaitensaba11cemp", matching=0.97, waiting_time=10000):
                self.not_found("buscaitensaba11cemp")
            self.click_relative(889, 266)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.tab()
            self.tab()
            self.type_keys_with_interval(1,'te12!@')
            self.tab()
            self.type_keys_with_interval(1,'te12!@')
            self.tab()
            self.type_keys_with_interval(1,'te12!@')
            
            if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
                self.not_found("salvarrs")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            #if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
            #    self.not_found("excluirrs")
            #self.click()
            #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirrs")
            #self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---PDV---####
                             
            if not self.find( "abrircadastros_abacadastro", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro")
            self.click()
            if not self.find( "pdv", matching=0.97, waiting_time=10000):
                self.not_found("pdv")
            self.click()
            if not self.find( "terminais", matching=0.97, waiting_time=10000):
                self.not_found("terminais")
            self.click()
            #if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
            #    self.not_found("localizarpaises")
            #self.click()            
            #if not self.find( "editarfim", matching=0.97, waiting_time=10000):
            #    self.not_found("editarfim")
            #self.click()
            #if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
            #    self.not_found("retornarpe")
            #self.click()
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()
            self.type_right()
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
                self.not_found("salvarrs")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "buscarcodteteste", matching=0.97, waiting_time=10000):
                self.not_found("buscarcodteteste")
            self.click_relative(12, 29)
            self.type_keys_with_interval(1,'te12')
            self.enter()
            if not self.find( "redesocialteste", matching=0.97, waiting_time=10000):
                self.not_found("redesocialteste")
            self.click()
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                self.not_found("excluirrs")
            self.click()
            #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirrs")
            #self.click()
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---MAPA FISCAL---####
                             
            if not self.find( "abrircadastros_abacadastro", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro")
            self.click()
            if not self.find( "pdv", matching=0.97, waiting_time=10000):
                self.not_found("pdv")
            self.click()
            if not self.find( "mapafiscal", matching=0.97, waiting_time=10000):
                self.not_found("mapafiscal")
            self.click()
            self.enter()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()
            self.type_keys_with_interval(1,'8748')
            self.tab()
            self.type_keys_with_interval(1,'8748')
            self.tab()
            self.space()
            self.space()
            self.tab()
            self.type_down()
            self.type_down()
            if not self.find( "empresareducaoZ", matching=0.97, waiting_time=10000):
                self.not_found("empresareducaoZ")
            self.click_relative(59, 133)
            self.backspace()
            self.enter()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.tab()
            self.tab()
            self.tab()
            x=0
            while x<31:
                self.type_keys_with_interval(1,'123')
                self.tab()
                x=x+1
            if not self.find( "aba1reducaoZ", matching=0.97, waiting_time=10000):
                self.not_found("aba1reducaoZ")
            self.click_relative(25, 165)            
            x=0
            while x<31:
                self.backspace()
                self.tab()
                x=x+1
                
            if not self.find( "cancelarreducaoZ", matching=0.97, waiting_time=10000):
                self.not_found("cancelarreducaoZ")
            self.click()
            self.wait(500)
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---MOTIVOS DIVERSOS---####
                             
            if not self.find( "abrircadastros_abacadastro", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro")
            self.click()
            if not self.find( "pdv", matching=0.97, waiting_time=10000):
                self.not_found("pdv")
            self.click()
            if not self.find( "motivosdiversos", matching=0.97, waiting_time=10000):
                self.not_found("motivosdiversos")
            self.click()
            #if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
            #    self.not_found("localizarpaises")
            #self.click()            
            #if not self.find( "editarfim", matching=0.97, waiting_time=10000):
            #    self.not_found("editarfim")
            #self.click()
            #if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
            #   self.not_found("retornarpe")
            #self.click()
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
                self.not_found("salvarrs")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "buscarcodteteste", matching=0.97, waiting_time=10000):
                self.not_found("buscarcodteteste")
            self.click_relative(12, 29)
            self.type_keys_with_interval(1,'te12')
            self.enter()
            if not self.find( "redesocialteste", matching=0.97, waiting_time=10000):
                self.not_found("redesocialteste")
            self.click()
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                self.not_found("excluirrs")
            self.click()
            #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirrs")
            #self.click()
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---CADASTRO DE ECF---####
                             
            if not self.find( "abrircadastros_abacadastro", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro")
            self.click()
            if not self.find( "pdv", matching=0.97, waiting_time=10000):
                self.not_found("pdv")
            self.click()
            if not self.find( "cadastrodeecf", matching=0.97, waiting_time=10000):
                self.not_found("cadastrodeecf")
            self.click()
            #if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
            #    self.not_found("localizarpaises")
            #self.click()            
            #if not self.find( "editarfim", matching=0.97, waiting_time=10000):
            #    self.not_found("editarfim")
            #self.click()
            #if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
            #    self.not_found("retornarpe")
            #self.click()
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()
            self.type_keys_with_interval(1,'8748')
            self.tab()
            x=0
            while x<7:
                self.type_keys_with_interval(1,'te12!@')
                self.tab()
                x=x+1
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'t1!')
            self.tab()
            self.type_keys_with_interval(1,'t1!')
            self.tab()
            self.type_keys_with_interval(1,'t1!')
            if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
                self.not_found("salvarrs")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "buscarcodteteste", matching=0.97, waiting_time=10000):
                self.not_found("buscarcodteteste")
            self.click_relative(12, 29)
            self.type_keys_with_interval(1,'te12')
            self.enter()
            if not self.find( "redesocialteste", matching=0.97, waiting_time=10000):
                self.not_found("redesocialteste")
            self.click()
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                self.not_found("excluirrs")
            self.click()
            #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirrs")
            #self.click()
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---DOCUMENTACOES---####
                             
            if not self.find( "abrircadastros_abacadastro", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro")
            self.click()
            if not self.find( "documentacoes", matching=0.97, waiting_time=10000):
                self.not_found("documentacoes")
            self.click()
            if not self.find( "tiposdedocumentos", matching=0.97, waiting_time=10000):
                self.not_found("tiposdedocumentos")
            self.click()
            #if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
            #    self.not_found("localizarpaises")
            #self.click()            
            #if not self.find( "editarfim", matching=0.97, waiting_time=10000):
            #    self.not_found("editarfim")
            #self.click()
            #if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
            #    self.not_found("retornarpe")
            #self.click()
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
                self.not_found("salvarrs")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "buscarcodteteste", matching=0.97, waiting_time=10000):
                self.not_found("buscarcodteteste")
            self.click_relative(12, 29)
            self.type_keys_with_interval(1,'te12')
            self.enter()
            if not self.find( "redesocialteste", matching=0.97, waiting_time=10000):
                self.not_found("redesocialteste")
            self.click()
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                self.not_found("excluirrs")
            self.click()
            #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirrs")
            #self.click()
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
            if not self.find( "abrircadastros_abacadastro", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro")
            self.click()
            if not self.find( "documentacoes", matching=0.97, waiting_time=10000):
                self.not_found("documentacoes")
            self.click()
            if not self.find( "documentos", matching=0.97, waiting_time=10000):
                self.not_found("documentos")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()            
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()
            if not self.find( "buscartipodocumento", matching=0.97, waiting_time=10000):
                self.not_found("buscartipodocumento")
            self.click_relative(152, 85)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.tab()
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            if not self.find( "buscarclientefornecCadDoc", matching=0.97, waiting_time=10000):
                self.not_found("buscarclientefornecCadDoc")
            self.click_relative(197, 160)
            self.enter()
            if not self.find( "cod0081260selecaocliente", matching=0.97, waiting_time=10000):
                self.not_found("cod0081260selecaocliente")
            self.click()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.tab()
            self.tab()
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "buscararquivoCadDoc", matching=0.97, waiting_time=10000):
                self.not_found("buscararquivoCadDoc")
            self.click_relative(630, 4)
            if not self.find( "abrirarquivoCadDoc", matching=0.97, waiting_time=10000):
                self.not_found("abrirarquivoCadDoc")
            self.click_relative(599, 441)
            if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
                self.not_found("salvarrs")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "buscarcodteteste", matching=0.97, waiting_time=10000):
                self.not_found("buscarcodteteste")
            self.click_relative(12, 29)
            self.type_keys_with_interval(1,'te12')
            self.enter()
            if not self.find( "redesocialteste", matching=0.97, waiting_time=10000):
                self.not_found("redesocialteste")
            self.click()
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                self.not_found("excluirrs")
            self.click()
            #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirrs")
            #self.click()
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
            if not self.find( "abrircadastros_abacadastro", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro")
            self.click()
            if not self.find( "documentacoes", matching=0.97, waiting_time=10000):
                self.not_found("documentacoes")
            self.click()
            if not self.find( "documentosreferenciados", matching=0.97, waiting_time=10000):
                self.not_found("documentosreferenciados")
            self.click()
            #if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
            #    self.not_found("localizarpaises")
            #self.click()            
            #if not self.find( "editarfim", matching=0.97, waiting_time=10000):
            #    self.not_found("editarfim")
            #self.click()
            #if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
            #    self.not_found("retornarpe")
            #self.click()
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()
            x=0
            while x<9:
                self.type_down()
                x=x+1
            if not self.find( "buscaobslancfiscal", matching=0.97, waiting_time=10000):
                self.not_found("buscaobslancfiscal")
            self.click_relative(154, 24)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.tab()
            self.type_down()
            if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
                self.not_found("salvarrs")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "buscarcodteteste", matching=0.97, waiting_time=10000):
                self.not_found("buscarcodteteste")
            self.click_relative(12, 29)
            self.type_keys_with_interval(1,'15')
            self.enter()
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                self.not_found("excluirrs")
            self.click()
            #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirrs")
            #self.click()
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            self.wait(1000)
            
            if not self.find( "abacompras", matching=0.97, waiting_time=10000):
                self.not_found("abacompras")
            self.click()
            if not self.find( "requisicoesdecompra", matching=0.97, waiting_time=10000):
                self.not_found("requisicoesdecompra")
            self.click()
            if not self.find( "periodorequisicoesdecompras", matching=0.97, waiting_time=10000):
                self.not_found("periodorequisicoesdecompras")
            self.click_relative(337, 111)
            if not self.find( "carregaranoreqcompras", matching=0.97, waiting_time=10000):
                self.not_found("carregaranoreqcompras")
            self.click()
            if not self.find( "anoanteriorreqcompras", matching=0.97, waiting_time=10000):
                self.not_found("anoanteriorreqcompras")
            self.click()            
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            self.tab()
            x=0
            while x<5:
                self.type_down()
                x=x+1
            self.tab()
            self.space()
            x=0
            while x<7:
                self.space()
                self.type_down()
                x=x+1  
            self.space()          
            x=0
            while x<7:
                self.space()
                self.type_up()
                x=x+1          
            self.tab()
            if not self.find( "usuariosolicitante", matching=0.97, waiting_time=10000):
                self.not_found("usuariosolicitante")
            self.click_relative(45, 25)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.tab()
            if not self.find( "usuarioautorizador", matching=0.97, waiting_time=10000):
                self.not_found("usuarioautorizador")
            self.click_relative(42, 23)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.tab()
            if not self.find( "reqcompraautorizado", matching=0.97, waiting_time=10000):
                self.not_found("reqcompraautorizado")
            self.click()
            if not self.find( "reqcompranautorizado", matching=0.97, waiting_time=10000):
                self.not_found("reqcompranautorizado")
            self.click()
            if not self.find( "reqcomprapendentes", matching=0.97, waiting_time=10000):
                self.not_found("reqcomprapendentes")
            self.click()
            if not self.find( "reqcomprascotando", matching=0.97, waiting_time=10000):
                self.not_found("reqcomprascotando")
            self.click()
            if not self.find( "reqcomprastodos", matching=0.97, waiting_time=10000):
                self.not_found("reqcomprastodos")
            self.click()
            
                            ####---SELEÇÃO ABA1---####
                             
            if not self.find( "abaselecao", matching=0.97, waiting_time=10000):
                self.not_found("abaselecao")
            self.click()
            if not self.find( "transacao", matching=0.97, waiting_time=10000):
                self.not_found("transacao")
            self.click_relative(10, 42)
            self.type_keys_with_interval(1,'te12!@')
            self.tab()
            self.space()
            self.space()
            self.tab()
            self.space()
            self.space()
            if not self.find( "buscarclassificacaoCC", matching=0.97, waiting_time=10000):
                self.not_found("buscarclassificacaoCC")
            self.click_relative(64, 40)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            if not self.find( "buscarcentrodecustosCC", matching=0.97, waiting_time=10000):
                self.not_found("buscarcentrodecustosCC")
            self.click_relative(85, 82)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            if not self.find( "buscarservicoCC", matching=0.97, waiting_time=10000):
                self.not_found("buscarservicoCC")
            self.click_relative(62, 123)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.enter()
            self.backspace()
            if not self.find( "buscarcompradorCC", matching=0.97, waiting_time=10000):
                self.not_found("buscarcompradorCC")
            self.click_relative(464, 43)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            if not self.find( "buscarcentrodecustosservicoCC", matching=0.97, waiting_time=10000):
                self.not_found("buscarcentrodecustosservicoCC")
            self.click_relative(486, 85)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            if not self.find( "buscarcondicaopagCC", matching=0.97, waiting_time=10000):
                self.not_found("buscarcondicaopagCC")
            self.click_relative(865, 40)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            if not self.find( "buscaritemCC", matching=0.97, waiting_time=10000):
                self.not_found("buscaritemCC")
            self.click_relative(867, 85)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            
            
            
            
                            ####---ABA1 REQCOMPRAS---####
            
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()
            self.tab()
            if not self.find( "solicitantereqcompras", matching=0.97, waiting_time=10000):
                self.not_found("solicitantereqcompras")           
            self.click_relative(54, 25)
                                   
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.tab()
            if not self.find( "solicitantereqcompras", matching=0.97, waiting_time=10000):
                self.not_found("solicitantereqcompras")
            self.click_relative(54, 25)
            self.tab()
            self.tab()
            self.tab()
            x=0
            while x<30:
                self.type_down()
                x=x+1
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.tab()
            self.tab()
            self.type_keys_with_interval(1,'te12!@')
            self.tab()
            self.type_keys_with_interval(1,'te12!@')
            self.tab()
            self.type_keys_with_interval(1,'te12!@')
            self.tab()
            
                            ####---ABA2 REQCOMPRAS---####
            
            if not self.find( "aba2reqcompras", matching=0.97, waiting_time=10000):
                self.not_found("aba2reqcompras")
            self.click()
            if not self.find( "addregistroaba2reqcompras", matching=0.97, waiting_time=10000):
                self.not_found("addregistroaba2reqcompras")
            self.click()            
            if not self.find( "buscaritensreqcompras", matching=0.97, waiting_time=10000):
                self.not_found("buscaritensreqcompras")
            self.click_relative(10, 31)
            self.type_keys_with_interval(1,'agulha gengival')
            self.enter()
            self.type_down()
            self.type_down()
            self.type_down()
            self.type_down()
            self.wait(500)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            """
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "quantidade_lancitens", matching=0.97, waiting_time=10000):
                self.not_found("quantidade_lancitens")
            self.click_relative(336, 280)
            self.backspace()
            self.enter()
            x=0
            while x<31:
                self.type_down()
                x=x+1
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            """
            self.type_keys_with_interval(1,'1')
            if not self.find( "botaoconfirmaritensreqcompras", matching=0.97, waiting_time=10000):
                self.not_found("botaoconfirmaritensreqcompras")
            self.click()
            self.wait(3000)
            
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---ABA3 REQCOMPRAS---####
                             
            if not self.find( "aba3servicosreqcompras", matching=0.97, waiting_time=10000):
                self.not_found("aba3servicosreqcompras")
            self.click()
            if not self.find( "addregistroaba2reqcompras", matching=0.97, waiting_time=10000):
                self.not_found("addregistroaba2reqcompras")
            self.click()
            if not self.find( "buscarservicoaba3reqcompras", matching=0.97, waiting_time=10000):
                self.not_found("buscarservicoaba3reqcompras")
            self.click_relative(62, 24)
            self.backspace()
            self.enter()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.enter()
            if not self.find( "buscarclassificacaoaba3reqcompras", matching=0.97, waiting_time=10000):
                self.not_found("buscarclassificacaoaba3reqcompras")
            self.click_relative(54, 22)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "buscarcentrodecustosreqcompras", matching=0.97, waiting_time=10000):
                self.not_found("buscarcentrodecustosreqcompras")
            self.click_relative(79, 24)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "obsaba3reqcompras", matching=0.97, waiting_time=10000):
                self.not_found("obsaba3reqcompras")
            self.click_relative(9, 20)
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "gravarregistroaba3", matching=0.97, waiting_time=10000):
                self.not_found("gravarregistroaba3")
            self.click()
            if not self.find( "cancelarregistroaba3", matching=0.97, waiting_time=10000):
                self.not_found("cancelarregistroaba3")
            self.click()
            
                            ####---ABA4 REQCOMPRAS---####
                             
            if not self.find( "aba4reqcompras", matching=0.97, waiting_time=10000):
                self.not_found("aba4reqcompras")
            self.click()
            if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
                self.not_found("salvarrs")
            self.click()
            
                            ####---BOTÕES NAS ABAS---####
                             
            if not self.find( "processos", matching=0.97, waiting_time=10000):
                self.not_found("processos")
            self.click_relative(74, -4)
            if not self.find( "anexardocumentos", matching=0.97, waiting_time=10000):
                self.not_found("anexardocumentos")
            self.click()
            if not self.find( "addarquivoanexo", matching=0.97, waiting_time=10000):
                self.not_found("addarquivoanexo")
            self.click_relative(5, 74)
            if not self.find( "abrirselecaodearquivos", matching=0.97, waiting_time=10000):
                self.not_found("abrirselecaodearquivos")
            self.click()
            if not self.find( "cancelaranexo", matching=0.97, waiting_time=10000):
                self.not_found("cancelaranexo")
            self.click_relative(599, 418)
            if not self.find( "cancelaranexodearquivos", matching=0.97, waiting_time=10000):
                self.not_found("cancelaranexodearquivos")
            self.click()
            if not self.find( "retornaranexoarquivos", matching=0.97, waiting_time=10000):
                self.not_found("retornaranexoarquivos")
            self.click_relative(23, 44)
            if not self.find( "email", matching=0.97, waiting_time=10000):
                self.not_found("email")
            self.click_relative(64, -3)
            if not self.find( "enviaremail", matching=0.97, waiting_time=10000):
                self.not_found("enviaremail")
            self.click()
            if not self.find( "retornaremail", matching=0.97, waiting_time=10000):
                self.not_found("retornaremail")
            self.click_relative(33, 49)
            self.wait(500)
            self.enter()
            if not self.find( "email", matching=0.97, waiting_time=10000):
                self.not_found("email")
            self.click_relative(64, -3)
            if not self.find( "editarpdfemail", matching=0.97, waiting_time=10000):
                self.not_found("editarpdfemail")
            self.click()
            if not self.find( "fechareditorrelatorio", matching=0.97, waiting_time=10000):
                self.not_found("fechareditorrelatorio")
            self.click_relative(1009, 11)
            if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                self.not_found("excluirrs")
            self.click()
            #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirrs")
            #self.click()
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---COTACOES DE COMPRA---####
                             
            if not self.find( "cotacoesdecompras", matching=0.97, waiting_time=10000):
                self.not_found("cotacoesdecompras")
            self.click()          
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()            
            self.enter()
            if not self.find( "periodorequisicoesdecompras", matching=0.97, waiting_time=10000):
                self.not_found("periodorequisicoesdecompras")
            self.double_click_relative(337, 111)
            self.tab()
            x=0
            while x<5:
                self.type_down()
                x=x+1
            self.tab()
            self.space()
            x=0
            while x<7:
                self.space()
                self.type_down()
                x=x+1  
            self.space()          
            x=0
            while x<7:
                self.space()
                self.type_up()
                x=x+1          
            self.tab()
            if not self.find( "usuariosolicitante", matching=0.97, waiting_time=10000):
                self.not_found("usuariosolicitante")
            self.click_relative(45, 25)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.tab()
            if not self.find( "usuarioautorizador", matching=0.97, waiting_time=10000):
                self.not_found("usuarioautorizador")
            self.click_relative(42, 23)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.tab()
            if not self.find( "buscarclientefornecedor", matching=0.97, waiting_time=10000):
                self.not_found("buscarclientefornecedor")
            self.click_relative(75, 24)
            self.enter()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.tab()
            
                            ####---SELECAO COTACAO---####
                             
            if not self.find( "abaselecao", matching=0.97, waiting_time=10000):
                self.not_found("abaselecao")
            self.click()
            if not self.find( "transacao", matching=0.97, waiting_time=10000):
                self.not_found("transacao")
            self.click_relative(10, 42)
            self.type_keys_with_interval(1,'te12!@')
            self.tab()
            self.space()
            self.space()
            self.tab()
            self.space()
            self.space()
            if not self.find( "buscarclassificacaoCC", matching=0.97, waiting_time=10000):
                self.not_found("buscarclassificacaoCC")
            self.click_relative(64, 40)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            if not self.find( "buscarcentrodecustosCC", matching=0.97, waiting_time=10000):
                self.not_found("buscarcentrodecustosCC")
            self.click_relative(85, 82)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            if not self.find( "buscarservicoCC", matching=0.97, waiting_time=10000):
                self.not_found("buscarservicoCC")
            self.click_relative(62, 123)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.enter()
            self.backspace()
            if not self.find( "buscarcompradorCC", matching=0.97, waiting_time=10000):
                self.not_found("buscarcompradorCC")
            self.click_relative(464, 43)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            if not self.find( "buscarcentrodecustosservicoCC", matching=0.97, waiting_time=10000):
                self.not_found("buscarcentrodecustosservicoCC")
            self.click_relative(486, 85)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            if not self.find( "buscarcondicaopagCC", matching=0.97, waiting_time=10000):
                self.not_found("buscarcondicaopagCC")
            self.click_relative(865, 40)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            if not self.find( "buscaritemCC", matching=0.97, waiting_time=10000):
                self.not_found("buscaritemCC")
            self.click_relative(867, 85)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            
                            ####---PEDIDOS DE COMPRA---####
                             
            if not self.find( "pedidosdecompras", matching=0.97, waiting_time=10000):
                self.not_found("pedidosdecompras")
            self.click_relative(174, 69)                                                     
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            self.enter()
            if not self.find( "periodorequisicoesdecompras", matching=0.97, waiting_time=10000):
                self.not_found("periodorequisicoesdecompras")
            self.double_click_relative(337, 111)
            self.tab()
            x=0
            while x<5:
                self.type_down()
                x=x+1
            self.tab()
            self.space()
            x=0
            while x<6:
                self.space()
                self.type_down()
                x=x+1  
            self.space()          
            x=0
            while x<6:
                self.space()
                self.type_up()
                x=x+1          
            self.tab()
            if not self.find( "usuariosolicitante", matching=0.97, waiting_time=10000):
                self.not_found("usuariosolicitante")
            self.click_relative(45, 25)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.tab()
            if not self.find( "usuarioautorizador", matching=0.97, waiting_time=10000):
                self.not_found("usuarioautorizador")
            self.click_relative(42, 23)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.tab()
            if not self.find( "buscarclientefornecedor", matching=0.97, waiting_time=10000):
                self.not_found("buscarclientefornecedor")
            self.click_relative(75, 24)
            self.enter()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.tab()
            
                            ####---SELEÇÃO PEDIDOS COMPRA---####
            """                 
            if not self.find( "abaselecao", matching=0.97, waiting_time=10000):
                self.not_found("abaselecao")
            self.click()
            if not self.find( "transacao", matching=0.97, waiting_time=10000):
                self.not_found("transacao")
            self.click_relative(10, 42)
            self.type_keys_with_interval(1,'te12!@')
            #if not self.find( "selecaoparcialpedidos", matching=0.97, waiting_time=10000):
            #    self.not_found("selecaoparcialpedidos")
            #self.click()
            #if not self.find( "selecaonenhumpedidos", matching=0.97, waiting_time=10000):
            #    self.not_found("selecaonenhumpedidos")
            #self.click()
            #if not self.find( "selecaotodospedidos", matching=0.97, waiting_time=10000):
            #    self.not_found("selecaotodospedidos")
            #self.click_relative(7, 25)            
            self.tab()
            self.space()
            self.space()
            self.tab()
            self.space()
            self.space()
            #codigo de operacao
            if not self.find( "buscarclassificacaoCC", matching=0.97, waiting_time=10000):
                self.not_found("buscarclassificacaoCC")
            self.click_relative(64, 40)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            #condicao de pagamento
            if not self.find( "condicaodepagamentopedidos", matching=0.97, waiting_time=10000):
                self.not_found("condicaodepagamentopedidos")
            self.click_relative(61, 83)
            
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            #centro de custos serviços
            if not self.find( "centrodecustospedidos", matching=0.97, waiting_time=10000):
                self.not_found("centrodecustospedidos")
            self.click_relative(85, 125)            
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            #classificacao
            if not self.find( "buscarcompradorCC", matching=0.97, waiting_time=10000):
                self.not_found("buscarcompradorCC")
            self.click_relative(464, 43)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            #transportador
            if not self.find( "buscartransportadorpedidos", matching=0.97, waiting_time=10000):
                self.not_found("buscartransportadorpedidos")
            self.click_relative(464, 82)
            self.enter() 
            self.type_down()
            self.type_down()           
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            #comprador
            if not self.find( "buscarcondicaopagCC", matching=0.97, waiting_time=10000):
                self.not_found("buscarcondicaopagCC")
            self.click_relative(865, 40)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            #centro de custos
            if not self.find( "buscarcentrodecustospedidoscompras", matching=0.97, waiting_time=10000):
                self.not_found("buscarcentrodecustospedidoscompras")
            self.click_relative(886, 84)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            #item
            if not self.find( "buscaritempedidos", matching=0.97, waiting_time=10000):
                self.not_found("buscaritempedidos")
            self.click_relative(464, 122)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            #servico
            if not self.find( "buscarservicopedidos", matching=0.97, waiting_time=10000):
                self.not_found("buscarservicopedidos")
            self.click_relative(864, 124)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.enter()
            self.backspace()
            """
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---PRÉ COMPRA---####
                             
            if not self.find( "abacompras", matching=0.97, waiting_time=10000):
                self.not_found("abacompras")
            self.click()
            if not self.find( "precompra", matching=0.97, waiting_time=10000):
                self.not_found("precompra")
            self.click()
            if not self.find( "2selecao", matching=0.97, waiting_time=10000):
                self.not_found("2selecao")
            self.click()
            if not self.find( "abaitens", matching=0.97, waiting_time=10000):
                self.not_found("abaitens")
            self.click()            
            if not self.find( "filtro", matching=0.97, waiting_time=10000):
                self.not_found("filtro")
            self.click()
            if not self.find( "retornarfiltragem", matching=0.97, waiting_time=10000):
                self.not_found("retornarfiltragem")
            self.click_relative(39, 51)
            if not self.find( "addregistroprecompra", matching=0.97, waiting_time=10000):
                self.not_found("addregistroprecompra")
            self.click()
            if not self.find( "buscaritensreqcompras", matching=0.97, waiting_time=10000):
                self.not_found("buscaritensreqcompras")
            self.click_relative(10, 31)
            self.type_keys_with_interval(1,'agulha gengival')
            self.enter()
            self.type_down()
            self.type_down()
            self.type_down()
            self.type_down()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(1500)
            if not self.find( "botaoconfirmaritensreqcompras", matching=0.97, waiting_time=10000):
                self.not_found("botaoconfirmaritensreqcompras")
            self.click()
            self.wait(3000)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            #if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
            #    self.not_found("selecionarmunicipiovcr")
            #self.click()
            #if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
            #    self.not_found("retornarpe")
            #self.click()
            if not self.find( "abcdemanda", matching=0.97, waiting_time=10000):
                self.not_found("abcdemanda")
            self.click()
            if not self.find( "retornargeracaocurvas", matching=0.97, waiting_time=10000):
                self.not_found("retornargeracaocurvas")
            self.click_relative(32, 45)
            if not self.find( "geracao", matching=0.97, waiting_time=10000):
                self.not_found("geracao")
            self.click_relative(63, -2)
            """
            if not self.find( "requisicaodecompras", matching=0.97, waiting_time=10000):
                self.not_found("requisicaodecompras")
            self.click()
            self.enter()
            if not self.find( "geracao", matching=0.97, waiting_time=10000):
                self.not_found("geracao")
            self.click_relative(63, -2)
            if not self.find( "cotacaodecompra", matching=0.97, waiting_time=10000):
                self.not_found("cotacaodecompra")
            self.click()
            self.enter()
            if not self.find( "geracao", matching=0.97, waiting_time=10000):
                self.not_found("geracao")
            self.click_relative(63, -2)
            
            if not self.find( "gerarpedidodecompraprecompra", matching=0.97, waiting_time=10000):
                self.not_found("gerarpedidodecompraprecompra")
            self.click()
            if not self.find( "buscarfornecedorgp", matching=0.97, waiting_time=10000):
                self.not_found("buscarfornecedorgp")
            self.click_relative(196, 40)
            self.wait(1000)
            self.type_keys_with_interval(1,'0081260')
            self.enter()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "buscaroperacao", matching=0.97, waiting_time=10000):
                self.not_found("buscaroperacao")
            self.click_relative(65, 240)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "buscarcondicaodepagamentogp", matching=0.97, waiting_time=10000):
                self.not_found("buscarcondicaodepagamentogp")
            self.click_relative(65, 272)
            if not self.find( "buscarcompradorgp", matching=0.97, waiting_time=10000):
                self.not_found("buscarcompradorgp")
            self.click_relative(488, 241)
            if not self.find( "cancelarfornecedorgeracaodopedido", matching=0.97, waiting_time=10000):
                self.not_found("cancelarfornecedorgeracaodopedido")
            self.click()
            self.enter()
            """
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---CONSULTA STATUS SOLICITACAO---####
                             
            if not self.find( "abacompras", matching=0.97, waiting_time=10000):
                self.not_found("abacompras")
            self.click()
            if not self.find( "consultastatussolicitacao", matching=0.97, waiting_time=10000):
                self.not_found("consultastatussolicitacao")
            self.click()
            if not self.find( "buscaritemCSM", matching=0.97, waiting_time=10000):
                self.not_found("buscaritemCSM")
            self.click_relative(78, 36)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "solicitanteCSM", matching=0.97, waiting_time=10000):
                self.not_found("solicitanteCSM")
            self.click_relative(184, 31)
            self.enter()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---ACORDO COMERCIAL---####
                             
            if not self.find( "abacompras", matching=0.97, waiting_time=10000):
                self.not_found("abacompras")
            self.click()
            if not self.find( "acordocomercial", matching=0.97, waiting_time=10000):
                self.not_found("acordocomercial")
            self.click()
            if not self.find( "acordocomercial2", matching=0.97, waiting_time=10000):
                self.not_found("acordocomercial2")
            self.click()
            self.backspace()
            self.enter()
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()
            if not self.find( "buscarfornecedorCAcordos", matching=0.97, waiting_time=10000):
                self.not_found("buscarfornecedorCAcordos")
            self.click_relative(131, 6)
            self.tab()
            self.type_keys_with_interval(1,'te12!@')
            self.tab()
            self.tab()
            self.type_keys_with_interval(1,'81260')
            self.tab()
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            x=0
            while x<3:
                self.type_down()
                x=x+1
            self.tab()
            self.type_keys_with_interval(1,'123')
            if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
                self.not_found("salvarrs")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                self.not_found("excluirrs")
            self.click()
            #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirrs")
            #self.click()
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---CONTA CORRENTE FORNECEDORES---####
                             
            if not self.find( "abacompras", matching=0.97, waiting_time=10000):
                self.not_found("abacompras")
            self.click()
            if not self.find( "acordocomercial", matching=0.97, waiting_time=10000):
                self.not_found("acordocomercial")
            self.click()
            if not self.find( "contacorrendefornecedores", matching=0.97, waiting_time=10000):
                self.not_found("contacorrendefornecedores")
            self.click()
            self.enter()            
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---VENDAS---####
                             
            if not self.find( "vendas", matching=0.97, waiting_time=10000):
                self.not_found("vendas")
            self.click()
            if not self.find( "orcamentos", matching=0.97, waiting_time=10000):
                self.not_found("orcamentos")
            self.click()        
            self.wait(1500)
            self.enter()
            if not self.find( "clientesMV", matching=0.97, waiting_time=10000):
                self.not_found("clientesMV")
            self.click_relative(535, 90)
            if not self.find( "buscarclienteprincipalMV", matching=0.97, waiting_time=10000):
                self.not_found("buscarclienteprincipalMV")
            self.click_relative(526, 113)
            self.wait(500)
            self.type_keys_with_interval(1,'0081260')
            self.enter()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.tab()
            if not self.find( "sistemaorigemMV", matching=0.97, waiting_time=10000):
                self.not_found("sistemaorigemMV")
            self.click_relative(600, 92)
            x=0
            while x<15:
                self.type_down()
                x=x+1
            x=0
            while x<15:
                self.type_up()
                x=x+1
            self.tab()
            x=0
            while x<6:
                self.type_down()
                x=x+1
            x=0
            while x<6:
                self.type_up()
                x=x+1
            self.tab()
            self.space()
            x=0
            while x<12:
                self.type_down()
                self.space()
                x=x+1
            self.space()
            x=0
            while x<12:
                self.type_up()
                self.space()
                x=x+1
            if not self.find( "selecaoMV", matching=0.97, waiting_time=10000):
                self.not_found("selecaoMV")
            self.click()
            if not self.find( "transacaoselecaoMV", matching=0.97, waiting_time=10000):
                self.not_found("transacaoselecaoMV")
            self.click_relative(7, 44)
            self.type_keys_with_interval(1,'t1!')
            self.backspace()
            self.backspace()
            self.backspace()
            self.tab()
            x=0
            while x<5:
                self.type_keys_with_interval(1,'874')
                self.backspace()
                self.backspace()
                self.backspace()
                self.tab()
                x=x+1
            self.space()
            self.space()
            self.tab()
            x=0
            while x<4:
                self.type_keys_with_interval(1,'874')
                self.backspace()
                self.backspace()
                self.backspace()
                self.tab()
                x=x+1
            x=0
            while x<3:
                self.type_keys_with_interval(1,'te12@!')
                self.backspace()
                self.backspace()
                self.backspace()
                self.backspace()
                self.backspace()
                self.backspace()
                self.tab()
                x=x+1
            if not self.find( "buscarclassMV", matching=0.97, waiting_time=10000):
                self.not_found("buscarclassMV")
            self.click_relative(63, 42)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            if not self.find( "buscarrotaMV", matching=0.97, waiting_time=10000):
                self.not_found("buscarrotaMV")
            self.click_relative(65, 83)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            if not self.find( "buscarvendedorMV", matching=0.97, waiting_time=10000):
                self.not_found("buscarvendedorMV")
            self.click_relative(464, 41)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            if not self.find( "buscaritemMV", matching=0.97, waiting_time=10000):
                self.not_found("buscaritemMV")
            self.click_relative(463, 188)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            if not self.find( "buscarcondicaodepagamentoMV", matching=0.97, waiting_time=10000):
                self.not_found("buscarcondicaodepagamentoMV")
            self.click_relative(865, 44)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            if not self.find( "selecionarstatusMV", matching=0.97, waiting_time=10000):
                self.not_found("selecionarstatusMV")
            self.click_relative(1178, 78)
            self.type_down()
            self.enter()
            self.wait(500)
            if not self.find( "selecionarstatusMV", matching=0.97, waiting_time=10000):
                self.not_found("selecionarstatusMV")
            self.click_relative(1178, 78)
            self.backspace()
            if not self.find( "selecao2orcamentos", matching=0.97, waiting_time=10000):
                self.not_found("selecao2orcamentos")
            self.click()
            if not self.find( "buscartransportadorMV", matching=0.97, waiting_time=10000):
                self.not_found("buscartransportadorMV")
            self.click_relative(63, 83)
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            self.wait(2500)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "selecionartransportadorMV", matching=0.97, waiting_time=10000):
                self.not_found("selecionartransportadorMV")
            self.double_click_relative(42, 83)           
            self.backspace()
            
                            ####---INCLUIR ORCAMENTO---####
                              
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()
            if not self.find( "b_codigoop_Orc", matching=0.97, waiting_time=10000):
                self.not_found("b_codigoop_Orc")
            self.click_relative(70, 184)           
            self.backspace()
            self.enter()
            self.wait(1500)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(1500)
            if not self.find( "bstatusorcamento", matching=0.97, waiting_time=10000):
                self.not_found("bstatusorcamento")
            self.click_relative(357, 26)
            if not self.find( "selecionarstatusabertaeminclusao", matching=0.97, waiting_time=10000):
                self.not_found("selecionarstatusabertaeminclusao")
            self.click()            
            self.wait(1500)
            if not self.find( "bcpagorcamento", matching=0.97, waiting_time=10000):
                self.not_found("bcpagorcamento")
            self.click_relative(47, 28)
            self.backspace()
            self.enter()
            self.wait(1500)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(1500)
            if not self.find( "bclienteorcamento", matching=0.97, waiting_time=10000):
                self.not_found("bclienteorcamento")
            self.click_relative(193, 41)
            self.backspace()
            self.enter()
            self.wait(1500)
            self.type_down()
            self.wait(1500)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(1500)
            if not self.find( "bvendorcamento", matching=0.97, waiting_time=10000):
                self.not_found("bvendorcamento")
            self.click_relative(56, 27)
            self.wait(1500)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(1500)
            self.tab()
            self.tab()
            if not self.find( "brotaorcamento", matching=0.97, waiting_time=10000):
                self.not_found("brotaorcamento")
            self.click_relative(53, 27)
            self.wait(1500)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(1500)
            if not self.find( "bclassorcamento", matching=0.97, waiting_time=10000):
                self.not_found("bclassorcamento")
            self.click_relative(53, 24)
            self.wait(1500)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(1500)
            self.tab()
            self.tab()
            if not self.find( "bcimorcamento", matching=0.97, waiting_time=10000):
                self.not_found("bcimorcamento")
            self.click_relative(62, 26)
            self.enter()
            self.wait(5000)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(1500)
            x=0
            while x<15:
                if not self.find( "integracaoloop", matching=0.97, waiting_time=10000):
                    self.not_found("integracaoloop")
                self.click_relative(89, 25)
                self.type_down()
                self.enter()
                x=x+1
            self.type_keys_with_interval(1,'te12!@')
            self.tab()
            self.type_keys_with_interval(1,'te12!@')
            self.tab()
            self.tab()
            self.type_keys_with_interval(1,'te12!@')
            self.tab()
            
            if not self.find( "aba1p2inclusaoorcamento", matching=0.97, waiting_time=10000):
                self.not_found("aba1p2inclusaoorcamento")
            self.click()
            if not self.find( "brecebimentoacordado", matching=0.97, waiting_time=10000):
                self.not_found("brecebimentoacordado")
            self.click_relative(50, 25)
            self.wait(1500)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(1500)
            if not self.find( "bpessoacontado", matching=0.97, waiting_time=10000):
                self.not_found("bpessoacontado")
            self.click_relative(63, 25)
            self.wait(1500)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "btransportador", matching=0.97, waiting_time=10000):
                self.not_found("btransportador")
            self.click_relative(196, 45)
            self.enter()
            self.wait(2500)
            self.type_down()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(1500)
            if not self.find( "fretepcontaloop", matching=0.97, waiting_time=10000):
                self.not_found("fretepcontaloop")
            self.click_relative(263, 43)
            self.type_up()
            self.enter()
            x=0
            while x<5:
                if not self.find( "fretepcontaloop", matching=0.97, waiting_time=10000):
                    self.not_found("fretepcontaloop")
                self.click_relative(263, 43)
                self.type_down()
                self.enter()
                x=x+1
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'t1!')
            self.tab()
            self.type_keys_with_interval(1,'t1!')
            self.tab()
            self.type_keys_with_interval(1,'t1!')
            self.tab()
            self.type_keys_with_interval(1,'123')
            
            if not self.find( "aba2inclusaoorcamento", matching=0.97, waiting_time=10000):
                self.not_found("aba2inclusaoorcamento")
            self.click()
            if not self.find( "addregistroaba2reqcompras", matching=0.97, waiting_time=10000):
                self.not_found("addregistroaba2reqcompras")
            self.click()
            if not self.find( "buscaritensreqcompras", matching=0.97, waiting_time=10000):
                self.not_found("buscaritensreqcompras")
            self.click_relative(10, 31)
            self.type_keys_with_interval(1,'agulha gengival')
            self.enter()
            self.type_down()
            self.type_down()
            self.type_down()
            self.type_down()
            self.wait(500)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            """
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "quantidade_lancitens", matching=0.97, waiting_time=10000):
                self.not_found("quantidade_lancitens")
            self.click_relative(336, 280)
            self.backspace()
            self.enter()
            x=0
            while x<31:
                self.type_down()
                x=x+1
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            """
            if not self.find( "quantidadeitens_teste", matching=0.97, waiting_time=10000):
                self.not_found("quantidadeitens_teste")
            self.click_relative(105, 218)
            self.type_keys_with_interval(1,'1')
            if not self.find( "botaoconfirmaritensreqcompras", matching=0.97, waiting_time=10000):
                self.not_found("botaoconfirmaritensreqcompras")
            self.click()
            self.wait(3000)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            #if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
            #    self.not_found("retornarpe")
            #self.click()
            
            if not self.find( "a2p2incluirorcamento", matching=0.97, waiting_time=10000):
                self.not_found("a2p2incluirorcamento")
            self.click()
            if not self.find( "addregistroaba2reqcompras", matching=0.97, waiting_time=10000):
                self.not_found("addregistroaba2reqcompras")
            self.click()
            if not self.find( "bservicoa2p2orc", matching=0.97, waiting_time=10000):
                self.not_found("bservicoa2p2orc")
            self.click_relative(28, 50)
            self.wait(1500)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(1500)
            if not self.find( "bclassa2p2orc", matching=0.97, waiting_time=10000):
                self.not_found("bclassa2p2orc")
            self.click_relative(24, 87)
            self.enter()
            self.wait(1500)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(1500)
            if not self.find( "bcentrocustoa2p2orc", matching=0.97, waiting_time=10000):
                self.not_found("bcentrocustoa2p2orc")
            self.click_relative(968, 51)
            self.enter()
            self.wait(1500)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(1500)
            if not self.find( "valorunitarioa2p2orc", matching=0.97, waiting_time=10000):
                self.not_found("valorunitarioa2p2orc")
            self.click_relative(679, 50)
            self.type_keys_with_interval(1,'123')
            self.tab()
            if not self.find( "gravarregistroaba3", matching=0.97, waiting_time=10000):
                self.not_found("gravarregistroaba3")
            self.click()
            if not self.find( "cancelarregistroaba3", matching=0.97, waiting_time=10000):
                self.not_found("cancelarregistroaba3")
            self.click()
            if not self.find( "excluirservicoorcamentoa2p2", matching=0.97, waiting_time=10000):
                self.not_found("excluirservicoorcamentoa2p2")
            self.click_relative(-57, 56)
            #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirrs")
            #self.click()
            self.enter()
            if not self.find( "aba3inclusaoorcamento", matching=0.97, waiting_time=10000):
                self.not_found("aba3inclusaoorcamento")
            self.click()
            if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
                self.not_found("salvarrs")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                self.not_found("excluirrs")
            self.click()
            #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirrs")
            #self.click()
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            
                            ####---INCLUIR PEDIDOS DE VENDA---####
            """                 
            if not self.find( "aba1pedidosdevendainclusao", matching=0.97, waiting_time=10000):
                self.not_found("aba1pedidosdevendainclusao")
            self.click()                            
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()
            if not self.find( "bcoporcamento", matching=0.97, waiting_time=10000):
                self.not_found("bcoporcamento")
            self.click_relative(54, 26)
            self.backspace()
            self.enter()
            self.wait(500)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "bstatusorcamento", matching=0.97, waiting_time=10000):
                self.not_found("bstatusorcamento")
            self.click_relative(357, 26)
            if not self.find( "selecionarstatusabertaeminclusao", matching=0.97, waiting_time=10000):
                self.not_found("selecionarstatusabertaeminclusao")
            self.click()            
            self.wait(500)
            if not self.find( "bcpagorcamento", matching=0.97, waiting_time=10000):
                self.not_found("bcpagorcamento")
            self.click_relative(47, 28)
            self.backspace()
            self.enter()
            self.wait(500)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "bclienteorcamento", matching=0.97, waiting_time=10000):
                self.not_found("bclienteorcamento")
            self.click_relative(193, 41)
            self.backspace()
            self.enter()
            self.type_down()
            self.wait(500)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "bvendorcamento", matching=0.97, waiting_time=10000):
                self.not_found("bvendorcamento")
            self.click_relative(56, 27)
            self.wait(500)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.tab()
            self.tab()
            if not self.find( "brotaorcamento", matching=0.97, waiting_time=10000):
                self.not_found("brotaorcamento")
            self.click_relative(53, 27)
            self.wait(500)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "bclassorcamento", matching=0.97, waiting_time=10000):
                self.not_found("bclassorcamento")
            self.click_relative(53, 24)
            self.wait(500)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.tab()
            self.tab()
            if not self.find( "bcimorcamento", matching=0.97, waiting_time=10000):
                self.not_found("bcimorcamento")
            self.click_relative(62, 26)
            self.enter()
            self.wait(3500)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            x=0
            while x<15:
                if not self.find( "integracaoloop", matching=0.97, waiting_time=10000):
                    self.not_found("integracaoloop")
                self.click_relative(89, 25)
                self.type_down()
                self.enter()
                x=x+1
            self.type_keys_with_interval(1,'te12!@')
            self.tab()
            self.type_keys_with_interval(1,'te12!@')
            self.tab()
            self.type_keys_with_interval(1,'te12!@')
            self.tab()
            
            if not self.find( "aba1p2inclusaoorcamento", matching=0.97, waiting_time=10000):
                self.not_found("aba1p2inclusaoorcamento")
            self.click()
            if not self.find( "brecebimentoacordado", matching=0.97, waiting_time=10000):
                self.not_found("brecebimentoacordado")
            self.click_relative(50, 25)
            self.wait(500)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "bpessoacontado", matching=0.97, waiting_time=10000):
                self.not_found("bpessoacontado")
            self.click_relative(63, 25)
            self.wait(500)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "btransportador", matching=0.97, waiting_time=10000):
                self.not_found("btransportador")
            self.click_relative(196, 45)
            self.enter()
            self.wait(5000)
            self.type_down()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "fretepcontaloop", matching=0.97, waiting_time=10000):
                self.not_found("fretepcontaloop")
            self.click_relative(263, 43)
            self.type_up()
            self.enter()
            x=0
            while x<5:
                if not self.find( "fretepcontaloop", matching=0.97, waiting_time=10000):
                    self.not_found("fretepcontaloop")
                self.click_relative(263, 43)
                self.type_down()
                self.enter()
                x=x+1
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'t1!')
            self.tab()
            self.type_keys_with_interval(1,'t1!')
            self.tab()
            self.type_keys_with_interval(1,'t1!')
            self.tab()
            self.type_keys_with_interval(1,'123')
            
            if not self.find( "aba2inclusaoorcamento", matching=0.97, waiting_time=10000):
                self.not_found("aba2inclusaoorcamento")
            self.click()
            if not self.find( "addregistroaba2reqcompras", matching=0.97, waiting_time=10000):
                self.not_found("addregistroaba2reqcompras")
            self.click()
            
            if not self.find( "buscaritensreqcompras", matching=0.97, waiting_time=10000):
                self.not_found("buscaritensreqcompras")
            self.click_relative(10, 31)
            self.type_keys_with_interval(1,'104455')
            self.enter()
            self.wait(500)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.type_keys_with_interval(1,'1')
            if not self.find( "botaoconfirmaritensreqcompras", matching=0.97, waiting_time=10000):
                self.not_found("botaoconfirmaritensreqcompras")
            self.click()
            self.wait(3000)
            self.type_right()
            self.enter()
            self.wait(1000)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
            if not self.find( "a2p2incluirorcamento", matching=0.97, waiting_time=10000):
                self.not_found("a2p2incluirorcamento")
            self.click()
            if not self.find( "addregistroaba2reqcompras", matching=0.97, waiting_time=10000):
                self.not_found("addregistroaba2reqcompras")
            self.click()
            if not self.find( "bservicoa2p2orc", matching=0.97, waiting_time=10000):
                self.not_found("bservicoa2p2orc")
            self.click_relative(28, 50)
            self.wait(500)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.enter()
            if not self.find( "bclassa2p2orc", matching=0.97, waiting_time=10000):
                self.not_found("bclassa2p2orc")
            self.click_relative(24, 87)
            self.enter()
            self.wait(500)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "bcentrocustoa2p2orc", matching=0.97, waiting_time=10000):
                self.not_found("bcentrocustoa2p2orc")
            self.click_relative(968, 51)
            self.enter()
            self.wait(500)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "valorunitarioa2p2orc", matching=0.97, waiting_time=10000):
                self.not_found("valorunitarioa2p2orc")
            self.click_relative(679, 50)
            self.type_keys_with_interval(1,'123')
            self.tab()
            if not self.find( "gravarregistroaba3", matching=0.97, waiting_time=10000):
                self.not_found("gravarregistroaba3")
            self.click()
            self.enter()
            if not self.find( "cancelarregistroaba3", matching=0.97, waiting_time=10000):
                self.not_found("cancelarregistroaba3")
            self.click()
            if not self.find( "excluirregistroPVa2p2", matching=0.97, waiting_time=10000):
                self.not_found("excluirregistroPVa2p2")
            self.click_relative(-58, 58)
            self.enter()           
            #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirrs")
            #self.click()
            
            
            if not self.find( "aba3inclusaoorcamento", matching=0.97, waiting_time=10000):
                self.not_found("aba3inclusaoorcamento")
            self.click()
            if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
                self.not_found("salvarrs")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                self.not_found("excluirrs")
            self.click()
            if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                self.not_found("simexcluirrs")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            
                            ####---INCLUIR VENDAS BALCAO---####
            
            if not self.find( "aba3inclusaoMV", matching=0.97, waiting_time=10000):
                self.not_found("aba3inclusaoMV")
            self.click()
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()    
            self.enter()
            
                            ####---INCLUIR CONDICIONAIS---####
                             
            if not self.find( "aba4condicionaisMV", matching=0.97, waiting_time=10000):
                self.not_found("aba4condicionaisMV")
            self.click()
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()    
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---INCLUIR TRANSFERENCIAS---####
                             
            if not self.find( "aba6transferenciasinclusaoMV", matching=0.97, waiting_time=10000):
                self.not_found("aba6transferenciasinclusaoMV")
            self.click()
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()    
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            """
                            ####---INCLUIR AMOSTRA---####
            """              
            if not self.find( "aba7amostraMV", matching=0.97, waiting_time=10000):
                self.not_found("aba7amostraMV")
            self.click()
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()
            if not self.find( "bcoporcamento", matching=0.97, waiting_time=10000):
                self.not_found("bcoporcamento")
            self.click_relative(54, 26)
            self.backspace()
            self.enter()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "bstatusorcamento", matching=0.97, waiting_time=10000):
                self.not_found("bstatusorcamento")
            self.click_relative(357, 26)
            if not self.find( "selecionarstatusabertaeminclusao", matching=0.97, waiting_time=10000):
                self.not_found("selecionarstatusabertaeminclusao")
            self.click()            
            self.wait(500)
            if not self.find( "bcpagorcamento", matching=0.97, waiting_time=10000):
                self.not_found("bcpagorcamento")
            self.click_relative(47, 28)
            self.backspace()
            self.enter()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "bclienteorcamento", matching=0.97, waiting_time=10000):
                self.not_found("bclienteorcamento")
            self.click_relative(193, 41)
            self.backspace()
            self.enter()
            self.type_down()
            self.wait(500)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "bvendorcamento", matching=0.97, waiting_time=10000):
                self.not_found("bvendorcamento")
            self.click_relative(56, 27)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.tab()
            self.tab()
            if not self.find( "brotaorcamento", matching=0.97, waiting_time=10000):
                self.not_found("brotaorcamento")
            self.click_relative(53, 27)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "bclassorcamento", matching=0.97, waiting_time=10000):
                self.not_found("bclassorcamento")
            self.click_relative(53, 24)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.tab()
            self.tab()
            if not self.find( "bcimorcamento", matching=0.97, waiting_time=10000):
                self.not_found("bcimorcamento")
            self.click_relative(62, 26)
            self.enter()
            self.wait(3500)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            x=0
            while x<15:
                if not self.find( "integracaoloop", matching=0.97, waiting_time=10000):
                    self.not_found("integracaoloop")
                self.click_relative(89, 25)
                self.type_down()
                self.enter()
                x=x+1
            self.type_keys_with_interval(1,'te12!@')
            self.tab()
            self.type_keys_with_interval(1,'te12!@')
            self.tab()
            self.type_keys_with_interval(1,'te12!@')
            self.tab()
            
            if not self.find( "aba1p2inclusaoorcamento", matching=0.97, waiting_time=10000):
                self.not_found("aba1p2inclusaoorcamento")
            self.click()
            if not self.find( "brecebimentoacordado", matching=0.97, waiting_time=10000):
                self.not_found("brecebimentoacordado")
            self.click_relative(50, 25)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "bpessoacontado", matching=0.97, waiting_time=10000):
                self.not_found("bpessoacontado")
            self.click_relative(63, 25)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "btransportador", matching=0.97, waiting_time=10000):
                self.not_found("btransportador")
            self.click_relative(196, 45)
            self.enter()
            self.wait(2500)
            self.type_down()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "fretepcontaloop", matching=0.97, waiting_time=10000):
                self.not_found("fretepcontaloop")
            self.click_relative(263, 43)
            self.type_up()
            self.enter()
            x=0
            while x<5:
                if not self.find( "fretepcontaloop", matching=0.97, waiting_time=10000):
                    self.not_found("fretepcontaloop")
                self.click_relative(263, 43)
                self.type_down()
                self.enter()
                x=x+1
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'t1!')
            self.tab()
            self.type_keys_with_interval(1,'t1!')
            self.tab()
            self.type_keys_with_interval(1,'t1!')
            self.tab()
            self.type_keys_with_interval(1,'123')
            
            if not self.find( "aba2inclusaoorcamento", matching=0.97, waiting_time=10000):
                self.not_found("aba2inclusaoorcamento")
            self.click()
            if not self.find( "addregistroaba2reqcompras", matching=0.97, waiting_time=10000):
                self.not_found("addregistroaba2reqcompras")
            self.click()
            if not self.find( "buscaritensreqcompras", matching=0.97, waiting_time=10000):
                self.not_found("buscaritensreqcompras")
            self.click_relative(10, 31)
            self.type_keys_with_interval(1,'104455')
            self.enter()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.type_keys_with_interval(1,'1')
            if not self.find( "botaoconfirmaritensreqcompras", matching=0.97, waiting_time=10000):
                self.not_found("botaoconfirmaritensreqcompras")
            self.click()
            self.wait(3000)
            self.type_right()
            self.enter()
            self.wait(1000)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
            if not self.find( "a2p2incluirorcamento", matching=0.97, waiting_time=10000):
                self.not_found("a2p2incluirorcamento")
            self.click()
            if not self.find( "addregistroaba2reqcompras", matching=0.97, waiting_time=10000):
                self.not_found("addregistroaba2reqcompras")
            self.click()
            if not self.find( "bservicoa2p2orc", matching=0.97, waiting_time=10000):
                self.not_found("bservicoa2p2orc")
            self.click_relative(28, 50)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "bclassa2p2orc", matching=0.97, waiting_time=10000):
                self.not_found("bclassa2p2orc")
            self.click_relative(24, 87)
            self.enter()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "bcentrocustoa2p2orc", matching=0.97, waiting_time=10000):
                self.not_found("bcentrocustoa2p2orc")
            self.click_relative(968, 51)
            self.enter()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "valorunitarioa2p2orc", matching=0.97, waiting_time=10000):
                self.not_found("valorunitarioa2p2orc")
            self.click_relative(679, 50)
            self.type_keys_with_interval(1,'123')
            self.tab()
            if not self.find( "gravarregistroaba3", matching=0.97, waiting_time=10000):
                self.not_found("gravarregistroaba3")
            self.click()
            if not self.find( "cancelarregistroaba3", matching=0.97, waiting_time=10000):
                self.not_found("cancelarregistroaba3")
            self.click()
            if not self.find( "excluirservicoamostraa2p2", matching=0.97, waiting_time=10000):
                self.not_found("excluirservicoamostraa2p2")
            self.click_relative(-56, 55)
            if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                self.not_found("simexcluirrs")
            self.click()
            
            if not self.find( "aba3inclusaoorcamento", matching=0.97, waiting_time=10000):
                self.not_found("aba3inclusaoorcamento")
            self.click()
            if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
                self.not_found("salvarrs")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                self.not_found("excluirrs")
            self.click()
            if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                self.not_found("simexcluirrs")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            """
                            ####---EMISSAO DE NOTA FISCAL---####
                            ####################################
            if not self.find( "vendas", matching=0.97, waiting_time=10000):
                self.not_found("vendas")
            self.click()
            if not self.find( "emissaonotafiscal", matching=0.97, waiting_time=10000):
                self.not_found("emissaonotafiscal")
            self.click()
            self.wait(3000)
            self.enter()
            if not self.find( "periodomovimentodenotas", matching=0.97, waiting_time=10000):
                self.not_found("periodomovimentodenotas")
            self.double_click_relative(323, 111)
            #if not self.find( "carregardiaMN", matching=0.97, waiting_time=10000):
            #    self.not_found("carregardiaMN")
            #self.click()
            #if not self.find( "carregardiaatualMN", matching=0.97, waiting_time=10000):
            #    self.not_found("carregardiaatualMN")
            #self.click()
            self.tab()
            self.type_up()
            x=0
            while x<3:
                self.type_down()
                x=x+1
            self.type_up()
            self.type_up()
            if not self.find( "clienteMN", matching=0.97, waiting_time=10000):
                self.not_found("clienteMN")
            self.click()
            if not self.find( "buscarclienteMN", matching=0.97, waiting_time=10000):
                self.not_found("buscarclienteMN")
            self.click_relative(537, 114)
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            self.wait(2500)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(2500)
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()
            
                            ####---INCLUSAO NOTA FISCAL---####
                             
            self.tab()
            self.type_keys_with_interval(1,'1')
            self.tab()
            x=0
            while x<6:
                self.tab()
                x=x+1
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            x=0
            while x<3:
                self.type_down()
                x=x+1
            x=0
            while x<3:
                self.type_up()
                x=x+1
            self.tab()
            self.type_up()
            x=0
            while x<4:
                self.type_down()
                x=x+1
            x=0
            while x<4:
                self.type_up()
                x=x+1
            self.tab()
            x=0
            while x<8:
                self.type_down()
                x=x+1
            x=0
            while x<8:
                self.type_up()
                x=x+1
            if not self.find( "b_cfopNF", matching=0.97, waiting_time=10000):
                self.not_found("b_cfopNF")
            self.click_relative(55, 24)
            self.backspace()
            self.type_keys_with_interval(1,'5.102')
            self.enter()
            self.wait(500)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "b_condicaopagamentoNF", matching=0.97, waiting_time=10000):
                self.not_found("b_condicaopagamentoNF")
            self.click_relative(42, 26)
            self.backspace()
            self.enter()
            self.wait(1500)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(3000)
            if not self.find( "b_localdeestoqueNF", matching=0.97, waiting_time=10000):
                self.not_found("b_localdeestoqueNF")
            self.click_relative(41, 26)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "b_clienteNF", matching=0.97, waiting_time=10000):
                self.not_found("b_clienteNF")
            self.click_relative(193, 39)
            self.backspace()
            self.type_keys_with_interval(1,'18')
            self.enter()
            self.wait(1500)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "b_vendedorNF", matching=0.97, waiting_time=10000):
                self.not_found("b_vendedorNF")
            self.click_relative(68, 26)
            self.enter()
            self.wait(500)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.tab()
            self.tab()
            if not self.find( "b_rotaNF", matching=0.97, waiting_time=10000):
                self.not_found("b_rotaNF")
            self.click_relative(65, 22)
            self.enter()
            self.wait(500)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "b_classificacaoNF", matching=0.97, waiting_time=10000):
                self.not_found("b_classificacaoNF")
            self.click_relative(64, 23)
            self.backspace()
            self.enter()
            self.wait(500)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.tab()
            self.tab()
            if not self.find( "b_CImarketplaceNF", matching=0.97, waiting_time=10000):
                self.not_found("b_CImarketplaceNF")
            self.click_relative(65, 25)
            self.enter()
            self.wait(1500)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.tab()
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'t1!')
            self.tab()
            self.type_keys_with_interval(1,'t1!')
            self.tab()    
            self.type_keys_with_interval(1,'t1!')
            self.tab()
            self.tab()
            self.type_keys_with_interval(1,'t1!')
            self.tab()
            self.type_keys_with_interval(1,'t1!')
            if not self.find( "a1p2NF", matching=0.97, waiting_time=10000):
                self.not_found("a1p2NF")
            self.click()
            if not self.find( "b_transportadorNF", matching=0.97, waiting_time=10000):
                self.not_found("b_transportadorNF")
            self.click_relative(197, 43)
            self.enter()
            self.wait(500)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "i_placaa1p2NF", matching=0.97, waiting_time=10000):
                self.not_found("i_placaa1p2NF")
            self.click_relative(2, 227)
            self.backspace()
            self.backspace()
            self.type_keys_with_interval(1,'abc1234')
            self.tab()
            self.type_keys_with_interval(1,'abc1234')
            self.tab()
            x=0
            while x<28:
                self.type_up()
                x=x+1
            self.tab()
            self.type_up()
            x=0
            while x<5:
                self.type_down()
                x=x+1
            x=0
            while x<5:
                self.type_up()
                x=x+1
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()    
            self.type_keys_with_interval(1,'t1!')
            self.tab()
            self.type_keys_with_interval(1,'t1!')
            self.tab()
            self.type_keys_with_interval(1,'t1!')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            
            
            if not self.find( "a1p3NF", matching=0.97, waiting_time=10000):
                self.not_found("a1p3NF")
            self.click()
            if not self.find( "a1p4NF", matching=0.97, waiting_time=10000):
                self.not_found("a1p4NF")
            self.click()
            
                            ####---ABA2 NOTA FISCAL---####
                             
            if not self.find( "a2NF", matching=0.97, waiting_time=10000):
                self.not_found("a2NF")
            self.click()
            if not self.find( "ir_a2p1NF", matching=0.97, waiting_time=10000):
                self.not_found("ir_a2p1NF")
            self.click()
            if not self.find( "buscaritensreqcompras", matching=0.97, waiting_time=10000):
                self.not_found("buscaritensreqcompras")
            self.click_relative(10, 31)
            self.type_keys_with_interval(1,'agulha gengival')
            self.enter()
            self.type_down()
            self.type_down()
            self.type_down()
            self.type_down()
            self.wait(500)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            """
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "quantidade_lancitens", matching=0.97, waiting_time=10000):
                self.not_found("quantidade_lancitens")
            self.click_relative(336, 280)
            self.backspace()
            self.enter()
            x=0
            while x<31:
                self.type_down()
                x=x+1
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            """
            self.type_keys_with_interval(1,'1')
            if not self.find( "botaoconfirmaritensreqcompras", matching=0.97, waiting_time=10000):
                self.not_found("botaoconfirmaritensreqcompras")
            self.click()
            self.wait(3000)
            if not self.find( "qntdmovimentarlotes", matching=0.97, waiting_time=10000):
                self.not_found("qntdmovimentarlotes")
            self.double_click_relative(121, 231)
            self.backspace()
            self.backspace()
            self.backspace()
            self.backspace()
            self.type_keys_with_interval(1,'1')
            self.tab()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(1500)
            self.tab()
            self.wait(500)
            self.type_keys_with_interval(1,'5206')
            self.wait(500)
            self.tab()
            self.tab()
            self.tab()
            self.tab()
            self.tab()
            self.type_keys_with_interval(1,'00184')
            x=0
            while x<13:
                self.tab()
                x=x+1
            x=0
            while x<6:
                self.type_down()
                x=x+1
            self.tab()
            x=0
            while x<21:
                self.type_down()
                x=x+1
            self.tab()
            x=0
            while x<4:
                self.type_down()
                x=x+1
            if not self.find( "valoripiiss", matching=0.97, waiting_time=10000):
                self.not_found("valoripiiss")
            self.click_relative(336, 41)
            self.tab()
            x=0
            while x<6:
                self.type_down()
                x=x+1
            self.tab()
            x=0
            while x<14:
                self.type_down()
                x=x+1
            if not self.find( "valorpisDII", matching=0.97, waiting_time=10000):
                self.not_found("valorpisDII")
            self.click_relative(338, 94)
            self.tab()
            x=0
            while x<6:
                self.type_down()
                x=x+1
            self.tab()
            x=0
            while x<35:
                self.type_down()
                x=x+1
            self.tab()
            self.tab()
            if not self.find( "valorcofinsDII", matching=0.97, waiting_time=10000):
                self.not_found("valorcofinsDII")
            self.click_relative(336, 148)
            self.tab()
            x=0
            while x<6:
                self.type_down()
                x=x+1
            self.tab()
            x=0
            while x<35:
                self.type_down()
                x=x+1
             
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            self.enter()
            self.wait(2000)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()           
            self.enter()  
            if not self.find( "a2p2NF", matching=0.97, waiting_time=10000):
                self.not_found("a2p2NF")
            self.click()
            if not self.find( "b_servicoa2p2NF", matching=0.97, waiting_time=10000):
                self.not_found("b_servicoa2p2NF")
            self.click_relative(101, 230)
            self.enter()
            self.wait(500)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            self.wait(500)
            self.tab()
            self.tab()
            self.type_keys_with_interval(1,'1')
            self.tab()
            self.type_keys_with_interval(1,'1')
            if not self.find( "b_classa2p2NF", matching=0.97, waiting_time=10000):
                self.not_found("b_classa2p2NF")
            self.click_relative(94, 267)
            self.enter()
            self.wait(500)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "b_centrocustosa2p2NF", matching=0.97, waiting_time=10000):
                self.not_found("b_centrocustosa2p2NF")
            self.click_relative(1038, 230)
            self.enter()
            self.wait(500)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "b_municipioa2p2NF", matching=0.97, waiting_time=10000):
                self.not_found("b_municipioa2p2NF")
            self.click_relative(459, 266)
            self.enter()
            self.wait(500)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "gravara2p2NF", matching=0.97, waiting_time=10000):
                self.not_found("gravara2p2NF")
            self.click_relative(1209, 270)
            self.enter()
            self.wait(2000)
            self.enter() 
            if not self.find( "salvardadosservicoimposto", matching=0.97, waiting_time=10000):
                self.not_found("salvardadosservicoimposto")
            self.click()            
            self.enter()
            #self.enter()
            #self.enter()
            #if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
            #    self.not_found("retornarpe")
            #self.click()
            if not self.find( "a2NF", matching=0.97, waiting_time=10000):
                self.not_found("a2NF")
            self.click()  
            if not self.find( "cancelara2p2NF", matching=0.97, waiting_time=10000):
                self.not_found("cancelara2p2NF")
            self.click()
            if not self.find( "apagara2p2NF", matching=0.97, waiting_time=10000):
                self.not_found("apagara2p2NF")
            self.click_relative(-57, 33)
            #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirrs")
            #self.click()
            self.enter()
            
            if not self.find( "aba3NF", matching=0.97, waiting_time=10000):
                self.not_found("aba3NF")
            self.click()
            if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
                self.not_found("salvarrs")
            self.click()
            self.wait(1500)
            self.enter()
            if not self.find( "aba3NF", matching=0.97, waiting_time=10000):
                self.not_found("aba3NF")
            self.click()
            self.enter()
            if not self.find( "ir_a2p1NF", matching=0.97, waiting_time=10000):
                self.not_found("ir_a2p1NF")
            self.click()            
            if not self.find( "retornarconsulta", matching=0.97, waiting_time=10000):
                self.not_found("retornarconsulta")
            self.click_relative(33, 44)
            self.wait(500)
            self.enter()            
            if not self.find( "finalizarNF", matching=0.97, waiting_time=10000):
                self.not_found("finalizarNF")
            self.click_relative(64, -4)
            self.wait(3000)
            if not self.find( "finalizarNFeimprimir", matching=0.97, waiting_time=10000):
                self.not_found("finalizarNFeimprimir")
            self.click()
            self.wait(3000)
            if not self.find( "quantidadeNFfinal", matching=0.97, waiting_time=10000):
                self.not_found("quantidadeNFfinal")
            self.click_relative(397, 466)
            self.type_keys_with_interval(1,'1')
            self.tab()
            if not self.find( "finalizarNF", matching=0.97, waiting_time=10000):
                self.not_found("finalizarNF")
            self.click()
            self.wait(500)
            if not self.find( "b_localcobrancaparcela", matching=0.97, waiting_time=10000):
                self.not_found("b_localcobrancaparcela")
            self.click_relative(55, 45)
            self.wait(500)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "b_classparcela", matching=0.97, waiting_time=10000):
                self.not_found("b_classparcela")
            self.click_relative(55, 93)
            self.wait(500)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "b_sacadorparcela", matching=0.97, waiting_time=10000):
                self.not_found("b_sacadorparcela")
            self.click_relative(54, 138)
            self.type_keys_with_interval(1,'0081260')
            self.enter()
            self.wait(500)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "b_tipopagamentoparcelas", matching=0.97, waiting_time=10000):
                self.not_found("b_tipopagamentoparcelas")
            self.click_relative(57, 184)
            self.wait(500)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "b_planofinanceiroparcelas", matching=0.97, waiting_time=10000):
                self.not_found("b_planofinanceiroparcelas")
            self.click_relative(572, 45)
            self.wait(500)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "b_operacaoparcelas", matching=0.97, waiting_time=10000):
                self.not_found("b_operacaoparcelas")
            self.click_relative(537, 93)
            self.wait(500)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "b_comissaoparcelas", matching=0.97, waiting_time=10000):
                self.not_found("b_comissaoparcelas")
            self.click_relative(534, 137)
            self.wait(500)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "continuarfinalizacaoNF", matching=0.97, waiting_time=10000):
                self.not_found("continuarfinalizacaoNF")
            self.click()
            if not self.find( "retornarfinanceirofinalNF", matching=0.97, waiting_time=10000):
                self.not_found("retornarfinanceirofinalNF")
            self.click_relative(37, 45)
            if not self.find( "retornarimpressaoNFfinal", matching=0.97, waiting_time=10000):
                self.not_found("retornarimpressaoNFfinal")
            self.click_relative(30, 46)
            self.wait(500)
            if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                self.not_found("excluirrs")
            self.click()
            #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirrs")
            #self.click()
            self.enter()
            self.type_keys_with_interval(1,'Nota feita com teste automatizado')
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            self.wait(500)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---ROMANEIOS DE SAIDA---####
            
            if not self.find( "vendas", matching=0.97, waiting_time=10000):
                self.not_found("vendas")
            self.click()
            if not self.find( "romaneiosdesaida", matching=0.97, waiting_time=10000):
                self.not_found("romaneiosdesaida")
            self.click()
            self.enter()
            if not self.find( "b_transportadorCMR", matching=0.97, waiting_time=10000):
                self.not_found("b_transportadorCMR")
            self.click_relative(478, 88)
            self.type_keys_with_interval(1,'0081260')
            self.enter()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.tab()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()
            self.tab()
            self.tab()
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_up()
            self.type_up()
            self.tab()
            if not self.find( "b_transportador_inclusao", matching=0.97, waiting_time=10000):
                self.not_found("b_transportador_inclusao")
            self.click_relative(81, 154)
            self.enter()
            self.wait(3000)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(1500)
            if not self.find( "b_rota_inclusao", matching=0.97, waiting_time=10000):
                self.not_found("b_rota_inclusao")
            self.click_relative(458, 157)
            self.enter()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.tab()
            self.tab()
            self.type_keys_with_interval(1,'te12!@')
            self.tab()
            self.type_keys_with_interval(1,'te12!@')
            self.tab()
            self.type_keys_with_interval(1,'abc1234')
            self.tab()
            self.type_keys_with_interval(1,'abc1234')
            self.tab()
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
                self.not_found("salvarrs")
            self.click()
            self.wait(500)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            self.type_right()
            self.enter()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "s_busca_CMR", matching=0.97, waiting_time=10000):
                self.not_found("s_busca_CMR")
            self.click()
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                self.not_found("excluirrs")
            self.click()
            #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirrs")
            #self.click()
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()            
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---EXPEDICAO---####
                             
            if not self.find( "vendas", matching=0.97, waiting_time=10000):
                self.not_found("vendas")
            self.click()
            if not self.find( "expedicao", matching=0.97, waiting_time=10000):
                self.not_found("expedicao")
            self.click()
            if not self.find( "expedicao2", matching=0.97, waiting_time=10000):
                self.not_found("expedicao2")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()  
            if not self.find( "b_clienteMovExp", matching=0.97, waiting_time=10000):
                self.not_found("b_clienteMovExp")
            self.click_relative(374, 83)
            self.enter()
            self.wait(1500)
            self.type_keys_with_interval(1,'0081260')
            self.enter()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            if not self.find( "exibiritenssim", matching=0.97, waiting_time=10000):
                self.not_found("exibiritenssim")
            self.click()
            if not self.find( "exibiritensnao", matching=0.97, waiting_time=10000):
                self.not_found("exibiritensnao")
            self.click()
            if not self.find( "situacaoloopMovExp", matching=0.97, waiting_time=10000):
                self.not_found("situacaoloopMovExp")
            self.double_click_relative(64, 25)
            x=0
            while x<4:
                self.type_up()
                x=x+1
            x=0
            while x<4:
                self.type_down()
                x=x+1
            self.tab()
            x=0
            while x<2:
                self.type_up()
                x=x+1
            x=0            
            while x<2:
                self.type_down()
                x=x+1
            if not self.find( "a2selecaomovexp", matching=0.97, waiting_time=10000):
                self.not_found("a2selecaomovexp")
            self.click()
            if not self.find( "b_itemselecao", matching=0.97, waiting_time=10000):
                self.not_found("b_itemselecao")
            self.click_relative(12, 46)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "b_rotasMovEnt", matching=0.97, waiting_time=10000):
                self.not_found("b_rotasMovEnt")
            self.click_relative(97, 124)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "situacao2movent", matching=0.97, waiting_time=10000):
                self.not_found("situacao2movent")
            self.click()
            if not self.find( "situacao3movent", matching=0.97, waiting_time=10000):
                self.not_found("situacao3movent")
            self.click()
            if not self.find( "situacao1movent", matching=0.97, waiting_time=10000):
                self.not_found("situacao1movent")
            self.click()
            self.tab()
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "addregistromovent", matching=0.97, waiting_time=10000):
                self.not_found("addregistromovent")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()  
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            
            #if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
            #    self.not_found("salvarrs")
            #self.click()
            self.wait(500)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                self.not_found("excluirrs")
            self.click()            
            #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirrs")
            #self.click()
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()         
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()   
                       
                            ####---CONFERENCIA DE PEDIDOS---####
                             
            if not self.find( "vendas", matching=0.97, waiting_time=10000):
                self.not_found("vendas")
            self.click()
            if not self.find( "expedicao", matching=0.97, waiting_time=10000):
                self.not_found("expedicao")
            self.click()
            if not self.find( "conferenciadepedidos", matching=0.97, waiting_time=10000):
                self.not_found("conferenciadepedidos")
            self.click()
            x=0
            while x<3:
                self.tab()
                self.space()
                self.space()
                x=x+1
            if not self.find( "b_itemConfPed", matching=0.97, waiting_time=10000):
                self.not_found("b_itemConfPed")
            self.click_relative(117, 235)
            self.type_keys_with_interval(1,'agulha gengival')
            self.enter()
            self.type_down()
            self.type_down()
            self.type_down()
            self.type_down()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(1500)
            self.tab()
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.enter()
            if not self.find( "aba2confPed", matching=0.97, waiting_time=10000):
                self.not_found("aba2confPed")
            self.double_click()
            if not self.find( "op_emb", matching=0.97, waiting_time=10000):
                self.not_found("op_emb")
            self.click()
            if not self.find( "op_prvent", matching=0.97, waiting_time=10000):
                self.not_found("op_prvent")
            self.click()
            if not self.find( "op_lanc", matching=0.97, waiting_time=10000):
                self.not_found("op_lanc")
            self.click()
            if not self.find( "op_emi", matching=0.97, waiting_time=10000):
                self.not_found("op_emi")
            self.click()
            if not self.find( "botãobuscar", matching=0.97, waiting_time=10000):
                self.not_found("botãobuscar")
            self.click()
            self.wait(500)
            self.enter()
            self.wait(5000)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "situacaoconfped", matching=0.97, waiting_time=10000):
                self.not_found("situacaoconfped")
            self.click_relative(541, 21)
            x=0
            while x<10:
                self.type_down()
                self.space()
                x=x+1
            self.space()
            x=0
            while x<10:
                self.type_up()
                self.space()
                x=x+1
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click() 
            
                            ####---CADASTRO DE ETIQUETAS---####
                             
            if not self.find( "vendas", matching=0.97, waiting_time=10000):
                self.not_found("vendas")
            self.click()
            if not self.find( "expedicao", matching=0.97, waiting_time=10000):
                self.not_found("expedicao")
            self.click()
            if not self.find( "cadastrodeetiquetas", matching=0.97, waiting_time=10000):
                self.not_found("cadastrodeetiquetas")
            self.click()
            if not self.find( "incluirclaro", matching=0.97, waiting_time=10000):
                self.not_found("incluirclaro")
            self.click()
            if not self.find( "cbmestre", matching=0.97, waiting_time=10000):
                self.not_found("cbmestre")
            self.click_relative(7, 25)
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123123')
            self.tab()
            if not self.find( "retornarclaro", matching=0.97, waiting_time=10000):
                self.not_found("retornarclaro")
            self.click()
            if not self.find( "localizarclaro", matching=0.97, waiting_time=10000):
                self.not_found("localizarclaro")
            self.click()
            if not self.find( "editarclaro", matching=0.97, waiting_time=10000):
                self.not_found("editarclaro")
            self.click()            
            if not self.find( "excluiretiqueta", matching=0.97, waiting_time=10000):
                self.not_found("excluiretiqueta")
            self.click_relative(2, 81)
            #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirrs")
            #self.click()
            self.enter()
            if not self.find( "retornarclaro", matching=0.97, waiting_time=10000):
                self.not_found("retornarclaro")
            self.click()
            if not self.find( "localizarclaro", matching=0.97, waiting_time=10000):
                self.not_found("localizarclaro")
            self.click()
            if not self.find( "retornarclaro", matching=0.97, waiting_time=10000):
                self.not_found("retornarclaro")
            self.click()
            
                            ####---LEITURA DE ETIQUETAS---####
                             
            if not self.find( "vendas", matching=0.97, waiting_time=10000):
                self.not_found("vendas")
            self.click()
            if not self.find( "expedicao", matching=0.97, waiting_time=10000):
                self.not_found("expedicao")
            self.click()
            if not self.find( "leituradeetiquetas", matching=0.97, waiting_time=10000):
                self.not_found("leituradeetiquetas")
            self.click()
            self.type_keys_with_interval(1,'1')
            self.enter()
            if not self.find( "aba2confPed", matching=0.97, waiting_time=10000):
                self.not_found("aba2confPed")
            self.double_click()
            if not self.find( "op_emb", matching=0.97, waiting_time=10000):
                self.not_found("op_emb")
            self.click()
            if not self.find( "op_prvent", matching=0.97, waiting_time=10000):
                self.not_found("op_prvent")
            self.click()
            if not self.find( "op_lanc", matching=0.97, waiting_time=10000):
                self.not_found("op_lanc")
            self.click()
            if not self.find( "op_emi", matching=0.97, waiting_time=10000):
                self.not_found("op_emi")
            self.click()
            if not self.find( "botãobuscar", matching=0.97, waiting_time=10000):
                self.not_found("botãobuscar")
            self.click()
            self.wait(500)
            self.enter()
            self.wait(5000)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(1500)
            self.tab()
            self.backspace()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "gravarcodigo1", matching=0.97, waiting_time=10000):
                self.not_found("gravarcodigo1")
            self.double_click_relative(176, 47)                       
            #if not self.find( "aba1etiquetasdepedidos", matching=0.97, waiting_time=10000):
            #    self.not_found("aba1etiquetasdepedidos")
            #self.click()
            self.wait(1000)                       
            if not self.find( "codigodebarrasaba1", matching=0.97, waiting_time=10000):
                self.not_found("codigodebarrasaba1")
            self.double_click_relative(36, 283)            
            self.type_keys_with_interval(1,'123')
            self.tab()
            if not self.find( "gravarcodigos2", matching=0.97, waiting_time=10000):
                self.not_found("gravarcodigos2")
            self.click()
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---VENDAS PERDIDAS---####
                             
            if not self.find( "vendas", matching=0.97, waiting_time=10000):
                self.not_found("vendas")
            self.click()
            if not self.find( "vendasperdidas", matching=0.97, waiting_time=10000):
                self.not_found("vendasperdidas")
            self.click()
            self.enter()
            if not self.find( "aba2vendasperdidas", matching=0.97, waiting_time=10000):
                self.not_found("aba2vendasperdidas")
            self.click()
            if not self.find( "a2_VP_vendedor", matching=0.97, waiting_time=10000):
                self.not_found("a2_VP_vendedor")
            self.click_relative(66, 22)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            if not self.find( "a2_VP_motivo", matching=0.97, waiting_time=10000):
                self.not_found("a2_VP_motivo")
            self.click_relative(65, 22)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            if not self.find( "a2_VP_item", matching=0.97, waiting_time=10000):
                self.not_found("a2_VP_item")
            self.click_relative(64, 24)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            if not self.find( "a2_VP_cliente", matching=0.97, waiting_time=10000):
                self.not_found("a2_VP_cliente")
            self.click_relative(65, 23)
            self.type_keys_with_interval(1,'0081260')
            self.enter()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()
            if not self.find( "b_item_perdido", matching=0.97, waiting_time=10000):
                self.not_found("b_item_perdido")
            self.click_relative(75, 128)
            self.enter()
            self.wait(2500)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(1500)
            if not self.find( "b_cliente_perdidas", matching=0.97, waiting_time=10000):
                self.not_found("b_cliente_perdidas")
            self.click_relative(72, 173)
            self.enter()
            self.wait(2500)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(1500)
            if not self.find( "b_vendedor_perdido", matching=0.97, waiting_time=10000):
                self.not_found("b_vendedor_perdido")
            self.click_relative(69, 219)
            self.enter()
            self.wait(2500)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(1500)
            if not self.find( "b_motivo_perdido", matching=0.97, waiting_time=10000):
                self.not_found("b_motivo_perdido")
            self.click_relative(427, 221)
            self.enter()
            self.wait(2500)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(1500)
            if not self.find( "op1_perdido", matching=0.97, waiting_time=10000):
                self.not_found("op1_perdido")
            self.click_relative(399, 128)
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "op2_perdido", matching=0.97, waiting_time=10000):
                self.not_found("op2_perdido")
            self.click_relative(401, 176)
            self.type_keys_with_interval(1,'te12!@')
            x=0
            while x<5:
                self.tab()
                x=x+1
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
                self.not_found("salvarrs")
            self.click()
            self.wait(500)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                self.not_found("excluirrs")
            self.click()            
            #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirrs")
            #self.click()
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()         
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---ORDEM DE SERVIÇO---####
                             
            if not self.find( "vendas", matching=0.97, waiting_time=10000):
                self.not_found("vendas")
            self.click()
            if not self.find( "ordensdeservico", matching=0.97, waiting_time=10000):
                self.not_found("ordensdeservico")
            self.click()
            if not self.find( "selecao_ordemservico", matching=0.97, waiting_time=10000):
                self.not_found("selecao_ordemservico")
            self.click()
            if not self.find( "b_condpag_mos", matching=0.97, waiting_time=10000):
                self.not_found("b_condpag_mos")
            self.click_relative(70, 193)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            if not self.find( "b_executor_mos", matching=0.97, waiting_time=10000):
                self.not_found("b_executor_mos")
            self.click_relative(73, 241)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            if not self.find( "b_tipoos_mos", matching=0.97, waiting_time=10000):
                self.not_found("b_tipoos_mos")
            self.click_relative(72, 287)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.enter()
            self.backspace()
            if not self.find( "b_recepcionista_mos", matching=0.97, waiting_time=10000):
                self.not_found("b_recepcionista_mos")
            self.click_relative(463, 194)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            if not self.find( "b_servico_mos", matching=0.97, waiting_time=10000):
                self.not_found("b_servico_mos")
            self.click_relative(462, 239)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            if not self.find( "b_client_mos", matching=0.97, waiting_time=10000):
                self.not_found("b_client_mos")
            self.click_relative(634, 122)
            self.type_keys_with_interval(1,'0081260')
            self.enter()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.tab()
            if not self.find( "s_cf", matching=0.97, waiting_time=10000):
                self.not_found("s_cf")
            self.click()
            if not self.find( "s_nf", matching=0.97, waiting_time=10000):
                self.not_found("s_nf")
            self.click()
            if not self.find( "s_docto", matching=0.97, waiting_time=10000):
                self.not_found("s_docto")
            self.click()
            if not self.find( "periodo_mos", matching=0.97, waiting_time=10000):
                self.not_found("periodo_mos")
            self.click_relative(32, 7)
            if not self.find( "periodo_ano", matching=0.97, waiting_time=10000):
                self.not_found("periodo_ano")
            self.click()
            if not self.find( "periodo_ano_atual", matching=0.97, waiting_time=10000):
                self.not_found("periodo_ano_atual")
            self.click()
            self.tab()
            self.type_down()
            self.type_down()
            self.type_up()
            self.type_up()
            if not self.find( "s_situ_andamento", matching=0.97, waiting_time=10000):
                self.not_found("s_situ_andamento")
            self.click()
            if not self.find( "s_sit_finalizoficina", matching=0.97, waiting_time=10000):
                self.not_found("s_sit_finalizoficina")
            self.click()
            if not self.find( "s_sit_fechadas", matching=0.97, waiting_time=10000):
                self.not_found("s_sit_fechadas")
            self.click()
            if not self.find( "s_sit_canceladas", matching=0.97, waiting_time=10000):
                self.not_found("s_sit_canceladas")
            self.click()
            if not self.find( "s_sit_todas", matching=0.97, waiting_time=10000):
                self.not_found("s_sit_todas")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---FRETES E RPA---####
                             
            if not self.find( "vendas", matching=0.97, waiting_time=10000):
                self.not_found("vendas")
            self.click()
            if not self.find( "freteserpa", matching=0.97, waiting_time=10000):
                self.not_found("freteserpa")
            self.click()
            if not self.find( "lancamentodefretes", matching=0.97, waiting_time=10000):
                self.not_found("lancamentodefretes")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "aba2selecao_CMF", matching=0.97, waiting_time=10000):
                self.not_found("aba2selecao_CMF")
            self.click()
            if not self.find( "b_transportador_CMF", matching=0.97, waiting_time=10000):
                self.not_found("b_transportador_CMF")
            self.click_relative(508, 93)
            self.type_keys_with_interval(1,'0081260')
            self.enter()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.tab()
            if not self.find( "b_operacao_CMF", matching=0.97, waiting_time=10000):
                self.not_found("b_operacao_CMF")
            self.click_relative(500, 168)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.tab()
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()
            self.type_keys_with_interval(1,'874874')
            self.tab()
            self.type_keys_with_interval(1,'1')
            self.tab()
            self.type_keys_with_interval(1,'1')
            self.tab()
            x=0
            while x<9:
                self.type_up()
                x=x+1
            x=0
            while x<45:
                self.type_down()
                x=x+1
            self.tab()
            self.type_down()
            x=0
            while x<11:
                self.type_up()
                x=x+1
            self.tab()
            self.tab()
            self.tab()
            self.tab()
            if not self.find( "b_codoperacao_MFrete", matching=0.97, waiting_time=10000):
                self.not_found("b_codoperacao_MFrete")
            self.click_relative(68, 133)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.tab()
            self.tab()
            self.tab()
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.tab()
            if not self.find( "b_transportador_Mfrete", matching=0.97, waiting_time=10000):
                self.not_found("b_transportador_Mfrete")
            self.click_relative(202, 41)
            self.type_keys_with_interval(1,'0081260')
            self.enter()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "b_grupofiscal_Mfrete", matching=0.97, waiting_time=10000):
                self.not_found("b_grupofiscal_Mfrete")
            self.click_relative(798, 42)
            self.type_keys_with_interval(1,'diferido')
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "b_centrocusto_Mfrete", matching=0.97, waiting_time=10000):
                self.not_found("b_centrocusto_Mfrete")
            self.click_relative(86, 83)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            if not self.find( "b_municipiocoleta_Mfrete", matching=0.97, waiting_time=10000):
                self.not_found("b_municipiocoleta_Mfrete")
            self.click_relative(435, 82)
            self.type_keys_with_interval(1,'guarapuava')
            self.tab()
            self.tab()
            self.tab()
            self.type_down()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "b_municipioentrega_Mfrete", matching=0.97, waiting_time=10000):
                self.not_found("b_municipioentrega_Mfrete")
            self.click_relative(808, 81)
            self.type_keys_with_interval(1,'curitiba')
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.type_right()
            self.enter()
            self.tab()
            self.tab()
            x=0
            while x<4:
                y=0
                while y<3:
                    self.type_keys_with_interval(1,'123')
                    self.tab()
                    y=y+1
                z=0
                while z<6:
                    self.type_down()
                    z=z+1
                self.tab()
                self.tab()
                x=x+1
            x=0
            while x<18:
                self.type_down()
                x=x+1
            x=0
            while x<14:
                if not self.find( "sittribIPI", matching=0.97, waiting_time=10000):
                    self.not_found("sittribIPI")
                self.click_relative(795, 43)
                self.type_down()
                self.enter()
                x=x+1
            x=0
            while x<21:
                if not self.find( "sittribICMS", matching=0.97, waiting_time=10000):
                    self.not_found("sittribICMS")
                self.click_relative(792, 42)
                self.type_down()
                self.enter()
                x=x+1
            x=0
            while x<4:
                if not self.find( "sittribPIS", matching=0.97, waiting_time=10000):
                    self.not_found("sittribPIS")
                self.click_relative(792, 44)                
                self.type_down()
                self.enter()
                x=x+1
            x=0
            while x<33:
                if not self.find( "sittribCOFINS", matching=0.97, waiting_time=10000):
                    self.not_found("sittribCOFINS")
                self.click_relative(794, 43)
                self.type_down()
                self.enter()
                x=x+1
            self.tab()
            self.tab()
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
                self.not_found("salvarrs")
            self.click()
            self.wait(500)
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                self.not_found("excluirrs")
            self.click()            
            #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirrs")
            #self.click()
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()         
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---EMISSAO DE RPA---####
                             
            if not self.find( "vendas", matching=0.97, waiting_time=10000):
                self.not_found("vendas")
            self.click()
            if not self.find( "freteserpa", matching=0.97, waiting_time=10000):
                self.not_found("freteserpa")
            self.click()
            if not self.find( "emissaoderpa", matching=0.97, waiting_time=10000):
                self.not_found("emissaoderpa")
            self.click()
            self.enter()
            if not self.find( "b_transportador_MRPA", matching=0.97, waiting_time=10000):
                self.not_found("b_transportador_MRPA")
            self.click_relative(297, 86)
            self.type_keys_with_interval(1,'0081260')
            self.enter()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.tab()
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()
            self.tab()
            if not self.find( "b_transportador_RPAtransporte", matching=0.97, waiting_time=10000):
                self.not_found("b_transportador_RPAtransporte")
            self.click_relative(561, 87)
            self.enter()
            self.wait(1500)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.tab()
            self.type_keys_with_interval(1,'te12!@')
            self.tab()
            self.tab()
            self.tab()
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
                self.not_found("salvarrs")
            self.click()
            self.wait(500)
            self.enter()
            if not self.find( "cancelar_RPAtransportadores", matching=0.97, waiting_time=10000):
                self.not_found("cancelar_RPAtransportadores")
            self.click()
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---CHECAGEM DE LANCAMENTO---####
                             
            if not self.find( "vendas", matching=0.97, waiting_time=10000):
                self.not_found("vendas")
            self.click()
            if not self.find( "checagemdelancamentos", matching=0.97, waiting_time=10000):
                self.not_found("checagemdelancamentos")
            self.click()
            if not self.find( "b_calendario_checagemlanc", matching=0.97, waiting_time=10000):
                self.not_found("b_calendario_checagemlanc")
            self.click_relative(32, 8)            
            if not self.find( "periodo_ano", matching=0.97, waiting_time=10000):
                self.not_found("periodo_ano")
            self.click()
            if not self.find( "periodo_ano_atual", matching=0.97, waiting_time=10000):
                self.not_found("periodo_ano_atual")
            self.click()
            if not self.find( "checagem_clancamento", matching=0.97, waiting_time=10000):
                self.not_found("checagem_clancamento")
            self.click()
            self.wait(1500)
            if not self.find( "aba2_clancamento", matching=0.97, waiting_time=10000):
                self.not_found("aba2_clancamento")
            self.click()
            if not self.find( "aba3_clancamento", matching=0.97, waiting_time=10000):
                self.not_found("aba3_clancamento")
            self.click()
            if not self.find( "titulos_baixados_CL", matching=0.97, waiting_time=10000):
                self.not_found("titulos_baixados_CL")
            self.click()
            if not self.find( "exibir_coperacao_CL", matching=0.97, waiting_time=10000):
                self.not_found("exibir_coperacao_CL")
            self.click()
            if not self.find( "checagem_clancamento", matching=0.97, waiting_time=10000):
                self.not_found("checagem_clancamento")
            self.click()
            self.wait(1500)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---MOVIMENTO DE COMISSAO---####
                             
            if not self.find( "vendas", matching=0.97, waiting_time=10000):
                self.not_found("vendas")
            self.click()
            if not self.find( "movimentodecomissao", matching=0.97, waiting_time=10000):
                self.not_found("movimentodecomissao")
            self.click()
            self.enter()
            if not self.find( "aba2_MCI", matching=0.97, waiting_time=10000):
                self.not_found("aba2_MCI")
            self.click()
            if not self.find( "b_vendedor_MCI", matching=0.97, waiting_time=10000):
                self.not_found("b_vendedor_MCI")
            self.click_relative(380, 79)
            self.enter()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.tab()
            self.backspace()
            self.tab()
            if not self.find( "b_condpagamento_MCI", matching=0.97, waiting_time=10000):
                self.not_found("b_condpagamento_MCI")
            self.double_click_relative(70, 150)
            self.wait(500)            
            self.enter()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.tab()
            self.backspace()
            self.tab()
            if not self.find( "b_cliente_MCI", matching=0.97, waiting_time=10000):
                self.not_found("b_cliente_MCI")
            self.click_relative(70, 190)
            self.enter()
            self.wait(2000)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.tab()
            self.backspace()
            self.tab()
            if not self.find( "b_rota_MCI", matching=0.97, waiting_time=10000):
                self.not_found("b_rota_MCI")
            self.click_relative(460, 190)
            self.enter()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.tab()
            self.backspace()
            self.tab()
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()
            self.tab()
            self.tab()
            self.type_down()
            self.type_up()
            if not self.find( "b_vendedor_MDC", matching=0.97, waiting_time=10000):
                self.not_found("b_vendedor_MDC")
            self.click_relative(81, 158)
            self.enter()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "b_cliente_MDC", matching=0.97, waiting_time=10000):
                self.not_found("b_cliente_MDC")
            self.click_relative(79, 195)
            self.enter()
            self.wait(2000)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.tab()
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
                self.not_found("salvarrs")
            self.click()
            self.wait(500)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                self.not_found("excluirrs")
            self.click()            
            #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirrs")
            #self.click()
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()         
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---GERACAO DE ENQUETE---####
            
            if not self.find( "vendas", matching=0.97, waiting_time=10000):
                self.not_found("vendas")
            self.click()
            if not self.find( "geracaodeenquetes", matching=0.97, waiting_time=10000):
                self.not_found("geracaodeenquetes")
            self.click()
            if not self.find( "b_item_genq", matching=0.97, waiting_time=10000):
                self.not_found("b_item_genq")
            self.click_relative(60, 22)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.tab()
            if not self.find( "b_clientefornecedor_genq", matching=0.97, waiting_time=10000):
                self.not_found("b_clientefornecedor_genq")
            self.click_relative(61, 22)
            self.type_keys_with_interval(1,'0081260')
            self.enter()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.tab()
            if not self.find( "b_servico_genq", matching=0.97, waiting_time=10000):
                self.not_found("b_servico_genq")
            self.click_relative(65, 22)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            self.tab()
            x=0
            while x<4:
                if not self.find( "loop_origemmovimento_genq", matching=0.97, waiting_time=10000):
                    self.not_found("loop_origemmovimento_genq")
                self.click_relative(171, 24)
                self.type_down()
                self.enter()
                x=x+1
            x=0
            while x<4:
                if not self.find( "loop_origemmovimento_genq", matching=0.97, waiting_time=10000):
                    self.not_found("loop_origemmovimento_genq")
                self.click_relative(171, 24)
                self.type_up()
                self.enter()
                x=x+1
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()         
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---GESTAO DOC E---####
                             
            if not self.find( "vendas", matching=0.97, waiting_time=10000):
                self.not_found("vendas")
            self.click()
            if not self.find( "gestaodoce", matching=0.97, waiting_time=10000):
                self.not_found("gestaodoce")
            self.click()
            if not self.find( "loop_doce_gd", matching=0.97, waiting_time=10000):
                self.not_found("loop_doce_gd")
            self.click_relative(750, 86)
            x=0
            while x<7:
                self.type_down()
                self.space()
                x=x+1
            x=0
            while x<7:
                self.type_up()
                self.space()
                x=x+1
            self.type_down()
            self.type_down()
            self.space()
            self.type_up()
            self.space()
            if not self.find( "loop_situacao_gdc", matching=0.97, waiting_time=10000):
                self.not_found("loop_situacao_gdc")
            self.click_relative(113, 23)
            x=0
            while x<19:
                self.type_down()
                self.space()
                x=x+1
            self.tab()
            self.type_down()
            self.type_down()
            self.type_down()
            if not self.find( "periodo_gdc", matching=0.97, waiting_time=10000):
                self.not_found("periodo_gdc")
            self.click_relative(389, 84)
            if not self.find( "periodo_ano", matching=0.97, waiting_time=10000):
                self.not_found("periodo_ano")
            self.click()
            if not self.find( "periodo_ano_atual", matching=0.97, waiting_time=10000):
                self.not_found("periodo_ano_atual")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            self.wait(1000)
            if not self.find( "seleciona_gestaodoce", matching=0.97, waiting_time=10000):
                self.not_found("seleciona_gestaodoce")
            self.click_relative(36, 23)
            if not self.find( "inutilizar_gdc", matching=0.97, waiting_time=10000):
                self.not_found("inutilizar_gdc")
            self.click_relative(81, -1)
            if not self.find( "documentosselecionados", matching=0.97, waiting_time=10000):
                self.not_found("documentosselecionados")
            self.click()
            self.type_keys_with_interval(1,'feito por teste automatico')
            self.enter()
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
            

            
        def not_found(self, label):
            print(f"Element not found: {label}")  
        
if __name__ == '__main__':
    Bot.main()








