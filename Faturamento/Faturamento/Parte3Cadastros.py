from botcity.core import DesktopBot

class Bot(DesktopBot):
        def action(self, execution=None):
            #######################-----LOGIN-----############################
        
            #self.execute(r"C:\Users\Rafael\Desktop\2207\faturamento.exe")
            self.execute(r"C:\teorema\bin\faturamento.exe")
            
            if not self.find( "btn_codigo_usuario", matching=0.97, waiting_time=100000):
                self.not_found("btn_codigo_usuario")
            self.click_relative(47, 12)
                    
            self.type_keys_with_interval(1,"999")
            self.wait(500)
            self.type_keys_with_interval(1,"tsfmx24")

            self.enter()

            if not self.find( "btn_login", matching=0.97, waiting_time=10000):
                self.not_found("btn_login")
            self.click()
            self.enter()

            ###################################################################
            self.wait(2000)
            if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro2")
            self.click()
            if not self.find( "classificacoes", matching=0.97, waiting_time=10000):
                self.not_found("classificacoes")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            self.wait(5000)            
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
            self.type_keys_with_interval(1,'te12!@')
            self.tab()
            self.type_down()
            self.type_up()
            if not self.find( "salvarsss_cadastro", matching=0.97, waiting_time=10000):
                self.not_found("salvarsss_cadastro")
            self.click()
            if not self.find( "retornars", matching=0.97, waiting_time=10000):
                self.not_found("retornars")
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
            if not self.find( "exclurs", matching=0.97, waiting_time=10000):
                self.not_found("exclurs")
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
            if not self.find( "retornarsssss", matching=0.97, waiting_time=10000):
                self.not_found("retornarsssss")
            self.click()
            
                            ####---CONDICAO PAGAMENTO---####
                             
            if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro2")
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
            self.type_keys_with_interval(100,"001001001")
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
            
                            ####---COMISSOES---####
                             
            if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro2")
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
            if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro2")
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
            self.enter()
            #if not self.find( "simexcluirfaixa", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirfaixa")
            #self.click()
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
            
                            ####---FUNCOES---####
                             
            if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro2")
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
            
                            ####---BANCOS---####
                             
            if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro2")
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
            
                            ####---CONTAS---####
                             
            if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro2")
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
            #if not self.find( "bancoCC", matching=0.97, waiting_time=10000):
            #    self.not_found("bancoCC")
            #self.click_relative(453, 47)
            if not self.find( "b_banco_CConta", matching=0.97, waiting_time=10000):
                self.not_found("b_banco_CConta")
            self.click_relative(455, 167)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            #if not self.find( "codigocontabilcontaCC", matching=0.97, waiting_time=10000):
            #   self.not_found("codigocontabilcontaCC")
            #self.click_relative(865, 47)
            if not self.find( "b_codigoContabilConta_CConta", matching=0.97, waiting_time=10000):
                self.not_found("b_codigoContabilConta_CConta")
            self.click_relative(871, 170)
            self.type_keys_with_interval(1,"00245")
            if not self.find( "cod00245pcCC", matching=0.97, waiting_time=10000):
                self.not_found("cod00245pcCC")
            self.click()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            #if not self.find( "empresaCC", matching=0.97, waiting_time=10000):
            #    self.not_found("empresaCC")
            #self.click_relative(49, 95)
            if not self.find( "b_empresa_CContas", matching=0.97, waiting_time=10000):
                self.not_found("b_empresa_CContas")
            self.click_relative(56, 217)
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
            
                            ####---LOCAIS DE COBRANCA---####
                             
            if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro2")
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
            
                            ####---MOEDAS---####
                             
            if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro2")
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
            self.enter()
            #if not self.find( "simexcluirfaixa", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirfaixa")
            #self.click()
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
            
                            ####---TIPOS DE PAGAMENTO---####
                             
            if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro2")
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
            
                            ####---TABELA DE IMPOSTOS---####
                             
            if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro2")
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
            self.enter()
            #if not self.find( "simexcluirfaixa", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirfaixa")
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
            
                            ####---CATEGORIAS DE CAMPANHA---####
                             
            if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro2")
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
            
                            ####---AUTORIZADORES---####
                             
            if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro2")
            self.click()
            if not self.find( "autorizadores", matching=0.97, waiting_time=10000):
                self.not_found("autorizadores")
            self.click()
            if not self.find( "okparametronaodefinido", matching=0.97, waiting_time=10000):
                self.not_found("okparametronaodefinido")
            self.click()
            
                            ####---CONFIGURACOES---####
                             
            if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro2")
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
            self.enter()
            #if not self.find( "simexcluirfaixa", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirfaixa")
            #self.click()
            
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
            self.enter()
            #if not self.find( "simexcluirfaixa", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirfaixa")
            #self.click()
            self.enter()
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---IMPRESSORA DE CODIGO DE BARRAS---####
                             
            if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro2")
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
            
                            ####---CONFIG IMPORTACAO EMPORIUM---####
                             
            if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro2")
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
            #if not self.find( "vendedorimpemp", matching=0.97, waiting_time=10000):
            #    self.not_found("vendedorimpemp")
            #self.click_relative(113, 4)
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
                                              
            if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro2")
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
            self.enter()
            #if not self.find( "simexcluirfaixa", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirfaixa")
            #self.click()
            
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
            self.enter()
            #if not self.find( "simexcluirfaixa", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirfaixa")
            #self.click()
            
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
            self.enter()
            #if not self.find( "simexcluirfaixa", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirfaixa")
            #self.click()
            
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
            self.enter()
            #if not self.find( "simexcluirfaixa", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirfaixa")
            #self.click()
            
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
            self.enter()
            #if not self.find( "simexcluirfaixa", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirfaixa")
            #self.click()
            
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
            self.enter()
            #if not self.find( "simexcluirfaixa", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirfaixa")
            #self.click()
            
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
            self.enter()
            #if not self.find( "simexcluirfaixa", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirfaixa")
            #self.click()
            
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
            self.enter()
            #if not self.find( "simexcluirfaixa", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirfaixa")
            #self.click()
            
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
            self.enter()
            #if not self.find( "simexcluirfaixa", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirfaixa")
            #self.click()
            
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
                             
            if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro2")
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
            
                            ####---MAPA FISCAL---####
                             
            if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro2")
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
                             
            if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro2")
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
            
                            ####---CADASTRO DE ECF---####
                             
            if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro2")
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
            
                            ####---DOCUMENTACOES---####
                             
            if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro2")
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
            
            if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro2")
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
            
            if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro2")
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
            self.wait(1000)
            if not self.find( "fecharsistemaparte3", matching=0.97, waiting_time=10000):
                self.not_found("fecharsistemaparte3")
            self.click()           
            if not self.find( "simexcluircft1", matching=0.97, waiting_time=10000):
                self.not_found("simexcluircft1")
            self.click()
            #self.enter()


            def not_found(self, label):
                print(f"Element not found: {label}")
if __name__ == '__main__':
    Bot.main()












































































































































