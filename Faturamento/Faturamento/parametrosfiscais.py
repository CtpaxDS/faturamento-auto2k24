from botcity.core import DesktopBot

class Bot(DesktopBot):
        def action(self, execution=None):

            #######################-----LOGIN-----############################
        
            #self.execute(r"C:\Users\Rafael\Desktop\2207\faturamento.exe")
            self.execute(r"C:\teorema\bin\\faturamento.exe")
            
            if not self.find( "btn_codigo_usuario", matching=0.97, waiting_time=30000):
                self.not_found("btn_codigo_usuario")
            self.click_relative(47, 12)
                    
            self.type_keys_with_interval(1,"002")
            self.wait(500)
            self.type_keys_with_interval(1,"1811")
            self.enter()

            if not self.find( "btn_login", matching=0.97, waiting_time=10000):
                self.not_found("btn_login")
            self.click()
            self.enter()

            ###################################################################
        
        
        
                        ####---ABRINDO PARAMETROS---####
            self.enter()
            self.wait(1500)
            if not self.find( "parametros_abrir_cadastro", matching=0.97, waiting_time=10000):
                self.not_found("parametros_abrir_cadastro")
            self.click_relative(27, 32)
            self.wait(1500)
            if not self.find( "parametr0s", matching=0.97, waiting_time=10000):
                self.not_found("parametr0s")
            self.click()
            if not self.find( "parametros", matching=0.97, waiting_time=10000):
                self.not_found("parametros")
            self.click()
            self.type_down()
            self.wait(1500)
            if not self.find( "parametrosempresa", matching=0.97, waiting_time=10000):
                self.not_found("parametrosempresa")
            self.click()
            if not self.find( "faturament0_localizape", matching=0.97, waiting_time=10000):
                self.not_found("faturament0_localizape")
            self.click()
            if not self.find( "faturement0_editar_empresas", matching=0.97, waiting_time=10000):
                self.not_found("faturement0_editar_empresas")
            self.click()
            self.wait(3500)
            if not self.find( "faturamento_parametros_de_empresa_localizar", matching=0.97, waiting_time=10000):
                self.not_found("faturamento_parametros_de_empresa_localizar")
            self.click()          
            if not self.find( "faturamento_inclur_cadastro", matching=0.97, waiting_time=10000):
                self.not_found("faturamento_inclur_cadastro")
            self.click()
            if not self.find( "naope", matching=0.97, waiting_time=10000):
                self.not_found("naope")
            self.click()
            if not self.find( "buscaempresape", matching=0.97, waiting_time=10000):
                self.not_found("buscaempresape")
            self.click()
            self.backspace()
            if not self.find( "faturamento_consulta_de_empresas_localizar_empresas", matching=0.97, waiting_time=10000):
                self.not_found("faturamento_consulta_de_empresas_localizar_empresas")
            self.click()
            self.type_keys_with_interval(1,"0015")
            #if not self.find( "cod0101ictusteste", matching=0.97, waiting_time=10000):
                #self.not_found("cod0101ictusteste")   
            #self.click() 
            #if not self.find( "retornarpe", matching=0.97, waiting_time=10000):
            #    self.not_found("retornarpe")
            #self.click()                
            if not self.find( "seleci0nar_consulta_empresas", matching=0.97, waiting_time=10000):
                self.not_found("seleci0nar_consulta_empresas")
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
            if not self.find( "livros_fiscais_contabilidade", matching=0.97, waiting_time=10000):
                self.not_found("livros_fiscais_contabilidade")
            self.click_relative(155, 26)
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
            if not self.find( "alterar_lancamentos_contabeis", matching=0.97, waiting_time=10000):
                self.not_found("alterar_lancamentos_contabeis")
            self.click_relative(163, 30)
            self.type_down()
            self.enter()
            if not self.find( "alterarlancamentoscontabeis", matching=0.97, waiting_time=10000):
                self.not_found("alterarlancamentoscontabeis")
            self.click_relative(162, 28)
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
                if not self.find( "nivel_exigencia_cadastro", matching=0.97, waiting_time=10000):
                    self.not_found("nivel_exigencia_cadastro")
                self.click_relative(160, 30)
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
            if not self.find( "cadastramento_sem_macros", matching=0.97, waiting_time=10000):
                self.not_found("cadastramento_sem_macros")
            self.click_relative(163, 30)
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
                
            
            if not self.find( "modo_checagem_fincanceira", matching=0.97, waiting_time=10000):
                self.not_found("modo_checagem_fincanceira")
            self.click_relative(166, 26)
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
                if not self.find( "exigencia_plano_financeiro", matching=0.97, waiting_time=10000):
                    self.not_found("exigencia_plano_financeiro")
                self.click_relative(167, 30)
                self.type_up()
                self.enter()
                x=x+1
                
            y=0
            while y<3:
                if not self.find( "exige_plano_financeiro", matching=0.97, waiting_time=10000):
                    self.not_found("exige_plano_financeiro")
                self.click_relative(164, 22)
                self.type_down()
                y=y+1
            self.enter()
            
            
            x=0
            while x<2:
                if not self.find( "exigencia_centro_de_custo", matching=0.97, waiting_time=10000):
                    self.not_found("exigencia_centro_de_custo")
                self.click_relative(220, 30)   
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
                if not self.find( "exigencia_classificacao", matching=0.97, waiting_time=10000):
                    self.not_found("exigencia_classificacao")
                self.click_relative(160, 23)
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
            if not self.find( "usar_baixa_de_cheque", matching=0.97, waiting_time=10000):
                self.not_found("usar_baixa_de_cheque")
            self.click_relative(161, 27)
            self.type_down()
            self.enter()
            if not self.find( "tipocontabilizacaobaixa", matching=0.97, waiting_time=10000):
                self.not_found("tipocontabilizacaobaixa")
            self.click_relative(161, 28)
            self.type_up()
            self.enter()
            
            x=0
            while x < 2:
                if not self.find( "permitir_desconto_durante_baix", matching=0.97, waiting_time=10000):
                    self.not_found("permitir_desconto_durante_baix")
                self.click_relative(165, 29)
                self.type_down()
                self.enter()
                x=x+1
            '''
            x=0
            while x<3:
                if not self.find( "permitirdescontodurantebaixa", matching=0.97, waiting_time=10000):
                    self.not_found("permitirdescontodurantebaixa")
                self.click_relative(161, 24)
                self.type_up()
                x=x+1
            self.enter()
            '''
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
            
            if not self.find( "op_encontrodecontas", matching=0.97, waiting_time=10000):
                self.not_found("op_encontrodecontas")
            
            self.click_relative(164, 27)
            self.type_up()
            self.enter()
            if not self.find( "op_encontrodecontas", matching=0.97, waiting_time=10000):
                self.not_found("op_encontrodecontas")
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
            if not self.find( "tipo_de_reajuste_juros_de_mora", matching=0.97, waiting_time=10000):
                self.not_found("tipo_de_reajuste_juros_de_mora")
            self.click_relative(156, 25)
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
            if not self.find( "dia_carencia_reajuste", matching=0.97, waiting_time=10000):
                self.not_found("dia_carencia_reajuste")
            self.click_relative(163, 26)                        
            self.type_keys_with_interval(1,'123')
            self.enter()
            self.enter()
            self.type_keys_with_interval(1,'123')
            if not self.find( "dia_tolerencia_vencimento", matching=0.97, waiting_time=10000):
                    self.not_found("dia_tolerencia_vencimento")
            self.click_relative(163, 27)
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
                if not self.find( "tipode_desconto", matching=0.97, waiting_time=10000):
                    self.not_found("tipode_desconto")
                self.click_relative(164, 31)
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
            if not self.find( "subir_tela_parametros", matching=0.97, waiting_time=10000):
                self.not_found("subir_tela_parametros")
            self.click()
            x=0
            while x<7:
                if not self.find( "subir_tela_parametros2", matching=0.97, waiting_time=10000):
                    self.not_found("subir_tela_parametros2")
                self.double_click()
                x=x+1

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
                if not self.find( "empresas_limites", matching=0.97, waiting_time=10000):
                    self.not_found("empresas_limites")
                self.click_relative(205, 25)
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
            
            if not self.find( "calcular_pre_lancto", matching=0.97, waiting_time=10000):
                self.not_found("calcular_pre_lancto")
            self.click_relative(210, 29)
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
            
            if not self.find( "codificacao_de_custo", matching=0.97, waiting_time=10000):
                self.not_found("codificacao_de_custo")
            self.click_relative(169, 29)
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
                if not self.find( "duplacidade_movto_itens", matching=0.97, waiting_time=10000):
                    self.not_found("duplacidade_movto_itens")
                self.click_relative(217, 25)
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
             
            if not self.find( "permite_cadastrar_itens_com_valor", matching=0.97, waiting_time=10000):
                self.not_found("permite_cadastrar_itens_com_valor")
            self.click_relative(218, 36)
            self.type_up()
            self.enter()
            if not self.find( "permiteinclusaodeitensnaimportacao", matching=0.97, waiting_time=10000):
                 self.not_found("permiteinclusaodeitensnaimportacao")
            self.click_relative(210, 23)
            self.type_down()
            self.enter()
             
            x=0
            while x<4:
                if not self.find( "manuntecao_de_preco_abaixo", matching=0.97, waiting_time=10000):
                    self.not_found("manuntecao_de_preco_abaixo")
                self.click_relative(212, 25)
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
            if not self.find( "transferencia_de_itens_entre_empresas", matching=0.97, waiting_time=10000):
                self.not_found("transferencia_de_itens_entre_empresas")
            self.click_relative(204, 29)
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
            if not self.find( "casas_decimais_preco", matching=0.97, waiting_time=10000):
                self.not_found("casas_decimais_preco")
            self.click_relative(125, 26)
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
            if not self.find( "calculos_precos", matching=0.97, waiting_time=10000):
                self.not_found("calculos_precos")
            self.click_relative(128, 35)
            self.type_keys_with_interval(1,'123')
            self.enter()
            if not self.find( "origem_pis", matching=0.97, waiting_time=10000):
                self.not_found("origem_pis")
            self.click_relative(123, 22)
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
            self.tab()
            
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
             
            #if not self.find( "validarsituacaoclientegerarpedido", matching=0.97, waiting_time=10000):
                #self.not_found("validarsituacaoclientegerarpedido")
            #self.click_relative(213, 25)
            #self.type_down()
            #self.enter()
            #if not self.find( "validarsituacaoclientegerarpedido", matching=0.97, waiting_time=10000):
                #self.not_found("validarsituacaoclientegerarpedido")
            #self.click_relative(213, 25)
            #self.type_down()
            #self.enter()
            if not self.find( "situacao_cliente_gerar_pedido", matching=0.97, waiting_time=10000):
                 self.not_found("situacao_cliente_gerar_pedido")
            self.click_relative(212, 36)
            self.type_up()
            self.enter() 
            if not self.find( "reservar_estoque_orcamento", matching=0.97, waiting_time=10000):
                self.not_found("reservar_estoque_orcamento")
            self.click_relative(211, 28)
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
                if not self.find( "calcular_qtdes", matching=0.97, waiting_time=10000):
                    self.not_found("calcular_qtdes")
                self.click_relative(214, 31)
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
                self.click_relative(208, 27)
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
                if not self.find( "item_sem_estoque_pedido", matching=0.97, waiting_time=10000):
                    self.not_found("item_sem_estoque_pedido")
                self.click_relative(164, 31)
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
                if not self.find( "codigo_imprimir_pedido", matching=0.97, waiting_time=10000):
                    self.not_found("codigo_imprimir_pedido")
                self.click_relative(159, 30)
                self.type_down()
                self.enter()
                x=x+1
                
            x=0
            while x<3:
                if not self.find( "codigo_imprimir_vendas_balcao", matching=0.97, waiting_time=10000):
                    self.not_found("codigo_imprimir_vendas_balcao")
                self.click_relative(161, 29)
                self.type_down()
                self.enter()
                x=x+1
                
            x=0
            while x<3:
                if not self.find( "codigo_imprimir_condifcionais", matching=0.97, waiting_time=10000):
                    self.not_found("codigo_imprimir_condifcionais")
                self.click_relative(157, 27)
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
                if not self.find( "Margem_minima_pra_vendas", matching=0.97, waiting_time=10000):
                    self.not_found("Margem_minima_pra_vendas")
                self.click_relative(134, 23)
                self.type_up()
                self.enter()
                x=x+1
            self.tab()
            """
            if not self.find( "validarestoquedescontospedido", matching=0.97, waiting_time=10000):
               self.not_found("validarestoquedescontospedido")
            self.click_relative(162, 29)
            self.type_down()
            self.enter()  
            if not self.find( "validarestoquedescontospedido", matching=0.97, waiting_time=10000):
               self.not_found("validarestoquedescontospedido")
            self.click_relative(162, 29)
            self.type_up()
            self.enter()"""
            
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
            if not self.find( "mostrar_autom_itens_agregacao", matching=0.97, waiting_time=10000):
                self.not_found("mostrar_autom_itens_agregacao")
            self.click_relative(94, 26)
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
            if not self.find( "ultilizar_cartao_de_fechamento", matching=0.97, waiting_time=10000):
                self.not_found("ultilizar_cartao_de_fechamento")
            self.click_relative(166, 28)
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
            if not self.find( "percentual_maximo_desconto", matching=0.97, waiting_time=10000):
                self.not_found("percentual_maximo_desconto")
            self.click_relative(164, 32)
            self.type_keys_with_interval(1,'123')
            self.tab()
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
            if not self.find( "dias_validade_orcamento", matching=0.97, waiting_time=10000):
                self.not_found("dias_validade_orcamento")
            self.click_relative(162, 28)
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
            if not self.find( "alteracao_valor", matching=0.97, waiting_time=10000):
                self.not_found("alteracao_valor")
            self.click_relative(156, 25)
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
                if not self.find( "venda_a_prazo", matching=0.97, waiting_time=10000):
                    self.not_found("venda_a_prazo")
                self.click_relative(161, 31)
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
            self.click_relative(158, 29)
            self.type_up()
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
            self.click_relative(99, 25)
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
                             
            
            
            if not self.find( "custo_a_ultilizacao", matching=0.97, waiting_time=10000):
                self.not_found("custo_a_ultilizacao")
            self.click_relative(158, 23)
            self.type_down()    
            x=0
            while x<4:
                self.type_down()
                self.enter()
                x=x+1
          
            if not self.find( "composicao_sem_estoque", matching=0.97, waiting_time=10000):
                self.not_found("composicao_sem_estoque")
            self.click_relative(88, 25)
            self.type_down()
            self.enter()
            if not self.find( "liberacao_transformacao", matching=0.97, waiting_time=10000):
                 self.not_found("liberacao_transformacao")
            self.click_relative(166, 34)
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
            self.type_keys_with_interval(1,'051')
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
            if not self.find( "tipo_nf_de_servicos", matching=0.97, waiting_time=10000):
                self.not_found("tipo_nf_de_servicos")
            self.click_relative(149, 30)
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
            if not self.find( "faturamento_excluir02", matching=0.97, waiting_time=10000):
                self.not_found("faturamento_excluir02")
            self.click()
            
            
            
                            ####---ABA9 CODIGOS PADROES---####
                             
            if not self.find( "aba9codigospadroes", matching=0.97, waiting_time=10000):
                self.not_found("aba9codigospadroes")
            self.click()
            
                                ####---A5 P1---####
            if not self.find( "aba5p1_parametrosEmpresa_garantia", matching=0.97, waiting_time=10000):
                self.not_found("aba5p1_parametrosEmpresa_garantia")
            self.click_relative(47, 140)
                                 
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
            if not self.find( "voltar", matching=0.97, waiting_time=10000):
                self.not_found("voltar")
            self.click()
            self.wait(1000)
                            ####---OPERACAO DE ENTRADA---####
                             
            if not self.find( "b_transformacaodeitens_parametros", matching=0.97, waiting_time=10000):
                self.not_found("b_transformacaodeitens_parametros")
            self.click_relative(79, 25)                                               
            if not self.find( "achar", matching=0.97, waiting_time=10000):
                self.not_found("achar")
            self.click()
            if not self.find( "cod_017", matching=0.97, waiting_time=10000):
                self.not_found("cod_017")
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
            if not self.find( "achar_cod_menor17", matching=0.97, waiting_time=10000):
                self.not_found("achar_cod_menor17")
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
            if not self.find( "achar_cod_menor17", matching=0.97, waiting_time=10000):
                self.not_found("achar_cod_menor17")
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
            if not self.find( "menor_COD_017", matching=0.97, waiting_time=10000):
                self.not_found("menor_COD_017")
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
            if not self.find( "cod_017_cod", matching=0.97, waiting_time=10000):
                self.not_found("cod_017_cod")
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
            if not self.find( "codigo_num_017", matching=0.97, waiting_time=10000):
                self.not_found("codigo_num_017")
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
            if not self.find( "numero_codigo_017", matching=0.97, waiting_time=10000):
                self.not_found("numero_codigo_017")
            self.click()
            if not self.find( "escolhe", matching=0.97, waiting_time=10000):
                self.not_found("escolhe")
            self.click()
            self.wait(1000)
            if not self.find( "devolucaoitens", matching=0.97, waiting_time=10000):
                self.not_found("devolucaoitens")
            self.click_relative(388, 127)            
            if not self.find( "numero_dezesete", matching=0.97, waiting_time=10000):
                self.not_found("numero_dezesete")
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
            if not self.find( "achar_cod_0002", matching=0.97, waiting_time=10000):
                self.not_found("achar_cod_0002")
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
            
            if not self.find( "cod_002", matching=0.97, waiting_time=10000):
                self.not_found("cod_002")
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
            if not self.find( "cpd_002", matching=0.97, waiting_time=10000):
                self.not_found("cpd_002")
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
            if not self.find( "cod_v_frete_002", matching=0.97, waiting_time=10000):
                self.not_found("cod_v_frete_002")
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
            if not self.find( "codigo_frete_002", matching=0.97, waiting_time=10000):
                self.not_found("codigo_frete_002")
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
            if not self.find( "codiguinho_002_", matching=0.97, waiting_time=10000):
                self.not_found("codiguinho_002_")
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
            if not self.find( "faturamento_cod_paramentros_002", matching=0.97, waiting_time=10000):
                self.not_found("faturamento_cod_paramentros_002")
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
            if not self.find( "acharcod_02", matching=0.97, waiting_time=10000):
                self.not_found("acharcod_02")
            self.click()
            if not self.find( "selecionar_vendasB", matching=0.97, waiting_time=10000):
                self.not_found("selecionar_vendasB")
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
            #if not self.find( "cod101teste", matching=0.97, waiting_time=10000):
            #    self.not_found("cod101teste")
            #self.click()           
            if not self.find( "retornar_consulta_de_vedes", matching=0.97, waiting_time=10000):
                self.not_found("retornar_consulta_de_vedes")
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
            if not self.find( "achar_cod_01", matching=0.97, waiting_time=10000):
                self.not_found("achar_cod_01")
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
            if not self.find( "cod_0001", matching=0.97, waiting_time=10000):
                self.not_found("cod_0001")
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
            if not self.find( "cod_cod_0001", matching=0.97, waiting_time=10000):
                self.not_found("cod_cod_0001")
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
            self.type_keys_with_interval(1,'consig')
            if not self.find( "retornar_consig", matching=0.97, waiting_time=10000):
                self.not_found("retornar_consig")
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
            #if not self.find( "cod101teste", matching=0.97, waiting_time=10000):
            #    self.not_found("cod101teste")
            #self.click() 
            self.type_keys_with_interval(1,"00091")          
            if not self.find( "selecionar_vendedores", matching=0.97, waiting_time=10000):
                self.not_found("selecionar_vendedores")
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
            if not self.find( "cod001", matching=0.97, waiting_time=10000):
                self.not_found("cod001")
            self.click()
            if not self.find( "selecionar_cod_op", matching=0.97, waiting_time=10000):
                self.not_found("selecionar_cod_op")
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
            if not self.find( "banco_do_bradesco", matching=0.97, waiting_time=10000):
                self.not_found("banco_do_bradesco")
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
            if not self.find( "achar_cod066", matching=0.97, waiting_time=10000):
                self.not_found("achar_cod066")
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
            if not self.find( "cod0045pagamentos", matching=0.97, waiting_time=10000):
                self.not_found("cod0045pagamentos")
            self.click()
            self.wait(1000)
            if not self.find( "selecionar_cod_operacional", matching=0.97, waiting_time=10000):
                self.not_found("selecionar_cod_operacional")
            self.click()

            
                            ####---ABA9 P4---####
                             
            if not self.find( "aba9p4", matching=0.97, waiting_time=10000):
                self.not_found("aba9p4")
            self.click()
            x=0
            while x< 16:
                self.type_keys_with_interval(1,'te12!@')
                self.tab()
                x=x+1
            
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
            #if not self.find( "cod00101testevendedorpadrao", matching=0.97, waiting_time=10000):
            #    self.not_found("cod00101testevendedorpadrao")
            #self.click()
            if not self.find( "escolhe", matching=0.97, waiting_time=10000):
                self.not_found("escolhe")
            self.click()
            self.wait(1000)
            if not self.find( "operacaopadraoecommerce", matching=0.97, waiting_time=10000):
                self.not_found("operacaopadraoecommerce")
            self.click_relative(80, 24)
            self.type_keys_with_interval(1,'consig')
            if not self.find( "escolhe", matching=0.97, waiting_time=10000):
                self.not_found("escolhe")
            self.click()
            self.wait(1000)
            if not self.find( "condicaodepagamentopadraoecommerce", matching=0.97, waiting_time=10000):
                self.not_found("condicaodepagamentopadraoecommerce")
            self.click_relative(80, 25)
            if not self.find( "cod0019saidasvendas", matching=0.97, waiting_time=10000):
                self.not_found("cod0019saidasvendas")
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
            if not self.find( "gestao_adm_empresa", matching=0.97, waiting_time=10000):
                self.not_found("gestao_adm_empresa")
            self.click_relative(59, 24)
            self.type_keys_with_interval(1,"0111")
            if not self.find( "gestao_adm_selecionar", matching=0.97, waiting_time=10000):
                self.not_found("gestao_adm_selecionar")
            self.click_relative(165, 40)
                            ####---FINALIZACAO---####
                             
            if not self.find( "faturament0_transporte_salvar", matching=0.97, waiting_time=10000):
                self.not_found("faturament0_transporte_salvar")
            self.click()
            if not self.find( "reserva_producao_confirmar", matching=0.97, waiting_time=10000):
                self.not_found("reserva_producao_confirmar")
            self.click_relative(389, 202)
            self.click()
            self.wait(1000)
            #if not self.find( "consulta_de_operacoes", matching=0.97, waiting_time=10000):
                #self.not_found("consulta_de_operacoes")
            #self.click_relative(98, 41)
            #if not self.find("cod00101ictusteste", matching=0.97, waiting_time=10000):
                #self.not_found("cod0111ictusteste")
            #self.click()
            #self.wait(500)
            #if not self.find( "editarfimpa", matching=0.97, waiting_time=10000):
                #self.not_found("editarfimpa")
            #self.click()
            #if not self.find( "excluirfimpa", matching=0.97, waiting_time=10000):
                #self.not_found("excluirfimpa")
            #self.click()
            #self.wait(500)
            #if not self.find( "botaosimexcluirfimpa", matching=0.97, waiting_time=10000):
                #self.not_found("botaosimexcluirfimpa")
            #self.click()
            #self.wait(500)
            #self.enter()
            #if not self.find( "faturamento_error", matching=0.97, waiting_time=10000):
                #self.not_found("faturamento_error")
            #self.click_relative(314, 192)
            #if not self.find( "faturamento_error_02", matching=0.97, waiting_time=10000):
               # self.not_found("faturamento_error_02")
            #self.click_relative(318, 200)
            #if not self.find( "faturamento_error_03", matching=0.97, waiting_time=10000):
            #    self.not_found("faturamento_error_03")
            #self.click_relative(308, 147)
            if not self.find( "retornarfimpa", matching=0.97, waiting_time=10000):
                self.not_found("retornarfimpa")
            self.click()
            #if not self.find( "localizape", matching=0.97, waiting_time=10000):
               # self.not_found("localizape")
            #self.click()
            #if not self.find( "retornarfimpa", matching=0.97, waiting_time=10000):
                #self.not_found("retornarfimpa")
            #self.click()
                             
                            ####---LIBERACAO E BLOQUEIO---####

            if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro2")
            self.click()
            if not self.find( "faturamento_parametros", matching=0.97, waiting_time=10000):
                self.not_found("faturamento_parametros")
            self.click()
            if not self.find( "faturamento_block_periodos", matching=0.97, waiting_time=10000):
                 self.not_found("faturamento_block_periodos")
            self.click()
            if not self.find( "faturamento_l0calizar_periodos_liberados", matching=0.97, waiting_time=10000):
                self.not_found("faturamento_l0calizar_periodos_liberados")
            60
            self.click()
            if not self.find( "faturament0_editar_periodos_liberados_bloqueados", matching=0.97, waiting_time=10000):
                self.not_found("faturament0_editar_periodos_liberados_bloqueados")
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
            self.type_keys_with_interval(1,"0111")          
            #if not self.find("cod0111Bteste", matching=0.97, waiting_time=10000):
                #self.not_found("cod0111Bteste")
            #self.click()            
            if not self.find( "escolhe", matching=0.97, waiting_time=10000):
                self.not_found("escolhe")
            self.click()
            if not self.find( "retornar_parametros_cadastro_empresas", matching=0.97, waiting_time=10000):
                self.not_found("retornar_parametros_cadastro_empresas")
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

            if not self.find( "faturament0_salvar_calendarios", matching=0.97, waiting_time=10000):
                #self.not()
                _
                found("faturament0_salvar_calendarios")
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
                
            if not self.find( "abrircadastros_abacadastro2", matching=0.97, waiting_time=10000):
                self.not_found("abrircadastros_abacadastro2")
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
            #if not self.find( "cod0101comnometeste", matching=0.97, waiting_time=10000):
            #    self.not_found("cod0101comnometeste")
            #self.click()            
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
            
            #if not self.find( "cod0101Aprteste", matching=0.97, waiting_time=10000):
            #    self.not_found("cod0101Aprteste")
            #self.click()            
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
