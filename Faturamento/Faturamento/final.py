from botcity.core import DesktopBot

class Bot(DesktopBot):
        def action(self, execution=None):

            #######################-----LOGIN-----############################
        
            self.execute(r"C:\Users\Rafael\Desktop\2207\faturamento.exe")
            
            if not self.find( "btn_codigo_usuario", matching=0.97, waiting_time=100000):
                self.not_found("btn_codigo_usuario")
            self.click_relative(47, 12)
                    
            self.type_keys_with_interval(1,"999")
            self.type_keys_with_interval(1,"tsfmx24")
            self.enter()

            if not self.find( "btn_login", matching=0.97, waiting_time=10000):
                self.not_found("btn_login")
            self.click()
            self.enter()

            ###################################################################
             
            if not self.find( "utilitarios", matching=0.97, waiting_time=10000):
                self.not_found("utilitarios")
            self.click()
            self.type_down()
            self.type_down()
            if not self.find( "agenda_telefonica", matching=0.97, waiting_time=10000):
                self.not_found("agenda_telefonica")
            self.click()
            self.enter()
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()
            x=0
            while x<6:
                self.type_keys_with_interval(1,'te12!@')
                self.tab()
                x=x+1
            if not self.find( "b_municipio_agendatelefonica", matching=0.97, waiting_time=10000):
                self.not_found("b_municipio_agendatelefonica")
            self.click_relative(156, 234)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "b_ramoAtividade_agendaTelefonica", matching=0.97, waiting_time=10000):
                self.not_found("b_ramoAtividade_agendaTelefonica")
            self.click_relative(155, 258)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.tab()
            self.tab()
            self.type_keys_with_interval(1,'testeteorema@testeteorema.com')
            if not self.find( "email_agendaTelefonica", matching=0.97, waiting_time=10000):
                self.not_found("email_agendaTelefonica")
            self.click_relative(607, 278)
            self.wait(1000)         
            if not self.find( "fecharemail1", matching=0.97, waiting_time=10000):
                self.not_found("fecharemail1")
            self.click_relative(425, 10)
            self.wait(1000)
            if not self.find( "fecharemail2", matching=0.97, waiting_time=10000):
                self.not_found("fecharemail2")
            self.click()
            self.tab()
            self.type_keys_with_interval(1,'www.google.com.br')
            if not self.find( "abreSite_agendaTelefonica", matching=0.97, waiting_time=10000):
                self.not_found("abreSite_agendaTelefonica")
            self.click()
            if not self.find( "fechargoogle", matching=0.97, waiting_time=10000):
                self.not_found("fechargoogle")
            self.click_relative(213, 9)       
            self.tab()
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "salvarrs", matching=0.97, waiting_time=10000):
                self.not_found("salvarrs")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            self.wait(500)
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()            
            if not self.find( "cod_teste_agendaTelefonica", matching=0.97, waiting_time=10000):
                self.not_found("cod_teste_agendaTelefonica")
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
            self.wait(500)
            self.enter()
            self.wait(500)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            self.wait(500)
            
                            ####---LIGACOES TELEFONICAS---####
                             
            if not self.find( "utilitarios", matching=0.97, waiting_time=10000):
                self.not_found("utilitarios")
            self.click()
            if not self.find( "ligacoesTelefonicas", matching=0.97, waiting_time=10000):
                self.not_found("ligacoesTelefonicas")
            self.click()
            self.tab()
            x=0
            while x<5:
                self.type_keys_with_interval(1,'123')
                self.tab()
                x=x+1
            self.tab()
            self.tab()
            x=0
            while x<4:
                self.backspace()
                self.tab()
                x=x+1
            self.tab()
            self.backspace()
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()
            if not self.find( "selecaoTela_ligacaoTelefonica", matching=0.97, waiting_time=10000):
                self.not_found("selecaoTela_ligacaoTelefonica")
            self.click_relative(175, 79)
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            x=0
            while x<4:
                self.type_keys_with_interval(1,'te12!@')
                self.tab()
                x=x+1
            self.backspace()
            if not self.find( "b_solicitante_ligacaoTelefonica", matching=0.97, waiting_time=10000):
                self.not_found("b_solicitante_ligacaoTelefonica")
            self.click_relative(160, 286)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            if not self.find( "salvar_fundoClaro", matching=0.97, waiting_time=10000):
                self.not_found("salvar_fundoClaro")
            self.click()
            if not self.find( "retornar_fundoClaro", matching=0.97, waiting_time=10000):
                self.not_found("retornar_fundoClaro")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click() 
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            if not self.find( "excluir_fundoClaro", matching=0.97, waiting_time=10000):
                self.not_found("excluir_fundoClaro")
            self.click()
            self.enter()
            if not self.find( "retornar_fundoClaro", matching=0.97, waiting_time=10000):
                self.not_found("retornar_fundoClaro")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click() 
            self.wait(500)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---AGENDA COMPROMISSOS---####

            if not self.find( "utilitarios", matching=0.97, waiting_time=10000):
                self.not_found("utilitarios")
            self.click()
            if not self.find( "agendaCompromissos", matching=0.97, waiting_time=10000):
                self.not_found("agendaCompromissos")
            self.click()
            if not self.find( "refresh", matching=0.97, waiting_time=10000):
                self.not_found("refresh")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---ALTERA DATA---####
                             
            if not self.find( "utilitarios", matching=0.97, waiting_time=10000):
                self.not_found("utilitarios")
            self.click()
            if not self.find( "alteraData", matching=0.97, waiting_time=10000):
                self.not_found("alteraData")
            self.click()
            self.type_keys_with_interval(1,'123')
            self.tab()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---CALCULADORA---####
                             
            if not self.find( "utilitarios", matching=0.97, waiting_time=10000):
                self.not_found("utilitarios")
            self.click()
            if not self.find( "calculadora", matching=0.97, waiting_time=10000):
                self.not_found("calculadora")
            self.click()
            if not self.find( "fechar_calculadora", matching=0.97, waiting_time=10000):
                self.not_found("fechar_calculadora")
            self.click_relative(280, 10)
            
            
                            ####---CALENDARIO---####
                             
            if not self.find( "utilitarios", matching=0.97, waiting_time=10000):
                self.not_found("utilitarios")
            self.click()
            if not self.find( "calendario", matching=0.97, waiting_time=10000):
                self.not_found("calendario")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---RECADOS---####
                             
            if not self.find( "utilitarios", matching=0.97, waiting_time=10000):
                self.not_found("utilitarios")
            self.click()
            if not self.find( "recados", matching=0.97, waiting_time=10000):
                self.not_found("recados")
            self.click()
            self.tab()
            self.tab()
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'123')
            self.tab()
            self.type_keys_with_interval(1,'cadastro')
            self.tab()
            self.tab()
            self.type_right()
            self.tab()
            self.type_right()
            self.type_right()
            if not self.find( "incluirpe", matching=0.97, waiting_time=10000):
                self.not_found("incluirpe")
            self.click()
            if not self.find( "b_para_recados", matching=0.97, waiting_time=10000):
                self.not_found("b_para_recados")
            self.click_relative(33, 200)
            if not self.find( "selecionarmunicipiovcr", matching=0.97, waiting_time=10000):
                self.not_found("selecionarmunicipiovcr")
            self.click()
            self.wait(500)
            self.tab()
            self.tab()
            x=0
            while x<5:
                self.type_keys_with_interval(1,'te12!@')
                self.tab()
                x=x+1
            self.space()
            self.space()
            self.tab()
            self.type_keys_with_interval(1,'te12!@')
            if not self.find( "cancelar_recado", matching=0.97, waiting_time=10000):
                self.not_found("cancelar_recado")
            self.click()
            self.enter()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "editarfim", matching=0.97, waiting_time=10000):
                self.not_found("editarfim")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---ABERTURA DE CHAMADOS---####
                             
            if not self.find( "utilitarios", matching=0.97, waiting_time=10000):
                self.not_found("utilitarios")
            self.click()
            if not self.find( "aberturaChamados", matching=0.97, waiting_time=10000):
                self.not_found("aberturaChamados")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click() 
            self.wait(5000)
            if not self.find( "editarChamado", matching=0.97, waiting_time=10000):
                self.not_found("editarChamado")
            self.click()
            if not self.find( "retornarChamado", matching=0.97, waiting_time=10000):
                self.not_found("retornarChamado")
            self.click_relative(33, 36)
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            
                            ####---SOBRE---####

            if not self.find( "ajuda", matching=0.97, waiting_time=10000):
                self.not_found("ajuda")
            self.click()
            self.type_down()
            self.type_down()
            if not self.find( "abrir_outro", matching=0.97, waiting_time=10000):
                self.not_found("abrir_outro")
            self.click_relative(18, -37)
            
            
            self.type_right()
            self.enter()
            
                            ####---INFORMACOES RELEASE---####
            
            if not self.find( "ajuda", matching=0.97, waiting_time=10000):
                self.not_found("ajuda")
            self.click()                 
            if not self.find( "informacoesRelease", matching=0.97, waiting_time=10000):
                self.not_found("informacoesRelease")
            self.click()
            if not self.find( "voltar_infReleases", matching=0.97, waiting_time=10000):
                self.not_found("voltar_infReleases")
            self.click()
            if not self.find( "fechargestaoadm", matching=0.97, waiting_time=10000):
                self.not_found("fechargestaoadm")
            self.click()
            if not self.find( "simfecharfim", matching=0.97, waiting_time=10000):
                self.not_found("simfecharfim")
            self.click()
            
            
            ########################---GAMBIARRA
            """
            if not self.find( "CONFIGCLIENTES_aba2", matching=0.97, waiting_time=10000):
                self.not_found("CONFIGCLIENTES_aba2")
            self.click()
            if not self.find( "CONFIGCLIENTES_retirarclientes", matching=0.97, waiting_time=10000):
                self.not_found("CONFIGCLIENTES_retirarclientes")
            self.click_relative(-53, 122)
            if not self.find( "CONFIGCLIENTES_aba1", matching=0.97, waiting_time=10000):
                self.not_found("CONFIGCLIENTES_aba1")
            self.click()
            self.enter()
            """
            ########################---GAMBIARRA
            """ 
            if not self.find( "aba2_CO_manutençãoteste", matching=0.97, waiting_time=10000):
                self.not_found("aba2_CO_manutençãoteste")
            self.click()
            if not self.find( "op_Todas_manutencaoTeste_CO", matching=0.97, waiting_time=10000):
                self.not_found("op_Todas_manutencaoTeste_CO")
            self.click_relative(-3, 249)
            """
            
            
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             
             

            



def not_found(self, label):
                print(f"Element not found: {label}")  
        
if __name__ == '__main__':
    Bot.main()


































