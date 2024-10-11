from botcity.core import DesktopBot

class Bot(DesktopBot):
        def action(self, execution=None):

            #######################-----LOGIN-----############################
        
            #self.execute(r"C:\Users\Rafael\Desktop\2207\faturamento.exe")
            self.execute(r"C:\Users\Rafael\Desktop\2207\teste23\23mes07\faturamento.exe")
            
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
             
                            ####---REDES SOCIAIS---#### 
            
            self.wait(1500)
            if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=100000):
                self.not_found("abrircadastros_abacadastro2")
            self.click()
            self.wait(1500)
            if not self.find( "redessociais", matching=0.97, waiting_time=10000):
                self.not_found("redessociais")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            self.wait(1000)            
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            self.wait(3000)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            self.wait(1000)
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
            
                            ####---AVALIACOES ISO---####
                             
            if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro2")
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
            
                            ####---LINHAS, RAMOS, ATIVIDADES ETC---####
                             
            if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro2")
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
            
                            ####---VENDEDORES, COMPRADORES---####
            
            if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro2")
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
            self.enter()
            #if not self.find( "confirmaexcluiraba2vcr", matching=0.97, waiting_time=10000):
            #    self.not_found("confirmaexcluiraba2vcr")
            #self.click()
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
            
                            ####---ENQUETES---####
            
            if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro2")
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
            
                            ####---ITENS DE ESTOQUE---####
                             
            if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro2")
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
            if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                self.not_found("simexcluirrs")
            self.click()
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
            if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                self.not_found("simexcluirrs")
            self.click()
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
            if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                self.not_found("simexcluirrs")
            self.click()
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
            self.tab()
            if not self.find( "gravarNCMIE", matching=0.97, waiting_time=10000):
                self.not_found("gravarNCMIE")
            self.click()
            if not self.find( "paranaNCMIE", matching=0.97, waiting_time=10000):
                self.not_found("paranaNCMIE")
            self.click()
            if not self.find( "excluirregistroNCMIE", matching=0.97, waiting_time=10000):
                self.not_found("excluirregistroNCMIE")
            self.click_relative(7, 57)
            self.enter()
            #if not self.find( "simexcluirNCMIE", matching=0.97, waiting_time=10000):
            #    self.not_found("simexcluirNCMIE")
            #self.click()
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
            
                            ####---CADASTRO DE ITENS---####
            
                             
            if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro2")
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
            if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                self.not_found("simexcluirrs")
            self.click()
            if not self.find( "cadastroitensreferencia", matching=0.97, waiting_time=10000):
                self.not_found("cadastroitensreferencia")
            self.click_relative(718, 91)
            self.type_keys_with_interval(1,'te12!@')
            self.enter()
            self.enter()
            if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                self.not_found("simexcluirrs")
            self.click()
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
            """
            if not self.find( "operacaocalculoprecoci", matching=0.97, waiting_time=10000):
                self.not_found("operacaocalculoprecoci")
            self.click_relative(55, 23)
            self.tab()
            self.tab()
            self.tab()
            self.type_down()
            
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
            """
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
            x=0
            while x<6:
                self.tab()
                x=x+1
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
            #self.tab()
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
            self.tab()
            x=0
            while x<13:
                self.type_keys_with_interval(1,'123')
                self.tab()
                x=x+1
            self.wait(500)
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
            self.wait(1500)
            if not self.find( "salvarenquete", matching=0.97, waiting_time=10000):
                self.not_found("salvarenquete")
            self.click()
            self.enter()
            self.enter()
            """
            if not self.find( "salvar", matching=0.97, waiting_time=10000):
                self.not_found("salvar")
            self.click()
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
            """

            
            
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
            self.type_keys_with_interval(1,'104455')
            self.enter()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.type_keys_with_interval(1,'1')
            if not self.find( "confirmaritemCIaba2p2", matching=0.97, waiting_time=10000):
                self.not_found("confirmaritemCIaba2p2")
            self.click()
            self.wait(3000)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "excluirregistroa2p2.1_CI", matching=0.97, waiting_time=10000):
                self.not_found("excluirregistroa2p2.1_CI")
            self.click_relative(17, 163)           
            if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                self.not_found("simexcluirrs")
            self.click()
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
            self.type_keys_with_interval(1,'104455')
            self.enter()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.type_keys_with_interval(1,'1')
            if not self.find( "confirmaritemCIaba2p2", matching=0.97, waiting_time=10000):
                self.not_found("confirmaritemCIaba2p2")
            self.click()
            self.wait(3000)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "excluirregistroa2p2.1_CI", matching=0.97, waiting_time=10000):
                self.not_found("excluirregistroa2p2.1_CI")
            self.click_relative(17, 163)
            if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                self.not_found("simexcluirrs")
            self.click()
            
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
            self.type_keys_with_interval(1,'104455')
            self.enter()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.type_keys_with_interval(1,'1')
            if not self.find( "confirmaritemCIaba2p2", matching=0.97, waiting_time=10000):
                self.not_found("confirmaritemCIaba2p2")
            self.click()
            self.wait(3000)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "excluirregistroa2p4_CI", matching=0.97, waiting_time=10000):
                self.not_found("excluirregistroa2p4_CI")
            self.click_relative(16, 187)
                       
            if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                self.not_found("simexcluirrs")
            self.click()
            
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
            if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                self.not_found("simexcluirrs")
            self.click()
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
            if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                self.not_found("simexcluirrs")
            self.click()
            
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
            
            if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                self.not_found("simexcluirrs")
            self.click()
            
                
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
            if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                self.not_found("simexcluirrs")
            self.click()
            
            
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
            if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                self.not_found("simexcluirrs")
            self.click()

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
            if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                self.not_found("simexcluirrs")
            self.click() 
            self.tab()
            self.type_keys_with_interval(1,'te12!@')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.enter()
            if not self.find( "excluirregistroa2p2.1_CI", matching=0.97, waiting_time=10000):
                self.not_found("excluirregistroa2p2.1_CI")
            self.click_relative(17, 163)
            if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                self.not_found("simexcluirrs")
            self.click()
            
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
            if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                self.not_found("simexcluirrs")
            self.click()
                             
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
            if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                self.not_found("simexcluirrs")
            self.click()
            
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
            
            
            
                            ####---FORMULAS---####
                             
            if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro2")
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
            self.enter()        
            #if not self.find( "simabandonar", matching=0.97, waiting_time=10000):
            #    self.not_found("simabandonar")
            #self.click()
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()
            if not self.find( "simexcluirrs", matching=0.97, waiting_time=10000):
                self.not_found("simexcluirrs")
            self.click()
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
            self.enter()  
            #if not self.find( "simabandonar", matching=0.97, waiting_time=10000):
            #    self.not_found("simabandonar")
            #self.click()
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
                             
            if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro2")
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
            
                            ####---DESCONTO POR AGRUPAMENTO---####
                             
            if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro2")
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
                             
            if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro2")
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
            
                            ####---SERVIÇOS---####
                             
            if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                    self.not_found("abrircadastros_abacadastro2")
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
            


                            ####---CADASTROS AUXILIARES---####
                             
            if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro2")
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
            
                            ####---PLANO DE CONTAS, CUSTOS E FINANCEIRO---####
                             
            if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro2")
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
            self.enter()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.enter()
            self.wait(500)
            #if not self.find( "okerronaoencontrado", matching=0.97, waiting_time=10000):
            #    self.not_found("okerronaoencontrado")
            #self.click()
            self.backspace()
            self.wait(500)
            if not self.find( "centrodecustofinalPC", matching=0.97, waiting_time=10000):
                self.not_found("centrodecustofinalPC")
            self.click_relative(142, 40)
            self.enter()
            self.backspace()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.enter()
            #if not self.find( "okerronaoencontrado", matching=0.97, waiting_time=10000):
            #    self.not_found("okerronaoencontrado")
            #self.click()
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
            if not self.find( "sairsistemapa", matching=0.97, waiting_time=10000):
                self.not_found("sairsistemapa")
            self.click()
            if not self.find( "simsairsistemapa", matching=0.97, waiting_time=10000):
                self.not_found("simsairsistemapa")
            self.click()
            #self.enter()
            

            def not_found(self, label):
                print(f"Element not found: {label}")
if __name__ == '__main__':
    Bot.main()





























































































































































































































