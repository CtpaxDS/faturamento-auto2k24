from botcity.core import DesktopBot

class Bot(DesktopBot):
        def action(self, execution=None):
            
            #######################-----LOGIN-----############################
        
            #self.execute(r"C:\Users\Rafael\Desktop\2207\faturamento.exe")
            self.execute(r"C:\Users\Rafael\Desktop\2207\teste23\23mes07\faturamento.exe")
            
            if not self.find( "btn_codigo_usuario", matching=0.97, waiting_time=10000):
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
            
            self.wait(1500)
            if not self.find( "abacompras2", matching=0.97, waiting_time=10000):
                self.not_found("abacompras2")
            self.click()
            self.wait(1500)
            self.type_down()
            self.wait(1500)
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
            #if not self.find( "solicitantereqcompras", matching=0.97, waiting_time=10000):
            #    self.not_found("solicitantereqcompras")           
            #self.click_relative(54, 25)
            if not self.find( "b_solicitante_MRC", matching=0.97, waiting_time=10000):
                self.not_found("b_solicitante_MRC")
            self.click_relative(465, 160)                       
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
            self.tab()
            self.tab()
            self.tab()
            self.tab()
            self.type_down()
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
            self.tab()
            self.tab()
            self.type_down()
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
            if not self.find( "anexardocumentos2", matching=0.97, waiting_time=10000):
                self.not_found("anexardocumentos2")
            self.click()
            
            if not self.find( "addarquivoanexo", matching=0.97, waiting_time=10000):
                self.not_found("addarquivoanexo")
            self.click_relative(5, 74)
            if not self.find( "abrirselecaodearquivos", matching=0.97, waiting_time=10000):
                self.not_found("abrirselecaodearquivos")
            self.click()
            #if not self.find( "cancelaranexo", matching=0.97, waiting_time=10000):
            #    self.not_found("cancelaranexo")
            #self.click_relative(599, 418)
            self.key_esc()
            if not self.find( "cancelaranexodearquivos", matching=0.97, waiting_time=10000):
                self.not_found("cancelaranexodearquivos")
            self.click()
            self.key_esc()
            #if not self.find( "retornaranexoarquivos", matching=0.97, waiting_time=10000):
            #    self.not_found("retornaranexoarquivos")
            #self.click_relative(23, 44)
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
                             
            self.wait(1500)
            if not self.find( "abacompras2", matching=0.97, waiting_time=10000):
                self.not_found("abacompras2")
            self.click()
            #self.type_down()
            self.wait(1500)
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
                             
            if not self.find( "abacompras2", matching=0.97, waiting_time=10000):
                self.not_found("abacompras2")
            self.click()
            if not self.find( "consultastatussolicitacao", matching=0.97, waiting_time=10000):
                self.not_found("consultastatussolicitacao")
            self.click()
            if not self.find( "b_item_CSM", matching=0.97, waiting_time=10000):
                self.not_found("b_item_CSM")
            self.click_relative(730, 96)
            self.type_keys_with_interval(1,'123')
            self.enter()
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
                             
            if not self.find( "abacompras2", matching=0.97, waiting_time=10000):
                self.not_found("abacompras2")
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
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            self.wait(2000)
            x=0
            while x<18:
                self.type_down()
                x=x+1
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
            x=0
            while x<3:
                self.type_down()
                x=x+1
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'te12!@')
            self.tab()
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
                             
            if not self.find( "abacompras2", matching=0.97, waiting_time=10000):
                self.not_found("abacompras2")
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
            self.key_esc()
            
                            ####---VENDAS---####
                             
            self.wait(1500)
            if not self.find("vendas2", matching=0.97, waiting_time=10000):
                self.not_found("vendas2")
            self.click()
            #self.type_down()
            self.wait(1500)
            if not self.find( "orcamentos", matching=0.97, waiting_time=10000):
                self.not_found("orcamentos")
            self.click()        
            self.wait(1500)
            self.enter()
            if not self.find( "clientesMV", matching=0.97, waiting_time=10000):
                self.not_found("clientesMV")
            self.click_relative(535, 90)
            """if not self.find( "buscarclienteprincipalMV", matching=0.97, waiting_time=10000):
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
            """
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
            if not self.find( "CONFIGCLIENTES_aba2", matching=0.97, waiting_time=10000):
                self.not_found("CONFIGCLIENTES_aba2")
            self.click()
            if not self.find( "op_todas_manutencao_botaoteste", matching=0.97, waiting_time=10000):
                self.not_found("op_todas_manutencao_botaoteste")
            self.click_relative(9, 30)
            self.enter()
            self.enter()
            self.enter()           
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
            #if not self.find( "selecionarstatusabertaeminclusao", matching=0.97, waiting_time=10000):
            #    self.not_found("selecionarstatusabertaeminclusao")
            #self.click()   
            self.enter()         
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
            self.tab()
            self.tab()
            if not self.find( "bvendorcamento", matching=0.97, waiting_time=10000):
                self.not_found("bvendorcamento")
            self.click_relative(423, 535)
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
            
            if not self.find( "a2p2_orcamento", matching=0.97, waiting_time=10000):
                self.not_found("a2p2_orcamento")
            self.click_relative(83, 136)
            if not self.find( "addregistroaba2reqcompras", matching=0.97, waiting_time=10000):
                self.not_found("addregistroaba2reqcompras")
            self.click()
            if not self.find( "b_a2p2_servico_orcamento", matching=0.97, waiting_time=10000):
                self.not_found("b_a2p2_servico_orcamento")
            self.click_relative(78, 177)
            self.wait(1500)
            self.enter()
            self.wait(1500)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(1500)
            if not self.find( "b_a2p2_class_orcamento", matching=0.97, waiting_time=10000):
                self.not_found("b_a2p2_class_orcamento")
            self.click_relative(438, 212)
            self.wait(1500)
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            self.wait(1500)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(1500)
            if not self.find( "b_a2p2_centroCusto_orcamento", matching=0.97, waiting_time=10000):
                self.not_found("b_a2p2_centroCusto_orcamento")
            self.click_relative(97, 214)
            self.wait(1500)
            self.enter()
            self.wait(1500)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(1500)
            if not self.find( "valorunitario_a2p2_orcamento", matching=0.97, waiting_time=10000):
                self.not_found("valorunitario_a2p2_orcamento")
            self.click_relative(701, 174)
            self.type_keys_with_interval(1,'123')
            self.tab()
            if not self.find( "gravarregistroaba3", matching=0.97, waiting_time=10000):
                self.not_found("gravarregistroaba3")
            self.click()
            if not self.find( "cancelarregistroaba3", matching=0.97, waiting_time=10000):
                self.not_found("cancelarregistroaba3")
            self.click()
            if not self.find( "excluirRegistro_a2p2_orcamento", matching=0.97, waiting_time=10000):
               self.not_found("excluirRegistro_a2p2_orcamento")
            self.click_relative(-8, 183)
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
            self.enter()
            self.wait(500)
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            self.wait(1000)
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            self.wait(3000)
            if not self.find( "analise_orcamento", matching=0.97, waiting_time=10000):
                self.not_found("analise_orcamento")
            self.click()
            
            if not self.find( "requisitar_orcamento", matching=0.97, waiting_time=10000):
                self.not_found("requisitar_orcamento")
            self.click()
            if not self.find( "retornaropcaogeracao", matching=0.97, waiting_time=10000):
                self.not_found("retornaropcaogeracao")
            self.click_relative(24, 34)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
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
            
                            ####---INCLUIR vendas2 BALCAO---####
            
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
            if not self.find( "vendas2", matching=0.97, waiting_time=10000):
                self.not_found("vendas2")
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
            #self.tab()
            self.wait(500)
            x=0
            while x<6:
                self.tab()
                x=x+1
            self.type_keys_with_interval(1,'1111')
            self.wait(1500)
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.wait(1500)
            self.tab()
            x=0
            while x<3:
                self.type_down()
                x=x+1
            x=0
            while x<3:
                self.type_up()
                x=x+1
            self.wait(1500)
            self.tab()
            self.wait(1500)
            self.type_up()
            x=0
            while x<4:
                self.type_down()
                x=x+1
            x=0
            while x<4:
                self.type_up()
                x=x+1
            self.wait(500)
            self.tab()
            self.wait(1500)
            x=0
            while x<8:
                self.type_down()
                x=x+1
            self.wait(500)
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
            #self.type_keys_with_interval(1,'18')
            self.enter()
            self.wait(2000)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(1500)
            self.tab()
            self.tab()
            if not self.find( "b_vendedorNF", matching=0.97, waiting_time=10000):
                self.not_found("b_vendedorNF")
            self.click_relative(68, 26)
            self.wait(1500)
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            self.wait(1500)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(1500)
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
            self.wait(1500)
            self.type_keys_with_interval(1,'5206')
            self.wait(1500)
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
            if not self.find( "a2p2NF", matching=0.97, waiting_time=10000):
                self.not_found("a2p2NF")
            self.click()
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
            
            if not self.find( "notas_salvar", matching=0.97, waiting_time=10000):
                self.not_found("notas_salvar")
            self.click_relative(642, 51)
            self.wait(1500)
            self.enter()
           
            if not self.find( "dados_do_itemimposto", matching=0.97, waiting_time=10000):
                self.not_found("dados_do_itemimposto")
            self.click_relative(37, 43)
            #if not self.find( "ir_a2p1NF", matching=0.97, waiting_time=10000):
                #self.not_found("ir_a2p1NF")
            #self.click()
            if not self.find( "notasfiscais_documentosrefe", matching=0.97, waiting_time=10000):
                self.not_found("notasfiscais_documentosrefe")
            self.click_relative(256, 170)
            if not self.find( "Notafiscal_incluir", matching=0.97, waiting_time=10000):
                self.not_found("Notafiscal_incluir")
            self.click_relative(10, 192)
            if not self.find( "retornarconsulta", matching=0.97, waiting_time=10000):
                self.not_found("retornarconsulta")
            self.click_relative(33, 44)
            self.wait(3000)
            self.enter()            
            """if not self.find( "finalizarNF", matching=0.97, waiting_time=10000):
                self.not_found("finalizarNF")
            self.click_relative(64, -4)
            self.wait(3000)
            if not self.find( "finalizarNFeimprimir", matching=0.97, waiting_time=10000):
                self.not_found("finalizarNFeimprimir")
            self.click()
            self.wait(3000)
            self.enter()
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
            self.wait(500)"""
            #if not self.find( "excluirrs", matching=0.97, waiting_time=10000):
                #self.not_found("excluirrs")
            #self.click()
            #if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                #self.not_found("simexcluirrs")
            #self.click()
            #self.enter()
            if not self.find( "notasfiscais_incluiref", matching=0.97, waiting_time=10000):
                self.not_found("notasfiscais_incluiref")
            self.click_relative(17, 195)
            if not self.find( "referencial", matching=0.97, waiting_time=10000):
                self.not_found("referencial")
            self.click_relative(223, 113)
            if not self.find( "referencial_calendario", matching=0.97, waiting_time=10000):
                self.not_found("referencial_calendario")
            self.click_relative(329, 275)
            if not self.find( "faturamento_referencial_ano_data", matching=0.97, waiting_time=10000):
                self.not_found("faturamento_referencial_ano_data")
            self.click_relative(359, 265)
            if not self.find( "faturamento_referencial_ano_data", matching=0.97, waiting_time=10000):
                self.not_found("faturamento_referencial_ano_data")
            self.click_relative(359, 265)
            if not self.find( "faturamento_tipo_documento", matching=0.97, waiting_time=10000):
                self.not_found("faturamento_tipo_documento")
            self.click_relative(593, 114)
            self.type_down()
            self.enter()
            self.wait(500)
            if not self.find( "referencia_documento", matching=0.97, waiting_time=10000):
                self.not_found("referencia_documento")
            self.click_relative(353, 132)
            if not self.find( "referencia_localizar", matching=0.97, waiting_time=10000):
                self.not_found("referencia_localizar")
            self.click_relative(107, 40)
            if not self.find( "referencia_marcar", matching=0.97, waiting_time=10000):
                self.not_found("referencia_marcar")
            self.click_relative(28, 185)
            if not self.find( "faturamento_selecionar_documentos_referenciados", matching=0.97, waiting_time=10000):
                self.not_found("faturamento_selecionar_documentos_referenciados")
            self.click()
            if not self.find( "notasficais_exluir", matching=0.97, waiting_time=10000):
                self.not_found("notasficais_exluir")
            self.click_relative(16, 243)
            if not self.find( "notasfiscais_sim_excluir", matching=0.97, waiting_time=10000):
                self.not_found("notasfiscais_sim_excluir")
            self.click_relative(416, 208)
            if not self.find( "notasfiscais_observações", matching=0.97, waiting_time=10000):
                self.not_found("notasfiscais_observações")
            self.click_relative(86, 220)
            if not self.find( "notas_fiscais_salvar", matching=0.97, waiting_time=10000):
                  self.not_found("notas_fiscais_salvar")
            self.click_relative(633, 39)
            self.type_keys_with_interval(1,'Nota feita com teste automatizado')
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---ROMANEIOS DE SAIDA---####
            
            if not self.find( "vendas2", matching=0.97, waiting_time=10000):
                self.not_found("vendas2")
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
            if not self.find( "b_rota_movRomaneios", matching=0.97, waiting_time=10000):
                self.not_found("b_rota_movRomaneios")
            self.click_relative(64, 195)
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
            #if not self.find( "s_busca_CMR", matching=0.97, waiting_time=10000):
            #    self.not_found("s_busca_CMR")
            #self.click()
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
                             
            if not self.find( "vendas2", matching=0.97, waiting_time=10000):
                self.not_found("vendas2")
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
                             
            if not self.find( "vendas2", matching=0.97, waiting_time=10000):
                self.not_found("vendas2")
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
                             
            if not self.find( "vendas2", matching=0.97, waiting_time=10000):
                self.not_found("vendas2")
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
                             
            if not self.find( "vendas2", matching=0.97, waiting_time=10000):
                self.not_found("vendas2")
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
                             
            if not self.find( "vendas2", matching=0.97, waiting_time=10000):
                self.not_found("vendas2")
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
                             
            if not self.find( "vendas2", matching=0.97, waiting_time=10000):
                self.not_found("vendas2")
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
            self.enter()
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
                             
            if not self.find( "vendas2", matching=0.97, waiting_time=10000):
                self.not_found("vendas2")
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
            self.click_relative(73, 157)
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
            self.click_relative(240, 202)
            self.type_keys_with_interval(1,'diferido')
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "b_centrocusto_Mfrete", matching=0.97, waiting_time=10000):
                self.not_found("b_centrocusto_Mfrete")
            self.click_relative(840, 260)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.backspace()
            if not self.find( "b_municipiocoleta_Mfrete", matching=0.97, waiting_time=10000):
                self.not_found("b_municipiocoleta_Mfrete")
            self.click_relative(69, 299)
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
            self.click_relative(440, 306)
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
            self.wait(1000)
            self.type_right()
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            self.type_right()
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
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
            self.enter()         
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---EMISSAO DE RPA---####
                             
            if not self.find( "vendas2", matching=0.97, waiting_time=10000):
                self.not_found("vendas2")
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
                             
            if not self.find( "vendas2", matching=0.97, waiting_time=10000):
                self.not_found("vendas2")
            self.click()
            if not self.find( "checagemdelancamentos", matching=0.97, waiting_time=10000):
                self.not_found("checagemdelancamentos")
            self.click()
            if not self.find( "b_calendario_checagemlanc", matching=0.97, waiting_time=10000):
                self.not_found("b_calendario_checagemlanc")
            self.click_relative(33, 6)          
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
                             
            if not self.find( "vendas2", matching=0.97, waiting_time=10000):
                self.not_found("vendas2")
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
            self.backspace()
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
            
            if not self.find( "vendas2", matching=0.97, waiting_time=10000):
                self.not_found("vendas2")
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
                             
            if not self.find( "vendas2", matching=0.97, waiting_time=10000):
                self.not_found("vendas2")
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
            if not self.find( "fechargestaoadm", matching=0.97, waiting_time=10000):
                self.not_found("fechargestaoadm")
            self.click()
            #self.enter()
            #if not self.find( "fechargestaoadm", matching=0.97, waiting_time=10000):
            #    self.not_found("fechargestaoadm")
            #self.click()
            if not self.find( "simfecharfim", matching=0.97, waiting_time=10000):
                self.not_found("simfecharfim")
            self.click()
            #self.enter()




            def not_found(self, label):
                print(f"Element not found: {label}")  
        
if __name__ == '__main__':
    Bot.main()



















































































































































































































