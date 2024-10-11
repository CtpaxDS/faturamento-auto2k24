from botcity.core import DesktopBot

class Bot(DesktopBot):
        def action(self, execution=None):

            #######################-----LOGIN-----############################
        
            #self.execute(r"C:\Users\Rafael\Desktop\2207\faturamento.exe")
            self.execute(r"C:\teorema\bin\\faturamento.exe")
            
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

            self.wait(1500)
            if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro2")
            self.click()
            self.wait(1500)
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
            self.wait(3000)
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()
            self.wait(2000)
            
            
            self.type_keys_with_interval(1,'te12!@')
        
            #self.type_right()
            #self.type_right()
            #if not self.find( "cpfcadastrocliente", matching=0.97, waiting_time=10000):
            #    self.not_found("cpfcadastrocliente")
            #self.click_relative(3, 25
            
            
            #self.enter()
            self.tab()
            self.type_keys_with_interval(1,'187.036.350-74')
            self.tab()
            self.type_keys_with_interval(1,'14.734.534-8')
            self.enter()
            #self.type_keys_with_interval(100,'te12!@')
            #self.tab()
            self.type_keys_with_interval(100,'01012022')
            self.tab()
            self.tab()
            self.type_keys_with_interval(1,"12021999")
            
            
            
                            ####---ABA1 CADASTRO---####
                             
            self.type_keys_with_interval(1,'te12!@')
            self.tab()
            self.type_keys_with_interval(1,'te12!@')
            self.tab()
            self.type_keys_with_interval(1,'te12!@')
            self.tab()
            self.type_keys_with_interval(10,'85055370')
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
            if not self.find( "selecionar_munip", matching=0.97, waiting_time=10000):
                self.not_found("selecionar_munip")
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
            self.tab()
            self.type_keys_with_interval(1,"222")
            self.tab()
            self.type_keys_with_interval(1,"302")
            '''
            x=0
            while x<8:
                if not self.find( "operadoratelcel", matching=0.97, waiting_time=10000):
                    self.not_found("operadoratelcel")
                self.click_relative(533, 131)                              
                self.type_down()
                self.enter()
                x=x+1
            '''    
           
            if not self.find( "local_google", matching=0.97, waiting_time=10000):
                self.not_found("local_google")
            self.click()
            self.tab()
            self.wait(5000)
        
                            ####---PESSOA FISICA---####
                             
            #if not self.find( "nomefantasiapessoafisica", matching=0.97, waiting_time=10000):
                #self.not_found("nomefantasiapessoafisica")
            #self.click_relative(13, 45)
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(1,'121212')
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
            self.type_keys_with_interval(1,'0001')
           
            if not self.find( "selecionar_munips", matching=0.97, waiting_time=10000):
             self.not_found("selecionar_munips")
            self.click()
            self.enter()
            self.enter()
            self.type_keys_with_interval(1,'te12!@')
            self.tab()
            self.tab()
            
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
            if not self.find( "addcont_emais_01", matching=0.97, waiting_time=10000):
                self.not_found("addcont_emais_01")
            self.click_relative(429, 5)
            if not self.find( "close_email_ctl", matching=0.97, waiting_time=10000):
                self.not_found("close_email_ctl")
            self.click()
            if not self.find( "e-mail_doc", matching=0.97, waiting_time=10000):
                self.not_found("e-mail_doc")
            self.click_relative(103, 28)
            self.type_keys_with_interval(1,'emailtesteteorema123@gmail.com')
            if not self.find( "botaoemail2cft", matching=0.97, waiting_time=10000):
                self.not_found("botaoemail2cft")
            self.click_relative(868, 43)
            if not self.find( "addacont_close", matching=0.97, waiting_time=10000):
                self.not_found("addacont_close")
            self.click_relative(425, 9)
            if not self.find( "close_email_", matching=0.97, waiting_time=10000):
                self.not_found("close_email_")
            self.click()
            if not self.find( "skypecft", matching=0.97, waiting_time=10000):
                self.not_found("skypecft")
            self.click_relative(21, 25)           
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.type_keys_with_interval(1,'www.google.com.br')
            """if not self.find( "abrirsiteinternetexp", matching=0.97, waiting_time=10000):
                self.not_found("abrirsiteinternetexp")
            self.click()
            if not self.find( "fechargooglecerto", matching=0.97, waiting_time=10000):
                self.not_found("fechargooglecerto")
            self.click_relative(1260, 6)"""            
            if not self.find( "idmarketplace", matching=0.97, waiting_time=10000):
                self.not_found("idmarketplace")
            self.click_relative(10, 28)
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "contatodadosdecontato", matching=0.97, waiting_time=10000):
                self.not_found("contatodadosdecontato")
            self.click_relative(925, 89)
            self.type_keys_with_interval(1,'te12!@')
            
                            ####---MARCADORES---####
                             
            self.tab()                 
            #if not self.find( "clientemarcadores", matching=0.97, waiting_time=10000):
            #    self.not_found("clientemarcadores")
            #self.click()
            #self.space()
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
            while x<16:
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
            if not self.find( "selecionar_local_cobranca", matching=0.97, waiting_time=10000):
                self.not_found("selecionar_local_cobranca")
            self.click()
            if not self.find( "vendedorcompradorcft", matching=0.97, waiting_time=10000):
                self.not_found("vendedorcompradorcft")
            self.click_relative(64, 26)
            #if not self.find( "cod00101cft", matching=0.97, waiting_time=10000):
            #    self.not_found("cod00101cft")
            #self.click()
            if not self.find( "selecionar_cft", matching=0.97, waiting_time=10000):
                self.not_found("selecionar_cft")
            self.click()
            if not self.find( "classificacaocft", matching=0.97, waiting_time=10000):
                self.not_found("classificacaocft")
            self.click_relative(69, 25)
            if not self.find( "retornar_consulta_classificacao", matching=0.97, waiting_time=10000):
                self.not_found("retornar_consulta_classificacao")
            self.click()
            if not self.find( "codcontabilfixocft", matching=0.97, waiting_time=10000):
                self.not_found("codcontabilfixocft")
            self.click_relative(65, 25)
            self.type_keys_with_interval(1,"00051")
            if not self.find( "cod00051cft", matching=0.97, waiting_time=10000):
                self.not_found("cod00051cft")
            self.click()
            if not self.find( "selecionar_cft", matching=0.97, waiting_time=10000):
                self.not_found("selecionar_cft")
            self.click()
            if not self.find( "tabeladeprecositenscft", matching=0.97, waiting_time=10000):
                self.not_found("tabeladeprecositenscft")
            self.click_relative(66, 25)
            if not self.find( "cod00000cft", matching=0.97, waiting_time=10000):
                self.not_found("cod00000cft")
            self.click()
            if not self.find( "selecionar_precos", matching=0.97, waiting_time=10000):
                self.not_found("selecionar_precos")
            self.click()
            self.backspace()
            if not self.find( "transportadoragrupamentocft", matching=0.97, waiting_time=10000):
                self.not_found("transportadoragrupamentocft")
            self.click_relative(86, 256)            
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "cod_0006241", matching=0.97, waiting_time=10000):
                self.not_found("cod_0006241")
            self.click()
            if not self.find( "selecionar_consultas_transportes", matching=0.97, waiting_time=10000):
                self.not_found("selecionar_consultas_transportes")
            self.click()
            if not self.find( "ramodeatividadecft", matching=0.97, waiting_time=10000):
                self.not_found("ramodeatividadecft")
            self.click_relative(68, 24)
            if not self.find( "cod00001cft", matching=0.97, waiting_time=10000):
                self.not_found("cod00001cft")
            self.click()
            if not self.find( "selecionar_ramu_atividade", matching=0.97, waiting_time=10000):
                self.not_found("selecionar_ramu_atividade")
            self.click()
            if not self.find( "planofinanceirocft", matching=0.97, waiting_time=10000):
                self.not_found("planofinanceirocft")
            self.click_relative(83, 26)
            if not self.find( "cod_000000032", matching=0.97, waiting_time=10000):
                self.not_found("cod_000000032")
            self.click()       
            if not self.find( "selecionar_plano_fincaneiro", matching=0.97, waiting_time=10000):
                self.not_found("selecionar_plano_fincaneiro")
            self.click()
            if not self.find( "contacorrentecft", matching=0.97, waiting_time=10000):
                self.not_found("contacorrentecft")
            self.click_relative(68, 26)
            if not self.find( "cod001cft", matching=0.97, waiting_time=10000):
                self.not_found("cod001cft")
            self.click()
            if not self.find( "selecionar_contas", matching=0.97, waiting_time=10000):
                self.not_found("selecionar_contas")
            self.click()
            if not self.find( "segmentocft", matching=0.97, waiting_time=10000):
                self.not_found("segmentocft")
            self.click_relative(66, 24)
            if not self.find( "cod00001cft", matching=0.97, waiting_time=10000):
                self.not_found("cod00001cft")
            self.click()
            if not self.find( "selecionar_segmentos", matching=0.97, waiting_time=10000):
                self.not_found("selecionar_segmentos")
            self.click()
            if not self.find( "tabeladeprecosservicoscft", matching=0.97, waiting_time=10000):
                self.not_found("tabeladeprecosservicoscft")
            self.click_relative(66, 31)
            if not self.find( "cod00000cft", matching=0.97, waiting_time=10000):
                self.not_found("cod00000cft")
            self.click()
            if not self.find( "selecionar_precos_00012", matching=0.97, waiting_time=10000):
                self.not_found("selecionar_precos_00012")
            self.click()
            self.backspace()
            if not self.find( "condicaodepagamento", matching=0.97, waiting_time=10000):
                self.not_found("condicaodepagamento")
            self.click_relative(67, 26)
            self.type_keys_with_interval(1,"0048")
            if not self.find( "cod0048cft", matching=0.97, waiting_time=10000):
                self.not_found("cod0048cft")
            self.click()
            if not self.find( "condicao_de_pagamento_selecionar", matching=0.97, waiting_time=10000):
                self.not_found("condicao_de_pagamento_selecionar")
            self.click()
            if not self.find( "comissaocft", matching=0.97, waiting_time=10000):
                self.not_found("comissaocft")
            self.click_relative(68, 27)
            if not self.find( "cod001cft", matching=0.97, waiting_time=10000):
                self.not_found("cod001cft")
            self.click()
            if not self.find( "selecionar_comissao", matching=0.97, waiting_time=10000):
                self.not_found("selecionar_comissao")
            self.click()
            if not self.find( "centrodecustocft", matching=0.97, waiting_time=10000):
                self.not_found("centrodecustocft")
            self.click_relative(85, 27)
            if not self.find( "cod001cft", matching=0.97, waiting_time=10000):
                self.not_found("cod001cft")
            self.click()
            if not self.find( "selecionar_centro_de_Custo", matching=0.97, waiting_time=10000):
                self.not_found("selecionar_centro_de_Custo")
            self.click()
            self.backspace()
            if not self.find( "codigocontabilfixocft", matching=0.97, waiting_time=10000):
                self.not_found("codigocontabilfixocft")
            self.click_relative(66, 26)
            self.type_keys_with_interval(1,"0051")
            if not self.find( "cod00051cft", matching=0.97, waiting_time=10000):
                self.not_found("cod00051cft")
            self.click()
            if not self.find( "selecionar_planos_de_contas", matching=0.97, waiting_time=10000):
                self.not_found("selecionar_planos_de_contas")
            self.click()
            if not self.find( "linhacft", matching=0.97, waiting_time=10000):
                self.not_found("linhacft")
            self.click_relative(67, 26)
            if not self.find( "retornar_consulta_linhas", matching=0.97, waiting_time=10000):
                self.not_found("retornar_consulta_linhas")
            self.click()
            if not self.find( "operacaopdvbalcaocft", matching=0.97, waiting_time=10000):
                self.not_found("operacaopdvbalcaocft")
            self.click_relative(67, 26)
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "cod0001", matching=0.97, waiting_time=10000):
                self.not_found("cod0001")
            self.click()      
            if not self.find( "selecionar_codigos_operacao", matching=0.97, waiting_time=10000):
                self.not_found("selecionar_codigos_operacao")
            self.click()
            
                            ####---ABA2 P2 CFT---####
                
            if not self.find( "aba2p2cft", matching=0.97, waiting_time=10000):
                self.not_found("aba2p2cft")
            self.click()
            if not self.find( "codigocontabilclientescft", matching=0.97, waiting_time=10000):
                self.not_found("codigocontabilclientescft")
            self.click_relative(63, 27)
            self.type_keys_with_interval(1,"00051")
            if not self.find( "cod00051cft", matching=0.97, waiting_time=10000):
                self.not_found("cod00051cft")
            self.click()
            if not self.find( "selecionar_plano_accont", matching=0.97, waiting_time=10000):
                self.not_found("selecionar_plano_accont")
            self.click()
            if not self.find( "codigocontabilfornecedorescft", matching=0.97, waiting_time=10000):
                self.not_found("codigocontabilfornecedorescft")
            self.click_relative(65, 25)
            self.type_keys_with_interval(1,"00051")
            if not self.find( "cod00051cft", matching=0.97, waiting_time=10000):
                self.not_found("cod00051cft")
            self.click()
            if not self.find( "selecionar_plans_accont", matching=0.97, waiting_time=10000):
                self.not_found("selecionar_plans_accont")
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
            if not self.find( "addnovoregistroa2p3_CFT", matching=0.97, waiting_time=10000):
                self.not_found("addnovoregistroa2p3_CFT")
            self.click_relative(11, 162)
            self.enter()
            if not self.find( "aba2cftparte2", matching=0.97, waiting_time=10000):
                self.not_found("aba2cftparte2")
            self.click()
            self.enter()
            if not self.find( "aba2cftparte2", matching=0.97, waiting_time=10000):
                self.not_found("aba2cftparte2")
            self.click()           
            if not self.find( "codcontabilclientecft", matching=0.97, waiting_time=10000):
                self.not_found("codcontabilclientecft")
            self.click_relative(-110, 50)
            self.enter()
            self.type_keys_with_interval(1,"00051")          
            if not self.find( "cod00051cft", matching=0.97, waiting_time=10000):
                self.not_found("cod00051cft")
            self.click()
            if not self.find( "selecionar_plans_acccont", matching=0.97, waiting_time=10000):
                self.not_found("selecionar_plans_acccont")
            self.click()
            self.wait(500)
            self.enter()
            self.wait(500)
            self.enter()
            if not self.find( "aba2cftparte2", matching=0.97, waiting_time=10000):
                self.not_found("aba2cftparte2")
            self.click()
            if not self.find( "codigocontabilfornecedor", matching=0.97, waiting_time=10000):
                self.not_found("codigocontabilfornecedor")
            self.click_relative(60, 26)
            self.enter()
            self.type_keys_with_interval(1,"00051")
            if not self.find( "cod00051cft", matching=0.97, waiting_time=10000):
                self.not_found("cod00051cft")
            self.click()
            if not self.find( "selecionar_plan_accont", matching=0.97, waiting_time=10000):
                self.not_found("selecionar_plan_accont")
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
                             
            #if not self.find( "inserirfotocft", matching=0.97, waiting_time=10000):
            #    self.not_found("inserirfotocft")
            #self.click()
            #self.key_esc()
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
            self.type_keys_with_interval(1,"0525")
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
            self.type_keys_with_interval(1,"0525")
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
            #if not self.find( "codtestecfta6p6", matching=0.97, waiting_time=10000):
            #    self.not_found("codtestecfta6p6")
            #self.click_relative(-98, 7)
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
            self.enter()
            self.key_esc()
            self.key_esc()
            #if not self.find( "cancelaarqteste1", matching=0.97, waiting_time=10000):
            #    self.not_found("cancelaarqteste1")
            #self.click_relative(5, 184)
            #if not self.find( "retornaanexoarqteste1", matching=0.97, waiting_time=10000):
            #    self.not_found("retornaanexoarqteste1")
            #self.click_relative(25, 41)          
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
            if not self.find( "fecharsistemacft", matching=0.97, waiting_time=10000):
                self.not_found("fecharsistemacft")
            self.click()
            if not self.find( "simexcluircft1", matching=0.97, waiting_time=10000):
                self.not_found("simexcluircft1")
            self.click()
            #self.enter()
            
            
            

            def not_found(self, label):
                print(f"Element not found: {label}")
if __name__ == '__main__':
    Bot.main()








































































































































































































































