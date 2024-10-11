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
             
                            ####---PAISES---#### 

            self.wait(1500)
            if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro2")
            self.click()
            self.wait(1500)
            if not self.find( "parametrosfiscais", matching=0.97, waiting_time=10000):
                self.not_found("parametrosfiscais")
            self.double_click()
            #if not self.find( "parametrosfiscais", matching=0.97, waiting_time=10000):
            #    self.not_found("parametrosfiscais")
            #self.double_click()
            self.wait(1500)
            if not self.find( "regionalizacao", matching=0.97, waiting_time=10000):
                self.not_found("regionalizacao")
            self.click()
            if not self.find( "paises", matching=0.97, waiting_time=10000):
                self.not_found("paises")
            self.click()
            if not self.find( "localizar_pais", matching=0.97, waiting_time=10000):
                self.not_found("localizar_pais")
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
            if not self.find( "salvarpe", matching=0.97, waiting_time=10000):
                self.not_found("salvarpe")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()            
            if not self.find( "acharpais", matching=0.97, waiting_time=10000):
               self.not_found("acharpais")
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
            if not self.find( "retornar_paiseses", matching=0.97, waiting_time=10000):
                self.not_found("retornar_paiseses")
            self.click()
                            ####---REGIOES---####
                             
            if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro2")
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
            if not self.find( "salvarpaiseses", matching=0.97, waiting_time=10000):
                self.not_found("salvarpaiseses")
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
            if not self.find( "retronar_crop_actions", matching=0.97, waiting_time=10000):
                self.not_found("retronar_crop_actions")
            self.click()
            
                            ####---ESTADOS---####
                                         
            if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro2")
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
            if not self.find( "salvar_cadastro_estado", matching=0.97, waiting_time=10000):
                self.not_found("salvar_cadastro_estado")
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
            if not self.find( "retornar_paisisisi", matching=0.97, waiting_time=10000):
                self.not_found("retornar_paisisisi")
            self.click()
            
                            ####---MUNICIPIOS---####
                             
            if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro2")
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
            #if not self.find( "salvarpaises", matching=0.97, waiting_time=10000):
                #self.not_found("salvarpaises")
            #self.click()
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
            if not self.find( "cancelar_operacao", matching=0.97, waiting_time=10000):
                self.not_found("cancelar_operacao")
            self.click()
            #if not self.find( "savecommit", matching=0.97, waiting_time=10000):
                #self.not_found("savecommit")
            #self.click()
            #if not self.find( "excluirferiado", matching=0.97, waiting_time=10000):
                #self.not_found("excluirferiado")
            #self.click()
            #self.enter()
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
            if not self.find( "cancalar_paisisis", matching=0.97, waiting_time=10000):
                self.not_found("cancalar_paisisis")
            self.click()
            if not self.find( "confirmar_sim_excluir", matching=0.97, waiting_time=10000):
                self.not_found("confirmar_sim_excluir")
            self.click()
            if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
                self.not_found("retornarpe")
            self.click()
            if not self.find( "localizarpaises", matching=0.97, waiting_time=10000):
                self.not_found("localizarpaises")
            self.click()
            if not self.find( "retornar_cadastro", matching=0.97, waiting_time=10000):
                self.not_found("retornar_cadastro")
            self.click()
            
                            ####---GRUPO FISCAL DE ITENS---####
                             
            if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro2")
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
            if not self.find( "salvar-per", matching=0.97, waiting_time=10000):
             self.not_found("salvar-per")
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
            if not self.find( "retornar_aper", matching=0.97, waiting_time=10000):
                self.not_found("retornar_aper")
            self.click()
            
                            ####---CODIGOS DE OPERACAO---####
                             
            if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro2")
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
            if not self.find( "incluir_r0", matching=0.97, waiting_time=10000):
                self.not_found("incluir_r0")
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
            if not self.find( "dadosdaoperacao", matching=0.97, waiting_time=10000):
                self.not_found("dadosdaoperacao")
            self.click()
            if not self.find( "subir_tela_gamb", matching=0.97, waiting_time=10000):
                self.not_found("subir_tela_gamb")
            self.click()
            x=0
            while x<10:
                if not self.find( "subir_tela_escuro_gamb", matching=0.97, waiting_time=10000):
                    self.not_found("subir_tela_escuro_gamb")
                self.double_click()
                x=x+1
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
            if not self.find( "selecionar_codigos_fiscais", matching=0.97, waiting_time=10000):
                self.not_found("selecionar_codigos_fiscais")
            self.click()
            if not self.find( "tabeladeprecositens", matching=0.97, waiting_time=10000):
                self.not_found("tabeladeprecositens")
            self.click_relative(69, 30)
            if not self.find( "cod00000tabela", matching=0.97, waiting_time=10000):
                self.not_found("cod00000tabela")
            self.click()
            if not self.find( "selcionar_precos_consultas", matching=0.97, waiting_time=10000):
                self.not_found("selcionar_precos_consultas")
            self.click()
            self.backspace()
            self.backspace()
            if not self.find( "tabeladeprecosservicos", matching=0.97, waiting_time=10000):
                self.not_found("tabeladeprecosservicos")
            self.click_relative(61, 25)
            if not self.find( "cod00000tabela", matching=0.97, waiting_time=10000):
                self.not_found("cod00000tabela")
            self.click()
            if not self.find( "selecionar_laplaga", matching=0.97, waiting_time=10000):
                self.not_found("selecionar_laplaga")
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
            
            if not self.find( "salvar_exige_nota", matching=0.97, waiting_time=10000):
                self.not_found("salvar_exige_nota")
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
            
            if not self.find( "retornar_codigos_operacoes", matching=0.97, waiting_time=10000):
                self.not_found("retornar_codigos_operacoes")
            self.click()

            
                            ####---CODIGOS FISCAIS---####
            
            if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro2")
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
            if not self.find( "incluir_codigo_fiscais", matching=0.97, waiting_time=10000):
                self.not_found("incluir_codigo_fiscais")
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
            if not self.find( "selecionar_codigos_op", matching=0.97, waiting_time=10000):
                self.not_found("selecionar_codigos_op")
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
            self.space()
            self.space()
            #if not self.find( "ativoimobilizadomarcado2", matching=0.97, waiting_time=10000):
            #    self.not_found("ativoimobilizadomarcado2")
            #self.click()            
            #if not self.find( "ativoimobilizadomarcado", matching=0.97, waiting_time=10000):
            #    self.not_found("ativoimobilizadomarcado")
            #self.click()
            if not self.find( "materialdeusoeconsumolimpo", matching=0.97, waiting_time=10000):
                self.not_found("materialdeusoeconsumolimpo")
            self.click()            
            if not self.find( "materialdeusoeconsumo", matching=0.97, waiting_time=10000):
                self.not_found("materialdeusoeconsumo")
            self.click()
            self.space()           
            #if not self.find( "materialdeusoeconsumomarcado", matching=0.97, waiting_time=10000):
            #    self.not_found("materialdeusoeconsumomarcado")
            #self.click()
            if not self.find( "geraretencao", matching=0.97, waiting_time=10000):
                self.not_found("geraretencao")
            self.click()
            self.space()
            self.space()
            #if not self.find( "geraretencaomarcado2", matching=0.97, waiting_time=10000):
            #    self.not_found("geraretencaomarcado2")
            #self.click()           
            #if not self.find( "geraretencaomarcado", matching=0.97, waiting_time=10000):
            #    self.not_found("geraretencaomarcado")
            #self.click()
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
            if not self.find( "salvar_cfop", matching=0.97, waiting_time=10000):
                self.not_found("salvar_cfop")
            self.click()
            if not self.find( "retornar_cpo", matching=0.97, waiting_time=10000):
                self.not_found("retornar_cpo")
            self.click()
            if not self.find( "localizar_cpo", matching=0.97, waiting_time=10000):
                self.not_found("localizar_cpo")
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
            if not self.find( "transporte_localizar_0p", matching=0.97, waiting_time=10000):
                self.not_found("transporte_localizar_0p")
            self.click()          
            if not self.find( "retornar_cf0p", matching=0.97, waiting_time=10000):
                self.not_found("retornar_cf0p")
            self.click() 
                            ####---CODIGOS FISCAIS IMP---####
                             
            if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro2")
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
            if not self.find( "inclusao", matching=0.97, waiting_time=10000):
                self.not_found("inclusao")
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
            if not self.find( "selecionar_cod_fisca", matching=0.97, waiting_time=10000):
                self.not_found("selecionar_cod_fisca")
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
            if not self.find( "salvar_cadastro_CFOP", matching=0.97, waiting_time=10000):
                self.not_found("salvar_cadastro_CFOP")
            self.double_click_relative(294, 37)
            #if not self.find( "salvarco", matching=0.97, waiting_time=10000):
            #   self.not_found("salvarco")
            #self.click()
            #if not self.find( "salvarco", matching=0.97, waiting_time=10000):
            #    self.not_found("salvarco")
            #self.click()
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
                             
            if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro2")
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
            
            self.wait(1500)
            if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro2")
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
            if not self.find( "retornarpe", matching=0.97, waiting_time
                             =10000):
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





























































































